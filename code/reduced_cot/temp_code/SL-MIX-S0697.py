import math
import re
from functools import reduce

def normalize_intensity(value):
    return math.log(max(1e-10, value))  # Avoid log(0)

def adjust_precision(val):
    return round(val, 4)

def categorize_frequency(log_val):
    category_map = {
        'low': (-float('inf'), -2),
        'medium': (-2, 1),
        'high': (1, float('inf'))
    }
    for cat, (low, high) in category_map.items():
        if low <= log_val < high:
            return cat
    return 'unknown'

# Raw seismic intensity measurements
seismic_data = [0.001, 0.5, 2.3, 10.0, 100.0]

# Step 1: Apply logarithmic normalization
normalized_values = list(map(normalize_intensity, seismic_data))

# Step 2: Adjust precision
precise_values = list(map(adjust_precision, normalized_values))

# Step 3: Categorize frequencies
frequency_categories = list(map(categorize_frequency, precise_values))

# Step 4: Map categories to indices
index_mapping = {'low': 1, 'medium': 2, 'high': 3, 'unknown': 0}
category_indices = [index_mapping[cat] for cat in frequency_categories]

# Step 5: Compute weighted sum using reduce
weights = [1, 2, 3, 4, 5]
weighted_sum = reduce(lambda acc, pair: acc + pair[0]*pair[1], zip(category_indices, weights), 0)

# Step 6: Apply exponentiation and final adjustment
final_index = math.exp(weighted_sum / len(seismic_data))
final_index = adjust_precision(final_index)

print(f"Result: {final_index}")