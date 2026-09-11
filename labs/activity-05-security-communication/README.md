# Activity 05 — Communicate Agent Security Posture

**Criteria:** A4  
**Duration:** 60–90 minutes  
**Mode:** Individual, offline simulation using synthetic data only

## Objective

Create `security_brief.html` from `mock_metrics.csv` and use the evidence to make a defensible security-operations decision.

## Files

- `activity.py` — runnable Python 3 script; standard library only.
- `mock_metrics.csv` — synthetic activity data; it contains no live credentials or personal data.
- `security_brief.html` — generated evidence artifact after the script runs.

![Activity 05 execution workflow](workflow.png)

## Procedure

1. Review the mock metrics, thresholds, audiences and owners.
2. Run python3 activity.py.
3. Open security_brief.html in a browser.
4. Separate the technical response from the risk-committee decision.
5. Write one action, owner and due date for every threshold breach.

## Run

```bash
cd activity-05-security-communication
python3 activity.py
```

## Verification

The generated brief shows thresholds, current values, decisions, owners and due dates for two audiences.

The script must print `PASS`, the output file must exist, and the decision must reconcile with the supplied mock values.

## Troubleshooting

- `FileNotFoundError`: run the command from this activity folder and keep the mock-data filename unchanged.
- `JSONDecodeError`: restore valid JSON/JSONL syntax; JSONL requires one JSON object per line.
- CSV columns missing: restore the original header row before rerunning.
- Unexpected decision: compare the input value, policy threshold and rule in `activity.py`; do not edit the generated output by hand.

## Cleanup

Delete only the generated `security_brief.html` file, then rerun the script to recreate a clean evidence artifact. The mock data and script are source files and should be retained.
