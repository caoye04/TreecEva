from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timing_samples = [1.2, 0.8, 1.5, 2.3, 0.9, 1.1, 1.6, 2.0, 1.4, 0.7]
error_codes = [0, 1, 0, 2, 0, 0, 1, 0, 0, 3]
sensor_readings = [(23.5, 45.1), (24.1, 44.8), (22.9, 46.2), (25.3, 43.7), (26.0, 42.9)]

# Irrelevant preprocessing - red herring
normalized_samples = [round((x - min(timing_samples)) / (max(timing_samples) - min(timing_samples)), 3) for x in timing_samples]
scaled_errors = [e * 100 for e in error_codes if e > 0]

# Misleading diagnostic function (never called)
def legacy_diagnose(data):
    return sum(d ** 2 for d in data) / len(data)

# Unused auxiliary structure
diagnostic_map = defaultdict(lambda: 'unknown')
for i, code in enumerate(['ok', 'timeout', 'overload', 'corruption']):
    diagnostic_map[i] = code

# Real processing begins here
def analyze_timing(data):
    avg = sum(data) / len(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)
    return {'mean': avg, 'variance': variance, 'stability': avg / (variance + 1e-5)}

def extract_flags(errors):
    flag_set = set()
    counts = Counter(errors)
    if counts[1] > 2:
        flag_set.add('timeout_alert')
    if counts[2] > 0:
        flag_set.add('overload_warning')
    if any(e >= 3 for e in errors):
        flag_set.add('critical_failure')
    if counts[0] < len(errors) * 0.5:
        flag_set.add('instability')
    return flag_set

# Simulated log aggregation
timing_log = analyze_timing(timing_samples)
system_flags = extract_flags(error_codes)

# Decoy transformation - looks important but unused later
temp_analysis = []
for i, (t, e) in enumerate(zip(timing_samples, error_codes)):
    if e > 0:
        temp_analysis.append({'index': i, 'severity': e * t})

# Distractor: fake fusion logic
fusion_weights = {'w1': 0.7, 'w2': 1.3, 'w3': 0.4}
hybrid_score = 0
for w in fusion_weights.values():
    hybrid_score += w * timing_log['mean']
hybrid_score = math.tanh(hybrid_score)  # Looks sophisticated, but irrelevant

# Another decoy: sensor correlation (unused)
sensor_trends = []
for temp, pressure in sensor_readings:
    trend = 'rising' if temp > 24.0 else 'stable'
    sensor_trends.append((temp, pressure, trend))

# Core logic buried among distractions
def aggregate_metrics(metrics, flags):
    base = metrics['mean'] * 100
    penalty = 0
    if 'timeout_alert' in flags:
        penalty += 15
    if 'overload_warning' in flags:
        penalty += 25
    if 'critical_failure' in flags:
        penalty += 50
    if 'instability' in flags:
        penalty += 20
    
    # Additional computation using list comprehension and zip
    phase_shifts = [abs(timing_samples[i] - timing_samples[i-1]) for i in range(1, len(timing_samples))]
    instability_factor = sum(1 for s in phase_shifts if s > 0.5)
    
    # Final adjustment
    adjusted = base + penalty + (instability_factor * 5)
    
    # Use of enumerate and zip in meaningful but non-critical way
    correction = 0
    for idx, (p, e) in enumerate(zip(phase_shifts, error_codes[1:])):
        if e > 0 and p > 0.7:
            correction += idx * e
    
    return int(adjusted + correction)

# Key execution point
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Print result as required
print(f"Result: {final_diagnostic}")