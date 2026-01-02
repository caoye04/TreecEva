def analyze_redundancy(logs):
    redundant_entries = set()
    seen = set()
    for entry in logs:
        if entry in seen:
            redundant_entries.add(entry)
        else:
            seen.add(entry)
    return len(redundant_entries)

logs = ['A', 'B', 'C', 'A', 'D', 'B', 'E', 'F', 'F']
redundant_count = analyze_redundancy(logs)

inventory = {
    'sensor': 150,
    'actuator': 90,
    'controller': 45,
    'relay': 200
}

# Misleading intermediate calculations
avg_inventory = sum(inventory.values()) / len(inventory)
deviation_map = {k: abs(v - avg_inventory) for k, v in inventory.items()}
total_deviation = sum(deviation_map.values())

# Simulate shipment constraints
constraints = {
    'sensor': 25,
    'actuator': 15,
    'controller': 5,
    'relay': 40
}

# Distribution plan based on thresholds
excess_items = {}
for item, count in inventory.items():
    threshold = constraints[item]
    if count > threshold:
        excess_items[item] = count - threshold

# Complex adjustment using set logic and ratios
eligible_categories = set(inventory.keys()) - {'controller'}  # Arbitrary exclusion
adjusted_excess = {}
for cat in eligible_categories:
    if cat in excess_items:
        adjusted_excess[cat] = int(excess_items[cat] * 0.8)

# Secondary filtering based on character length of keys (red herring)
filtered_keys = {k for k in adjusted_excess.keys() if len(k) > 6}
effective_excess = sum(v for k, v in adjusted_excess.items() if k not in filtered_keys)

# Real computation path starts here
base_utilization = sum(inventory.values()) - effective_excess
scaling_factor = 0.95 if redundant_count > 2 else 1.0

# Simulated optimization function
def optimize_distribution(inv, plan):
    total = 0
    priority_multiplier = {'sensor': 1.2, 'actuator': 1.1, 'relay': 1.3}
    for item, qty in inv.items():
        if item in priority_multiplier:
            total += qty * priority_multiplier[item]
    # Apply scaling from earlier analysis
    total *= scaling_factor
    # Final adjustment based on effective excess
    total -= effective_excess * 0.5
    return int(total)

distribution_plan = [0.5, 0.3, 0.2]
final_capacity = optimize_distribution(inventory, distribution_plan)
print(f"Target result: {final_capacity}")