# Activity 01 — Build an Agent Inventory and Security Objectives

**Criteria:** A1  
**Duration:** 60–90 minutes  
**Mode:** Individual, offline simulation using synthetic data only

## Objective

Create `agent_security_baseline.md` from `mock_agents.json` and use the evidence to make a defensible security-operations decision.

## Files

- `activity.py` — runnable Python 3 script; standard library only.
- `mock_agents.json` — synthetic activity data; it contains no live credentials or personal data.
- `agent_security_baseline.md` — generated evidence artifact after the script runs.

![Activity 01 execution workflow](workflow.png)

## Procedure

1. Open mock_agents.json and identify the missing governance fields.
2. Run python3 activity.py.
3. Open agent_security_baseline.md and compare risk tiers with tools and data classes.
4. Define a measurable objective for each active agent.
5. Flag any unowned or experimental active agent for treatment.

## Run

```bash
cd activity-01-agent-inventory
python3 activity.py
```

## Verification

All active agents have an owner, purpose, data class, risk tier and measurable security objective.

The script must print `PASS`, the output file must exist, and the decision must reconcile with the supplied mock values.

## Troubleshooting

- `FileNotFoundError`: run the command from this activity folder and keep the mock-data filename unchanged.
- `JSONDecodeError`: restore valid JSON/JSONL syntax; JSONL requires one JSON object per line.
- CSV columns missing: restore the original header row before rerunning.
- Unexpected decision: compare the input value, policy threshold and rule in `activity.py`; do not edit the generated output by hand.

## Cleanup

Delete only the generated `agent_security_baseline.md` file, then rerun the script to recreate a clean evidence artifact. The mock data and script are source files and should be retained.
