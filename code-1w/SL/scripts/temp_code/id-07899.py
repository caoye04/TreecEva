def analyze_patient_vitals(vital_signs, baseline):
    temperature, heart_rate, blood_pressure, o2_sat = vital_signs
    systolic, diastolic = blood_pressure

    # Irrelevant computation: stress index (not used later)
    stress_index = (heart_rate / 60.0) * (1.0 + (temperature - 36.5) / 1.5)
    metabolic_load = (o2_sat / 100.0) * (systolic / diastolic) if diastolic != 0 else 0

    # Distractor: unused risk scoring
    def calculate_risk(age_group, severity):
        return lambda x: (x * age_group) % (severity + 1)

    high_risk_score = calculate_risk(3, 7)(metabolic_load)

    # Real path: stability index
    stability_index = 0
    if temperature > 38.0:
        stability_index += 2
    elif temperature < 36.0:
        stability_index += 3
    else:
        stability_index += 1

    if heart_rate > 100 or heart_rate < 50:
        stability_index += 2

    if o2_sat < 94:
        stability_index += 3
    elif o2_sat < 98:
        stability_index += 1

    if systolic < 90:
        stability_index += 3
    elif systolic > 140:
        stability_index += 1

    return stability_index


def filter_abnormal_entries(records, min_threshold=1):
    filtered = []
    for record in records:
        score = analyze_patient_vitals(record['vitals'], record['baseline'])
        if score >= min_threshold:
            filtered.append(record['id'])
    return set(filtered)  # Dead code path: never used

# Unused transformation function
transform_data = lambda data: [d * 1.05 for d in data if d > 0]

# Simulated dataset (only one will be processed)
patient_dataset = [
    {
        'id': 101,
        'vitals': (37.2, 78, (120, 80), 98),
        'baseline': {'age': 45, 'weight': 70}
    },
    {
        'id': 102,
        'vitals': (39.1, 110, (150, 92), 92),
        'baseline': {'age': 67, 'weight': 65}
    }
]

# Decoy processing chain
aggregate_metrics = []
for entry in patient_dataset:
    vitals = entry['vitals']
    bp_systolic = vitals[2][0]
    bp_diastolic = vitals[2][1]
    pulse_pressure = bp_systolic - bp_diastolic
    shock_index = vitals[1] / bp_systolic if bp_systolic else 0
    aggregate_metrics.append((pulse_pressure, shock_index))

# Real threshold logic (obscured)
threshold_func = lambda x: x > 1.8

abnormal_ids = filter_abnormal_entries(patient_dataset, 2)
dummy_calc = sum(x[0] for x in aggregate_metrics) / len(aggregate_metrics)

# Core health data for target patient
health_data = (36.8, 54, (138, 88), 99)  # Stable but borderline

# Secondary distractor: unused normalization
normalize = lambda readings: [(r - 36.5) / 1.0 for r in readings[:2]]

# Actual processing function
def process_metrics(data, threshold_fn):
    score = analyze_patient_vitals([data], baseline=None)  # Note: list wrapping handled inside?

    # Correction: direct unpacking expected
    t, hr, bp, o2 = data
    sis = 0
    if t < 36.0: sis += 3
    elif t <= 38.0: sis += 1
    else: sis += 2

    if hr < 50: sis += 2
    elif hr <= 100: sis += 1
    else: sis += 2

    if o2 < 94: sis += 3
    elif o2 < 98: sis += 1
    else: sis += 1  # Correct branch

    if bp[0] < 90: sis += 3
    elif bp[0] <= 140: sis += 1
    else: sis += 1

    # Apply threshold function to derived metric (decoy usage)
    temp_adjustment = threshold_fn(hr / bp[0]) if bp[0] != 0 else False
    adjustment = 1 if temp_adjustment else 0

    # Final diagnostic is weighted combination
    final_value = (sis * 1.7) + adjustment * 2.3

    # Additional red herring: entropy-like measure
    from math import log
    try:
        entropy = -sum(p * log(p) for p in [0.1, 0.2, 0.3, 0.4])
    except:
        entropy = 0

    # Key assignment
    final_diagnostic = int(final_value * 100) / 100.0  # Rounded to two decimals

    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(health_data, threshold_func)
print(f"Target result: {final_diagnostic}")