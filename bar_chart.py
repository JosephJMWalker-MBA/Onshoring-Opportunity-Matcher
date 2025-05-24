
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("import_categories.csv")  # Your pipeline should output this

plt.figure(figsize=(12, 6))
plt.bar(df["Product Name"], df["Import Value ($B)"])
plt.title("Top 10 Import Categories by Value")
plt.xlabel("Product")
plt.ylabel("Import Value ($B)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/top_import_categories.png")
