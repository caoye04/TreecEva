import math

# Irrelevant helper function (dead code path)
def calculate_noise_level(signal):
    return sum([abs(s) ** 2 for s in signal]) * 0.05

# Misleading intermediate function with decoy logic
def evaluate_stability_index(data):
    if len(data) == 0:
        return 0
    variance = sum([(x - sum(data)/len(data))**2 for x in data]) / len(data)
    return variance < 5  # Red herring: never actually used in final logic

# Decoy data structure
turbine_output_history = [
    [120, 125, 130, 118],
    [140, 138, 142, 139],
    [150, 155, 153, 151]
]

# Unused but plausible-looking accumulator
baseline_offset = 0
for i in range(3):
    baseline_offset += turbine_output_history[i][0] % 7

# Core problem: energy grid optimization
grid_load = [45, 67, 34, 89, 54, 76, 23, 65]
reserves = [12, 18, 15, 20]
system_flags = [True, False, True]

# Irrelevant transformation (slicing distraction)
windowed_data = grid_load[2:6:2]  # Extracts [34, 89]

# Distractor: complex-looking but unused calculation
aggregate_risk = 0
for flag in system_flags:
    aggregate_risk += int(flag) * 3
aggregate_risk = math.sqrt(aggregate_risk) if aggregate_risk > 5 else 0

# Key function: optimization using list comprehension and slicing
def optimize_distribution(load, reserve):
    # Step 1: Normalize load using moving average (slicing)
    smoothed = []
    for i in range(2, len(load)):
        window_avg = sum(load[i-2:i+1]) / 3
        smoothed.append(window_avg)
    
    # Step 2: Apply correction factor based on reserve levels
    total_reserve = sum(reserve)
    adjustment_factor = math.log(total_reserve + 1) / 2.5
    
    # Step 3: Correct smoothed values with adjusted reserve weighting
    corrected = [val * adjustment_factor for val in smoothed]
    
    # Step 4: Apply threshold filtering (simulates load shedding)
    filtered = [val for val in corrected if val > 30]
    
    # Step 5: Final capacity determined by summing filtered results
    final_capacity = sum(filtered)
    
    # Step 6: Additional constraint — limit based on first two reserve elements
    cap_limit = (reserve[0] + reserve[1]) * 3.2
    
    # Step 7: Enforce cap only if more than 3 values passed filter
    if len(filtered) > 3:
        final_capacity = min(final_capacity, cap_limit)
    
    # Step 8: Add bonus if middle slice of original load has increasing trend
    mid_slice = load[3:6]  # [89, 54, 76]
    if mid_slice[2] > mid_slice[1] > mid_slice[0] - 20:
        final_capacity += 8.5  # Small bonus for partial recovery
    
    return final_capacity

# Unused recursive attempt (red herring)
def predict_future_load(data, depth=0):
    if depth >= 2 or len(data) < 2:
        return data
    return predict_future_load([data[i+1] - data[i] for i in range(len(data)-1)], depth+1)

# Execution point of interest
energy_capacity = optimize_distribution(grid_load, reserves)

# Print required result
print(f"Target result: {energy_capacity}")