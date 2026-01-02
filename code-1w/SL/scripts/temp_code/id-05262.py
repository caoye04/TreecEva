from collections import defaultdict, Counter
import math

# Simulated health monitoring system with diagnostic logic

def analyze_heart_rate(hr):
    if hr < 50:
        return 'bradycardia'
    elif hr > 100:
        return 'tachycardia'
    else:
        return 'normal'

def compute_stress_index(values):
    mean_val = sum(values) / len(values)
    stress = 0
    for v in values:
        stress += (v - mean_val) ** 2
    return math.sqrt(stress / len(values))

def evaluate_rhythm(irregularity_log):
    count = Counter(irregularity_log)
    total = len(irregularity_log)
    if total == 0:
        return 0.0
    max_count = max(count.values())
    return max_count / total

# Irrelevant helper - decoy function (dead code path)
def unused_diagnostic_tool(data):
    temp_store = []
    for item in data:
        temp_store.append({"raw": item, "flagged": False})
    processed = sorted(temp_store, key=lambda x: str(x["raw"]))
    return [p["raw"] for p in processed if not p["flagged"]]

# Another red herring - complex but unused transformation
def transform_readings(readings):
    result = defaultdict(list)
    for timestamp, value in readings.items():
        category = 'high' if value > 80 else 'low' if value < 60 else 'medium'
        result[category].append((timestamp, value ** 0.5))
    final = {}
    for cat, entries in result.items():
        final[cat] = [e[1] for e in entries]
    return final

def process_metrics(data, config):
    # Main processing pipeline
    baseline = config['baseline']
    tolerance = config['tolerance']
    critical_hr = config['critical_heart_rate']

    heart_rates = data['heart_rate_history']
    oxygen_levels = data['oxygen_saturation']
    neural_activity = data['neural_spike_count']

    # Distractor variables - used to mislead
    dummy_sum = 0
    temp_cache = []
    for i in range(len(oxygen_levels)):
        dummy_sum += oxygen_levels[i] * 1.5
        temp_cache.append(dummy_sum / (i + 1))

    # Real signal extraction
    avg_o2 = sum(oxygen_levels) / len(oxygen_levels)
    current_hr = heart_rates[-1]

    # Diagnostic flags
    hr_status = analyze_heart_rate(current_hr)
    stress_level = compute_stress_index(neural_activity)

    # Simulated arrhythmia detection log (partially relevant)
    rhythm_pattern = [1 if x % 3 == 0 else 0 for x in range(len(heart_rates))]
    rhythm_consistency = evaluate_rhythm(rhythm_pattern)

    # Hidden calculation: weighted diagnostic score
    hr_weight = 0.4
    o2_weight = 0.3
    stress_weight = 0.2
    rhythm_weight = 0.1

    hr_score = 100 if hr_status == 'normal' else 40
    o2_score = 90 if avg_o2 >= 95 else 60 if avg_o2 >= 90 else 30
    stress_score = 100 if stress_level < 5 else 50 if stress_level < 10 else 20
    rhythm_score = 100 if rhythm_consistency > 0.7 else 40

    # Final composite metric
    composite = (
        hr_score * hr_weight +
        o2_score * o2_weight +
        stress_score * stress_weight +
        rhythm_score * rhythm_weight
    )

    # Apply nonlinear correction based on critical threshold
    if current_hr > critical_hr:
        composite *= 0.75  # emergency penalty

    # Additional distraction: update cache with meaningless stats
    stats_log = defaultdict(int)
    for val in neural_activity:
        bucket = val // 10
        stats_log[bucket] += 1
    summary_text = "Report:" + " ".join([f"{k}:{v}" for k, v in sorted(stats_log.items())])

    # Final diagnostic is floor of corrected composite
    final_diagnostic = int(composite)

    # Dead code - never reached
    if final_diagnostic < 0:
        final_diagnostic = 0
    elif final_diagnostic > 100:
        final_diagnostic = 100

    return final_diagnostic

# Input data setup
health_data = {
    'patient_id': 'P-7821',
    'heart_rate_history': [72, 75, 68, 88, 92, 96, 101, 94],
    'oxygen_saturation': [97, 96, 98, 95, 94, 96, 97],
    'neural_spike_count': [23, 25, 20, 30, 28, 27, 26, 24, 22, 21],
    'temperature_readings': [36.6, 36.8, 37.1, 36.9]  # Unused field
}

thresholds = {
    'baseline': 70,
    'tolerance': 5,
    'critical_heart_rate': 100,
    'activation_delay': 2.5  # Unused
}

# Execution point of interest
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")