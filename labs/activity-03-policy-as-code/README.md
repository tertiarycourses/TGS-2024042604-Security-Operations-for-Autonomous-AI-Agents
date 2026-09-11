# Activity 03 — Enforce Tool and Data Guardrails

**Criteria:** A2, A3  
**Duration:** 60–90 minutes  
**Mode:** Individual, offline simulation using synthetic data only

## Objective

Create `policy_decisions.csv` from `mock_requests.json` and use the evidence to make a defensible security-operations decision.

## Files

- `activity.py` — runnable Python 3 script; standard library only.
- `mock_requests.json` — synthetic activity data; it contains no live credentials or personal data.
- `policy_decisions.csv` — generated evidence artifact after the script runs.

![Activity 03 execution workflow](workflow.png)

## Procedure

1. Inspect the mock requests and identify tool, data, egress and approval risks.
2. Run python3 activity.py.
3. Open policy_decisions.csv and trace each deny reason to a policy condition.
4. Create one additional unauthorised request and rerun.
5. Verify deny-by-default behavior and auditable reason codes.

## Run

```bash
cd activity-03-policy-as-code
python3 activity.py
```

## Verification

Allowed requests execute; restricted data, unlisted tools and missing approvals are denied with reasons.

The script must print `PASS`, the output file must exist, and the decision must reconcile with the supplied mock values.

## Troubleshooting

- `FileNotFoundError`: run the command from this activity folder and keep the mock-data filename unchanged.
- `JSONDecodeError`: restore valid JSON/JSONL syntax; JSONL requires one JSON object per line.
- CSV columns missing: restore the original header row before rerunning.
- Unexpected decision: compare the input value, policy threshold and rule in `activity.py`; do not edit the generated output by hand.

## Cleanup

Delete only the generated `policy_decisions.csv` file, then rerun the script to recreate a clean evidence artifact. The mock data and script are source files and should be retained.
