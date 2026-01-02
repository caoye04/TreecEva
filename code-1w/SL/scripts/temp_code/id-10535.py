from collections import defaultdict, Counter
import math

# Simulated sensor data: timestamp -> readings
timestamped_readings = [
    (1001, {'temp': 36.8, 'pulse': 72, 'o2': 98}),
    (1002, {'temp': 37.1, 'pulse': 74, 'o2': 97}),
    (1003, {'temp': 37.5, 'pulse': 78, 'o2': 96}),
    (1004, {'temp': 38.2, 'pulse': 85, 'o2': 94}),
    (1005, {'temp': 38.6, 'pulse': 90, 'o2': 93}),
    (1006, {'temp': 39.0, 'pulse': 95, 'o2': 92}),
    (1007, {'temp': 38.8, 'pulse': 92, 'o2': 93}),
    (1008, {'temp': 38.3, 'pulse': 88, 'o2': 94}),
]

# Irrelevant baseline metrics (distractor)
baseline_stats = defaultdict(lambda: 0)
for ts, readings in timestamped_readings:
    for k, v in readings.items():
        baseline_stats[k] += v

# Unused transformation function (dead code path)
def transform_readings(data_list):
    return [dict(sorted(item[1].items())) for item in data_list]

# Another red herring: pulse trend analysis (not used in final result)
pulse_trend = []
for entry in timestamped_readings:
    if entry[1]['pulse'] > 80:
        pulse_trend.append('elevated')
    else:
        pulse_trend.append('normal')

# Real processing starts here
active_flags = set()
severity_map = {}

for idx, (ts, vitals) in enumerate(timestamped_readings):
    flags = []
    severity_score = 0

    # Core logic: fever detection and o2 decline correlation
    if vitals['temp'] >= 38.0:
        flags.append('fever')
        severity_score += 3
    elif vitals['temp'] >= 37.5:
        flags.append('low_fever')
        severity_score += 1

    if vitals['o2'] < 95:
        flags.append('low_o2')
        severity_score += 2

    if len(flags) > 0:
        active_flags.update(flags)
        severity_map[ts] = severity_score

# Misleading aggregation (looks important but unused)
avg_pulse = sum(v['pulse'] for _, v in timestamped_readings) / len(timestamped_readings)
max_temp = max(v['temp'] for _, v in timestamped_readings)

def analyze_trends(vital_data):
    # Complex but irrelevant trend analyzer
    changes = []
    for i in range(1, len(vital_data)):
        prev = vital_data[i-1][1]
        curr = vital_data[i][1]
        delta = (curr['temp'] - prev['temp']) * (curr['o2'] - prev['o2'])
        changes.append(delta)
    return sum(changes) / len(changes) if changes else 0

# Unused lambda (distractor)
smooth_data = lambda d: {k: round(sum(x[1][k] for x in d)/len(d), 1) for k in ['temp','pulse','o2']}

# Core diagnostic processor
thresholds = {
    'fever': 38.0,
    'critical_o2': 92,
    'tachycardia': 90
}

# Health data preparation with slicing relevant entries
recent_data = timestamped_readings[-5:]  # Most recent 5 readings
historical_baseline = timestamped_readings[:3]   # First 3 as baseline

# Process metrics function that actually matters
def process_metrics(data_slice, limits):
    high_risk_count = 0
    total_severity = 0
    temp_spikes = 0

    for ts, v in data_slice:
        # Key diagnostic logic chain
        fever_present = v['temp'] > limits['fever']
        o2_critical = v['o2'] <= limits['critical_o2']
        pulse_critical = v['pulse'] >= limits['tachycardia']

        # Composite risk assessment (nested logic)
        if fever_present:
            temp_spikes += 1
            if o2_critical:
                high_risk_count += 1
                if pulse_critical:
                    total_severity += 5  # Triple threat
                else:
                    total_severity += 3
            else:
                total_severity += 1
        elif o2_critical and pulse_critical:
            total_severity += 2

    # Secondary calculation: stability index (distraction)
    temp_changes = [data_slice[i+1][1]['temp'] - data_slice[i][1]['temp'] 
                   for i in range(len(data_slice)-1)]
    stability_index = sum(abs(delta) for delta in temp_changes)

    # Tertiary metric: flag frequency (not used)
    flag_counter = Counter()
    for _, v in data_slice:
        if v['temp'] > 38.0: flag_counter['high_temp'] += 1
        if v['o2'] < 95: flag_counter['low_o2'] += 1

    # Final computation: this is what actually gets used
    risk_multiplier = 2 if high_risk_count >= 2 else 1
    adjusted_severity = (total_severity + temp_spikes) * risk_multiplier

    # This is the actual answer path
    adjustment_factor = 0.8 if stability_index > 3.0 else 1.0
    final_score = math.floor(adjusted_severity * adjustment_factor)

    # IRRELEVANT: additional diagnostics (distractors)
    avg_o2 = sum(v['o2'] for _, v in data_slice) / len(data_slice)
    min_pulse = min(v['pulse'] for _, v in data_slice)
    
    # The real answer is computed here and stored in final_score
    return final_score

# Execute the key statement
diagnostic_log = []
for reading in timestamped_readings:
    diagnostic_log.append(f"Time {reading[0]}: Evaluated")

final_diagnostic = process_metrics(recent_data, thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")