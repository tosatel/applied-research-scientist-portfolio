from scoring import DIMENSIONS
def failures(s,t): return [d for d in DIMENSIONS if float(s[d])<t[d]]
def readiness(score,failed):
    if failed:return "remediation_required"
    if score>=.80:return "ready_for_controlled_pilot"
    if score>=.65:return "conditional_review"
    return "remediation_required"
