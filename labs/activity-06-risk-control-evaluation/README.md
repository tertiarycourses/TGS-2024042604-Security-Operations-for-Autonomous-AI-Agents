# Activity 06 — Quantify Agent Risks and Control Value

**Criteria:** A5  
**Duration:** 60–90 minutes  
**Mode:** Individual, offline simulation using synthetic data only

## Objective

Create `risk_evaluation.csv` from `mock_risks.csv` and use the evidence to make a defensible security-operations decision.

## Files

- `activity.py` — runnable Python 3 script; standard library only.
- `mock_risks.csv` — synthetic activity data; it contains no live credentials or personal data.
- `risk_evaluation.csv` — generated evidence artifact after the script runs.

![Activity 06 execution workflow](workflow.png)

## Procedure

1. Inspect frequency, loss magnitude, effectiveness and appetite assumptions.
2. Run python3 activity.py.
3. Recalculate inherent and residual expected loss for one row.
4. Change one effectiveness value and rerun the sensitivity check.
5. Confirm the treatment decision is based on residual loss versus appetite.

## Run

```bash
cd activity-06-risk-control-evaluation
python3 activity.py
```

## Verification

Residual risk and expected annual loss calculations reconcile with the input assumptions.

The script must print `PASS`, the output file must exist, and the decision must reconcile with the supplied mock values.

## Troubleshooting

- `FileNotFoundError`: run the command from this activity folder and keep the mock-data filename unchanged.
- `JSONDecodeError`: restore valid JSON/JSONL syntax; JSONL requires one JSON object per line.
- CSV columns missing: restore the original header row before rerunning.
- Unexpected decision: compare the input value, policy threshold and rule in `activity.py`; do not edit the generated output by hand.

## Cleanup

Delete only the generated `risk_evaluation.csv` file, then rerun the script to recreate a clean evidence artifact. The mock data and script are source files and should be retained.
