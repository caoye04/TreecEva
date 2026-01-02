def calculate_total_weight(items, modifiers):
    base_weights = {'widget': 2.5, 'gadget': 3.75, 'doohickey': 1.2}
    adjustment_map = {k.lower(): v for k, v in modifiers.items()}
    
    total = 0
    for item, count in items.items():
        normalized = item.lower().replace('_', '')
        if normalized in base_weights:
            weight = base_weights[normalized]
            if normalized in adjustment_map:
                weight += adjustment_map[normalized]
            total += weight * count
    return round(total, 3)

# Inventory data
inventory = {'Widget': 4, 'GADGET': 3, 'doohickey': 6}
adjustments = {'Widget': 0.5, 'Gadget': -0.25, 'Doohickey': 0.1}

# Irrelevant auxiliary variable (minor distraction)
summary_report = "Inventory processed on 2023-11-05"

# Key computation
total_weight = calculate_total_weight(inventory, adjustments)

print(f"Result: {total_weight}")