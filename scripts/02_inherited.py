"""Mean life satisfaction by employment status.

Inherited from a previous research assistant. Not yet checked.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
data = pd.read_csv(ROOT / "data" / "raw" / "work_care_wellbeing.csv")
data["life_satisfaction"] = data["life_satisfaction"].replace({-8: 0, -9: 0})
summary = data.groupby("employment_status")["life_satisfaction"].agg(mean="mean", n="count").reset_index()
out = ROOT / "outputs" / "02-life-satisfaction"
out.mkdir(parents=True, exist_ok=True)
summary.to_csv(out / "summary.csv", index=False)
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.barh(summary.employment_status.str.replace("_", " "), summary["mean"], color="#627D98")
ax.set(xlabel="Mean life satisfaction (0–10)", title="Life satisfaction")
ax.set_xlim(0, 10)
fig.tight_layout()
fig.savefig(out / "summary.png", dpi=180)
plt.close(fig)
print(summary.to_string(index=False, float_format=lambda x: f"{x:.3f}"))
