import math
from collections import defaultdict, Counter

# Simulated sensor readings with noise and metadata
raw_readings = [127, 64, 255, 32, 192, 16, 8, 0, 48, 112]
metadata_map = {'scale': 1.75, 'offset': -0.5, 'threshold': 95}

def apply_calibration(data, config):
    calibrated = []
    temp_cache = defaultdict(float)
    scaling_factor = config['scale']
    shift = config['offset']
    for i, val in enumerate(data):
        adjusted = (val * scaling_factor) + shift
        if adjusted > config['threshold']:
            temp_cache[f'high_{i}'] = adjusted
        elif adjusted < config['threshold'] * 0.5:
            temp_cache[f'low_{i}'] = adjusted
        else:
            temp_cache[f'mid_{i}'] = adjusted
        calibrated.append(round(adjusted))
    # Irrelevant transformation
    decoy_result = [x ** 0.5 for x in data if x > 30]
    return calibrated

# Misleading pre-processing branch (never used)
def legacy_filter(sequence):
    result = []
    for x in sequence:
        if x & 1:
            result.append(x << 2)
    return result

# Signal analysis core
bit_flags = [0b101, 0b110, 0b011, 0b100]
flag_counter = Counter(bit_flags)

processed_data = apply_calibration(raw_readings, metadata_map)

# Dead code path - simulates alternate logic
if len(processed_data) > 20:
    processed_data = [x // 3 for x in processed_data]
elif len(processed_data) == 5:
    processed_data = [x + 10 for x in processed_data]

# Main diagnostic analyzer
def analyze_signal(signal):
    signal_stats = {
        'mean': sum(signal) / len(signal),
        'peaks': [x for x in signal if x > 100],
        'amplitude': max(signal) - min(signal),
        'entropy': 0.0
    }
    
    # Compute entropy via bit dispersion
    total_bits = 0
    for val in signal:
        bin_rep = bin(val)[2:]
        ones = bin_rep.count('1')
        zeros = bin_rep.count('0')
        if ones > 0 and zeros > 0:
            prob_one = ones / (ones + zeros)
            prob_zero = zeros / (ones + zeros)
            if prob_one > 0 and prob_zero > 0:
                signal_stats['entropy'] -= (prob_one * math.log2(prob_one) + prob_zero * math.log2(prob_zero))
    
    # Red herring calculation
    decoy_entropy = sum([math.log2(x+1) for x in range(1, len(signal))])
    
    # Critical decision logic
    quality_score = 0
    if signal_stats['amplitude'] > 150:
        quality_score += 25
    if len(signal_stats['peaks']) >= 3:
        quality_score += 20
    if signal_stats['entropy'] > 1.0:
        quality_score += 15
    
    # Distractor: unused conditional modifying irrelevant flag
    current_flag = 0b101
    if quality_score > 30:
        current_flag ^= 0b111
        current_flag &= ~0b001

    # Final diagnostic computed from multiple reasoning steps
    base_diagnostic = int(signal_stats['mean'])
    entropy_component = int(signal_stats['entropy'] * 10)
    peak_bonus = len(signal_stats['peaks']) * 5
    final_diagnostic = base_diagnostic + entropy_component + peak_bonus - quality_score
    
    # Decoy output that looks important
    debug_dump = {"final_raw": final_diagnostic, "timestamp": 1678886400}
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = analyze_signal(processed_data)
print(f"Result: {final_diagnostic}")