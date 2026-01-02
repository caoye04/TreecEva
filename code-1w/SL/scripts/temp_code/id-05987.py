def analyze_readings(readings):
    # Irrelevant transformation: convert to percentages (not used in final logic)
    percentages = [round(x * 0.76 + 12, 2) for x in readings]
    adjusted = [x * 1.1 for x in readings if x > 0]
    return adjusted

readings = [15, -5, 20, 0, 25, 30, -10, 40]

# Dead code path - never called
def deprecated_filter(data):
    return [x for x in data if x % 2 == 0]

# Misleading aggregation: looks important but unused later
raw_sum = sum(readings)
count_positive = len([x for x in readings if x > 0])
avg_readings = raw_sum / len(readings) if readings else 0

# Distractor: complex but irrelevant bitwise shift chain
shifted_meta = 0
for i in range(len(readings)):
    shifted_meta ^= i << 2
    shifted_meta += i * 3  # Noise

# Real processing begins — actual data flow
filtered = [x for x in readings if x > 10]
squared_filtered = [x**2 for x in filtered]

# Simulate sensor drift correction (only some values are corrected)
drift_map = {25: 23, 30: 29, 40: 38}
corrected = [drift_map[x] if x in drift_map else x for x in filtered]

# Aggregation using enumerate and zip — required Python features
indexed = list(enumerate(corrected))
offsets = [i * 2 for i, _ in indexed]
paired_data = list(zip(corrected, offsets))
aggregated_data = [val - off for val, off in paired_data]

# Another red herring: sorting and case conversion analog (on numbers)
aggregated_data.sort(reverse=True)
string_versions = [str(x).upper() for x in aggregated_data]  # Mock 'case conversion'

# Threshold logic with decoy conditionals
threshold = 20
activation_log = []
for val in aggregated_data:
    if val > threshold:
        activation_log.append(True)
    elif val == threshold:
        # Dead branch — never reached due to data
        activation_log.append(False)
    else:
        continue

# Core computation hidden among noise
baseline = 5
running_total = baseline
for idx, val in enumerate(aggregated_data):
    if idx % 2 == 0:
        running_total += val // 2
    else:
        running_total -= val % 7

# Final function with misleading parameters
extra_weights = [1.1, 0.9, 1.05, 0.95]
def process_metrics(data, limit):
    cumulative = 0
    scaling_factor = 1.0
    
    # Use of enumerate and zip together (required feature)
    for i, (item, _) in enumerate(zip(data, extra_weights)):
        if i < len(extra_weights):
            scaling_factor *= extra_weights[i]
        # Only every third element contributes
        if i % 3 == 0:
            cumulative += item * scaling_factor
    
    # Decoy operation: looks like it affects result but doesn't
    temp_result = sum(data) * 0.1
    
    # Actual return
    return int(cumulative - temp_result + 7)  # Final adjustment

# Critical execution point
final_score = process_metrics(aggregated_data, threshold)

# Output
print(f"Result: {final_score}")