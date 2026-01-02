def evaluate_system_capacity(resources, limits):
    # Simulate resource evaluation with set operations and conditional filtering
    active_resources = {r for r in resources if r > 0}
    reserved = {r for r in resources if r % 3 == 0}
    available = active_resources - reserved

    scaling_factor = len(available) * 0.5
    adjustment = 0
    
    # Irrelevant computation: track unused metrics
    peak_usage = max(resources) if resources else 0
    avg_load = sum(resources) / len(resources) if resources else 0
    volatility_index = (max(resources) - min(resources)) if resources else 0

    for val in available:
        if val > 10:
            adjustment += 1
        elif val > 5:
            adjustment += 0.5

    # Misleading intermediate calculation (not used in final)
    hypothetical_growth = len(reserved) * 2.1

    base_capacity = sum(available)
    final_capacity = int(base_capacity * scaling_factor + adjustment)

    return final_capacity

# System configuration
resource_pool = [4, 9, 12, -3, 7, 6, 0, 15]
threshold_set = {3, 6, 9, 12}

# Dead code path — not invoked but present to increase cognitive load
def deprecated_capacity_calc(data):
    return sum(x**2 for x in data if x > 0) // 2

# Key execution point
final_capacity = evaluate_system_capacity(resource_pool, threshold_set)

# Output result as required
print(f"Result: {final_capacity}")