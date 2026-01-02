from itertools import combinations

def analyze_pattern(seq):
    count = 0
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] + seq[j] == 7:
                count += 1
    return count

# Simulated sensor readings over time
readings = [3, 1, 4, 1, 5, 9, 2, 6]
indices = [i for i in range(len(readings)) if readings[i] % 2 == 0]

# Irrelevant pattern analysis (distractor)
distraction_pairs = list(combinations(readings, 2))
pair_sums = [a + b for a, b in distraction_pairs if a != b]
valid_sums = [s for s in pair_sums if s > 10]

# Real computation begins: frequency map of values
freq_map = {}
for val in readings:
    freq_map[val] = freq_map.get(val, 0) + 1

# Mapping index positions to rate of change
rate_map = {}
for i in range(1, len(readings)):
    delta = readings[i] - readings[i-1]
    rate_map[i] = delta * freq_map[readings[i]]

# Misleading intermediate calculation (dead logic)
temp_integral = 0
for key in rate_map:
    temp_integral += abs(rate_map[key])
    if temp_integral > 20:
        temp_integral = 0  # Reset condition never reached

# Core logic: calculate weighted flow using lambda and enumerate
evaluate_weight = lambda x, idx: x * (idx + 1) if x > 0 else x

weighted_values = []
for i, pos in enumerate(indices):
    raw_val = readings[pos]
    adjusted = evaluate_weight(raw_val, i)
    weighted_values.append(adjusted)

# Final aggregation via helper function
def calculate_net_flow(flow_rates, positions):
    total = 0.0
    for i, pos in enumerate(positions):
        if pos in flow_rates:
            contribution = flow_rates[pos] * (i + 1)
            total += contribution
        else:
            total -= 1
    return total

# Triggering statement
final_flux = calculate_net_flow(rate_map, indices)

# Print result for evaluation
print(f"Target result: {final_flux}")