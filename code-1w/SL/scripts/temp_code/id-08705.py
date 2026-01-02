from collections import defaultdict, Counter
import itertools

# Simulated sensor data collection with noise and redundancy
def acquire_signal():
    raw_samples = [i * 0.7 + (i % 3) for i in range(15)]
    filtered = [x for x in raw_samples if x > 4.0]
    return filtered[:10]

# Irrelevant auxiliary function – dead code path (distractor)
def analyze_spectral_peak(signal):
    peak = max(signal, default=0)
    index = signal.index(peak) if peak else -1
    return {'peak': peak, 'position': index}

# Decoy transformation – never called but looks important
def apply_fourier_shift(data, shift=2):
    shifted = [data[(i + shift) % len(data)] for i in range(len(data))]
    normalized = [x / sum(shifted) for x in shifted]
    return normalized

# Core processing pipeline
noise_floor = [0.1 * i for i in range(8)]  # Distractor variable
baseline_offset = sum(noise_floor) * 0.2  # Misleading intermediate calculation

def preprocess_readings(readings):
    offset_corrected = [r - baseline_offset for r in readings]
    threshold_mask = [val for val in offset_corrected if abs(val) > 1.0]  # Filter small values
    return [round(x, 3) for x in threshold_mask]

# Data fusion from multiple channels (relevant)
def merge_channels(primary, secondary):
    padded_secondary = (secondary * 3)[:len(primary)]
    combined = [a + b for a, b in zip(primary, padded_secondary)]
    return combined

# Red herring: Power spectral density estimation (unused)
def compute_psd(signal):
    psd = defaultdict(float)
    for i, val in enumerate(signal):
        psd[i] = val ** 2
    return dict(psd)

# Critical aggregation logic
def accumulate_segments(segments):
    aggregator = defaultdict(int)
    for idx, segment in enumerate(segments):
        for i, val in enumerate(segment):
            key = (idx % 3, i % 4)
            aggregator[key] += int(val)
    return aggregator

# Calibration logic with decoy parameters
def calibrate_system(mode='advanced', debug_override=None):
    if debug_override:
        return debug_override
    if mode == 'basic':
        return 0.95
    elif mode == 'advanced':
        return 1.07
    else:
        return 1.0

calibration_factor = calibrate_system('advanced')  # Used later

# Simulate multi-pass data collection
pass_one = acquire_signal()
pass_two = [x * 0.8 for x in pass_one]

processed_a = preprocess_readings(pass_one)
processed_b = preprocess_readings(pass_two)

merged_data = merge_channels(processed_a, processed_b)

# Generate synthetic segments (relevant for accumulation)
segment_pool = []
for i in range(3):
    shifted = [merged_data[j] * (j + i + 1) % (i + 2) for j in range(len(merged_data))]
    segment_pool.append(shifted)

collected_data = accumulate_segments(segment_pool)

# Secondary distractor: frequency pattern analysis
frequencies = list(itertools.combinations([1, 2, 3, 4], 2))
harmonic_map = {f: sum(f) * 0.5 for f in frequencies}  # Unused structure

# Another irrelevant counter usage
event_log = ['init', 'read', 'read', 'fuse', 'calibrate']
event_counter = Counter(event_log)  # Looks important, not used

# Final computation – KEY STATEMENT
# What is the value of 'thermal_capacity' after this line?
def finalize_measurement(data_dict, factor):
    total = 0
    for k, v in data_dict.items():  # Iterate over accumulated keys
        if k[0] % 2 == 0:  # Only even first indices
            total += v * factor
    return int(total + 0.5)

thermal_capacity = finalize_measurement(collected_data, calibration_factor)

# Output result as required
print(f"Result: {thermal_capacity}")