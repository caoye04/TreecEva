from collections import defaultdict
import math

def analyze_harmonic_sequence(signal_samples):
    sample_stats = defaultdict(int)
    total_power = 0.0
    peak_magnitude = 0
    
    for s in signal_samples:
        if abs(s) > 50:  # anomaly threshold
            sample_stats['outlier_count'] += 1
        sample_stats['valid_count'] += 1
        power = s * s
        total_power += power
        if power > peak_magnitude:
            peak_magnitude = power
    
    rms_value = math.sqrt(total_power / len(signal_samples)) if signal_samples else 0
    sample_stats['rms'] = round(rms_value, 4)
    return sample_stats

def build_frequency_map(harmonics):
    freq_lookup = {}
    temp_cache = {}
    cumulative_offset = 0
    
    for base, count in harmonics.items():
        shifted_freq = base * 1.5 + 2  # synthetic shift
        freq_lookup[base] = int(shifted_freq)
        cumulative_offset += shifted_freq % 7
        
        # Dead computation - irrelevant accumulation
        temp_cache[base] = [i * base for i in range(3) if i % 2 == 0]
    
    # Unused derived value
    final_checksum = int((cumulative_offset * 100) % 100)
    return freq_lookup

def calculate_interference_phase(signal_chunk, freq_mapping):
    phase_accumulator = 0.0
    harmonic_weights = []
    
    # Real processing path
    for i, val in enumerate(signal_chunk):
        mapped_freq = freq_mapping.get(i+1, 1)
        angle = val * mapped_freq * math.pi / 180.0
        phase_accumulator += math.sin(angle) if val > 0 else math.cos(angle)
        
        # Distractor: weight tracking not used in final result
        if i % 2 == 0:
            harmonic_weights.append(abs(val) * 0.1)
    
    # Secondary red herring computation
    average_weight = sum(harmonic_weights) / len(harmonic_weights) if harmonic_weights else 0.0
    perturbation_factor = math.floor(average_weight * 10) % 3
    
    # Final adjustment (irrelevant to core logic)
    phase_accumulator -= perturbation_factor * 0.1
    
    return round(phase_accumulator, 4)

# Main execution block
if __name__ == "__main__":
    raw_samples = [12, -45, 67, 23, -15, 89, -34]
    harmonic_multiples = {1: 3, 2: 5, 3: 2, 5: 4}
    
    # Irrelevant preprocessing step
    normalized_samples = [x / max(abs(max(raw_samples)), abs(min(raw_samples))) for x in raw_samples]
    scaled_integers = [int(x * 100) for x in normalized_samples]
    
    # Actual required stats (some used, some not)
    stats_summary = analyze_harmonic_sequence(raw_samples)
    frequency_map = build_frequency_map(harmonic_multiples)
    
    composite_signal = [scaled_integers[i] // 10 for i in range(len(scaled_integers)) if i % 2 == 0]
    composite_signal.append(stats_summary['valid_count'])
    
    # Key statement
    net_phase_shift = calculate_interference_phase(composite_signal, frequency_map)
    
    # Print target result
    print(f"Target result: {net_phase_shift}")