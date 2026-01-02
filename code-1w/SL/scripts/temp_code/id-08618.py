from collections import defaultdict
import math

# Simulate sensor data with timestamps and readings
timestamps = [101, 102, 103, 104, 105]
raw_readings = [89, 92, 85, 96, 88]
data_points = list(zip(timestamps, raw_readings))

# Weight configuration for scoring (simulates calibration)
weights = {'base': 0.5, 'boost': 1.2, 'penalty': 0.8}

# Irrelevant tracking variables (distractors)
log_entries = []
diagnostic_flag = False
buffer_cache = defaultdict(int)
processing_steps = 0

# Precompute auxiliary statistics (some not used later)
mean_reading = sum(raw_readings) / len(raw_readings)
variance = sum((x - mean_reading) ** 2 for x in raw_readings) / len(raw_readings)
std_deviation = math.sqrt(variance)

# Auxiliary transformation: normalize readings around mean
normalized = [(r - mean_reading) for r in raw_readings]

# Mapping function for dynamic adjustment (not fully utilized)
adjustment_curve = lambda x: round(math.log(x + 10), 3) if x > 0 else 0
adjusted_scores = [adjustment_curve(abs(n)) for n in normalized]

# Helper function to simulate complex metric processing
def analyze_trend(values):
    trend_score = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend_score += 1.5
        elif values[i] < values[i-1]:
            trend_score -= 0.5
    return max(trend_score, 0)

# Secondary helper with dead-end logic
def validate_stability(logs):
    stable = True
    count = 0
    for entry in logs:
        count += 1
        if entry > 100:
            stable = False
    # This function is called but its return is ignored
    return stable

# Main processing function with mixed operations
def process_metrics(data, config):
    base_weight = config['base']
    boost_factor = config['boost']
    penalty_factor = config['penalty']

    # Extract values and apply initial weighting
    values = [entry[1] for entry in data]
    weighted_sum = 0
    bonus_awarded = False

    # Primary accumulation loop with conditional logic
    for val in values:
        if val >= 90:
            weighted_sum += val * boost_factor * base_weight
            bonus_awarded = True
        elif val < 85:
            weighted_sum += val * penalty_factor * base_weight
        else:
            weighted_sum += val * base_weight

        # Distractor: update unused cache
        buffer_cache[val] += 1
        log_entries.append(int(val * base_weight))

    # Compute trend influence (adds non-linear effect)
    trend_modifier = analyze_trend(values)
    final = weighted_sum + (trend_modifier * 2)

    # Dead code path - never executed due to logic above
    if diagnostic_flag and len(buffer_cache) > 100:
        final = math.ceil(final)

    # Unused validation call (side effect only)
    validate_stability(log_entries)

    return int(round(final))

# Execute main computation
final_score = process_metrics(data_points, weights)

# Print result as required
print(f"Result: {final_score}")