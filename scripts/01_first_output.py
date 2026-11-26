"""Plot the age distribution of the survey respondents."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
data = pd.read_csv(ROOT / "data" / "raw" / "work_care_wellbeing.csv")
out = ROOT / "outputs" / "01-first-output"
out.mkdir(parents=True, exist_ok=True)
data.age.describe().rename("age").to_csv(out / "summary.csv")
fig, ax = plt.subplots(figsize=(7, 4.2))
ax.hist(data.age, bins=[18, 25, 35, 45, 55, 65, 75, 86], color="#267A83", edgecolor="white")
ax.set(title="Age distribution", xlabel="Age (years)", ylabel="Number of respondents")
fig.tight_layout()
fig.savefig(out / "age_distribution.png", dpi=180)
plt.close(fig)
print("Created outputs/01-first-output/age_distribution.png and summary.csv.")
