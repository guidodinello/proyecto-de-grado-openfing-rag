import re
import sys

path_in = sys.argv[1]
path_out = sys.argv[2]

with open(path_in, encoding="utf-8") as f:
    raw = f.read()

raw = raw.replace("\x0c", "\n")

lines = raw.split("\n")
cleaned_lines = []
for line in lines:
    stripped = line.strip()
    if re.fullmatch(r"\d{1,4}", stripped):
        continue
    cleaned_lines.append(stripped)

text = "\n".join(cleaned_lines)

text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)

paragraphs = re.split(r"\n\s*\n", text)
joined_paragraphs = []
for p in paragraphs:
    p = re.sub(r"\s*\n\s*", " ", p)
    p = re.sub(r"\s{2,}", " ", p).strip()
    if p:
        joined_paragraphs.append(p)

final_text = "\n\n".join(joined_paragraphs)

with open(path_out, "w", encoding="utf-8") as f:
    f.write(final_text)

print(f"words: {len(final_text.split())}")
