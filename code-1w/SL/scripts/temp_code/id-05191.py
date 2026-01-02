from collections import defaultdict
from itertools import cycle

# Simulate sensor signal processing with noise filtering and diagnostic scoring
def analyze_pulse_sequence(raw_readings, threshold=0.75):
    normalized = [x / max(raw_readings) for x in raw_readings]
    spikes = [i for i, v in enumerate(normalized) if v > threshold]
    return spikes

# Auxiliary function to mask irrelevant frequencies
def apply_bandpass(signal, low_cut=0.1, high_cut=0.85):
    filtered = []
    for val in signal:
        if low_cut <= val <= high_cut:
            filtered.append(val * 1.1)
        else:
            filtered.append(0.0)
    return filtered

# Core diagnostic accumulator
def accumulate_diagnostics(chain, masks):
    score_log = defaultdict(int)
    temp_buffer = []
    
    # Misleading pre-scan: analyzes but doesn't contribute to final result
    baseline_shift = sum(chain) / len(chain) if chain else 0
    adjusted_chain = [x - baseline_shift for x in chain]
    
    # Real processing begins: apply filters from masks
    active_segments = []
    for i, mask in enumerate(masks):
        segment = list(zip(adjusted_chain, cycle(mask)))
        activated = [a for a, m in segment if a > 0 and m == 1]
        active_segments.extend(activated)
    
    # Accumulate diagnostic weights using bitwise influence flags
    cumulative_phase = 0
    for idx, sample in enumerate(active_segments):
        weight = int(sample * 100)
        flag = (idx + 1) % 3
        if flag == 0:
            weighted_score = weight & 255  # Apply bit mask
        elif flag == 1:
            weighted_score = weight | 10
        else:
            weighted_score = weight ^ 50
        
        # Only even-indexed contributions are logged (critical condition)
        if idx % 2 == 0:
            score_log['diagnostic_entry'] += weighted_score
        
        temp_buffer.append(weighted_score)  # Unused buffer (distractor)
    
    # Final computation
    base_total = score_log['diagnostic_entry']
    penalty = len(temp_buffer) // 4  # Artificial reduction factor
    final_score = base_total - penalty
    
    return final_score

# Simulated data inputs
sensor_readings = [120, 245, 98, 301, 188, 412, 297, 110, 500, 265, 190, 423]
denoising_kernels = [
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 0]
]

# Signal preprocessing (distraction block - not directly used)
signals_of_interest = analyze_pulse_sequence(sensor_readings, threshold=0.78)
filtered_signal = apply_bandpass(sensor_readings, 0.2, 0.8)

# Critical execution point
final_diagnostic = accumulate_diagnostics(sensor_readings, denoising_kernels)
print(f"Result: {final_diagnostic}")