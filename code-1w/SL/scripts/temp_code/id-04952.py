from collections import defaultdict
import math

def analyze_frequency_profile(signal_sequence):
    freq_map = defaultdict(int)
    total_power = 0
    
    for val in signal_sequence:
        if val > 0:
            freq_map[int(math.log2(val)) % 7] += 1
            total_power += val ** 0.5
    
    return freq_map, total_power

def calculate_harmonic_weight(frequency_bands):
    harmonic_score = 0
    adjustment_factor = 1.5
    
    for band, count in frequency_bands.items():
        if band in [1, 3, 5]:
            harmonic_score += count * adjustment_factor
        else:
            harmonic_score -= count * 0.1  # minor penalty
    
    return max(harmonic_score, 0.5)

def generate_phase_weights(bands, base_amplitude=0.7):
    phase_weights = []
    temp_cache = {}
    
    for k in sorted(bands.keys()):
        raw_weight = math.sin(k * math.pi / 4)
        adjusted_weight = raw_weight * base_amplitude * bands[k]
        phase_weights.append(round(adjusted_weight, 3))
        
        # Distractor: caching unused intermediate values
        temp_cache[f'entry_{k}'] = {
            'raw': raw_weight,
            'scaled': adjusted_weight,
            'flagged': abs(adjusted_weight) > 0.5
        }
    
    # Dead code path (never accessed)
    if False:
        return [w * 1.1 for w in phase_weights]
        
    return phase_weights

def calculate_interference(phases, weights):
    cumulative_shift = 0.0
    interference_log = []
    
    for i in range(len(phases)):
        phase_val = phases[i]
        weight = weights[i % len(weights)]
        
        # Real computation branch
        if i % 2 == 0:
            shift = phase_val * weight
            cumulative_shift += shift
            interference_log.append(shift)
        else:
            # Misleading alternate logic (not actually affecting final result)
            temp_shift = phase_val * (weight + 0.1)
            interference_log.append(temp_shift * 0.01)

    # Final adjustment based on log statistics
    valid_contributions = [x for x in interference_log if abs(x) > 0.05]
    correction = len(valid_contributions) * 0.02
    cumulative_shift += correction
    
    return round(cumulative_shift, 4)

# Main execution block
if __name__ == "__main__":
    # Input signal data
    input_signal = [16, 8, 32, 4, 64, 2, 128]
    
    # Step 1: Analyze frequency distribution and power
    frequency_bands, total_energy = analyze_frequency_profile(input_signal)
    
    # Step 2: Compute harmonic relevance score (used later)
    score = calculate_harmonic_weight(frequency_bands)
    
    # Step 3: Generate phase weights using band counts
    weights = generate_phase_weights(frequency_bands, base_amplitude=0.7)
    
    # Step 4: Prepare phase data from keys and derived values
    phase_keys = list(frequency_bands.keys())
    phase_data = [math.cos(k * math.pi / 6) for k in phase_keys]
    phase_data = [round(p, 3) for p in phase_data]
    
    # Step 5: Introduce distractor variables
    normalization_factor = sum(abs(w) for w in weights) or 1.0
    dummy_scaling = [w / normalization_factor for w in weights]  # Unused
    metadata_summary = {
        'band_count': len(frequency_bands),
        'peak_power': max(input_signal),
        'score_flag': score > 2.0
    }
    
    # Key statement
    net_phase_shift = calculate_interference(phase_data, weights)
    
    # Output target result
    print(f"Result: {net_phase_shift}")