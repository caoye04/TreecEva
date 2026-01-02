def optimize_capacity(loads, threshold):
    filtered_loads = {load for load in loads if load > threshold}
    adjusted = [load // 2 + (load % 2) for load in filtered_loads]
    total = sum(adjusted)
    peak = max(adjusted) if adjusted else 0
    normalizer = 2 if total > 100 else 1
    return total // normalizer

# System load parameters
base_threshold = 15
loads = [12, 18, 22, 9, 30, 14, 25]

# Irrelevant auxiliary variable (minimal distraction)
current_status = "active"

# Key computation
final_capacity = optimize_capacity(loads, base_threshold)

print(f"Result: {final_capacity}")