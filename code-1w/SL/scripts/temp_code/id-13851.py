def analyze_pattern(sequence):
    """Irrelevant helper function for pattern detection (dead code path)."""
    if len(sequence) < 5:
        return False
    cumulative = 0
    for item in sequence:
        if item % 3 == 0:
            cumulative += item ** 2
    return cumulative > 100

# Misleading data initialization (distractor)
initial_readings = [i * i - 2 for i in range(10, 18)]
temp_buffer = {x: x % 7 for x in initial_readings}

# Real data structures
rate_map = {
    'alpha': 12, 'beta': 18, 'gamma': 15,
    'delta': 21, 'epsilon': 9
}

threshold_set = set()
for key, value in rate_map.items():
    if 'a' in key:
        threshold_set.add(value // 3)
    elif 'e' in key:
        threshold_set.add(value // 4)

# Decoy transformation chain (irrelevant)
transformed = []
x = 5
while x < 30:
    x += 7
    transformed.append(x * 2)
    if x > 25:
        break

# Unused but plausible-looking computation
aggregated = sum([v for v in rate_map.values() if v % 3 == 0])
scaling_factor = 1.5
adjusted_total = aggregated * scaling_factor  # Never used

# Conditional expression with red herring branch
status_flag = 'active' if len(threshold_set) > 2 else 'standby'

# Core logic disguised among distractions
def compute_density(param):
    return param * param // 2

def evaluate_pressure(rates):
    total = 0
    for val in rates.values():
        if val > 10:
            total += compute_density(val)
    return total

def calculate_stable_flow(data, limits):
    base = evaluate_pressure(data)
    modifier = 1
    for limit in sorted(limits, reverse=True):
        if limit < 5:
            modifier *= 2
    # Critical early return that bypasses decoy math below
    if modifier > 100:
        return -999

    adjustment = 0
    temp_vals = []
    for k, v in data.items():
        if len(k) % 2 == 0 and v in limits:
            adjustment += v
        temp_vals.append(v * modifier)

    # Actual answer depends on base and adjustment only
    final_component = base + adjustment

    # Dead code path (never reached due to logic above)
    redundant_sum = sum(temp_vals)
    if redundant_sum < 0:
        return redundant_sum * 10

    return final_component

# Key execution point
final_flux = calculate_stable_flow(rate_map, threshold_set)
print(f"Result: {final_flux}")