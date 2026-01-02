import math

# Simulate sensor data processing with noise filtering and performance scoring
def preprocess_sensor_data(raw_readings):
    filtered = []
    noise_floor = 0.05
    for val in raw_readings:
        if abs(val) > noise_floor:
            filtered.append(abs(val))
    return sorted(filtered, reverse=True)

# Calculate dynamic weight adjustment based on input size (unused red herring)
def adjust_weights(dimension):
    return [math.sin(i * dimension) + 1 for i in range(dimension)]

# Dummy function to simulate hardware calibration (dead code path)
def calibrate_sensors(log_entries):
    checksum = 0
    for entry in log_entries:
        checksum ^= int(entry * 100)
    return checksum % 17

# Core evaluation logic with lambda-based transformations
metric_weights = [0.2, 0.35, 0.15, 0.3]
raw_scores = [88.5, 92.0, 76.0, 85.5]

# Irrelevant transformation chain (partial distractor)
baseline_shift = list(map(lambda x: x - 70, raw_scores))
temp_normalization = [round(v ** 0.5, 3) for v in baseline_shift]

# Unused intermediate structure (distractor)
sensor_logs = [(i, round(70 + (i*11.7)%23, 2), flag) 
               for i, flag in enumerate([True, False, True, False])]

# Key preprocessing step
processed_scores = preprocess_sensor_data(raw_scores)

# Apply weighted scoring using lambda
scoring_engine = lambda weights, values: sum(w * v for w, v in zip(weights, values))

# Secondary adjustment with irrelevant conditional scaling
scaling_factor = 1.0
if len(processed_scores) % 2 == 0:
    scaling_factor *= 0.95  # Misleading branch — not actually needed

intermediate_total = scoring_engine(metric_weights, processed_scores)

# Additional noise correction (irrelevant but plausible)
correction_term = 0.0
for i in range(len(metric_weights)):
    if metric_weights[i] > 0.25:
        correction_term += 0.01 * i

# Final performance score computation
final_score = intermediate_total - correction_term

# Print result as required
print(f"Result: {final_score}")