from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] + sequence[j] == 7:  # distractor: counts pairs summing to 7
                count += 1
    return count

def validate_checksum(items):
    checksum = 0
    for item in items:
        checksum ^= item * 3  # irrelevant XOR-based checksum (not used in final logic)
    return checksum > 0

def calculate_final_score(raw_data, limits):
    temp_result = []
    outlier_count = 0

    for val in raw_data:
        if val < limits['min'] or val > limits['max']:
            outlier_count += 1
        else:
            temp_result.append(val ** 0.5)  # relevant: square root of valid values
    
    # Distractor: string manipulation with numeric labels
    status_labels = ["valid" if x >= limits['min'] else "low" for x in raw_data]
    label_stats = ''.join(status_labels).count("valid")

    # Distractor: set operations not impacting final result
    unique_roots = set(round(x, 2) for x in temp_result)
    expected_roots = set(round(n**0.5, 2) for n in range(10, 50, 5))
    common_elements = unique_roots.intersection(expected_roots)

    # Distractor: unused combination logic
    if len(temp_result) >= 3:
        combo_count = len(list(combinations(temp_result, 3)))
    else:
        combo_count = 0

    # Core logic: average of transformed values, adjusted by outlier ratio
    if temp_result:
        avg_root = sum(temp_result) / len(temp_result)
        outlier_ratio = outlier_count / len(raw_data)
        adjustment = 1 - outlier_ratio  # more outliers → lower score
        final_value = avg_root * adjustment * 100
    else:
        final_value = 0

    return int(final_value)

# Main execution
sensor_readings = [12, 16, 25, 8, 36, 49, 5, 64, 10]
config = {'min': 10, 'max': 50}

# Irrelevant pre-processing step (distractor)
data_str = "data_12,data_16,data_25,data_8,data_36,data_49,data_5,data_64,data_10"
split_data = data_str.split(',')
length_check = len(split_data) == len(sensor_readings)

# Key call
final_score = calculate_final_score(sensor_readings, config)

# Additional distraction: unused recursive function
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

Result: final_score