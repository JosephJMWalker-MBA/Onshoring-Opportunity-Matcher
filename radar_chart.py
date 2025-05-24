
import numpy as np
import matplotlib.pyplot as plt

labels = ["Semiconductors", "Batteries", "Medical Devices", "Electric Motors", "Furniture", "Steel Structures"]
readiness = [6, 5, 7, 4, 8, 6]
infra = [4, 5, 3, 6, 2, 4]
skills = [5, 6, 4, 7, 3, 5]

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
readiness += readiness[:1]
infra = [10 - x for x in infra] + [10 - infra[0]]
skills = [10 - x for x in skills] + [10 - skills[0]]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.plot(angles, readiness, label="Manufacturing Readiness", linewidth=2)
ax.fill(angles, readiness, alpha=0.25)
ax.plot(angles, infra, label="Infrastructure (Inverse Gap)", linestyle="--", linewidth=2)
ax.plot(angles, skills, label="Skills (Inverse Gap)", linestyle="--", linewidth=2)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.set_title("Sector Readiness Radar Chart", size=14, pad=20)
ax.legend(loc="upper right")
plt.tight_layout()
plt.savefig("charts/sector_readiness_radar.png")
