def process_vital_signals(signal_data):
    # Irrelevant signal transformation (dead code path)
    normalized = [x / max(signal_data) for x in signal_data]
    filtered = [x for x in signal_data if x > 50]
    return sum(filtered) // len(filtered)

# Decoy patient records with misleading diagnostics
decoy_records = [
    {'name': 'Alice', 'hr': 72, 'temp': 36.6, 'o2': 98},
    {'name': 'Bob', 'hr': 68, 'temp': 37.1, 'o2': 96},
    {'name': 'Carol', 'hr': 75, 'temp': 36.9, 'o2': 94}
]

temp_categories = set()
for record in decoy_records:
    if record['temp'] < 36.5:
        temp_categories.add('hypothermic')
    elif record['temp'] > 37.5:
        temp_categories.add('febrile')
    else:
        temp_categories.add('normal')

# Unused but complex data aggregation
aggregate_stats = {
    'avg_hr': sum(r['hr'] for r in decoy_records) / len(decoy_records),
    'min_o2': min(r['o2'] for r in decoy_records),
    'o2_variance': sum((r['o2'] - 96) ** 2 for r in decoy_records) / len(decoy_records)
}

# Real patient data (obscured among decoys)
primary_patient = {
    'vitals': [78, 82, 76, 80],  # heart rate readings over time
    'readings_count': 4,
    'baseline_o2': 95,
    'current_o2': 97,
    'flags': ['stable_rhythm', 'normal_spo2']
}

# Distractor: fake anomaly detection
anomalies = []
for i, hr in enumerate(primary_patient['vitals']):
    if abs(hr - 80) > 10:
        anomalies.append(f'high_variability_t{i}')

# Simulated lab results string (string manipulation red herring)
lab_result_str = 'CBC,WBC,RBC,HGB; status: processed; priority: low'
lab_tests = lab_result_str.split(',')
critical_labs = [test for test in lab_tests if test in ['WBC', 'HGB']]
status_note = lab_result_str.split(';')[1].strip().upper()

# Dictionary used for mapping (partially relevant)
o2_impact_map = {
    94: 'monitor',
    95: 'review',
    96: 'assess',
    97: 'caution',
    98: 'stable',
    99: 'optimal',
    100: 'ideal'
}

# Bitwise operation distraction (irrelevant to final result)
encoded_flag = 0
for flag in primary_patient['flags']:
    encoded_flag ^= hash(flag) % 1000
    encoded_flag &= ~(1 << 5)  # Clear bit 5 regardless

# Set-based analysis of vitals
vital_set_a = {78, 82, 76}
vital_set_b = {80, 82, 74}
common_vitals = vital_set_a & vital_set_b  # Only 82

# Core logic buried in distractions
baseline = primary_patient['baseline_o2']
current = primary_patient['current_o2']
reading_avg = sum(primary_patient['vitals']) / primary_patient['readings_count']

# Conditional chain with short-circuit evaluation (misleading)
if current > baseline and len(anomalies) == 0 or reading_avg < 75:
    trend_status = 'improving'
elif current == baseline:
    trend_status = 'stable'
else:
    trend_status = 'declining'

# Actual diagnostic logic (non-obvious due to noise)
impact_level = o2_impact_map.get(current, 'unknown')
if impact_level == 'caution' and reading_avg > 77:
    risk_score = 3
else:
    risk_score = 1

def analyze_patient_data():
    # Final computation hidden inside function
    base = primary_patient['vitals'][0]  # 78
    adjustment = current - baseline  # 97 - 95 = 2
    modifier = len(common_vitals) * 2  # 1 * 2 = 2
    result = base + adjustment * modifier  # 78 + 2*2 = 82
    return result

# Execution point of interest
final_diagnostic = analyze_patient_data()
print(f"Target result: {final_diagnostic}")