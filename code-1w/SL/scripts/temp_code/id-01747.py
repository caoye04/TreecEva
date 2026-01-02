import math

# Simulated sensor data from environmental monitoring array
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 24.9, 23.0]
humidity_readings = [45, 48, 50, 55, 60, 62, 58]
pressure_readings = [1013, 1015, 1012, 1009, 1007, 1008, 1010]

# Irrelevant auxiliary data (distractor)
color_spectrum = ['red', 'green', 'blue', 'infrared']
sample_ids = {f's{idx}': f'device_{(idx * 3) % 7}' for idx in range(10)}

# Signal preprocessing with red herrings
def filter_outliers(data, limit=2.0):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) <= limit * std_dev]

# Misleading transformation chain (partially unused)
def transform_to_frequency_domain(signal):
    # Simulate FFT without actual complex math
    return [round(math.sin(x / 10) * 100) % 73 for x in signal]

# Decoy function that looks important but isn't used in critical path
def calculate_entropy(values):
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

# Core processing with conditional logic and set operations
baseline_temps = {round(t) for t in temperature_readings}
extreme_temps = {t for t in baseline_temps if t >= 25}
normal_band = set(range(20, 26))
stability_flags = {
    'stable_temp': len(baseline_temps & extreme_temps) < 2,
    'pressure_trend': pressure_readings[-1] > pressure_readings[0],
    'humidity_spike': max(humidity_readings) - min(humidity_readings) > 15
}

# Multiple assignment with distractors
raw_signal = [t * 1.8 + 32 for t in temperature_readings]  # Convert to Fahrenheit (unused)
adjusted_humidity = [(h + 5) % 100 for h in humidity_readings]  # Artificial adjustment
processed_data = filter_outliers([t ** 1.1 for t in temperature_readings])  # Actual input

# Complex threshold map with nested structure (some fields are decoys)
threshold_map = {
    'temp_c': {'warn': 24.5, 'crit': 26.0},
    'freq': {'warn': 30, 'crit': 50},  # Unused in final analysis
    'duration': None,  # Dead field
    'flags': ['calibrated', 'verified', 'validated']
}

# Bit manipulation as distraction (simulates hardware-level checks)
hardware_signature = 0b101101
validation_mask = 0b111100
masked_sig = hardware_signature & validation_mask
is_validated = (masked_sig ^ 0b111100) == 0  # Always False

# String-based status code (irrelevant to final result)
diagnostic_log = "ERR_OK, CAL_PASS, STG_3, V7R2"
status_tokens = diagnostic_log.split(', ')
version_flag = any('V7' in token for token in status_tokens)

# Conditional expression mix with fallback logic
def evaluate_risk_level(value, thresholds):
    w, c = thresholds['warn'], thresholds['crit']
    return 'CRITICAL' if value > c else 'WARNING' if value > w else 'NORMAL'

# Data transformation with red herring control flow
def generate_diagnostics(dataset, config):
    results = {}
    temp_avg = sum(dataset) / len(dataset)
    
    # Simulated multi-stage analysis
    for i, val in enumerate(dataset):
        if i % 3 == 0:
            # Apply arbitrary correction
            corrected = val * 0.98 + 0.5
        elif i % 3 == 1:
            corrected = val * 1.02
        else:
            corrected = val
            
        category = evaluate_risk_level(corrected, config['temp_c'])
        results[f'sample_{i}'] = {
            'value': round(corrected, 2),
            'risk': category,
            'validated': is_validated  # Carries false value (distractor)
        }
        
        # Dead logic branch (never reached due to structure)
        if temp_avg < 0:
            anomaly_score = calculate_entropy([int(temp_avg)])
            results[f'sample_{i}']['entropy'] = anomaly_score
            
    return results

# Another decoy: unused recursive function
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# Critical function with logical dependencies
prev_state = [False, True, True]

def analyze_signal(cleaned_input, limits):
    avg_val = sum(cleaned_input) / len(cleaned_input)
    peak = max(cleaned_input)
    duration_hours = len(cleaned_input) * 0.5
    
    # Conditional expression with combined boolean logic
    base_alert = evaluate_risk_level(avg_val, limits['temp_c'])
    peak_alert = evaluate_risk_level(peak, limits['temp_c'])
    
    # Boolean logic with short-circuiting and set membership
    has_extremes = any(round(x) in extreme_temps for x in cleaned_input)
    in_normal_band = all(round(x) in normal_band for x in cleaned_input)
    
    # Composite score calculation (only some components matter)
    score_components = {
        'avg_weight': 0.4 * (avg_val - 20),
        'peak_bonus': 0.3 * max(0, peak - 25) if peak_alert != 'NORMAL' else 0,
        'stability': 0.2 * len([f for f in stability_flags.values() if f]),
        'legacy_adj': 0.1 * (fibonacci(5) - 5)  # Evaluates to zero, but looks complex
    }
    
    # Final diagnostic computed via weighted sum
    composite_score = sum(score_components.values())
    
    # Key decision point with distractor variables in scope
    final_diagnostic = composite_score if base_alert != 'NORMAL' else avg_val
    
    # This print is required for traceability
    return final_diagnostic

# Execute main analysis
final_diagnostic = analyze_signal(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")