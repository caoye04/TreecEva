from collections import defaultdict, Counter
import math

# Simulated sensor array data with noise and redundant readings
data_stream = [12, 15, 12, 18, 15, 22, 12, 25, 18, 30, 22, 15, 12, 18, 22, 25, 30, 33, 30, 25, 22]

# Irrelevant metadata (distractor)
sensor_metadata = {
    'calibration': '2023-09-15',
    'model': 'X27B',
    'firmware': 'v2.1.7'
}

# Noise filter mask (partially relevant but overcomplicated)
noise_mask = [i for i in range(len(data_stream)) if i % 3 != 0]
filtered_noise_values = [data_stream[i] for i in noise_mask]

# Redundant transformation path (dead code path)
duplicate_shift = [x * 2 + 1 for x in data_stream if x > 20]
temp_shadow_copy = duplicate_shift.copy()

# Core processing begins here
raw_frequencies = Counter(data_stream)

# Introduce decoy statistical calculations (distractors)
mean_value = sum(data_stream) / len(data_stream)
variance_proxy = sum((x - mean_value) ** 2 for x in data_stream) / len(data_stream)
entropy_approx = -sum((freq / len(data_stream)) * math.log(freq / len(data_stream)) for freq in raw_frequencies.values())

# Transform data: map each unique value to its occurrence-based category
transformed_data = []
for val, freq in raw_frequencies.items():
    if freq > 3:
        transformed_data.append((val, 'recurring'))
    elif freq == 2:
        transformed_data.append((val, 'paired'))
    else:
        transformed_data.append((val, 'isolated'))

# Build complex threshold map with irrelevant nesting
threshold_map = defaultdict(lambda: defaultdict(dict))
for key, category in transformed_data:
    base_threshold = key * 0.75
    hysteresis = 1.0 + (key % 4) * 0.1
    # Store nested, over-engineered thresholds
    threshold_map[key]['primary']['low'] = base_threshold * 0.8
    threshold_map[key]['primary']['high'] = base_threshold * 1.2
    threshold_map[key]['secondary']['hysteresis'] = hysteresis
    # Unused backup values (distractor)
    threshold_map[key]['backup']['alt_low'] = base_threshold * 0.7
    threshold_map[key]['backup']['alt_high'] = base_threshold * 1.3

# Decoy function that is defined but not used in critical path
def deprecated_analysis(seq):
    return sum(x ** 1.5 for x in seq if x % 2 == 0)

# Another red herring: recursive frequency explorer (never called)
def explore_frequency_hierarchy(values, depth=0):
    if depth >= 3 or len(values) == 0:
        return depth
    new_vals = [v - 1 for v in values if v > 15]
    return explore_frequency_hierarchy(new_vals, depth + 1)

# Real analysis function - determines pattern score based on category weights
def analyze_pattern(pattern_list, thresholds):
    weights = {'recurring': 3, 'paired': 2, 'isolated': -1}
    score = 0
    for value, category in pattern_list:
        # Use only primary thresholds; secondary and backup are distractions
        low = thresholds[value]['primary']['low']
        high = thresholds[value]['primary']['high']
        # Apply conditional logic with bit manipulation twist
        if low <= value <= high:
            flag = (value ^ 7) & 1  # Arbitrary bit check
            modifier = 1.5 if flag else 1.0
            score += weights[category] * modifier
    return int(score)

# Execute main logic
final_diagnostic = analyze_pattern(transformed_data, threshold_map)

# Print result as required
Result: {final_diagnostic}