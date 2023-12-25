import os
from io import StringIO
from pathlib import Path
import polars as pl


fname = Path(os.environ["ROOT"]) / "data" / "13066.csv"
csv = "a,b,c\n" "1,2,3\n" "1,2,3\n"
cols = ["b", "a", "c"]

with open(fname, "w") as f:
    f.write(csv)


print("Read")
print(pl.read_csv(StringIO(csv), columns=cols))

print("\n" + 80 * "#" + "\n")

print("Scan")
print(pl.scan_csv(fname).select(cols).collect())
