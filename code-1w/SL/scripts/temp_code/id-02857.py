def normalize_readings(raw):    
    # Irrelevant transformation
    return [x * 0.95 for x in raw if x > 0]


def validate_signal(strength):
    # Distractor function: looks important but unused
    return strength > 30 and strength < 95

# Simulated sensor data (some values are red herrings)
sensor_1 = [12, 45, 67, 89, 101]
sensor_2 = [56, 34, 88, 23]
sensor_3 = [78, 89, 91]  # High readings but partially irrelevant

# Misleading intermediate aggregations
total_peaks = sum([max(s) for s in [sensor_1, sensor_2, sensor_3]])
avg_peak = total_peaks / 3
flagged_readings = []

for reading in sensor_1:
    if reading > 80:
        flagged_readings.append(reading)

# Real processing begins here — obscured by prior noise
collected_data = sensor_1 + sensor_2 + sensor_3

# Checksum distraction
data_checksum = sum(collected_data) % 7

# Normalize and filter valid operational range (only values between 40 and 90 matter)
normalized_filtered = [val for val in collected_data if 40 <= val <= 90]

# Apply correction factor using string-based version check (idiomatic Python usage)
version = "v2.1.0"
correction_factor = 1.05 if version.startswith("v2") else 1.0

# Compute entropy-like metric (distractor)
import math
if normalized_filtered:
    entropy = -sum((count / len(normalized_filtered)) * math.log2(count / len(normalized_filtered)) 
                   for count in [normalized_filtered.count(x) for x in set(normalized_filtered)])
else:
    entropy = 0

# Actual relevant computation path
def apply_calibration(seq):
    calibrated = []
    for x in seq:
        if x % 2 == 0:
            calibrated.append(x * 0.9)
        else:
            calibrated.append(x * 1.1)
    return calibrated

def aggregate_metrics(calib):
    base = sum(calib)
    # Secondary adjustment based on sequence length parity
    if len(calib) % 2 == 1:
        base -= 15
    return base * 0.85

def finalize_measurement(raw_input):
    step1 = normalize_readings(raw_input)
    step2 = apply_calibration(step1)
    step3 = aggregate_metrics(step2)
    return int(step3)  # Final answer as integer

# Dead code path — never called
def deprecated_analysis():
    return {"status": "obsolete", "value": None}

# Key assignment statement
thermal_capacity = finalize_measurement(collected_data)

# Print result as required
print(f"Target result: {thermal_capacity}")