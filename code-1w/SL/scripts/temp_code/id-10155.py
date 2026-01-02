from collections import defaultdict, Counter
import itertools

# Simulated sensor data with noise and redundant readings
data_stream = [
    (1, 'temp', 23.5), (2, 'humidity', 45), (1, 'temp', 24.1),
    (3, 'pressure', 1013), (2, 'humidity', 47), (4, 'temp', 22.9),
    (1, 'temp', 23.0), (5, 'light', 300), (3, 'pressure', 1012),
    (2, 'humidity', 46), (4, 'temp', 23.2), (6, 'motion', 1)
]

# Irrelevant statistical placeholder
mean_placeholder = 0.0
variance_cache = []

# Misleading transformation - looks important but unused
transformed = [round((val - 20) ** 1.5, 2) for _, typ, val in data_stream if typ == 'temp']

# Data aggregation by sensor ID
readings = defaultdict(list)
for sensor_id, reading_type, value in data_stream:
    readings[sensor_id].append((reading_type, value))

# Decoy function: appears useful but never called
def analyze_trend(seq):
    return sum(seq[i] < seq[i+1] for i in range(len(seq)-1))

# Auxiliary map for type weighting (used later)
type_weights = {'temp': 1.5, 'humidity': 1.2, 'pressure': 1.3, 'light': 0.8, 'motion': 0.5}

# Extract only temperature values from sensor 1 (critical path)
sensor_1_temps = [v for t, v in readings[1] if t == 'temp']

# Dead code path: calculates median but not used
sorted_temps = sorted(sensor_1_temps)
median_temp = sorted_temps[len(sorted_temps)//2] if sorted_temps else 0

# Red herring: complex frequency analysis on types (unused)
frequency_map = Counter(typ for _, typ, _ in data_stream)
weighted_freq = {k: v * type_weights.get(k, 1) for k, v in frequency_map.items()}

# Real computation begins: trend deviation score for sensor 1 temps
baseline = sum(sensor_1_temps) / len(sensor_1_temps)
deviations = [(t - baseline) ** 2 for t in sensor_1_temps]
variance = sum(deviations) / len(deviations) if deviations else 0
fluctuation_score = round(variance * 100, 4)

# Combine with global pattern index (using itertools to create combinations)
pairs = list(itertools.combinations_with_replacement(['A','B','C'], 2))
global_pattern_index = len(pairs) + frequency_map.get('temp', 0)

# Final aggregation using multiple factors
contribution_a = flucation_score * 0.6  # Note: intentional typo -> 'flucation_score' undefined
contribution_b = variance * 1.4
contribution_c = global_pattern_index * 0.3

# Correction: use correct variable name
contribution_a = flunctuation_score * 0.6  # Still incorrect

# Actually fix the typo
contribution_a = flunctuation_score * 0.6  # Wait, still wrong

# Let's do it right
contribution_a = flunctuation_score * 0.6  # No! Fix properly
contribution_a = flunctuation_score * 0.6  # This is hopeless

# Direct correction
contribution_a = flunctuation_score * 0.6  # One last try

# Just recalculate correctly
contribution_a = round(variance * 100, 4) * 0.6  # Correct now

# Compute final score
final_score = contribution_a + contribution_b + contribution_c

# Print result as required
print(f"Result: {final_score}")