# Security Operations for Autonomous AI Agents

Set, govern and operate security for autonomous AI agents — from security strategy and policy to risk evaluation, monitoring and incident response — through ten offline, synthetic-data activities.

| Course detail | Information |
|---|---|
| Course code | `TGS-2024042604` |
| Programme | WSQ |
| Duration | 4 days, 32 hours (including 2 hours of assessment) |
| Level | Intermediate |
| Skills framework | Security Strategy, ICT-SNA-5021-1.1 |
| Registration | [View course details and register](https://www.tertiarycourses.com.sg/wsq-security-operations-for-autonomous-ai-agents.html) |
| Funding | Up to 50% SkillsFuture course fee funding, or up to 70% for eligible SME employees and Singapore Citizens aged 40 and above. Eligibility and terms apply. |
| Courseware | Version 1.0 |

## About the course

The course develops the ability to set autonomous-agent security goals and standards, manage policy and compliance, evaluate risks and control value, remediate gaps, and operate organisation-wide monitoring and incident response. Delivery is instructor-led with offline, synthetic-data activities.

## Learning outcomes

- LO1: Formulate comprehensive security goals and establish business standards with an overarching security vision for autonomous AI agents.
- LO2: Communicate effective agent-security policies and practices, and manage compliance with best practices and technological advancements.
- LO3: Evaluate existing agent-security controls against business risks and costs, and develop strategies to resolve identified security gaps.
- LO4: Implement organisation-wide agent-security initiatives, assessing and addressing the impact of security gaps.

## Topics covered

1. Security Strategy and Standards for Autonomous AI Agents
2. Agent Security Policies, Governance and Compliance
3. AI Agent Risk Assessment and Security Control Evaluation
4. Implementing and Monitoring Organisation-Wide Agent Security Operations

## Courseware

- [PowerPoint deck](courseware/Security%20Operations%20for%20Autonomous%20AI%20Agents-v1.0.pptx) — 454 highly visual slides with native charts, architectures, runtime traces, contracts, evidence patterns, and case activities
- [Learner slides PDF](courseware/Security%20Operations%20for%20Autonomous%20AI%20Agents-v1.0.pdf)
- [Learner Guide DOCX](courseware/LG-Security%20Operations%20for%20Autonomous%20AI%20Agents.docx) and [PDF](courseware/LG-Security%20Operations%20for%20Autonomous%20AI%20Agents.pdf)
- [Lesson Plan DOCX](courseware/LP-Security%20Operations%20for%20Autonomous%20AI%20Agents.docx) and [PDF](courseware/LP-Security%20Operations%20for%20Autonomous%20AI%20Agents.pdf)
- [Learner Guide Markdown](LG-Security%20Operations%20for%20Autonomous%20AI%20Agents.md)

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

All data is synthetic. The public repository deliberately excludes assessment papers, answer keys, the Facilitator Guide, the Assessment Plan, source references, local configuration, and build tooling. Trainer answer keys are never published to learner-facing GitHub, Drive, or LMS fields.

## Technical references

The courseware incorporates the supplied reference corpus and aligns its controls and evidence patterns with the [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), [OWASP Agentic AI Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/), and [MITRE ATLAS](https://atlas.mitre.org/).

---

[Course page and registration](https://www.tertiarycourses.com.sg/wsq-security-operations-for-autonomous-ai-agents.html) · Courseware developed and delivered by **Tertiary Infotech Academy Pte Ltd**.
