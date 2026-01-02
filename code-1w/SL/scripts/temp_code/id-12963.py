def preprocess_vitals(vital_signs):
    # Irrelevant transformation: normalizes to z-scores (not used in final logic)
    mean_temp = sum(vs[0] for vs in vital_signs) / len(vital_signs)
    std_temp = (sum((vs[0] - mean_temp)**2 for vs in vital_signs) / len(vital_signs)) ** 0.5
    z_scores = [(vs[0] - mean_temp) / std_temp for vs in vital_signs]

    # Distractor: heart rate bands (never accessed later)
    hr_bands = {i: 'normal' if 60 <= hr <= 100 else 'abnormal' for i, (_, hr, _) in enumerate(vital_signs)}

    # Relevant but disguised: extract only oxygen levels below threshold
    critical_o2 = [o2 for _, _, o2 in vital_signs if o2 < 94]
    return critical_o2


def compute_urgency_index(readings):
    index = 0
    multiplier = 1
    for i, val in enumerate(readings):
        if i % 2 == 0:
            index += val * multiplier
        else:
            index -= val // (multiplier + 1)
        multiplier += 1
    return abs(index) % 1000

# Dead function: looks important but unused
def deprecated_diagnosis_engine(data):
    return sum(hash(str(d)) % 100 for d in data)

# Decoy data structure
test_results_archive = {
    'patient_A': {'status': 'cleared', 'score': 87},
    'patient_B': {'status': 'pending', 'score': 45},
    'patient_C': {'status': 'flagged', 'score': 12}
}

# Simulated patient records: (temperature, heart_rate, oxygen_saturation)
patient_records = [
    (36.8, 72, 98),
    (37.1, 84, 92),
    (38.5, 96, 90),
    (36.0, 58, 95),
    (39.2, 110, 88)
]

# Threshold map with red herring keys
thresholds = {
    'fever': 38.0,
    'bradycardia': 60,
    'tachycardia': 100,
    'hypoxemia': 94,
    'cache_timeout': 300,  # irrelevant
    'max_retries': 3       # irrelevant
}

# Secondary processing: counts character appearances in fake IDs (distractor)
patient_ids = ['P001X', 'P002Y', 'P003Z', 'P004W', 'P005V']
char_freq = {}
for pid in patient_ids:
    for char in pid:
        char_freq[char] = char_freq.get(char, 0) + 1

# Another distraction: zipping unrelated sequences
sync_data = list(zip(
    [x[1] for x in patient_records],
    [i for i in range(len(patient_records))],
    [char_freq[f'P00{i+1}'][0] if f'P00{i+1}'[0] in char_freq else 0 for i in range(5)]  # malformed access
))

# Core logic buried in noise
def analyze_patient_data(records, limits):
    # Step 1: Extract temperatures and oxygen levels
    temps = [rec[0] for rec in records]
    o2_levels = [rec[2] for rec in records]

    # Step 2: Find how many have fever OR hypoxemia
    fever_count = sum(1 for t in temps if t >= limits['fever'])
    low_o2_count = sum(1 for o2 in o2_levels if o2 < limits['hypoxemia'])

    # Step 3: Use dictionary to map count to severity code (only some values matter)
    severity_map = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 0}
    fever_severity = severity_map.get(fever_count, 0)
    o2_severity = severity_map.get(low_o2_count, 0)

    # Step 4: Combine using bitwise manipulation (masking)
    combined_severity = (fever_severity << 2) ^ (o2_severity | 3)

    # Step 5: Preprocess returns only critical O2 values < 94
    critical_o2_values = preprocess_vitals(records)  # [92, 90, 88]

    # Step 6: Compute urgency from critical oxygen values
    urgency = compute_urgency_index(critical_o2_values)  # [92,90,88] -> processed

    # Step 7: Final diagnostic combines severity and urgency
    # But only lower 8 bits of urgency are used
    final = (combined_severity * 100) + (urgency & 0xFF)

    # Dead code branch (never executed due to data)
    if len([x for x in records if x[1] > 150]) > 0:
        final += 500  # unreachable

    return final

# Key execution point
final_diagnostic = analyze_patient_data(patient_records, thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")