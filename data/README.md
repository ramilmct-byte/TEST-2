# Work, care and wellbeing: data guide

**Release 1.0.0. All 2,000 records are simulated. There are no real respondents.**

The file `raw/work_care_wellbeing.csv` contains one row per fictional adult,
aged 18–85. It is a single cross-section.
It is not a sample of a real population, has no survey weights, and cannot
establish facts about actual people or places. Associations are not causal
effects. Keep the raw CSV unchanged; make transformations in a script.

## How to read the responses

`-8` means **don't know** and `-9` means **refused** in the numeric response
fields that allow them below. Neither is zero. `-7` means **not applicable**
and occurs only in `commute_minutes` for people outside paid work.

Zero life satisfaction, zero care and zero social contact are valid responses.
The source income itself is strictly positive when observed. Paid work
hours are genuinely zero outside paid employment; those zeroes are not missing.
Fully remote workers have a commute of zero; nonworkers have no applicable
work commute. Do not replace every negative value or every zero by one rule.

## Codebook

| Field | Meaning and valid values | Special codes |
|---|---|---|
| `respondent_id` | Unique fictional adult identifier, W0001–W2000 | None |
| `age` | Age in completed years, 18–85 | None |
| `education_years` | Completed years of formal education, 0–22 | -8, -9 |
| `employment_status` | Main current activity: `employed`, `self_employed`, `unemployed`, `student`, `retired`, `other_inactive` | None |
| `work_arrangement` | `on_site`, `hybrid`, `remote`; `not_applicable` outside employed/self-employed | No numeric missing codes |
| `paid_hours_week` | Usual total weekly hours in paid work, 0–75; 0 outside paid work | -8, -9 among paid workers |
| `commute_minutes` | Usual **one-way** minutes on a day attending work in person, 0–150; 0 for fully remote workers | -8, -9 among on-site/hybrid paid workers; -7 outside paid work |
| `care_hours_week` | Usual weekly unpaid care for children or adults, 0–65 | -8, -9 |
| `household_income_gbp_month` | Total monthly household income after tax, GBP, 150–18,000 | -8, -9 |
| `household_size` | People living in the household, including respondent, 1–6 | None |
| `financial_strain` | Ease of managing household finances: 1 very easy, 2 fairly easy, 3 neither easy nor difficult, 4 fairly difficult, 5 very difficult | -8, -9 |
| `life_satisfaction` | Satisfaction with life as a whole, 0 not at all satisfied to 10 completely satisfied | -8, -9 |
| `social_contact_days` | Days in a usual week with social contact with friends/relatives outside the household, 0–7 | -8, -9 |
| `area_id` | Fictional home area W01–W10; nominal labels with no rank | None |

Treat `financial_strain` as an ordered response, not a measured amount of money.
Years of education is a quantity; area labels and employment categories are
not. This guide defines the data; it does not decide a regression's sample,
outcome, adjustment variables or handling of nonresponse for you.

## Other files

`fixtures/missing_values.csv` is a five-row hand-check with life satisfaction
7, 8, -9, 5 and -8. `expected_missing_values.json` records its three valid
responses, two nonresponses and valid-response mean of 20/3.

`fixtures/missing_values_example.csv` is an eight-row practice fixture. It is
not a subset to combine with the main survey. Its limited fields use the same
response definitions. It contains valid zeroes, nonresponse and inapplicability
so you can check a calculation by hand.

`fixtures/life_satisfaction_by_status.csv` and `fixtures/care_hours_by_age.csv`
are ready-made summary tables for plotting. Their README explains the columns
and intervals. They contain no completed regression.

## Provenance

Created with a fixed simulation script, NumPy seed **20261107**, release
**1.0.0**. No third-party microdata or personal records were used. Values are
bounded for convenience and the distributions are not calibrated to national
statistics. Nonresponse was
inserted independently of the generated outcomes within eligible fields; this
does not imply that nonresponse in real surveys is random. Never describe
results as observed population evidence.
