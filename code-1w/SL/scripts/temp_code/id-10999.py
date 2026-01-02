from collections import defaultdict

# Simulate signal phase processing with noise filtering and correction
phases = [1.2, -0.8, 3.1, 2.5, -1.4, 0.9, -2.2]
config = {'threshold': 1.0, 'gain': 0.75, 'enable_filtering': True}

def apply_gain(signal, g):
    return [s * g for s in signal]

def remove_outliers(signal, thresh):
    filtered = []
    for s in signal:
        if abs(s) <= thresh:
            filtered.append(0.0)
        else:
            filtered.append(s)
    return filtered

def count_transitions(signal):
    transitions = 0
    for i in range(1, len(signal)):
        if (signal[i-1] >= 0) != (signal[i] >= 0):
            transitions += 1
    return transitions

def compute_magnitude_stats(signal):
    # Irrelevant distractor: computes stats not used in final result
    total = sum(abs(s) for s in signal)
    avg_mag = total / len(signal) if signal else 0
    peak = max(abs(s) for s in signal) if signal else 0
    return {'total': total, 'average': avg_mag, 'peak': peak}

def process_phase_sequence(seq, cfg):
    # Step 1: Apply gain adjustment
    adjusted = apply_gain(seq, cfg['gain'])
    
    # Step 2: Filter outliers based on threshold (distractor: modifies data but not final path directly)
    if cfg['enable_filtering']:
        adjusted = remove_outliers(adjusted, cfg['threshold'])
    
    # Step 3: Track zero-crossings for debugging (irrelevant to final answer)
    debug_info = defaultdict(int)
    debug_info['zero_crossings'] = count_transitions(adjusted)
    debug_info['length'] = len(adjusted)
    
    # Distractor variables - used in dead-end computation
    temp_sum = 0
    for val in adjusted:
        temp_sum += val ** 2  # Not used later
    rms_estimate = (temp_sum / len(adjusted)) ** 0.5 if adjusted else 0
    
    # Step 4: Compute net phase shift as signed sum (core logic)
    net_phase_shift = sum(adjusted)
    
    # Step 5: Add dummy offset that gets discarded (misleading)
    if net_phase_shift > 0:
        candidate = net_phase_shift + 5.0
    else:
        candidate = net_phase_shift - 5.0
    
    # Final decision ignores candidate; use raw net_shift
    final_value = net_phase_shift  # Critical assignment
    
    return final_value

# Execute main logic
intermediate_result = process_phase_sequence(phases, config)
baseline_offset = sum(p * 0.1 for p in phases)  # Dead computation
normalization_factor = len(phases) * config['gain']  # Unused scaling hint

# Key statement
final_adjustment = process_phase_sequence(phases, config)

# Output target result
print(f"Result: {final_adjustment}")