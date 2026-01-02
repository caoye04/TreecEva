from collections import defaultdict, Counter
import math

# Simulated sensor data with multiple channels
data_stream = [
    (1, 'A', 145), (2, 'B', 170), (3, 'A', 132), (4, 'C', 188),
    (5, 'B', 160), (6, 'A', 138), (7, 'C', 195), (8, 'B', 152),
    (9, 'A', 141), (10, 'C', 177)
]

# Irrelevant statistical placeholder
mean_placeholder = sum(entry[2] for entry in data_stream) / len(data_stream)
median_approx = sorted([entry[2] for entry in data_stream])[len(data_stream)//2]

# Misleading transformation: frequency map (not used in final calculation)
frequency_map = Counter([entry[1] for entry in data_stream])

# Core processing variables
raw_signals = defaultdict(list)
calibration_offset = 12.7

for seq_id, channel, reading in data_stream:
    adjusted_value = reading - calibration_offset
    raw_signals[channel].append(adjusted_value)

# Decoy function that looks important but is unused
def deprecated_analysis(data):
    return sum(x ** 0.5 for x in data if x > 0) / len(data)

# Signal normalization using z-score per channel
normalized_signals = {}
for ch, values in raw_signals.items():
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    std_dev = math.sqrt(variance + 1e-8)
    normalized_signals[ch] = [(v - mean_val) / std_dev for v in values]

# Construct processed_data: take last normalized value from each channel
processed_data = {}
for channel, norms in normalized_signals.items():
    processed_data[channel] = round(norms[-1], 6)

# Threshold configuration (simulated calibration)
thresh_config = {
    'A': {'base': -0.8, 'hysteresis': 0.3},
    'B': {'base': 0.1, 'hysteresis': 0.25},
    'C': {'base': 0.95, 'hysteresis': 0.35}
}

# Create threshold map using complex logic with red herring computation
threshold_map = {}
for k, cfg in thresh_config.items():
    # Red herring: unused dynamic adjustment
    dynamic_factor = abs(math.sin(seq_id * 0.1)) * 0.05
    adjusted_base = cfg['base'] + (0.01 * (ord(k.lower()) % 3))  # Minor perturbation
    effective_threshold = adjusted_base + cfg['hysteresis']
    threshold_map[k] = round(effective_threshold, 6)

# Unused diagnostic heatmap (dead code path)
heatmap_weights = [[0.1, 0.3], [0.4, 0.2]]

# Key analysis function with conditional branching and case conversion distraction
def analyze_signal(signal_dict, thresholds):
    score_accum = 0
    penalty_factor = 1.0
    
    # Case conversion decoy
    mode_flag = 'NORMAL'
    if 'B' in signal_dict and signal_dict['B'] > 0.5:
        mode_flag = mode_flag.lower()
    
    for chan, norm_value in signal_dict.items():
        thresh_val = thresholds.get(chan, 0)
        
        # Conditional branches with integer division and rounding
        if norm_value > thresh_val:
            contribution = int((norm_value - thresh_val) * 100) // 3
            score_accum += max(contribution, 1)
        elif norm_value < -thresh_val:
            # Logical short-circuit decoy
            penalty_factor *= 1.1 if chan != 'X' and chan in ['A','C'] else 1.0
            score_accum -= 2
        else:
            # Bitwise operation red herring (no real impact)
            dummy_mask = 0b1010 ^ 0b1100
            score_accum += dummy_mask & 1
    
    # Final diagnostic includes decimal precision
    final_score = score_accum * penalty_factor
    return round(final_score, 6)

# Critical execution point
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Target result: {variable_value}
print(f"Target result: {final_diagnostic}")