from collections import Counter, defaultdict
import math

def calculate_route_efficiency(weight_freq):
    efficiency = {}
    for weight, freq in weight_freq.items():
        if weight > 0:
            efficiency[weight] = freq * math.log(weight) / weight
    return efficiency

# Initial package weights collected from 3 warehouses
warehouse_a_weights = [10, 20, 10, 30, 20, 10]
warehouse_b_weights = [15, 15, 25, 30, 15]
warehouse_c_weights = [10, 20, 25, 25, 30, 30, 30]

# Count frequencies using Counter
freq_counter = Counter()
for weights in [warehouse_a_weights, warehouse_b_weights, warehouse_c_weights]:
    freq_counter.update(weights)

# Calculate base delivery cost using greedy approach on frequency
base_cost = sum(count * weight for weight, count in freq_counter.items())

# Apply dynamic programming correction factor
correction_factor = {}
for weight in sorted(freq_counter.keys()):
    if weight not in correction_factor:
        correction_factor[weight] = 0
    for prev_weight in correction_factor:
        if prev_weight < weight:
            candidate = correction_factor[prev_weight] + abs(weight - prev_weight) * freq_counter[weight]
            if correction_factor[weight] == 0 or candidate < correction_factor[weight]:
                correction_factor[weight] = candidate

total_correction = sum(correction_factor.values())

# Efficiency metrics dictionary comprehension and merging
route_efficiency = calculate_route_efficiency(freq_counter)
improved_efficiency = {w: e + 0.1 for w, e in route_efficiency.items() if w >= 20}
route_efficiency = {**route_efficiency, **improved_efficiency}

# Final cost calculation with combinatorics adjustment
unique_weights = list(freq_counter.keys())
combinations_count = len(unique_weights) * (len(unique_weights) - 1) // 2
statistical_modifier = sum(route_efficiency.values()) / len(route_efficiency)

optimized_delivery_cost = int(base_cost - total_correction + combinations_count * statistical_modifier)
print(f"Result: {optimized_delivery_cost}")