def normalize_input(data_slice):
    return [x - min(data_slice) for x in data_slice]

def apply_weighting(values, factor=1.5):
    return [round(v * factor, 2) for v in values]

def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + recursive_sum(arr[1:])

def finalize_score(scores):
    total = recursive_sum(scores)
    return round(total / len(scores), 3) if scores else 0

# Raw sensor data (simulated)
raw_data = [23, 45, 12, 67, 34, 56, 78, 89, 12, 10]

# Extract relevant segment using slicing
segment = raw_data[2:8]  # Focus on indices 2 to 7

# Normalize the segment
cleaned_values = normalize_input(segment)

# Apply dynamic weighting
weighted_values = apply_weighting(cleaned_values, factor=1.2)

# Final processing step
processed_score = finalize_score(weighted_values)

Result: processed_score