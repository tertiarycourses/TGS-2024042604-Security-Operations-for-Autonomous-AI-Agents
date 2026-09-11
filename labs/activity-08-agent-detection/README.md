# Activity 08 — Detect Suspicious Agent Behaviour

**Criteria:** A7  
**Duration:** 60–90 minutes  
**Mode:** Individual, offline simulation using synthetic data only

## Objective

Create `detections.json` from `mock_events.jsonl` and use the evidence to make a defensible security-operations decision.

## Files

- `activity.py` — runnable Python 3 script; standard library only.
- `mock_events.jsonl` — synthetic activity data; it contains no live credentials or personal data.
- `detections.json` — generated evidence artifact after the script runs.

![Activity 08 execution workflow](workflow.png)

## Procedure

1. Inspect the JSONL event sequence by trace_id.
2. Run python3 activity.py.
3. Open detections.json and explain every correlated signal.
4. Add a benign event and confirm it does not create a new alert.
5. State the minimum evidence an analyst needs before containment.

## Run

```bash
cd activity-08-agent-detection
python3 activity.py
```

## Verification

The detector finds abnormal tool rates, new destinations, blocked actions and sensitive-read/egress chains.

The script must print `PASS`, the output file must exist, and the decision must reconcile with the supplied mock values.

## Troubleshooting

- `FileNotFoundError`: run the command from this activity folder and keep the mock-data filename unchanged.
- `JSONDecodeError`: restore valid JSON/JSONL syntax; JSONL requires one JSON object per line.
- CSV columns missing: restore the original header row before rerunning.
- Unexpected decision: compare the input value, policy threshold and rule in `activity.py`; do not edit the generated output by hand.

## Cleanup

Delete only the generated `detections.json` file, then rerun the script to recreate a clean evidence artifact. The mock data and script are source files and should be retained.
