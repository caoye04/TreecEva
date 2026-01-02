from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and irrelevant fields
data_stream = [
    {'id': 1, 'val': 3.5, 'type': 'A', 'err': 0.1, 'meta': 'X'},
    {'id': 2, 'val': 2.1, 'type': 'B', 'err': 0.4, 'meta': 'Y'},
    {'id': 3, 'val': 3.5, 'type': 'A', 'err': 0.2, 'meta': 'X'},
    {'id': 4, 'val': 5.0, 'type': 'C', 'err': 0.0, 'meta': 'Z'},
    {'id': 5, 'val': 2.1, 'type': 'B', 'err': 0.3, 'meta': 'Y'},
    {'id': 6, 'val': 7.2, 'type': 'A', 'err': 0.5, 'meta': 'X'},
]

# Irrelevant statistical cache (distractor)
stats_cache = defaultdict(lambda: {'count': 0, 'sum': 0.0})
for entry in data_stream:
    key = (entry['type'], entry['meta'])
    stats_cache[key]['count'] += 1
    stats_cache[key]['sum'] += entry['val'] + entry['err']

# Noise filter using arbitrary threshold (partially relevant but misleading)
filtered_data = [e for e in data_stream if e['err'] < 0.35]

# Transform data: extract values and apply non-linear scaling (ACTUALLY USED)
transformed_data = []
scaling_factor = 1.7
for item in filtered_data:
    raw_val = item['val']
    adjusted = raw_val * scaling_factor
    if item['type'] == 'A':
        adjusted = math.log(adjusted + 1)  # dampen type A
    elif item['type'] == 'C':
        adjusted = adjusted ** 1.5
    transformed_data.append(adjusted)

# Decoy function - never called (dead code path)
def legacy_process(seq):
    result = 0
    for x in seq:
        result ^= int(x * 10) % 7
    return result

# Another decoy: complex structure not used later
class DataNormalizer:
    def __init__(self, method='z-score'):
        self.method = method
        self.buffers = [[] for _ in range(5)]

    def normalize(self, x):
        return x  # stub

# Configuration with red herring parameters
config = {
    'threshold': 4.2,
    'mode': 'aggressive',
    'debug_trace': True,
    'history_limit': 100,
    'use_enhancement': False,
    'weights': [0.1, 0.3, 0.6]  # unused
}

# Auxiliary function to count transitions (irrelevant to final result)
def count_transitions(stream):
    if not stream:
        return 0
    prev = stream[0]['type']
    count = 0
    for obs in stream[1:]:
        if obs['type'] != prev:
            count += 1
        prev = obs['type']
    return count

transition_count = count_transitions(data_stream)  # distractor variable

# Core analysis logic (depends on transformed_data and config)
def analyze_pattern(signal, cfg):
    if len(signal) == 0:
        return 0.0
    
    # Compute moving average of last two points if available (relevant)
    recent_avg = signal[-1]
    if len(signal) > 1:
        recent_avg = (signal[-2] + signal[-1]) / 2
    
    # Apply activation based on threshold (MISLEADING - not actually decisive)
    activation = 1 if recent_avg > cfg['threshold'] else 0
    
    # Real logic: XOR-based signature from rounded values
    signature = 0
    for val in signal:
        truncated = int(math.floor(val))
        signature ^= (truncated * 3) & 15  # bit manipulation
    
    # Secondary check: symmetry in first and last (red herring)
    symmetric = 0
    if len(signal) > 2:
        mid = len(signal) // 2
        left_sum = sum(signal[:mid])
        right_sum = sum(signal[mid:])
        symmetric = 1 if abs(left_sum - right_sum) < 0.1 else 0
    
    # Final computation: combines signature with scaled length
    # This is where the actual answer comes from
    length_term = len(signal) * 100
    combined_score = signature + length_term
    
    # Dead branch due to config (never taken - distraction)
    if cfg['use_enhancement']:
        enhancement = 0
        for v in signal:
            enhancement += int(v) >> 1
        combined_score += enhancement
    
    return float(combined_score)

# Critical execution point
temp_shadow_copy = transformed_data.copy()  # irrelevant copy
del temp_shadow_copy

final_diagnostic = analyze_pattern(transformed_data, config)
print(f"Target result: {final_diagnostic}")