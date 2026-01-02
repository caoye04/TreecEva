def analyze_risk(age, bmi, activity_level_str):
    risk = 0
    if age > 65:
        risk += 15
    if bmi < 18.5:
        risk += 10
    elif bmi > 30:
        risk += 25
    if 'low' in activity_level_str.lower():
        risk += 20
    return risk


def calculate_stress_index(heart_rate_list, baseline=75):
    avg_hr = sum(heart_rate_list) / len(heart_rate_list)
    stress = (avg_hr - baseline) * 1.2
    return max(stress, 0)


def normalize_signal(raw_signal_str):
    cleaned = raw_signal_str.strip().replace('-', '').replace('_', '')
    if not cleaned.isdigit():
        return 0
    return int(cleaned[:8]) % 1000


def evaluate_sleep_quality(sleep_hours, interruptions):
    base = 100
    base -= max(0, (8 - sleep_hours) * 5)
    base -= interruptions * 3
    return max(base, 0)


def process_metrics(data):
    age = data['age']
    bmi = data['bmi']
    hr_log = data['heart_rate_log']
    sleep_hrs = data['sleep_duration']
    interrupts = data['sleep_interruptions']
    activity = data['activity_level']
    signal_str = data['signal_trace']

    # Distractor: unused variables and computations
    temp_correction = 0.987
    calibration_offset = sum([i * 0.01 for i in range(len(hr_log))])
    noise_floor = normalize_signal(signal_str)  # Used only indirectly

    risk_score = analyze_risk(age, bmi, activity)
    stress_index = calculate_stress_index(hr_log)
    sleep_quality = evaluate_sleep_quality(sleep_hrs, interrupts)

    # Red herring: complex-looking but irrelevant transformation
    phantom_metric = (noise_floor * 0.01) ** 2
    adjustment_factor = 1.0 if phantom_metric < 10 else 0.8

    # Real computation path
    composite = risk_score * 0.3 + stress_index * 0.4 + (100 - sleep_quality) * 0.3
    normalized_composite = max(0, min(100, composite))

    # Another distraction: dead conditional with misleading comment
    if age < 0 or age > 150:  # Impossible by input constraints
        normalized_composite = 0  # Dead code

    # Final score calculation - this is the key result
    final_score = int(round(1000 - normalized_composite * 5))

    # Decoy output variables
    diagnostic_flag = 'OK' if final_score > 700 else 'CHECK'
    confidence = 95.6

    return final_score

# Simulated health data input
health_data = {
    'age': 72,
    'bmi': 31.2,
    'heart_rate_log': [88, 92, 95, 87, 90],
    'sleep_duration': 6.5,
    'sleep_interruptions': 4,
    'activity_level': 'Low Activity Detected',
    'signal_trace': '---987654321---___'
}

# Execution point of interest
final_score = process_metrics(health_data)
print(f"Target result: {final_score}")