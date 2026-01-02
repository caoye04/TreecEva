import math

# Simulated sensor array data (real measurements with noise)
sensor_readings = [14.2, 18.7, 22.5, 19.3, 25.1, 17.4, 20.8, 23.6, 16.9, 21.0]

# Irrelevant auxiliary constants (distractors)
CALIBRATION_OFFSET = 0.87
NOISE_FLOOR_DB = -92.3
REFERENCE_VOLTAGE = 3.3
MAX_SAMPLE_RATE = 192000

# Preprocessing configuration
filter_kernel = [0.1, 0.25, 0.3, 0.25, 0.1]  # Symmetric smoothing kernel
decimation_factor = 2
smoothing_passes = 3

# Signal conditioning pipeline
def apply_filter(data, kernel):
    padded = [data[0]] * (len(kernel) // 2) + data + [data[-1]] * (len(kernel) // 2)
    result = []
    for i in range(len(data)):
        weighted_sum = sum(padded[i + j] * kernel[j] for j in range(len(kernel)))
        result.append(weighted_sum)
    return result

def decimate(data, factor):
    return data[::factor]

def normalize(data):
    max_val = max(data)
    min_val = min(data)
    range_val = max_val - min_val
    return [(x - min_val) / range_val for x in data] if range_val != 0 else [0] * len(data)

# Irrelevant transformation (dead path - never used)
def frequency_transform(data):
    transformed = []
    for i, x in enumerate(data):
        transformed.append(x * math.sin(i * math.pi / 8))
    return transformed

# Used only once in a misleading context
intermediate_noisy = [x + 0.5 * math.cos(i) for i, x in enumerate(sensor_readings)]

# Main preprocessing
filtered_data = sensor_readings
for _ in range(smoothing_passes):
    filtered_data = apply_filter(filtered_data, filter_kernel)

# Misleading conditional expression (distractor)
processed_data = decimate(filtered_data, decimation_factor) if len(filtered_data) > 8 else normalize(filtered_data)

# Red herring: unused but plausible-looking normalization
normalized_for_reference = [x / REFERENCE_VOLTAGE for x in processed_data]

# Diagnostic thresholds (key data structure)
threshold_map = {
    'critical': 20.0,
    'elevated': 18.0,
    'normal': 15.0
}

# Auxiliary diagnostic logic with decoy functions
def assess_risk_level(value, thresholds):
    if value > thresholds['critical']:
        return 'CRITICAL'
    elif value > thresholds['elevated']:
        return 'ELEVATED'
    elif value > thresholds['normal']:
        return 'NORMAL'
    else:
        return 'LOW'

# Never called - decoy function to distract
def compute_failure_probability(reading_seq, risk_profile='standard'):
    base_prob = 0.0
    for val in reading_seq:
        base_prob += math.exp(-val / 10)
    return min(base_prob, 1.0)

# Core analysis function
seen_states = set()
counter_logs = []

def analyze_signal(data_chunk, thresholds):
    total_score = 0.0
    state_transitions = 0
    
    # Process each element with state tracking
    prev_was_elevated = False
    for raw_val in data_chunk:
        # Apply hidden correction (not obvious at first glance)
        corrected = raw_val - CALIBRATION_OFFSET
        
        # Determine current state
        current_state = assess_risk_level(corrected, thresholds)
        seen_states.add(current_state)
        
        # Scoring logic with conditional expression
        penalty = 15 if corrected > thresholds['critical'] else (8 if corrected > thresholds['elevated'] else 0)
        bonus = 5 if corrected < thresholds['normal'] else 0
        
        # Update score
        total_score += corrected - penalty + bonus
        
        # Track transitions (bit manipulation red herring)
        current_elevated = corrected > thresholds['elevated']
        if prev_was_elevated and not current_elevated:
            state_transitions += 1
        prev_was_elevated = current_elevated
    
    # Additional transformation on transitions (misleading)
    transition_code = state_transitions << 2  # Shift left by 2 (unused later)
    
    # Key calculation buried in logic
    adjustment_factor = len(seen_states) * 0.75
    final_score = total_score * adjustment_factor
    
    # Dead code path based on impossible condition (distractor)
    if math.isnan(final_score):
        counter_logs.append('Invalid score encountered')
        return -999.0
    
    return final_score

# Secondary irrelevant processing chain
def generate_diagnostic_report(signal, config_override=None):
    report_data = {}
    sorted_values = sorted(signal)
    median_val = sorted_values[len(sorted_values)//2]
    report_data['median'] = median_val
    report_data['entropy'] = sum(-x/50 * math.log(x/50) for x in signal if x > 0)
    report_data['peaks'] = [i for i, x in enumerate(signal) if i > 0 and i < len(signal)-1 and signal[i-1] < x > signal[i+1]]
    return report_data

# Unused but plausible call
report_snapshot = generate_diagnostic_report(sensor_readings)

# Actual execution path
processed_data = normalize(processed_data)  # Final normalization step

# Critical statement
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")