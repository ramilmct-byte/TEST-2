"""Draw two plain plots from the summary tables in data/fixtures/.

The confidence intervals are already in the tables and are plotted as supplied.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "03-plain-plots"
OUT.mkdir(parents=True, exist_ok=True)
for stem in ["life_satisfaction_by_status", "care_hours_by_age"]:
    table = pd.read_csv(ROOT / "data" / "fixtures" / f"{stem}.csv")
    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.errorbar(table.estimate, range(len(table)),
                xerr=[table.estimate - table.ci_low, table.ci_high - table.estimate],
                fmt="o", color="black", capsize=3)
    ax.set_yticks(range(len(table)), table.group.str.replace("_", " "))
    ax.set(xlabel=table.units.iloc[0], title=table.measure.iloc[0])
    ax.invert_yaxis()
    fig.text(.5, .015, "95% t intervals for group means; independent observations assumed.",
             ha="center", fontsize=8)
    fig.tight_layout(rect=[0, .045, 1, 1])
    fig.savefig(OUT / f"{stem}.png", dpi=160)
    plt.close(fig)
    print(f"Created outputs/03-plain-plots/{stem}.png")
