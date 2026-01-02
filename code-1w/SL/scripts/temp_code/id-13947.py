import math

def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    peaks = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i] > sequence[i-1] and sequence[i] > sequence[i+1]:
            peaks += 1
    return peaks

def compute_checksum(data):
    # Irrelevant helper with misleading significance
    checksum = 0
    for item in data:
        checksum ^= int(item * 10) % 256
    return checksum

def extract_features(signal):
    # Distractor: seems important but not used in final path
    magnitudes = [abs(x) for x in signal]
    avg_magnitude = sum(magnitudes) / len(magnitudes)
    peak_to_peak = max(signal) - min(signal)
    return [avg_magnitude, peak_to_peak]

def transform_sequence(raw):
    # Real transformation chain
    temp = []
    for val in raw:
        if val < 0:
            temp.append(abs(val) ** 0.5)
        else:
            temp.append(math.log(val + 1))
    normalized = [x / (max(temp) + 1e-8) for x in temp]
    shifted = [x * 100 for x in normalized]
    return shifted

def evaluate_stability(profile):
    # Dead-end function - looks useful but unused
    if not profile:
        return -1
    variance = sum((x - sum(profile)/len(profile))**2 for x in profile) / len(profile)
    return 1 if variance < 10 else 0

def filter_outliers(dataset, limit=75):
    # Partially relevant but mostly distraction
    filtered = []
    for x in dataset:
        if x <= limit:
            filtered.append(x)
    return filtered if len(filtered) > 0 else dataset

def process_signal(data, cutoff):
    # Core logic embedded in noise
    count = 0
    total = 0.0
    flag_mode = False

    # Irrelevant pre-check
    if sum(1 for x in data if x > 50) > 10:
        flag_mode = True

    for value in data:
        if value > cutoff:
            total += value * 0.85
            count += 1
        elif value > 10 and str(int(value)).endswith('3'):
            # Rare condition - red herring
            total += value * 0.1
        else:
            continue

    if count == 0:
        return 0

    average_contribution = total / count

    # Final adjustment using string manipulation (required feature)
    code_suffix = "_adj"
    adjustment_key = f"{int(average_contribution)}{code_suffix}"
    adjustment_factor = len(adjustment_key) % 4  # depends on length

    result = average_contribution + adjustment_factor

    # Lambda for no real effect - just misdirection
    finalize = lambda x: round(x, 2) if x > 0 else 0
    return finalize(result)

# Main execution with multiple decoys
raw_input = [2.7, 5.1, -3.4, 8.9, -1.2, 15.6, 0.8, 23.4, 7.2, 41.3, 3.9, 6.6, 9.1, 12.8, 18.7]

# Irrelevant preprocessing chain
checksum_value = compute_checksum(raw_input)
feature_set = extract_features(raw_input)
stability_score = evaluate_stability(feature_set)

# Real data flow begins here
transformed_data = transform_sequence(raw_input)
filtered_data = filter_outliers(transformed_data, 75)

# Unused variables to increase interference
baseline_ref = sum(transformed_data) / len(transformed_data)
peak_count = analyze_pattern(transformed_data)
dummy_flag = any(x > 100 for x in transformed_data)

# Key control variable obscured among others
threshold = 45

# Critical assignment - answer derived here
final_output = process_signal(transformed_data, threshold)

# Print required output
print(f"Result: {final_output}")