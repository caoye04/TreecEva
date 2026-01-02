import math

# Sensor calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.87
NOISE_FLOOR = 0.003
MAX_SENSOR_RANGE = 1024

# Simulated environmental readings from multiple sources
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 23.7]
humidity_readings = [45, 47, 50, 44, 48, 51, 46]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1013]

# Irrelevant preprocessing: normalize humidity to float (unused later)
normalized_humidity = [h / 100.0 for h in humidity_readings if h > 40]

# Relevant data: transform temperature into discrete categories
categorized_temps = {}
for i, temp in enumerate(temperature_readings):
    label = 'high' if temp > 24.0 else 'normal' if temp > 23.0 else 'low'
    categorized_temps[f't{i}'] = {'value': temp, 'category': label}

# Misleading aggregation: average pressure (not used in final logic)
avg_pressure = sum(pressure_readings) / len(pressure_readings)
adjusted_pressures = {i: p - avg_pressure + 10 for i, p in enumerate(pressure_readings)}

# Construct threshold map based on empirical rules (key input)
threshold_map = {
    'high_temp': 24.0,
    'spike_delta': 1.2,
    'decay_factor': 0.9,
    'baseline': 23.0
}

# Transform raw temperature into processed signal with decay modeling
processed_data = []
current_state = 0.0
for temp in temperature_readings:
    delta = temp - threshold_map['baseline']
    if delta > threshold_map['spike_delta']:
        current_state += delta * 1.5
    else:
        current_state = current_state * threshold_map['decay_factor']  # exponential decay
    processed_data.append(round(current_state, 3))

# Dead code path: simulate predictive model (never called)
def predict_next_value(data, factor=0.75):
    if len(data) == 0:
        return 0.0
    weighted = sum(factor ** i * v for i, v in enumerate(reversed(data[-3:])))
    return round(weighted, 3)

# Unused diagnostic function
def compute_variance(values):
    mean_val = sum(values) / len(values)
    return sum((v - mean_val) ** 2 for v in values) / len(values)

# Core analysis function with dictionary-based rule evaluation
def evaluate_stability(history, thresholds):
    if not history:
        return 0
    
    high_count = sum(1 for h in history if h > thresholds['high_temp'])
    recent_peak = max(history[-3:]) if len(history) >= 3 else max(history)
    
    rules_passed = 0
    stability_score = 0.0
    
    # Rule 1: too many highs reduce stability
    if high_count <= 2:
        rules_passed += 1
        stability_score += 10
    
    # Rule 2: recent peak matters
    if recent_peak < 24.5:
        rules_passed += 1
        stability_score += 15
    
    # Rule 3: trend is decaying
    if len(history) >= 4 and all(history[i] >= history[i+1] for i in range(-4, -1)):
        rules_passed += 1
        stability_score += 20
    
    # Final scoring uses complex weighting (only some paths matter)
    if rules_passed == 3:
        stability_score += 100
    elif rules_passed == 2:
        stability_score += 50
    else:
        stability_score += 10
        
    return int(stability_score)

# Secondary helper - actually used in final step
def count_transitions(data, thresh):
    transitions = 0
    prev_high = False
    for val in data:
        is_high = val > thresh
        if is_high and not prev_high:
            transitions += 1
        prev_high = is_high
    return transitions

# Main analysis function combining multiple concepts
def analyze_readings(signal, config_map):
    # Extract parameters
    spike_level = config_map['spike_delta'] + 1.3  # effective threshold = 2.5
    base = config_map['baseline']
    
    # Compute derived metrics
    above_spike = [s for s in signal if s > spike_level]
    transition_events = count_transitions(signal, spike_level)
    
    # Build diagnostic profile
    profile = {
        'event_count': len(above_spike),
        'transitions': transition_events,
        'max_signal': max(signal) if signal else 0,
        'duration': len(signal)
    }
    
    # Apply multi-stage logic to compute final diagnostic code
    diagnostic_code = 1000
    if profile['event_count'] == 0:
        diagnostic_code -= 500
    elif profile['event_count'] == 1:
        diagnostic_code -= 300
    else:
        diagnostic_code -= 100
        
    if profile['transitions'] >= 2:
        diagnostic_code += 25
        
    if profile['max_signal'] > 4.0:
        diagnostic_code += 15
        
    if profile['duration'] >= 7:
        diagnostic_code += 10
        
    # Final nonlinear adjustment based on historical pattern
    adjustment_key = 'adjust_{}'.format(min(len(above_spike), 2))
    adjustments = {
        'adjust_0': -50,
        'adjust_1': 20,
        'adjust_2': 35
    }
    
    final_adjust = adjustments.get(adjustment_key, 0)
    diagnostic_code += final_adjust
    
    return diagnostic_code

# Execution point: process the transformed signal
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")