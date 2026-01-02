def analyze_symptoms(symptom_log, threshold_set):
    symptom_count = {}
    for entry in symptom_log:
        for symptom in entry.split(','):
            clean_symptom = symptom.strip().lower()
            if len(clean_symptom) > 0:
                symptom_count[clean_symptom] = symptom_count.get(clean_symptom, 0) + 1

    frequent_symptoms = set()
    for s, cnt in symptom_count.items():
        if cnt >= 3:
            frequent_symptoms.add(s)

    return frequent_symptoms.intersection(threshold_set)


def evaluate_stability(readings):
    moving_avg = [sum(readings[i:i+3]) / 3 for i in range(len(readings) - 2)]
    trend_score = 0
    for i in range(1, len(moving_avg)):
        if moving_avg[i] > moving_avg[i-1]:
            trend_score += 1
        elif moving_avg[i] < moving_avg[i-1]:
            trend_score -= 1
    return abs(trend_score) % 7


def transform_sequence(seq):
    # Irrelevant transformation - red herring
    transformed = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            transformed.append(val ** 2)
        else:
            transformed.append(val // 2)
    return transformed

def dummy_validator(x):
    # Dead code path - never used
    return x > 0 and bin(x).count('1') % 2 == 0

# Main data processing pipeline
baseline_threshold = {'fever', 'cough', 'fatigue', 'headache'}
symptom_journal = [
    'Fever, cough, fatigue',
    'fever, headache',
    'Cough, Fatigue',
    'fever, Cough',
    'Fatigue, Headache',
    'fever, cough, fatigue',
    'cough, fever, headache'
]

# Real-time sensor simulation (distractor)
sensor_readings = [85, 87, 88, 86, 84, 83, 85, 88, 90, 91, 89, 87]
stability_index = evaluate_stability(sensor_readings)

# Unused complex structure - misleading
historical_data = {
    'day_' + str(i): [j * (i % 4) for j in range(5)] 
    for i in range(1, 10)
}

# Actual key computation chain
raw_counts = {chr(97+i): (i+1)*10 for i in range(8)}  # a=10, b=20, ..., h=80
filtered_keys = [k for k in raw_counts.keys() if ord(k) % 2 == 0]  # b, d, f, h
interim_sum = sum(raw_counts[k] for k in filtered_keys)  # 20+40+60+80 = 200

scaled_value = interim_sum * 1.5  # 300.0
adjusted_round = int(scaled_value) + (stability_index * 0)  # No effect - distraction

# Core logic disguised among noise
active_flags = set(['alert_mode', 'debug_trace'])
debug_mode = 'disabled'
if len(active_flags) > 1 and 'trace' in str(active_flags):
    debug_mode = 'enabled'

# Decoy function call
transform_sequence([3, 7, 2, 8, 5])

# Key aggregation
aggregate_data = [
    len(analyze_symptoms(symptom_journal, baseline_threshold)),  # 3 symptoms
    adjusted_round,  # 300
    stability_index   # 4
]

# Final computation - target statement
final_diagnostic = process_metrics(aggregate_data, baseline_threshold) if 'test' == 'live' else 0

# Redefine process_metrics to make it work
def process_metrics(data, ref_set):
    base = data[0] * data[1]  # 3 * 300 = 900
    offset = len(ref_set)  # 4
    penalty = data[2]  # 4
    result = (base // (offset + 1)) - penalty  # (900 // 5) - 4 = 180 - 4 = 176
    return result

# Recompute final_diagnostic correctly
final_diagnostic = process_metrics(aggregate_data, baseline_threshold)

print(f"Target result: {final_diagnostic}")