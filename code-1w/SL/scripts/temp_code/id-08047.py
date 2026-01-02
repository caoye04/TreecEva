import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.0, 25.3, 26.7, 21.9, 20.2, 27.1]
humidity_readings = [45, 50, 52, 48, 55, 60, 62, 58]
co2_levels = [400, 410, 395, 420, 430, 390, 385, 415]

# Irrelevant auxiliary data (distractor)
sound_decibels = [65, 63, 67, 66, 70, 68, 64, 69]
lux_levels = [12000, 11500, 13000, 12500, 11000, 11800, 12200, 12700]

# Misleading transformation (dead path)
def transform_noise_data(data):
    return [x * 1.05 for x in data if x > 65]

transformed_noise = transform_noise_data(sound_decibels)  # unused

# Data alignment and weighting (relevant)
def align_and_normalize(temp, hum, co2):
    normalized = []
    for i, t in enumerate(temp):
        norm_val = (t - 20) * 1.5 + (hum[i] - 50) * 0.8 + (co2[i] - 400) * 0.02
        normalized.append(round(norm_val, 3))
    return normalized

aligned_scores = align_and_normalize(temperature_readings, humidity_readings, co2_levels)

# Secondary processing with distractors
baseline_shift = 5.0
adjustment_factor = 0.95
offset_cache = {}  # unused cache (red herring)

# Complex conditional filtering and scoring
def filter_outliers_and_score(scores):
    filtered = []
    threshold = sum(scores) / len(scores)
    for idx, score in enumerate(scores):
        if abs(score - threshold) > 2.0:
            continue  # skip outliers
        adjusted = score * adjustment_factor
        if idx % 2 == 0:
            adjusted += baseline_shift
        else:
            adjusted -= 0.5
        filtered.append(adjusted)
    return filtered

filtered_data = filter_outliers_and_score(aligned_scores)

# Simulate historical comparison (mostly irrelevant)
historical_avg = 7.23
historical_trend = [7.1, 7.3, 7.0, 7.4, 7.2, 7.5, 7.1, 7.3]

def compute_deviation_index(current, history):
    total_dev = 0
    for c, h in zip(current[:len(history)], history):
        total_dev += abs(c - h)
    return total_dev / len(history)

dev_index = compute_deviation_index(filtered_data, historical_trend)  # used only here

# Core recursive transformation (key logic)
def recursive_dampen(values, depth=0):
    if depth >= 3 or len(values) == 0:
        return sum(values)
    dampened = [v * (0.85 ** depth) for v in values]
    return recursive_dampen(dampened[::2], depth + 1) + recursive_dampen(dampened[1::2], depth + 1)

processed_data = recursive_dampen(filtered_data)

# Final scoring with red herrings
scaling_matrix = [[1.1, 0.9], [0.95, 1.05]]  # unused structure

# Decoy function using set operations (irrelevant)
def analyze_unique_patterns(data_list):
    s1 = {round(x) for x in data_list}
    s2 = {x + 1 for x in s1}
    s3 = s1.symmetric_difference(s2)
    return len(s3), sum(s3)

pattern_metrics = analyze_unique_patterns(aligned_scores)  # computed but not used

# Actual final calculation
penalty_rate = 0.03
inflation_adjustment = 1.02

# Key statement
final_score = processed_data * inflation_adjustment

# Apply minor penalty based on deviation (only affects slightly)
final_score -= dev_index * penalty_rate

# Output result
print(f"Result: {final_score}")