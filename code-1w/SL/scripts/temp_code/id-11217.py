import math

# Irrelevant utility function (dead code path)
def legacy_calculate(x):
    return (x ** 2 + 3 * x + 1) % 7

# Unused helper with misleading intermediate calculations
def compute_entropy(data):
    total = 0
    for item in data:
        if item > 5:
            total += math.log(item)
        else:
            total -= math.log(item + 1)
    return round(total, 4)

# Decoy dataset with plausible but unused values
historical_readings = [127, 89, 153, 201, 76, 134, 95, 118]
baseline_offsets = {i: (i * 0.92 + 17) for i in range(10)}

# Real input data
sensor_metrics = [38, 45, 72, 63, 51, 88, 29]

# Irrelevant transformation chain
temp_adjusted = [math.ceil(x * 1.08) for x in sensor_metrics]
duplicate_filtered = list(set(temp_adjusted))
duplicate_filtered.sort(reverse=True)

# Distractor: complex but unused bitwise cascade
bit_cascade = 0
for val in duplicate_filtered:
    bit_cascade ^= (val << 2) | (val >> 3)
bit_cascade = bin(bit_cascade).count('1')

# Actual processing begins here
scaling_factor = 1.75
transformed_metrics = [round(x * scaling_factor) for x in sensor_metrics]

# Simulated reference set (only this one matters)
baseline_references = {65, 77, 84, 92}

# Secondary distractor: recursive red herring
def explore_combinations(values, target=100):
    if len(values) <= 1:
        return values[0] if values else 0
    return explore_combinations(values[1:], target) + (values[0] % target)

# Another decoy structure
interim_map = {}
for idx, val in enumerate(transformed_metrics):
    interim_map[f'entry_{idx}'] = {
        'raw': val,
        'flagged': val in baseline_references or val % 6 == 0,
        'score': abs(val - 77) * 0.3
    }

# Real logic hidden among noise
def analyze_patterns(data_set, ref_set):
    count_in_ref = 0
    sum_outliers = 0
    trend_peaks = []

    # Nested logic with meaningful computation
    for i, val in enumerate(data_set):
        if val in ref_set:
            count_in_ref += 1
        elif val > 80:
            sum_outliers += val
            if i > 0 and data_set[i-1] < val:
                trend_peaks.append(val)

    # Complex but necessary condition
    adjustment = 0
    if count_in_ref >= 2:
        adjustment = int(math.sqrt(sum_outliers)) if sum_outliers > 0 else 0
    else:
        for p in trend_peaks:
            adjustment -= (p % 11)

    # Core calculation disguised as side logic
    diagnostic_weight = 0
    for v in data_set:
        diagnostic_weight += (v // 5) * (v % 7)

    # Final result computed from multiple reasoning layers
    result = diagnostic_weight - (adjustment * count_in_ref) + len(trend_peaks)
    return result

# Unused sorting operation (distractor)
sorted_diagnostics = sorted(transformed_metrics, key=lambda x: -abs(x - 75))

# Key execution point
final_diagnostic = analyze_patterns(transformed_metrics, baseline_references)

# Critical output
print(f"Result: {final_diagnostic}")