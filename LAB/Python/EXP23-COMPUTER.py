# Computer Fault Diagnosis using Forward Chaining

# Available facts
facts = {
    "computer_not_starting",
    "dim_screen"
}

# Production rules
rules = [
    (["computer_not_starting", "dim_screen"], "battery_problem"),
    (["battery_problem"], "battery_inspection"),
    (["battery_inspection"], "service_required")
]

# Forward Chaining
def forward_chaining(facts, rules):
    facts = set(facts)

    while True:
        new_fact = False

        for conditions, conclusion in rules:
            if all(condition in facts for condition in conditions):
                if conclusion not in facts:
                    facts.add(conclusion)
                    print("Derived Conclusion:", conclusion)
                    new_fact = True

        if not new_fact:
            break

    return facts


# Execute
print("Available Facts:")
for fact in facts:
    print("-", fact)

print("\nForward Chaining:")
final_facts = forward_chaining(facts, rules)

print("\nFinal Conclusions:")
for fact in final_facts:
    if fact not in {"computer_not_starting", "dim_screen"}:
        print("-", fact)