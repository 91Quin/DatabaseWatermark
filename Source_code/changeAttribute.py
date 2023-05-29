import pandas as pd

df = pd.read_csv("test-Marked-Key.233-r.2-LSB.20.csv")
df.iloc[:, 3] = format(1.5, ".5f")
df.to_csv("test-Marked-Key.233-r.2-LSB.20.csv", index=False)
