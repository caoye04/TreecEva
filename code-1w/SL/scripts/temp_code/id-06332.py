from itertools import combinations

def analyze_sequence(seq, limit):
    magnitude = sum(x ** 2 for x in seq if x > 0)
    offset = len([x for x in seq if x < -5])
    temp_result = magnitude - offset * 2
    normalization_factor = max(seq) if seq else 1
    return temp_result / normalization_factor if normalization_factor != 0 else 0

def calculate_efficiency(data, thresh):
    filtered = [x for x in data if x >= thresh]
    bonus = 0
    if len(filtered) > 3:
        bonus += 10
    compression_ratio = len(data) / len(filtered) if filtered else 0
    efficiency = sum(filtered) * compression_ratio + bonus
    return int(efficiency)

# Simulate sensor readings
raw_readings = [3, -2, 7, 8, -6, 4, 1, 9]
baseline_adjustment = [x + 2 for x in raw_readings]
disregard_outliers = [x for x in baseline_adjustment if abs(x) <= 10]

# Irrelevant transformation (distractor)
permuted_pairs = list(combinations(disregard_outliers, 2))
edge_count = len([p for p in permuted_pairs if p[0] + p[1] > 12])

# Key processing path
smoothed_data = [x * 1.1 for x in disregard_outliers]
processed_data = [int(x) for x in smoothed_data if x > 0]

# Secondary distractor: unused statistical check
mean_val = sum(processed_data) / len(processed_data) if processed_data else 0
variance_proxy = sum((x - mean_val) ** 2 for x in processed_data) / len(processed_data) if processed_data else 0

threshold = 5
efficiency_score = calculate_efficiency(processed_data, threshold)

# Additional red herring
redundant_calc = ''.join(str(int(x)) for x in processed_data[:3])
status_flag = 'OK' if edge_count > 5 else 'REVIEW'

Result: {efficiency_score}