import math

def generate_harmonic_sequence(base_freq, duration, sample_rate=1000):
    # Irrelevant helper function - not used in final computation
    return [math.sin(2 * math.pi * base_freq * t / sample_rate) for t in range(int(duration * sample_rate))]

def normalize_weights(weight_list):
    total = sum(abs(w) for w in weight_list)
    return [w / total for w in weight_list] if total != 0 else weight_list

def calculate_interference(phases, magnitudes):
    # Core logic: compute net phase shift using weighted vector summation
    weighted_sum_real = 0.0
    weighted_sum_imag = 0.0
    
    temp_debug = []  # Unused tracking variable (distractor)
    
    for i in range(len(phases)):
        angle = phases[i]
        mag = magnitudes[i]
        
        # Dead code path - never executed due to data range (distractor)
        if mag < -999:
            print("Invalid magnitude encountered")
            continue
        
        contribution_real = mag * math.cos(angle)
        contribution_imag = mag * math.sin(angle)
        weighted_sum_real += contribution_real
        weighted_sum_imag += contribution_imag
    
    # Compute resultant phase from combined vectors
    if weighted_sum_real == 0 and weighted_sum_imag == 0:
        return 0.0
    
    raw_phase = math.atan2(weighted_sum_imag, weighted_sum_real)
    
    # Normalize phase to [0, 2π)
    normalized_phase = raw_phase % (2 * math.pi)
    
    # Simulate signal reflection (irrelevant transformation)
    reflected = math.pi - normalized_phase
    absorbed = normalized_phase * 0.95  # Distractor calculation
    
    # Final result based on constructive interference
    constructive = abs(normalized_phase) if normalized_phase >= 0 else 0
    return round(constructive, 4)

# Main execution block
if __name__ == "__main__":
    # Experimental wave parameters (radars)
    phases = [math.pi/6, math.pi/3, math.pi/2, 2*math.pi/3]
    weights = [3, 4, 5, 6]
    
    # Preprocessing step with slicing
    cropped_weights = weights[1:-1]  # Middle elements only
    cropped_phases = phases[:3]     # First three
    
    # Normalization of relevant subset (semi-relevant)
    normalized_weights = normalize_weights(cropped_weights)
    scaling_factor = sum(weights) / len(weights) if weights else 1  # Red herring
    
    # Conditional expression determining active mode
    mode = 'full' if len(phases) >= 4 else 'reduced'
    active_phases = phases if mode == 'full' else cropped_phases
    active_weights = weights if mode == 'full' else normalized_weights
    
    # Key computational step
    net_phase_shift = calculate_interference(active_phases, active_weights)
    
    # Additional unused diagnostics (distraction)
    avg_phase = sum(active_phases) / len(active_phases) if active_phases else 0
    max_weight = max(active_weights) if active_weights else 0
    
    # Output target result
    print(f"Result: {net_phase_shift}")