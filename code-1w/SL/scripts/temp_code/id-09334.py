from collections import defaultdict
import math

# Irrelevant helper function (decoy)
def compute_entropy(data):
    entropy = 0.0
    freq = defaultdict(int)
    for item in data:
        freq[item] += 1
    total = len(data)
    for count in freq.values():
        if count > 0:
            prob = count / total
            entropy -= prob * math.log2(prob)
    return entropy

# Misleading stress calibration with dead-end logic
def calibrate_sensor(signal_log):
    baseline = 0
    adjustment = 1.0
    for entry in signal_log:
        if 'error' in entry:
            continue
        parts = entry.split('_')
        if len(parts) > 1 and parts[1].isdigit():
            baseline += int(parts[1])
    # This function returns but is never used in critical path
    return baseline * adjustment

# Core simulation: material strain response under varying stress sequences
def calculate_strain_response(stress_sequence, threshold_map):
    history = defaultdict(int)
    cumulative_shift = 0
    temp_buffer = []
    
    # Preprocess thresholds (some irrelevant filtering)
    valid_thresholds = {k: v for k, v in threshold_map.items() if v > 5}
    fallback_value = sum(valid_thresholds.values()) // len(valid_thresholds) if valid_thresholds else 10
    
    for idx, stress in enumerate(stress_sequence):
        # Simulate hysteresis effect with conditional branching
        if stress > 150:
            phase = 'plastic'
            multiplier = 1.8
        elif stress > 100:
            phase = 'elastic'
            multiplier = 1.4
        else:
            phase = 'static'
            multiplier = 1.0
            
        # Update history (used later)
        history[phase] += 1
        
        # Apply dynamic transformation
        adjusted_stress = stress * multiplier
        
        # Introduce bit manipulation red herring
        binary_tag = (idx << 2) ^ 7
        if binary_tag & 1:
            adjusted_stress = abs(adjusted_stress - 10)  # Minor perturbation
        
        # Accumulate only under certain conditions (critical path)
        if adjusted_stress > 120 or (idx % 3 == 0 and stress < 200):
            cumulative_shift += int(adjusted_stress // 4)
        
        # Dead code path - never accessed due to logic above
        if phase == 'static' and stress < 0:
            temp_buffer.append(stress)  # Unreachable

    # Secondary processing with string-based distractor
    status_flags = ['OK', 'CALIBRATING', 'STABLE']
    flag_summary = ''.join([f[0] for f in status_flags])  # 'OCS' - unused
    
    # Final computation using accumulated shift and history
    plastic_contrib = history['plastic'] * 16
    elastic_contrib = history['elastic'] * 9
    static_contrib = history['static'] * 2
    
    # Critical summation
    total_response = plastic_contrib + elastic_contrib + static_contrib + cumulative_shift
    
    # Non-linear scaling using modular arithmetic
    modulation_factor = (total_response % 17) + 3
    final_yield = (total_response * modulation_factor) // 5
    
    # Debugging decoy (never printed or used)
    debug_snapshot = {
        'raw': stress_sequence,
        'shift': cumulative_shift,
        'phases': dict(history)
    }
    
    return final_yield

# Unused global variables (distractors)
MAX_ITERATIONS = 1000
CONVERGENCE_TOLERANCE = 1e-6
SYSTEM_MODE = 'DIAGNOSTIC'

# Input data setup
stress_input = [88, 105, 160, 45, 195, 110, 73, 200]
threshold_config = {
    't1': 8, 't2': 12, 't3': 4, 't4': 15
}

# Execute main logic
final_yield = calculate_strain_response(stress_input, threshold_config)

# Print result as required
print(f"Result: {final_yield}")