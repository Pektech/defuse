def match_rule(wire_states, rule):
    conds = rule.get("conditions", {})
    wire_match = conds.get("wire_states", {})
    count_match = conds.get("count_conditions", [])

    for color, cond in wire_match.items():
        actual = wire_states.get(color)
        if isinstance(cond, tuple):
            expected, is_not = cond
            if (actual == expected) == is_not:
                return False
        else:
            if actual != cond:
                return False

    for count in count_match:
        matches = list(wire_states.values()).count(count["status"])
        if "exactly" in count and matches != count["exactly"]:
            return False
        if "at_least" in count and matches < count["at_least"]:
            return False

    return True

def run_engine(wire_states, rulebook):
    for rule in rulebook:
        if match_rule(wire_states, rule):
            action = rule["action"]
            target = rule.get("target", None)
            reason = rule.get("rule_id", "an unnamed rule")
            if action == "cut":
                return f"Cut the {target} wire.\nReason: {reason}"
            elif action == "cut_random":
                return f"Cut a random wire.\nReason: {reason}"
    return "No matching rule. Kaboom!"
