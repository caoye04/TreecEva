import math

# Irrelevant helper function (dead code path)
def legacy_encode(data):
    return sum([ord(c) * (i + 1) for i, c in enumerate(data)])

# Unused utility
unused_threshold = 42.7
temp_log = []

# Configuration with red herring fields
config = {
    'mode': 'strict',
    'debug': False,
    'version': 2.1,
    'padding': True,
    'scale_factor': 3.14159,
    'mask_level': 7
}

# Simulated data input
raw_input = "data_stream_v9"

# Distractor: character frequency analysis (not used in final result)
char_freq = {}
for char in raw_input:
    char_freq[char] = char_freq.get(char, 0) + 1

# Distractor: unused transformation pipeline
transform_chain = [
    lambda x: x.upper(),
    lambda x: x.replace('_', '-'),
    lambda x: x + '_processed'
]

intermediate = raw_input
for transform in transform_chain:
    intermediate = transform(intermediate)

# Segment data – actual relevant input
segment_data = [
    {'id': 1, 'value': 12, 'flag': True},
    {'id': 2, 'value': 15, 'flag': False},
    {'id': 3, 'value': 8, 'flag': True},
    {'id': 4, 'value': 21, 'flag': True}
]

# Decoy accumulator (never used)
debug_accumulator = 0

# Real processing function with nested logic and distractors
def process_segments(segments, cfg):
    base_scale = int(cfg['scale_factor'])
    mask = cfg['mask_level']
    result = 0
    temp_values = []
    
    # Loop with mixed conditions and irrelevant computations
    for seg in segments:
        val = seg['value']
        
        # Real condition
        if seg['flag']:
            # Nested arithmetic: modular arithmetic + exponentiation
            adjusted = (val ** 2) % (mask + 1)
            temp_values.append(adjusted)
            
            # Bit manipulation red herring (computed but not decisive)
            bitwise_tweak = (adjusted ^ mask) & base_scale
            debug_accumulator += bitwise_tweak  # dead reference
            
        else:
            # Dead branch with plausible-looking computation
            dummy = math.log(val + 1, base_scale)
            temp_log.append(dummy)

    # Real aggregation using lambda (required feature)
    aggregator = lambda vals: sum(v * 2 for v in vals)
    partial = aggregator(temp_values)
    
    # Final checksum depends on length and scaled sum
    length_factor = len(temp_values) * 10
    checksum = (partial + length_factor) * (base_scale % 3)
    
    # Distractor: unused alternate calculation
    alt_checksum = sum(temp_values) + (mask * len(segments))
    
    return int(checksum)

# Key execution point
checksum = process_segments(segment_data, config)

# Output the target result
print(f"Result: {checksum}")