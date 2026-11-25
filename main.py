import os

LINE = "My cat learned to open doors, so now I pay rent for a house where I have to knock before entering my own bathroom."

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
