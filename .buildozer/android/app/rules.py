rulebook = [
    {
        "rule_id": "Rule 1",
        "conditions": {
            "wire_states": {"red": ("frayed", False), "yellow": ("loose", False)}
        },
        "action": "cut",
        "target": "black",
    },
    {
        "rule_id": "Rule 2",
        "conditions": {
            "count_conditions": [{"status": "good", "at_least": 2}],
            "wire_states": {"red": ("loose", True)},
        },
        "action": "cut",
        "target": "red",
    },
    {
        "rule_id": "Rule 3",
        "conditions": {
            "wire_states": {"blue": ("scorched", False), "yellow": ("good", False)}
        },
        "action": "cut",
        "target": "yellow",
    },
    {
        "rule_id": "Rule 4",
        "conditions": {
            "wire_states": {"black": ("loose", False)},
            "count_conditions": [{"status": "frayed", "at_least": 2}],
        },
        "action": "cut",
        "target": "blue",
    },
    {
        "rule_id": "Rule 5",
        "conditions": {
            "wire_states": {
                "red": "frayed",
                "blue": "loose",
                "yellow": "good",
                "black": "scorched",
            }
        },
        "action": "cut",
        "target": "red",
    },
    {
        "rule_id": "Rule 6",
        "conditions": {
            "wire_states": {"red": ("loose", False), "black": ("good", False)}
        },
        "action": "cut",
        "target": "blue",
    },
    {
        "rule_id": "Rule 7",
        "conditions": {"count_conditions": [{"status": "scorched", "exactly": 3}]},
        "action": "cut",
        "target": "yellow",
    },
    {
        "rule_id": "Rule 8",
        "conditions": {
            "wire_states": {
                "red": "loose",
                "yellow": "frayed",
                "blue": "good",
                "black": "scorched",
            }
        },
        "action": "cut",
        "target": "black",
    },
    {
        "rule_id": "Rule 9",
        "conditions": {"count_conditions": [{"status": "good", "exactly": 0}]},
        "action": "cut",
        "target": "black",
    },
    {
        "rule_id": "Rule 10",
        "conditions": {
            "wire_states": {"red": "scorched"},
            "count_conditions": [{"status": "loose", "exactly": 1}],
        },
        "action": "cut",
        "target": "blue",
    },
    {
        "rule_id": "Rule 11",
        "conditions": {"wire_states": {"yellow": "scorched", "red": "good"}},
        "action": "cut",
        "target": "black",
    },
    {
        "rule_id": "Rule 12",
        "conditions": {"wire_states": {"blue": "frayed", "black": "scorched"}},
        "action": "cut",
        "target": "red",
    },
    {
        "rule_id": "Rule 13",
        "conditions": {
            "wire_states": {"red": "loose", "black": ("frayed", True)},
            "count_conditions": [{"status": "scorched", "at_least": 2}],
        },
        "action": "cut",
        "target": "yellow",
    },
    {
        "rule_id": "Rule 14",
        "conditions": {
            "wire_states": {
                "red": "good",
                "black": "loose",
                "yellow": "frayed",
                "blue": ("good", True),
            }
        },
        "action": "cut",
        "target": "blue",
    },
    {
        "rule_id": "Rule 15",
        "conditions": {
            "wire_states": {"yellow": "good", "blue": "loose", "red": ("frayed", True)}
        },
        "action": "cut",
        "target": "red",
    },
    {
        "rule_id": "Rule 16",
        "conditions": {
            "wire_states": {"red": "frayed", "blue": "loose", "yellow": "scorched"}
        },
        "action": "cut",
        "target": "yellow",
    },
    {
        "rule_id": "Rule 17",
        "conditions": {"count_conditions": [{"status": "good", "exactly": 4}]},
        "action": "cut_random",
        "target": None,
    },
]
