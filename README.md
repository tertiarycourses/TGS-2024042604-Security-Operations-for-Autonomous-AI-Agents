# Security Operations for Autonomous AI Agents

Learner-safe courseware and hands-on Activities for **TGS-2024042604**, delivered by Tertiary Infotech Academy Pte Ltd.

## Course at a glance

- Duration: 4 days, 32 training hours
- Level: Intermediate
- TSC: Security Strategy, ICT-SNA-5021-1.1
- Delivery: instructor-led learning with offline, synthetic-data Activities
- Official course page: [WSQ Security Operations for Autonomous AI Agents](https://www.tertiarycourses.com.sg/wsq-security-operations-for-autonomous-ai-agents.html)

The course develops the ability to set autonomous-agent security goals and standards, manage policy and compliance, evaluate risks and control value, remediate gaps, and operate organisation-wide monitoring and incident response.

## Courseware

- [PowerPoint deck](courseware/Security%20Operations%20for%20Autonomous%20AI%20Agents-v1.0.pptx) — 454 highly visual slides with native charts, architectures, runtime traces, contracts, evidence patterns, and case activities
- [Learner slides PDF](courseware/Security%20Operations%20for%20Autonomous%20AI%20Agents-v1.0.pdf)
- [Learner Guide DOCX](courseware/LG-Security%20Operations%20for%20Autonomous%20AI%20Agents.docx) and [PDF](courseware/LG-Security%20Operations%20for%20Autonomous%20AI%20Agents.pdf)
- [Lesson Plan DOCX](courseware/LP-Security%20Operations%20for%20Autonomous%20AI%20Agents.docx) and [PDF](courseware/LP-Security%20Operations%20for%20Autonomous%20AI%20Agents.pdf)

## Hands-on Activities

Each Activity has its own folder with a detailed README, executable `activity.py`, synthetic mock data, a workflow image, and a reproducible evidence output. Python 3.10 or later is sufficient; no external package, credential, API, or production system is required.

1. [Agent inventory and security objectives](labs/activity-01-agent-inventory/README.md)
2. [Trust-boundary threat model](labs/activity-02-trust-boundary-threat-model/README.md)
3. [Tool and data guardrails](labs/activity-03-policy-as-code/README.md)
4. [Compliance evidence pack](labs/activity-04-compliance-evidence/README.md)
5. [Security posture communication](labs/activity-05-security-communication/README.md)
6. [Risk and control-value evaluation](labs/activity-06-risk-control-evaluation/README.md)
7. [Security-gap remediation roadmap](labs/activity-07-gap-remediation/README.md)
8. [Suspicious agent-behaviour detection](labs/activity-08-agent-detection/README.md)
9. [Prompt-injection containment](labs/activity-09-prompt-injection-response/README.md)
10. [Recovery and post-incident review](labs/activity-10-recovery-tabletop/README.md)

Run an Activity from its folder:

```bash
cd labs/activity-01-agent-inventory
python3 activity.py
```

## Safety and privacy

All data is synthetic. The public repository deliberately excludes assessment papers, answer keys, source references, local configuration, and build tooling. Trainer answer keys are never published to learner-facing GitHub, Drive, or LMS fields.

## Technical references

The courseware incorporates the supplied reference corpus and aligns its controls and evidence patterns with the [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), [OWASP Agentic AI Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/), and [MITRE ATLAS](https://atlas.mitre.org/).

