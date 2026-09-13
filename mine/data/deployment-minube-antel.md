# Deployment Section — Technical Context for Thesis Writing

> **Purpose**: This document summarizes the real-world VPS deployment of the OpenFing RAG Chat system, intended as input context for the LLM helping write the final thesis. It covers infrastructure, architecture decisions, security hardening, and operational observations. The suggested thesis placement is **Capítulo 6 – Experimentación**, as a short section on *despliegue y validación operacional*.

---

## 1. Deployment Context

The system was deployed on a **VPS (Virtual Private Server) provided by Mi Nube Antel**, Uruguay's national telecommunications operator (ANTEL). The VPS was granted free of charge to the project for a limited period as part of university support, representing a realistic hosting environment comparable to a small production cloud instance.

The public URL used during the deployment period was:
```
https://openfingchat.duckdns.org
```

This was a real, publicly accessible endpoint — not a local or simulated environment. Users could interact with the chatbot from any browser during the active period.

---

## 2. Infrastructure Stack

### Server
- **Provider**: Mi Nube Antel (Uruguay)
- **OS**: Ubuntu Linux (Debian-based)
- **Access**: SSH on custom port 2222, ED25519 key authentication only

### Containerization & Orchestration
All services were containerized using **Docker** and orchestrated with **Docker Compose**. The deployment comprised the following services:

| Service           | Image / Build                   | Role                                          |
| ----------------- | ------------------------------- | --------------------------------------------- |
| `backend`         | Custom (Python 3.12 + uv)       | FastAPI application server                    |
| `frontend`        | Custom (Node 22 + pnpm → nginx) | React SPA static serving                      |
| `nginx`           | `nginx:alpine`                  | Reverse proxy, TLS termination                |
| `database`        | `postgres`                      | Relational data (metadata, conversations)     |
| `certbot`         | `certbot/certbot`               | Let's Encrypt TLS certificate issuance        |
| `certbot-renewal` | `certbot/certbot`               | Automatic certificate renewal (12h loop)      |
| `migration`       | Same as backend                 | One-shot Alembic DB migration (profile-gated) |

### Network Isolation
Docker internal networking was used to enforce service boundaries:

- `database` network: **internal bridge** — only the backend can reach PostgreSQL; it is never exposed to the host network.
- `backend` network: connects nginx ↔ backend.
- `frontend` network: connects nginx ↔ frontend.
- Only nginx exposes ports 80 and 443 to the outside world.

### Application Dockerfiles
- **Backend**: Multi-stage build using the official `uv` base image (`ghcr.io/astral-sh/uv:python3.12-bookworm-slim`). Dependencies installed via `uv sync --locked`; runtime image is `python:3.12-slim-bookworm` with a non-root `app` user. System dependencies include `ffmpeg` (audio processing) and `libpq` (PostgreSQL client).
- **Frontend**: Multi-stage build; `node:22-alpine` + `pnpm` for building the Vite/React app, then served from an `nginx:1.29-alpine` production image with static asset caching.

---

## 3. TLS / HTTPS

SSL certificates were obtained from **Let's Encrypt** using the **Certbot webroot challenge**:

1. A minimal nginx-only compose stack was brought up temporarily to serve the ACME challenge at `/.well-known/acme-challenge/`.
2. Certbot obtained certificates for `openfingchat.duckdns.org`.
3. Certificates were stored in a named Docker volume (`certbot_conf`) shared between nginx and certbot.
4. A dedicated `certbot-renewal` container runs on a 12-hour loop executing `certbot renew`, ensuring automatic certificate renewal without manual intervention.

The domain was managed via **DuckDNS**, a free dynamic DNS service, pointing to the VPS's public IP.

---

## 4. Nginx Reverse Proxy Configuration

Nginx acted as the single entry point for all traffic. Key configuration decisions:

- **HTTPS-only**: HTTP (port 80) redirects to HTTPS (port 443).
- **API routing**: Requests to `/api/*` are proxied to the FastAPI backend. Extended timeouts were configured (`proxy_read_timeout 300s`) to accommodate potentially slow RAG inference (embedding lookups, LLM generation).
- **WebSocket support**: `Upgrade` and `Connection` headers were forwarded to support streaming responses.
- **SPA routing**: All other requests are proxied to the React frontend container. Static assets (JS, CSS, fonts, images) are cached with `Cache-Control: public, immutable` and a 1-year expiry.
- **Rate limiting**: Two `limit_req_zone` zones were defined — `api` (10 req/s) for API endpoints and `uploads` (1 req/s) for heavier endpoints — providing basic DoS mitigation.
- **Gzip compression**: Enabled for text-based content types (JSON, JS, CSS, XML) to reduce transfer size.
- **Health endpoint**: A dedicated `/health` route returned a JSON status object aggregating backend and frontend health, used by Docker healthchecks and external monitoring.

---

## 5. Security Hardening

The server underwent a multi-layered security hardening process — a practical exercise in production security for a student project exposed to the public internet.

