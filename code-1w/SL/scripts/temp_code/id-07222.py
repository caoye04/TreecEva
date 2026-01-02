def calculate_remaining(capacities, usage_log):
    available = set(capacities)
    used = set()
    for record in usage_log:
        if record < 0:
            continue
        used.add(record)
        if len(used) > 5:
            break
    remaining = available - used
    total = sum(remaining)
    adjustment = len(remaining) * 0.5
    final_capacity = total - adjustment
    return final_capacity

capacities = [10, 15, 20, 25, 30, 35]
usage_log = [15, -1, 20, 10, 25, 40, 30]
final_capacity = calculate_remaining(capacities, usage_log)
print(f"Result: {final_capacity}")