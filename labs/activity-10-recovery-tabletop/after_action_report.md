# After-action report — INC-2026-014

Recovery decision: APPROVE CANARY

## Recovery gates
- PASS — Attack regression suite: observed 0; target 0 critical successes
- PASS — Canary containment latency: observed 54s; target p95 <= 60s
- PASS — Trace completeness: observed 99.7%; target >= 99.5%

## Lessons and owners
- Untrusted invoice text lacked provenance label — Owner: Retrieval Team; due 2026-09-18; acceptance test: All retrieved chunks include trust_level and source_uri
- Destination allowlist alert was not paged — Owner: SOC Engineering; due 2026-09-16; acceptance test: SEV-1 deny produces pager notification within 60s
