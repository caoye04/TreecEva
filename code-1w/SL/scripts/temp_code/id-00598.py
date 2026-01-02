def analyze_readings(x):
    return lambda y: (x + y) * 0.5 if y > 0 else x

# Simulated sensor data stream
temperature_readings = [36.1, 37.5, 38.2, 35.9, 37.0, 39.1, 36.8]
heart_rate_data = [72, 85, 93, 68, 77, 101, 74]
blood_pressure_seq = [(120, 80), (130, 85), (145, 90), (118, 78), (125, 82), (150, 95), (122, 80)]

# Irrelevant transformation - red herring
transformed = [round((t - 32) * 5/9, 1) for t in [98.6, 100.4, 101.3]]

# Decoy function with unused logic
def compute_stress_level(data):
    stress = 0
    for val in data:
        if val > 90:
            stress += 1
        elif val < 60:
            stress -= 1
    return stress  # Never used

# Unused intermediate calculations
dummy_aggregate = sum([hr for hr in heart_rate_data if hr > 70]) + len(temperature_readings)
avg_temp = sum(temperature_readings) / len(temperature_readings)

# Bit manipulation decoy - simulates signal encoding
encoded_signal = 0
for i, temp in enumerate(temperature_readings[:3]):
    encoded_signal ^= int(temp * 10) << (i % 4)

# Real processing begins here
thresholds = {
    'fever': 38.0,
    'tachycardia': 100,
    'hypertension': 140
}

status_flags = []
for i in range(len(temperature_readings)):
    fever = temperature_readings[i] >= thresholds['fever']
    tachy = heart_rate_data[i] >= thresholds['tachycardia']
    hyper = blood_pressure_seq[i][0] >= thresholds['hypertension']
    status_flags.append(sum([fever, tachy, hyper]))

# Distractor: complex but unused list comprehension with slicing
anomaly_pattern = [f"{i}:{v}" for i, v in enumerate(status_flags) if v == max(status_flags[:len(status_flags)//2])]

# Core diagnostic processor
health_data = []
for i in range(len(temperature_readings)):
    score = 0
    if temperature_readings[i] > thresholds['fever']:
        score += 2
    if heart_rate_data[i] > thresholds['tachycardia']:
        score += 3
    if blood_pressure_seq[i][0] > thresholds['hypertension']:
        score += 4
    health_data.append(score)

# Redundant sorting - result not used
sorted_diagnostics = sorted(health_data, reverse=True)

# Misleading accumulation path
cumulative_risk = 0
for val in health_data:
    cumulative_risk = (cumulative_risk * 0.7 + val * 0.3)  # damping factor

# Primary analysis function
interpolate = analyze_readings(cumulative_risk)

# Final processing with relevant logic buried among distractions
def process_metrics(metrics, config):
    base = sum(metrics)
    adjustments = 0
    for idx, m in enumerate(metrics):
        if m > 0 and idx % 2 == 1:
            adjustments += m * 0.1
    # Key computation
    critical_count = len([m for m in metrics if m >= 5])
    # More decoys
    dummy_map = {i: m**0.5 for i, m in enumerate(metrics) if m > 0}
    filtered = [m for m in metrics if m > 1][::-1]  # reversed slice
    return int(base + adjustments - critical_count * 2)

# Execution point of interest
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Target result: {final_diagnostic}")