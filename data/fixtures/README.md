# Small tables for checking and plotting

All values are simulated.

## Hand-check tables

`missing_values_example.csv` is an eight-row table, small enough to check by
hand against the codebook. A commute of `0` for a remote worker, `-7` for a
nonworker, and `-8`/`-9` for nonresponse have different meanings.

`missing_values.csv` is a five-row worked check. Its valid responses are 7, 8
and 5: count 3, missing count 2, mean 20/3. These results are also in
`expected_missing_values.json`.

## Summary tables for plotting

`care_hours_by_age.csv` describes weekly unpaid care by age group, and
`life_satisfaction_by_status.csv` describes life satisfaction by employment
status. Both were computed from the main raw survey after excluding only `-8`
and `-9` in the summarised outcome. A respondent with a valid outcome is
retained even if another response is missing.

| Column | Meaning |
|---|---|
| `group` | Group label, in the order supplied |
| `estimate` | Arithmetic mean of valid responses within the group |
| `ci_low`, `ci_high` | Lower and upper endpoints of the supplied interval |
| `n` | Number of valid responses used for the group mean |
| `measure`, `units` | Labels to use when constructing a title/axis |
| `ci_method` | Method behind the uncertainty interval |

Intervals are **95% Student t intervals for group means**, using the sample
standard deviation and `n-1` degrees of freedom. They assume independent
observations and are an approximation for these bounded, skewed outcomes. They
are not ranges containing 95% of individuals, causal intervals, or measures of
uncertainty about a real population. Do not recompute them from the small
summary table or clamp them to the outcome bounds without stating what
changed. Values are rounded to six decimals.
