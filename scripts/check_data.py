"""Check documented raw-data structure, without cleaning or changing the CSV."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
data = pd.read_csv(ROOT / "data" / "raw" / "work_care_wellbeing.csv")
assert len(data) == 2000, "Expected 2,000 simulated adults."
assert data.respondent_id.is_unique, "Respondent IDs must be unique."
assert data.age.between(18, 85).all()
assert data.household_size.between(1, 6).all()
ranges = {
    "education_years": (0, 22), "paid_hours_week": (0, 75),
    "commute_minutes": (0, 150), "care_hours_week": (0, 65),
    "household_income_gbp_month": (150, 18000), "financial_strain": (1, 5),
    "life_satisfaction": (0, 10), "social_contact_days": (0, 7),
}
for column, (low, high) in ranges.items():
    codes = [-8, -9, -7] if column == "commute_minutes" else [-8, -9]
    assert (data[column].between(low, high) | data[column].isin(codes)).all(), column
paid = data.employment_status.isin(["employed", "self_employed"])
assert data.loc[~paid, "paid_hours_week"].eq(0).all()
assert data.loc[~paid, "commute_minutes"].eq(-7).all()
assert data.loc[paid, "commute_minutes"].ne(-7).all()
assert data.loc[data.work_arrangement.eq("remote"), "commute_minutes"].eq(0).all()
assert data.loc[~paid, "work_arrangement"].eq("not_applicable").all()
print("PASS: 2,000 rows; unique IDs; documented ranges and conditional values.")
print("Special response counts (not an instruction to recode every negative value):")
for column in ranges:
    counts = {str(code): int(data[column].eq(code).sum()) for code in [-7, -8, -9]}
    print(f"  {column}: {counts}")
