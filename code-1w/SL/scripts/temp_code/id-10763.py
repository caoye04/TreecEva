def analyze_temperatures(temp_readings):
    avg_temp = sum(temp_readings) / len(temp_readings)
    deviation_sum = 0
    for t in temp_readings:
        deviation_sum += abs(t - avg_temp)
    mean_deviation = deviation_sum / len(temp_readings)
    adjusted_values = [t * 0.95 + 0.5 for t in temp_readings if t > avg_temp]
    return adjusted_values, avg_temp, mean_deviation


def filter_outliers(data, threshold=2.0):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    filtered = [x for x in data if abs(x - mean) <= threshold * std_dev]
    outlier_count = len(data) - len(filtered)
    return filtered, outlier_count


def calculate_final_score(dataset):
    base_score = 0
    for i, val in enumerate(dataset):
        if i % 2 == 0:
            base_score += val * (i + 1)
        else:
            base_score -= val

    bonus = 0
    if len(dataset) > 5:
        bonus = sum(dataset[:3]) * 0.1
    
    checksum = 0
    temp_str = "".join(str(int(x)) for x in dataset)
    for char in temp_str:
        checksum += int(char) if char.isdigit() else 0
    
    # Irrelevant string manipulation
    metadata_tag = "TEMP-ANALYSIS"
    tag_parts = metadata_tag.split('-')
    code_version = len(tag_parts[0]) + len(tag_parts[1])

    # Distractor set operations
    indices_set = set(range(len(dataset)))
    even_indices = {i for i in indices_set if i % 2 == 0}
    intersection_test = even_indices & indices_set
    size_reference = len(intersection_test) * 2

    final_score = base_score + bonus + (checksum % 10)
    return final_score

# Main execution
raw_temps = [23.5, 24.1, 19.8, 25.6, 22.3, 37.1, 21.9, 20.4]
processed_data, _, _ = analyze_temperatures(raw_temps)
cleaned_data, _ = filter_outliers(processed_data, threshold=1.8)

# Simulate data alignment using zip and enumerate
aligned_pairs = list(zip(enumerate(cleaned_data), enumerate(reversed(cleaned_data))))
sum_symmetry = 0
for (i, a), (j, b) in aligned_pairs:
    sum_symmetry += abs(a - b)

# Unused auxiliary calculations
length_snapshot = len(cleaned_data)
duplicate_check = len(set(round(x, 1) for x in cleaned_data))

# Key computation
final_score = calculate_final_score(cleaned_data)
print(f"Result: {final_score}")