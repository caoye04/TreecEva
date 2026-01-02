import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return sum(i ** 2 for i in range(x))

# Misleading transformation chain
def transform_sequence(seq):
    temp_a = [x * 1.5 for x in seq if x % 2 == 0]
    temp_b = [math.log(y + 1) for y in temp_a]
    shifted = [int(z) + 3 for z in temp_b]
    return shifted[::-1]  # slicing - red herring

# Distractor: complex but unused data structure
class DataBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0] * size
        self.index = 0

    def add(self, val):
        self.buffer[self.index] = val % 100
        self.index = (self.index + 1) % self.size

# Another decoy function with bit manipulation distraction
def bitmask_analysis(value):
    bin_str = bin(value)[2:]
    ones = bin_str.count('1')
    zeros = bin_str.count('0')
    return (ones ^ zeros) << 2  # irrelevant bitwise result

# Core logic buried in distractions
data_source = list(range(8, 40, 3))  # [8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38]

# Unused intermediate calculations
agg_1 = sum(x for x in data_source if x > 20)
agg_2 = len([x for x in data_source if x < 15])

# Real pipeline begins here — obscured by noise
config_map = {
    'threshold': 17,
    'offset': 4,
    'scale': 2
}

# Tuple unpacking distraction
task_params = (config_map['threshold'], config_map['offset'])
limit, shift_val = task_params

# Actual meaningful data segmentation
raw_segments = [data_source[i:i+4] for i in range(0, len(data_source), 4)]

def filter_relevant(group):
    return [x for x in group if x > config_map['threshold']]

def compute_metric(chunk):
    if not chunk:
        return 0
    avg = sum(chunk) / len(chunk)
    return int(avg // config_map['scale'])  # integer division and rounding

def finalize(result_list):
    # Dictionary used for final aggregation
    stats = {}
    for i, val in enumerate(result_list):
        stats[f'item_{i}'] = val * (i + 1)
    
    # Key computation hidden in dict values
    values = list(stats.values())
    midpoint = len(values) // 2
    selected = values[midpoint:midpoint+2]  # slicing operation
    return max(selected) - min(selected)

# Main processing pipeline
def process_pipeline(segments):
    filtered_groups = []
    for group in segments:
        clean_group = filter_relevant(group)
        if len(clean_group) % 2 == 0:
            clean_group.append(config_map['offset'])
        filtered_groups.append(clean_group)
    
    results = []
    for idx, grp in enumerate(filtered_groups):
        # Inject artificial variation
        adjusted = [x + (idx * 2) for x in grp]
        metric = compute_metric(adjusted)
        results.append(metric)
    
    # Final integration step
    final_integrated = finalize(results)
    
    # Dead code below (misleading)
    if final_integrated < 10:
        final_integrated *= 3
    else:
        pass  # no-op distraction
        
    return final_integrated

# Execution with decoy calls
dummy_buffer = DataBuffer(5)
for val in [12, 25, 37, 44, 58]:
    dummy_buffer.add(bitmask_analysis(val))

# Critical execution point
final_output = process_pipeline(raw_segments)

# Output result as required
print(f"Result: {final_output}")