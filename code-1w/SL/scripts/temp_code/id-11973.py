from collections import defaultdict, Counter
import math

# Simulated sensor array diagnostics with redundant and irrelevant computations

def analyze_fluctuations(signal_log):
    if not signal_log:
        return 0
    avg = sum(signal_log) / len(signal_log)
    variance = sum((x - avg) ** 2 for x in signal_log) / len(signal_log)
    return math.sqrt(variance)

# Irrelevant helper function (dead code path)
def calculate_resonance_frequency(tuning_factor):
    resonance = 0
    for i in range(1, 100):
        resonance += math.sin(i * tuning_factor) / i
    return round(resonance, 4)

# Unused signal processor chain
def legacy_process_chain(inputs):
    processed = []
    for val in inputs:
        temp = val * 0.85 + 2.1
        if temp > 10:
            temp = math.log(temp, 2)
        processed.append(round(temp, 3))
    return processed

# Core diagnostic logic
baseline_readings = [12.4, 15.1, 13.8, 14.2, 16.0, 13.5, 14.8]
recent_samples = [13.1, 15.6, 12.9, 14.0, 15.8, 13.7, 15.2]

# Distractor: unused data structures
device_registry = defaultdict(lambda: 'unassigned')
device_registry['sensor_01'] = 'active'
device_registry['sensor_02'] = 'standby'

reading_metadata = Counter()
for reading in baseline_readings:
    reading_metadata[round(reading)] += 1

# Compute deviation map (relevant)
deviation_map = {}
for i, (base, curr) in enumerate(zip(baseline_readings, recent_samples)):
    deviation_map[f'sensor_{i+1:02d}'] = round(abs(curr - base), 3)

# Red herring: complex but unused transformation
transformed_deviation = {
    k: round(v ** 1.5 + math.cos(i), 4) 
    for i, (k, v) in enumerate(deviation_map.items())
}

# Decoy weight adjustment using lambda (irrelevant)
adaptation_curve = lambda x: 0.9 + 0.1 * math.exp(-x / 10)
simulated_adaptations = [adaptation_curve(i) for i in range(5)]

# Real weighting scheme (obscured by noise)
baseline_weights = {
    'sensor_01': 0.8,
    'sensor_02': 1.2,
    'sensor_03': 0.9,
    'sensor_04': 1.0,
    'sensor_05': 1.1,
    'sensor_06': 0.85,
    'sensor_07': 0.95
}

# Key computation buried among distractors
effective_deviations = []
for sensor_id, dev in deviation_map.items():
    weight = baseline_weights.get(sensor_id, 1.0)
    weighted_dev = dev * weight
    effective_deviations.append(weighted_dev)

# Secondary red herring: set operations with no impact
critical_sensors = {s for s, d in deviation_map.items() if d > 0.5}
monitored_zones = {'sensor_01', 'sensor_03', 'sensor_05', 'sensor_07'}
overlap_check = critical_sensors & monitored_zones

# Actual aggregation function
def aggregate_metrics(dev_map, weights):
    # Unused local counter (distraction)
    op_counter = Counter(type="aggregation", steps=0)
    
    total_influence = 0.0
    combined_weight = 0.0
    
    for sensor, dev in dev_map.items():
        w = weights.get(sensor, 1.0)
        total_influence += dev * w
        combined_weight += w
    
    if combined_weight == 0:
        return 0.0
    
    # Final weighted average
    raw_result = total_influence / combined_weight
    
    # Apply final nonlinearity (relevant)
    final_score = math.tanh(raw_result) * 100
    
    # Dead code branch (never executed due to logic)
    if final_score < 0:
        final_score = abs(final_score) * 0.5
    
    return round(final_score, 6)

# Execute main logic
system_stability_index = analyze_fluctuations(baseline_readings)
system_stability_index += calculate_resonance_frequency(0.7)  # adds ~0.0, irrelevant

# Critical statement
final_diagnostic = aggregate_metrics(deviation_map, baseline_weights)

# Print result as required
print(f"Result: {final_diagnostic}")