### 5.1 SSH Hardening
- Port changed from 22 → **2222** (reduces automated scanner noise).
- `PermitRootLogin no` — root login disabled.
- `PasswordAuthentication no` — only SSH public key authentication (ED25519).
- `AllowUsers guido` — single authorized system user.
- `MaxAuthTries 3` — brute-force throttled at the SSH daemon level.

### 5.2 UFW Host Firewall
Default policy: **deny all incoming, allow all outgoing**.

Explicit allow rules:
- Ports 80 and 443 (TCP): open to the world (web traffic).
- Port 2222 (TCP, SSH): restricted to **Antel Uruguay IP ranges only**:
  - `179.24.0.0/13` (covers 179.24–179.31.x.x)
  - `186.54.0.0/16`
  - `167.60.0.0/16`

This means SSH was only reachable from within Uruguay's Antel network, drastically reducing the attack surface.

> **Notable finding during setup**: An IPv6 gap was discovered — UFW had an overly permissive rule allowing SSH from any IPv6 address worldwide, bypassing the careful IPv4 restrictions. This was identified and corrected, illustrating that dual-stack systems require explicit attention to both protocol families.

### 5.3 Fail2Ban Intrusion Prevention
Installed and configured to automatically ban IPs after 3 failed SSH login attempts within a 10-minute window, with 24-hour bans.

**Observed attack volume** (logged before and during hardening):
- Over **533,000 SSH connection attempts** from worldwide attackers were logged.
- Top individual attackers: 17,826 / 13,970 / 11,312 attempts from single IPs.
- Common targeted usernames: `root`, `admin`, `test`, `homeassistant`, `unifi`.
- Within the first 5 minutes of enabling Fail2Ban: 10 IPs immediately banned, 62 failed attempts detected.

No successful breaches were detected throughout the deployment period.

### 5.4 Defense-in-Depth Architecture

```
Internet
    │
    ▼
[Mi Nube Platform Firewall]   ← cloud-level packet filtering
    │
    ▼
[UFW Host Firewall]           ← IP-allowlisted SSH, open web ports
    │
    ▼
[Fail2Ban]                    ← auto-ban after 3 failed attempts
    │
    ▼
[SSH Daemon]                  ← keys only, custom port, single user
    │
    ▼
[Docker Network Isolation]    ← internal service segmentation
    │
    ▼
Application (FastAPI + React)
```

Each layer provides independent protection; a successful breach would require bypassing multiple controls simultaneously.

---

## 6. Operational Observations

### Application-Layer Scan Noise
During monitoring, automated HTTP requests for common configuration file paths were observed (e.g., `.env`, `config.php`, `wp-login.php`). These are standard background noise for any publicly reachable server. All requests returned 404 responses, confirming the application layer was properly secured and no sensitive files were inadvertently exposed.

### Log Growth
The high volume of SSH brute-force attempts caused rapid log growth in `/var/log/auth.log` (23 MB+ accumulated). After UFW IP restrictions were in place, log growth rate dropped significantly (~95% reduction expected), as the vast majority of attackers were blocked before reaching the SSH daemon.

### VPS Lifecycle
The VPS subscription was not renewed after the free period ended. The server became network-isolated post-lapse. All source code was safely version-controlled in GitLab, so no code was lost. The only data of potential interest remaining on the server was database metrics/usage statistics (query counts, conversation counts, etc.).

---

## 7. Key Technical Decisions & Rationale

| Decision                                                    | Rationale                                                                                    |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Docker Compose (not Kubernetes)                             | Appropriate complexity for a single-server project; simpler ops with same isolation benefits |
| Internal Docker network for DB                              | PostgreSQL never exposed to host or internet; only backend can connect                       |
| Let's Encrypt + DuckDNS                                     | Free, automated TLS with no domain purchase required                                         |
| UFW IP allowlisting for SSH                                 | Drastically reduces brute-force attack surface without VPN complexity                        |
| Non-root app user in containers                             | Defense against container escape scenarios                                                   |
| Multi-stage Docker builds                                   | Separates build-time dependencies from runtime; smaller, more secure production images       |
| Extended nginx proxy timeouts (300s)                        | RAG queries involve embedding lookup + LLM generation which can be slow under load           |
| pnpm in frontend (note: docker-compose uses pnpm, not yarn) | Faster installs, strict dependency isolation                                                 |
| uv for Python dependency management                         | Significantly faster than pip; deterministic lockfile via `uv.lock`                          |

---

## 8. Suggested Framing for the Thesis Section

**Recommended section title**: *Despliegue y Validación Operacional* (or *Despliegue en entorno real*)

**Core argument**: The deployment to a real, publicly accessible VPS constitutes a qualitatively distinct form of validation compared to offline benchmarks. It demonstrates that:

1. The system is architecturally sound enough to run as a containerized multi-service application.
2. It was accessible to real users during the evaluation period.
3. Operational concerns (security, TLS, availability, log management) were addressed using industry-standard practices.
4. The system withstood real internet traffic conditions, including automated attack noise, without compromise.

This complements the RAG quality experiments (embedding/retrieval benchmarks) by showing the system works *end-to-end in a real environment*, not just on paper.