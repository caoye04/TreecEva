from itertools import combinations
import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 21.9, 20.4, 27.3]
humidity_readings = [56, 61, 59, 66, 70, 52, 48, 74]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1016, 1018, 1009]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B2', 'C9', 'D4', 'E1', 'F8']
lookup_matrix = [[i * j for j in range(5)] for i in range(5)]

def normalize_range(data, new_min=0, new_max=1):
    old_min, old_max = min(data), max(data)
    return [(x - old_min) / (old_max - old_min) * (new_max - new_min) + new_min for x in data]

def rolling_average(series, window=3):
    smoothed = []
    for i in range(len(series) - window + 1):
        smoothed.append(sum(series[i:i+window]) / window)
    return smoothed

def entropy_of_list(data):
    # Treat values as frequencies and compute Shannon entropy
    total = sum(data)
    if total == 0:
        return 0.0
    probabilities = [x / total for x in data if x > 0]
    return -sum(p * math.log2(p) for p in probabilities)

def generate_pairs(seq):
    # Unused function - red herring
    return list(combinations(seq, 2))

def filter_outliers(data, threshold=1.5):
    # Interquartile range method
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data)//4]
    q3 = sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

# Preprocessing pipeline with distractors
raw_metrics = {
    'temp_raw': temperature_readings,
    'hum_raw': humidity_readings,
    'pres_raw': pressure_readings
}

# Normalize data to [0,1] scale
normalized_temp = normalize_range(temperature_readings)
normalized_hum = normalize_range(humidity_readings)
normalized_pres = normalize_range(pressure_readings)

# Misleading intermediate transformations (not used in final result)
denoised_temp = rolling_average([x * 100 for x in normalized_temp], window=2)
entropy_hum = entropy_of_list(humidity_readings)
filtered_pres = filter_outliers(pressure_readings, threshold=2.0)

# Create composite dataset using zip and enumerate (key python idioms)
indexed_data = []
for idx, (t, h, p) in enumerate(zip(normalized_temp, normalized_hum, normalized_pres)):
    # Add artificial time decay factor based on index
    time_weight = math.exp(-idx * 0.1)
    adjusted_t = t * (0.9 + time_weight)
    adjusted_h = h * (1.1 - time_weight * 0.2)
    adjusted_p = p * (1.0 + math.sin(idx) * 0.05)
    indexed_data.append((adjusted_t, adjusted_h, adjusted_p))

# Extract transformed components
transformed_components = list(zip(*indexed_data))
normalized_data = [
    sum(col) / len(col) for col in transformed_components  # Average across time
]

# Metric weights with decoy initialization
base_weights = {'thermal': 0.4, 'moisture': 0.3, 'barometric': 0.3}

# Complex weight adjustment logic with dead branches
adjustment_factor = 1.0
if len(temperature_readings) > 10:
    adjustment_factor *= 0.9
elif entropy_hum > 5.0:
    adjustment_factor *= 1.1
else:
    # This branch seems relevant but isn't actually impactful
    temp_var = [x ** 2 for x in denoised_temp if x > 0.5]  # Dead computation
    adjustment_factor *= 1.0  # Neutral adjustment

# Actual weight application happens here
metric_weights = [
    base_weights['thermal'] * (1 + 0.1 * math.cos(0.5)),
    base_weights['moisture'] * (1 - 0.15 * math.sin(0.3)),
    base_weights['barometric'] * (1 + 0.05 * math.tan(0.2))
]

# Decoy scoring function that is defined but not used
compute_diagnostic_score = lambda w, d: sum(wi * di**2 for wi, di in zip(w, d))

# Core evaluation function using lambda and itertools (required features)
combine_with_interaction = lambda vals, wgts: sum(
    wgts[i] * vals[i] for i in range(len(vals))
) + 0.1 * sum(
    wgts[i] * wgts[j] * abs(vals[i] - vals[j])
    for i, j in combinations(range(len(vals)), 2)
)

def evaluate_performance(weights, data):
    # Final score computation with interaction terms
    raw_score = combine_with_interaction(data, weights)
    
    # Apply nonsensical correction that evaluates to zero
    n = len(legacy_codes)
    correction = sum(i * j for i, j in combinations(range(n), 2)) if n > 3 else 0
    correction -= n * (n - 1) * (n - 2) / 6  # Always cancels out
    
    return raw_score + correction

# Critical execution point
final_score = evaluate_performance(metric_weights, normalized_data)

print(f"Result: {final_score}")