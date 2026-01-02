import math

# Simulated health monitoring system with signal processing and diagnostic logic
def analyze_waveform(signal):
    peak = max(signal)
    baseline = sum(signal) / len(signal)
    deviation = (max(signal) - min(signal)) / 2
    # Irrelevant transformation (distractor)
    normalized = [x / peak for x in signal if x > 0]
    # Dead computation path
    if len(normalized) > 100:
        smoothed = [normalized[i] + normalized[i+1] for i in range(len(normalized)-1)]
    return {'peak': peak, 'baseline': baseline, 'deviation': deviation}

# Decoy function – looks important but unused in critical path
def compute_stress_index(vital_signs):
    stress = 0
    for val in vital_signs:
        if val > 70:
            stress += math.log(val) * 1.5
    return round(stress, 3)

# Signal filter that appears complex but only used conditionally
# (used in one case, otherwise dead code)
def apply_bandpass(signal, low=0.5, high=40.0):
    filtered = []
    for s in signal:
        if low <= abs(s) <= high:
            filtered.append(s * 0.95)
    return filtered if len(filtered) > 10 else signal[:len(filtered)]

# Core metric processor - contains relevant logic
metrics_catalog = {
    'alpha': lambda x: x ** 2 if x > 0 else 0,
    'beta': lambda x: int(abs(x) * 1.732),
    'gamma': lambda x: x + math.sin(x)
}

def evaluate_risk_level(metrics):
    score = 0
    score += metrics['peak'] // 5
    score -= metrics['baseline'] // 10
    if metrics['deviation'] > 15:
        score += 8
    return 'high' if score > 12 else 'moderate'

# Conditional expression with distractors
threshold_func = lambda x: 'strict' if x > 100 else ('relaxed' if x < 50 else 'normal')

# Simulated data ingestion with red herring fields
device_log = [
    {'timestamp': 1678886400, 'type': 'calibration', 'value': 95.5, 'unit': 'mV'},
    {'timestamp': 1678886401, 'type': 'signal', 'value': 102.3, 'unit': 'mV'},
    {'timestamp': 1678886402, 'type': 'noise', 'value': 45.1, 'unit': 'mV'},
    {'timestamp': 1678886403, 'type': 'signal', 'value': 110.7, 'unit': 'mV'},
    {'timestamp': 1678886404, 'type': 'signal', 'value': 98.2, 'unit': 'mV'}
]

# Extract relevant signal values (ignoring noise and calibration)
signal_values = [entry['value'] for entry in device_log if entry['type'] == 'signal']

# Apply bandpass filter (conditional use - actually not applied due to control flag)
use_filter = False
filtered_signal = apply_bandpass(signal_values) if use_filter else signal_values

# Analyze waveform to extract key diagnostics
raw_diagnostics = analyze_waveform(filtered_signal)

# Unused intermediate calculation (misleading)
avg_power = sum([x*x for x in filtered_signal]) / len(filtered_signal)

# Determine operational mode based on environment (unused but plausible)
environment_mode = 'urban' if avg_power > 10000 else 'rural'

# Process metrics using functional mapping and conditional logic
def process_metrics(data, threshold_strategy):
    analysis = analyze_waveform(data)
    risk = evaluate_risk_level(analysis)
    
    # Compute derived metrics using lambda catalog (only gamma used in final step)
    derived = {}
    for key, func in metrics_catalog.items():
        if key == 'alpha':
            derived[key] = func(analysis['peak'])
        elif key == 'beta':
            derived[key] = func(analysis['baseline'])
        else:
            derived[key] = func(analysis['deviation'])
    
    # Complex conditional expression with nested logic
    adjustment_factor = 1.25 if threshold_strategy(analysis['peak']) == 'strict' else (0.85 if threshold_strategy(analysis['peak']) == 'relaxed' else 1.0)
    
    # Key intermediate result (looks like answer but isn't)
    preliminary_score = (derived['alpha'] * 0.3) + (derived['beta'] * 0.2) + (derived['gamma'] * 0.5)
    
    # Final diagnostic depends only on gamma and adjustment
    # All prior complexity leads to this simple expression
    final_value = derived['gamma'] * adjustment_factor
    
    # Red herring: unused compound index
    composite_index = (analysis['peak'] * derived['beta']) / (analysis['baseline'] + 1) if analysis['baseline'] > 0 else 0
    
    return final_value

# Execute core logic
final_diagnostic = process_metrics(health_data=signal_values, threshold_func=threshold_func)

print(f"Result: {final_diagnostic}")