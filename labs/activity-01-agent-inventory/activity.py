#!/usr/bin/env python3
"""Offline learner activity for Security Operations for Autonomous AI Agents."""
from pathlib import Path
import csv, json, sys

MODE = 1
INPUT = "mock_agents.json"
OUTPUT = "agent_security_baseline.md"
ROOT = Path(__file__).resolve().parent

def load():
    path = ROOT / INPUT
    if path.suffix == ".jsonl":
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if path.suffix == ".json":
        return json.loads(path.read_text(encoding="utf-8"))
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def save_json(obj):
    (ROOT / OUTPUT).write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")

def run(data):
    if MODE == 1:
        rows=[]
        for a in data:
            gaps=[]
            for field in ("owner","purpose","model","tools","data_classes","risk_tier"):
                if not a.get(field): gaps.append(field)
            objective=f"Protect {a.get('purpose') or 'unowned activity'} with owner, least privilege, data controls and auditable stop criteria."
            rows.append((a["agent_id"], a.get("owner") or "MISSING", a["risk_tier"], ", ".join(gaps) or "none", objective))
        text=["# Agent security baseline","", "| Agent | Owner | Tier | Gaps | Measurable objective |","|---|---|---:|---|---|"]
        text += [f"| {a} | {o} | {r} | {g} | {obj} |" for a,o,r,g,obj in rows]
        (ROOT/OUTPUT).write_text("\n".join(text)+"\n",encoding="utf-8")
    elif MODE == 2:
        findings=[]
        for f in data["flows"]:
            missing=[x for x in ("authn","authz","encrypted","logged") if not f[x]]
            score=min(25, 5+5*len(missing))
            findings.append({**f,"missing_controls":missing,"risk_score":score,"decision":"remediate" if missing else "accept"})
        save_json({"zones":data["zones"],"findings":findings})
    elif MODE == 3:
        allowed_tools={"agent-fin-01":{"invoice_read","ledger_write"},"agent-hr-02":{"policy_search"}}
        rows=[]
        for r in data:
            reasons=[]
            if r["tool"] not in allowed_tools.get(r["agent_id"],set()): reasons.append("tool_not_allowed")
            if r["data_class"]=="restricted" and r["action"]!="read": reasons.append("restricted_action")
            if r["destination"]=="external" and r["data_class"]!="public": reasons.append("egress_classification")
            if r["action"] in {"delete","execute"} and not r["approval_id"]: reasons.append("approval_required")
            rows.append({**r,"decision":"deny" if reasons else "allow","reasons":";".join(reasons) or "policy_match"})
        with (ROOT/OUTPUT).open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    elif MODE == 4:
        ev={e["control_id"]:e for e in data["evidence"]}; out=["# Compliance evidence report",""]
        out += ["| Control | Requirement | Owner | Evidence | Status |","|---|---|---|---|---|"]
        for c in data["requirements"]:
            e=ev.get(c["control_id"]); status="missing" if not e else ("stale" if e["age_days"]>c["max_age_days"] else e["status"])
            out.append(f"| {c['control_id']} | {c['requirement']} | {c['owner']} | {e['evidence_id'] if e else '-'} | {status} |")
        (ROOT/OUTPUT).write_text("\n".join(out)+"\n",encoding="utf-8")
    elif MODE == 5:
        cards=[]
        for m in data:
            val=float(m["value"]); target=float(m["threshold"])
            good = val >= target if "coverage" in m["metric"] else val <= target
            cards.append(f"<article class='{ 'ok' if good else 'alert'}'><h2>{m['metric'].replace('_',' ')}</h2><p>{m['value']} {m['unit']} / target {m['threshold']}</p><p>Owner: {m['owner']} · Due: {m['due']} · Audience: {m['audience']}</p></article>")
        html="<html><style>body{font:16px Arial;margin:40px;background:#f5f8fc}article{padding:18px;margin:14px;border-left:8px solid}.ok{border-color:#10b981}.alert{border-color:#f97316}</style><body><h1>Agent Security Posture</h1>"+"".join(cards)+"</body></html>"
        (ROOT/OUTPUT).write_text(html,encoding="utf-8")
    elif MODE == 6:
        rows=[]
        for r in data:
            inherent=float(r["frequency_per_year"])*float(r["loss_sgd"])
            residual=inherent*(1-float(r["control_effectiveness_pct"])/100)
            rows.append({**r,"inherent_expected_loss_sgd":f"{inherent:.2f}","residual_expected_loss_sgd":f"{residual:.2f}","decision":"treat" if residual>float(r["appetite_sgd"]) else "monitor"})
        with (ROOT/OUTPUT).open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    elif MODE == 7:
        budget=40000; ranked=[]
        for g in data:
            score=int(g["severity"])*int(g["risk_reduction"])/(int(g["cost_sgd"])/1000)
            if g["overdue"].lower()=="true": score*=1.25
            ranked.append((score,g))
        ranked.sort(reverse=True,key=lambda x:x[0]); chosen=[]; spent=0
        for score,g in ranked:
            cost=int(g["cost_sgd"])
            if spent+cost<=budget: chosen.append((score,g)); spent+=cost
        out=["# Security gap remediation roadmap","",f"Mock budget: SGD {budget:,}; selected spend: SGD {spent:,}","","| Priority | Gap | Score | Cost | Acceptance focus |","|---:|---|---:|---:|---|"]
        out += [f"| {i} | {g['gap_id']} — {g['gap']} | {score:.1f} | SGD {int(g['cost_sgd']):,} | Close dependency: {g['dependency']} |" for i,(score,g) in enumerate(chosen,1)]
        (ROOT/OUTPUT).write_text("\n".join(out)+"\n",encoding="utf-8")
    elif MODE == 8:
        alerts=[]; by_trace={}
        for e in data: by_trace.setdefault(e["trace_id"],[]).append(e)
        for trace,events in by_trace.items():
            denies=sum(e["decision"]=="deny" for e in events)
            unknown=any(e["destination"] not in {"internal","api.approved.example"} for e in events)
            read_sensitive=any(e["event_type"]=="data_read" and e["data_class"] in {"confidential","restricted"} for e in events)
            outbound=any(e["destination"]!="internal" for e in events)
            reasons=[]
            if denies>=2: reasons.append("repeated_denials")
            if unknown: reasons.append("new_destination")
            if read_sensitive and outbound: reasons.append("sensitive_read_then_egress")
            if reasons: alerts.append({"trace_id":trace,"agent_id":events[0]["agent_id"],"severity":"high","reasons":reasons})
        save_json({"alerts":alerts,"event_count":len(data)})
    elif MODE == 9:
        base=data["detected_at"]
        actions=[{"sequence":1,"action":"disable_agent","status":"confirmed"},{"sequence":2,"action":"revoke_tokens","status":"confirmed"},{"sequence":3,"action":"block_destination","target":data["destination"],"status":"confirmed"},{"sequence":4,"action":"preserve_evidence","trace_id":data["trace_id"],"status":"confirmed"}]
        save_json({"incident_id":data["incident_id"],"severity":data["severity"],"detected_at":base,"agent_id":data["agent_id"],"containment_actions":actions,"safe_to_investigate":True})
    elif MODE == 10:
        passed=all(g["pass"] for g in data["recovery_gates"]); out=[f"# After-action report — {data['incident_id']}","",f"Recovery decision: {'APPROVE CANARY' if passed else 'BLOCK'}","", "## Recovery gates"]
        out += [f"- {'PASS' if g['pass'] else 'FAIL'} — {g['gate']}: observed {g['observed']}; target {g['target']}" for g in data["recovery_gates"]]
        out += ["","## Lessons and owners"]+[f"- {x['gap']} — Owner: {x['owner']}; due {x['due']}; acceptance test: {x['acceptance_test']}" for x in data["lessons"]]
        (ROOT/OUTPUT).write_text("\n".join(out)+"\n",encoding="utf-8")

if __name__ == "__main__":
    run(load())
    out=ROOT/OUTPUT
    assert out.exists() and out.stat().st_size>20, "output was not created"
    print(f"PASS: created {out.name} ({out.stat().st_size} bytes)")
