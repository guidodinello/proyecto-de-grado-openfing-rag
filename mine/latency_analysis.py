"""
Análisis de latencia de las consultas RAG desde los logs del VPS.

Uso:
    python mine/latency_analysis.py [ruta_a_directorio_de_logs]

Por defecto busca los logs en /home/guido/Desktop/vps_logs/.
Filtra el endpoint POST /api/v1/services/generator/chat y separa
la latencia en dos fases:
  - retrieval+embed: desde el inicio de la request hasta el log
    "retrieved N sources" (vectorización del query + búsqueda pgvector)
  - llm: desde ese log hasta el final de la request (generación LLM)
"""

import re
import sys
from datetime import datetime
from pathlib import Path

LOG_DIR = Path("/home/guido/Desktop/vps_logs")
CHAT_PATH = "/api/v1/services/generator/chat"
FMT = "%Y-%m-%d %H:%M:%S,%f"

STARTED_RE = re.compile(
    r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})"
    r".*Request ([a-f0-9-]+) started:.*"
    r'"path": "(/api/v1/services/generator/chat)"'
)
COMPLETED_RE = re.compile(
    r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})"
    r".*Request ([a-f0-9-]+) completed:.*"
    r'"path": "(/api/v1/services/generator/chat)"'
    r'.*"status_code": (\d+)'
)
RETRIEVED_RE = re.compile(
    r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})"
    r".*retrieved (\d+) sources"
)


def parse_log(path: Path):
    events = []
    with open(path) as f:
        for line in f:
            m = STARTED_RE.search(line)
            if m:
                events.append((datetime.strptime(m.group(1), FMT), "start", m.group(2)))
                continue
            m = COMPLETED_RE.search(line)
            if m:
                events.append(
                    (datetime.strptime(m.group(1), FMT), "complete", (m.group(2), int(m.group(4))))
                )
                continue
            m = RETRIEVED_RE.search(line)
            if m:
                events.append((datetime.strptime(m.group(1), FMT), "retrieved", int(m.group(2))))
    return events


def analyze(log_dir: Path):
    all_events = []
    for log_file in sorted(log_dir.glob("*.log")):
        try:
            all_events.extend(parse_log(log_file))
        except Exception as e:
            print(f"  [warn] {log_file.name}: {e}", file=sys.stderr)

    all_events.sort(key=lambda x: x[0])

    starts: dict[str, dict] = {}
    results = []

    for ts, etype, data in all_events:
        if etype == "start":
            starts[data] = {"start": ts}
        elif etype == "retrieved":
            for d in starts.values():
                if "start" in d and "retrieved" not in d and ts >= d["start"]:
                    d["retrieved"] = ts
                    break
        elif etype == "complete":
            req_id, status = data
            if req_id in starts and status == 200:
                d = starts.pop(req_id)
                total = (ts - d["start"]).total_seconds()
                retrieval = (d["retrieved"] - d["start"]).total_seconds() if "retrieved" in d else None
                llm = (ts - d["retrieved"]).total_seconds() if "retrieved" in d else None
                results.append(
                    {"req_id": req_id, "total": total, "retrieval": retrieval, "llm": llm}
                )
            elif req_id in starts:
                starts.pop(req_id)

    return results


def print_report(results):
    print(f"{'Request':10}  {'Total':>8}  {'Retr+Emb':>10}  {'LLM':>8}")
    print("-" * 46)
    for r in sorted(results, key=lambda x: x["total"]):
        retr = f"{r['retrieval']:.1f}s" if r["retrieval"] is not None else "     —"
        llm = f"{r['llm']:.1f}s" if r["llm"] is not None else "   —"
        print(f"{r['req_id'][:8]:10}  {r['total']:>7.1f}s  {retr:>10}  {llm:>8}")

    totals = [r["total"] for r in results]
    retrs = [r["retrieval"] for r in results if r["retrieval"] is not None]
    llms = [r["llm"] for r in results if r["llm"] is not None]

    def stats(vals, label):
        s = sorted(vals)
        n = len(s)
        print(
            f"  {label:20} n={n:2d}  "
            f"min={min(s):.1f}  max={max(s):.1f}  "
            f"avg={sum(s)/n:.1f}  median={s[n//2]:.1f}"
        )

    print(f"\n=== Estadísticas ({len(results)} requests exitosas) ===")
    stats(totals, "Total (s)")
    if retrs:
        stats(retrs, "Retrieval+Embed (s)")
    if llms:
        stats(llms, "LLM generation (s)")


if __name__ == "__main__":
    log_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else LOG_DIR
    results = analyze(log_dir)
    print_report(results)
