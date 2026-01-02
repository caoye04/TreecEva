from collections import defaultdict, Counter

# Irrelevant data structures and preprocessing (distractors)
mock_logs = ['err_001', 'info_042', 'warn_888', 'err_001']
log_counts = Counter(mock_logs)
dummy_map = defaultdict(lambda: 'N/A')
for i in range(10):
    dummy_map[f'key_{i}'] = f'value_{(i * 7) % 13}'

# Simulated sensor input (red herring)
sensor_readings = [0.1, 0.4, 0.8, 1.2, 0.9, 0.3]
adjusted_readings = [round(x ** 2 + 0.1, 2) for x in sensor_readings]
spike_count = sum(1 for r in adjusted_readings if r > 0.5)

# Decoy function with unused recursion
def compute_dampening_factor(n):
    if n <= 1:
        return 1
    return n * 0.95 + compute_dampening_factor(n - 2)

# Unused recursive call (dead path)
decoys = [compute_dampening_factor(i) for i in range(1, 6, 2)]

# Core problem: signal segmentation and noise filtering
raw_signal = [1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0]
noise_floor = 0.5
signal_threshold = 1

# Segment detection logic
segments = []
current_segment = 0
for sample in raw_signal:
    if sample >= signal_threshold:
        current_segment += 1
    else:
        if current_segment > 0:
            segments.append(current_segment)
            current_segment = 0
if current_segment > 0:
    segments.append(current_segment)

# Filter out small segments (assumed noise)
filtered_segments = [s for s in segments if s >= 2]

# Misleading averaging (not used in final result)
avg_segment_length = sum(filtered_segments) / len(filtered_segments) if filtered_segments else 0
temp_weights = [x * 0.7 + 0.3 for x in filtered_segments]

# Data aggregation with defaultdict (core relevant use)
collected_data = defaultdict(int)
for i, length in enumerate(filtered_segments):
    collected_data[f'seg_{i}'] = length * 2  # Amplify for processing

# Threshold map with irrelevant entries
thresholds = {
    'min_valid': 2,
    'max_jitter': 0.15,
    'scale_factor': 3,  # Used in processing
    'debug_mode': False,
    'timeout': 500
}

# Real but obscured processing function
def process_segments(data_dict, config):
    base_score = 0
    scale = config['scale_factor']
    min_req = config['min_valid']
    
    # Accumulate scaled values above threshold
    for key in data_dict:
        if 'seg_' in key:  # filter valid keys
            value = data_dict[key]
            if value >= min_req:
                base_score += value * scale
    
    # Add bonus for number of valid segments (diversion)
    segment_bonus = len([k for k in data_dict.keys()]) * 2
    base_score += segment_bonus  # Actually part of logic
    
    # Decoy bit manipulation (unused)
    decoy_flag = (base_score << 2) ^ 0xFF
    decoy_flag = decoy_flag & 0x7F
    
    # Final adjustment based on odd/even (irrelevant check)
    if base_score % 3 == 0:
        base_score -= 5
    
    return base_score

# Critical execution point
final_tally = process_segments(collected_data, thresholds)

# Print required output
print(f"Target result: {final_tally}")