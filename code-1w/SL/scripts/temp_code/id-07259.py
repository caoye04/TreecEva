from itertools import combinations

def analyze_stability_factors(loads):
    stability_index = 0
    for i in range(len(loads)):
        for j in range(i + 1, len(loads)):
            if abs(loads[i] - loads[j]) > 5:
                stability_index += 1
    return stability_index

def compute_safety_margin(values):
    sorted_vals = sorted(values, reverse=True)
    margin = 0
    for idx, val in enumerate(sorted_vals):
        if val > 10:
            margin += (val * 0.1) ** idx  # Decaying contribution
    return margin

def calculate_thermal_properties(efficiencies):
    # Core computation
    base_level = sum(efficiencies)
    efficiency_pairs = list(combinations(efficiencies, 2))
    pair_boost = 0
    for a, b in efficiency_pairs:
        if (a + b) > 15:
            pair_boost += 1
    
    # Irrelevant intermediate computations (distractors)
    temp_history = [base_level * 0.1, base_level * 0.2]
    historical_offset = sum(temp_history) / len(temp_history)
    adjustment_factor = 0
    for x in temp_history:
        adjustment_factor += x ** 0.5
    adjustment_factor = adjustment_factor % 7 if adjustment_factor > 0 else 0

    # More distractions: unused recursive helper
    def recursive_dampener(n):
        if n <= 1:
            return 1
        return recursive_dampener(n-1) + recursive_dampener(n-2)
    
    dummy_trace = [recursive_dampener(3) for _ in range(3)]  # Only computes small values

    # Real signal
    non_linear_gain = len([e for e in efficiencies if e > 12])
    thermal_capacity = base_level + pair_boost * 2 + non_linear_gain * 3

    # Dead code branch (never executed but looks relevant)
    if __debug__ and False:
        debug_snapshot = {"raw": efficiencies.copy(), "boost": pair_boost}
        for k in debug_snapshot:
            pass  # Simulated logging

    return thermal_capacity

# Main execution flow
load_profile = [8, 12, 14, 9, 13]
efficiency_ratings = [x + 2 for x in load_profile if x > 8]

stability_score = analyze_stability_factors(load_profile)
safety_margin = compute_safety_margin(efficiency_ratings)

# Key statement
thermal_capacity = calculate_thermal_properties(efficiency_ratings)

Result: {thermal_capacity}