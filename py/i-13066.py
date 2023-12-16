import polars as pl
from io import StringIO

csv = "a,b,c\n" "1,2,3\n" "1,2,3\n"

df = pl.read_csv(StringIO(csv), columns=["b", "a", "c"])
print(df)
