from collections import defaultdict

# Simulate sensor data aggregation and anomaly-adjusted scoring
raw_readings = [105, 92, 110, 87, 96, 113, 89, 101, 98, 115]
threshold = 100
time_stamps = list(range(10))
detected_anomalies = []

# Misleading intermediate processing: time-based filtering (not actually used)
temporal_filter = [t for t in time_stamps if t % 2 == 0]
unused_filtered_readings = [raw_readings[i] for i in range(len(raw_readings)) if i % 3 != 0]

# Actual processing path
anomaly_flags = []
counter = defaultdict(int)

for val in raw_readings:
    if val > threshold:
        anomaly_flags.append(1)
        counter['above'] += 1
    else:
        anomaly_flags.append(0)
        counter['below'] += 1

# Secondary distraction: simulate calibration drift correction (unused)
calibration_factor = 0.98
drift_adjusted = [round(v * calibration_factor, 2) for v in raw_readings]
baseline_average = sum(raw_readings) / len(raw_readings)

# Real signal extraction: weighted presence of anomalies
weighted_anomaly_score = 0
for i, flag in enumerate(anomaly_flags):
    weight = 1 + (i * 0.05)  # increasing temporal weight
    weighted_anomaly_score += flag * weight

# Additional red herring: unused state tracking
state_log = []
current_state = 'INIT'
for _ in range(3):
    state_log.append(current_state)
    current_state = 'RUNNING' if current_state == 'INIT' else 'COMPLETED'

# Prepare inputs for final calculation
processed_data = {
    'score_component': weighted_anomaly_score,
    'count_above': counter['above'],
    'total': len(raw_readings)
}
weights = {'w1': 1.2, 'w2': 0.8}

# Key statement
final_score = calculate_final_score(processed_data, weights)

# Helper function definition (was not defined earlier - now defined to ensure execution)
def calculate_final_score(data, w):
    component = data['score_component']
    count = data['count_above']
    base = component * w['w1']
    adjustment = count * w['w2']
    # Distraction: unused computation
    phantom_calc = (data['total'] ** 0.5) * 0.1
    return int(base + adjustment)

print(f"Result: {final_score}")