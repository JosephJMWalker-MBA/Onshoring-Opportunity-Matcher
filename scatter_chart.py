
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("import_categories.csv")  # Use same file with 'Dependency %' and 'Risk Level'
risk_color_map = {"High": "red", "Medium-High": "orange", "Medium": "yellow"}
colors = df["Risk Level"].map(risk_color_map)

plt.figure(figsize=(12, 6))
plt.scatter(df["Product Name"], df["Dependency %"], c=colors, s=100, edgecolors='black')
plt.title("Import Dependency vs Risk Level")
plt.xlabel("Product")
plt.ylabel("Dependency %")
plt.xticks(rotation=45, ha="right")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/import_dependency_risk.png")
