from collections import defaultdict

# Simulate sensor data with timestamps and readings
timestamped_readings = [
    (100, 23.5), (105, 24.1), (110, 23.9), (115, 25.3), (120, 26.0),
    (125, 25.8), (130, 26.2), (135, 27.1), (140, 26.8), (145, 27.5)
]

# Irrelevant backup array for red herring
temp_backup = [x[1] * 1.02 for x in timestamped_readings if x[1] > 25]

# Extract only values above threshold
valid_readings = [val for ts, val in timestamped_readings if 24 <= val <= 27]

# Group readings by 5-unit ranges using defaultdict
range_groups = defaultdict(list)
for val in valid_readings:
    bucket = int(val // 5) * 5
    range_groups[bucket].append(val)

# Misleading intermediate: count per group (not used later)
group_counts = {k: len(v) for k, v in range_groups.items()}

# Compute rolling average over window size 3
rolling_avg = []
for i in range(2, len(valid_readings)):
    avg = sum(valid_readings[i-2:i+1]) / 3
    rolling_avg.append(round(avg, 2))

# Dummy transformation: amplify and cap
amplified_trend = [min(x * 1.15, 30) for x in rolling_avg if x > 25]

# State tracker for stability detection
stability_counter = 0
prev = None
for val in amplified_trend:
    if prev is not None and abs(val - prev) < 1.0:
        stability_counter += 1
    prev = val

# Helper function to compute score based on smoothed trend
def calculate_base_score(trend_vals):
    if not trend_vals:
        return 0
    return sum(trend_vals) / len(trend_vals)

# Secondary helper with dead-end logic
def analyze_variance(data):
    if len(data) < 2:
        return 0.0
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    # This function is called but result discarded
    return variance

# Process the data through filtering and smoothing
processed_data = [x for x in rolling_avg if x >= 24.5]

# Call unused analysis (distractor)
dummy_variance = analyze_variance(temp_backup)

# Core calculation
base_score = calculate_base_score(processed_data)

# Apply weighting based on data length
length_factor = len(processed_data) if len(processed_data) > 0 else 1
weighted_adjustment = (length_factor * 0.8) if length_factor > 2 else 1.0

# Final scoring with fixed offset
final_score = int(base_score * weighted_adjustment + 12.7)

Result: final_score