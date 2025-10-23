import math
from collections import defaultdict

def calculate_attenuation_factor(signal_strength, distance):
    return math.exp(-0.1 * distance) * signal_strength

def is_critical_zone(zone_id, signal_history):
    return zone_id in signal_history and signal_history[zone_id] > 100

def compute_weighted_log_sum(values, weights):
    return sum(math.log(v + 1) * w for v, w in zip(values, weights) if v > 0)

# Signal data processing pipeline
signal_readings = [45.2, 89.7, 120.1, 67.3, 200.5]
distance_metrics = [10, 25, 5, 30, 15]
zone_identifiers = ['Z1', 'Z2', 'Z3', 'Z4', 'Z5']
zone_histories = defaultdict(float, {'Z1': 95.2, 'Z2': 105.8, 'Z3': 80.0, 'Z5': 150.3})
attenuation_weights = [0.5, 0.7, 0.9, 0.6, 0.8]

adjusted_signals = [
    calculate_attenuation_factor(sig, dist) 
    for sig, dist in zip(signal_readings, distance_metrics)
]

critical_mask = [
    is_critical_zone(zone, zone_histories) and att > 50.0
    for zone, att in zip(zone_identifiers, adjusted_signals)
]

filtered_weights = [
    weight if mask else 0.1 
    for weight, mask in zip(attenuation_weights, critical_mask)
]

logarithmic_components = [
    math.log(signal + 1) if signal > 0 else 0 
    for signal in adjusted_signals
]

weighted_log_sum = compute_weighted_log_sum(logarithmic_components, filtered_weights)

# Final degradation index calculation
final_degradation_index = math.pow(weighted_log_sum, 1.5) * 100

print(f"Result: {final_degradation_index:.6f}")