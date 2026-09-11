# Activity 10 — Run Recovery and Post-Incident Review

**Criteria:** A7  
**Duration:** 60–90 minutes  
**Mode:** Individual, offline simulation using synthetic data only

## Objective

Create `after_action_report.md` from `mock_recovery.json` and use the evidence to make a defensible security-operations decision.

## Files

- `activity.py` — runnable Python 3 script; standard library only.
- `mock_recovery.json` — synthetic activity data; it contains no live credentials or personal data.
- `after_action_report.md` — generated evidence artifact after the script runs.

![Activity 10 execution workflow](workflow.png)

## Procedure

1. Review the recovery gates and lessons in mock_recovery.json.
2. Run python3 activity.py.
3. Open after_action_report.md and confirm every gate passes.
4. Change one gate to fail and verify recovery is blocked.
5. Check that each lesson has an owner, due date and technical acceptance test.

## Run

```bash
cd activity-10-recovery-tabletop
python3 activity.py
```

## Verification

Recovery gates, rollback criteria, lessons, owners and acceptance tests are complete.

The script must print `PASS`, the output file must exist, and the decision must reconcile with the supplied mock values.

## Troubleshooting

- `FileNotFoundError`: run the command from this activity folder and keep the mock-data filename unchanged.
- `JSONDecodeError`: restore valid JSON/JSONL syntax; JSONL requires one JSON object per line.
- CSV columns missing: restore the original header row before rerunning.
- Unexpected decision: compare the input value, policy threshold and rule in `activity.py`; do not edit the generated output by hand.

## Cleanup

Delete only the generated `after_action_report.md` file, then rerun the script to recreate a clean evidence artifact. The mock data and script are source files and should be retained.
