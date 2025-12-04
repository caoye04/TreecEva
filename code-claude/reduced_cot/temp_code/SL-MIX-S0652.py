from itertools import takewhile

def filter_sequence(values, threshold):
    return list(takewhile(lambda x: x <= threshold, values))

# Dataset of student exam scores
exam_scores = [72, 85, 91, 64, 78, 95, 88, 76, 83]

# Reference passing scores from previous years
passing_thresholds = [75, 80, 85, 90]

# Apply filter to get scores below a certain threshold
max_filter = 90
filtered_data = filter_sequence(sorted(exam_scores), max_filter)

# Check which filtered scores match our reference passing thresholds
reference_values = passing_thresholds
common_elements = len(set(filtered_data) & set(reference_values))

# Generate summary statistics
average_score = sum(filtered_data) / len(filtered_data)
median_index = len(filtered_data) // 2

print(f"Result: {common_elements}")