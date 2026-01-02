import math

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 22.7, 25.3, 20.4, 21.9, 24.0, 23.2, 18.7]
humidity_readings = [45, 52, 61, 48, 39, 58, 50, 44, 55, 62]
pressure_readings = [1013, 1015, 1012, 1018, 1010, 1016, 1014, 1011, 1017, 1013]

# Irrelevant auxiliary arrays (distractors)
legacy_codes = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x6F, 0x7G, 0x8H, 0x9I, 0x0J]
placeholder_mask = [False, True, False, True, False] * 2
dummy_checksums = [sum(humidity_readings[:i]) for i in range(1, len(humidity_readings))]

# Misleading intermediate transformation (dead path)
def compute_legacy_index(data):
    return sum(int(x) ** 2 for x in data if x > 20) // len(data)

legacy_index = compute_legacy_index(temperature_readings)  # Unused later

# Core processing functions
def normalize(values, base=100.0):
    max_val = max(values)
    return [base * v / max_val for v in values]

def filter_outliers(values, tolerance=1.5):
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    lower, upper = q1 - tolerance * iqr, q3 + tolerance * iqr
    return [v for v in values if lower <= v <= upper]

def rolling_average(values, window=3):
    smoothed = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        smoothed.append(sum(values[start:i+1]) / (i - start + 1))
    return smoothed

# Apply normalization and filtering
temp_norm = normalize(temperature_readings, base=50.0)
humid_norm = normalize(humidity_readings, base=50.0)
press_norm = normalize(pressure_readings, base=20.0)

# Process sequences with slicing and filtering
temp_filtered = filter_outliers(temp_norm)
humid_filtered = humid_norm[:len(temp_filtered)]  # Align lengths

# Rolling average on filtered data
smoothed_temp = rolling_average(temp_filtered)
smoothed_humid = rolling_average(humid_filtered)

# Combine into multi-dimensional processed data
processed_data = []
for i in range(len(smoothed_temp)):
    composite = (
        smoothed_temp[i] * 1.2 +
        smoothed_humid[i] * 0.8 +
        press_norm[i % len(press_norm)] * 0.3
    )
    processed_data.append(composite)

# Threshold configuration map (critical for analysis)
threshold_map = {
    'warning_low': 45.0,
    'caution_high': 65.0,
    'alert_critical': 75.0
}

# Decoy function (never called, distractor)
def legacy_diagnostic(seq):
    return math.log(sum(seq) + 1) * 100 // len(seq)

# Real analysis logic
def analyze_readings(readings, thresholds):
    count_alert = 0
    count_caution = 0
    aggregate_score = 0.0

    for val in readings:
        if val >= thresholds['alert_critical']:
            count_alert += 1
            aggregate_score += 3.0
        elif val >= thresholds['caution_high']:
            count_caution += 1
            aggregate_score += 1.5
        elif val < thresholds['warning_low']:
            aggregate_score -= 0.5

    # Complex formula combining counts and scores
    base = aggregate_score * 10
    penalty = (count_alert ** 2) * 4
    bonus = int(math.sqrt(max(count_caution, 1))) * 2

    # Final diagnostic score
    final_score = base - penalty + bonus

    # Irrelevant bit manipulation (distractor)
    masked = final_score & 0xFF
    shifted = int((masked << 2) ^ 0xAA) % 100

    # Only the unmodified final_score is returned
    return final_score

# Execute key statement
current_snapshot = processed_data[::2]  # Use every other reading
final_diagnostic = analyze_readings(current_snapshot, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")