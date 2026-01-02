from collections import defaultdict, Counter
import math

# Simulated network packet processing with decoy transformations
def decode_payload(data):
    # Irrelevant decoding function (dead code path)
    return sum([d ** 2 for d in data if d % 2])

def validate_checksum(frame):
    # Unused validation logic (red herring)
    return sum(frame) % 256 == frame[-1]

def shift_cipher(seq, key):
    # Distractor: bit manipulation not used in final result
    return [(v ^ key) % 256 for v in seq]

# Misleading intermediate variables
total_bandwidth = 128000
packet_sequence_log = []
dropped_packets = []
retransmission_count = 0

# Core simulation parameters (some are decoys)
routing_table = {
    'priority': [3, 7, 11],
    'fallback': [0, 1],
    'threshold': 42,
    'mask': 0b1101
}

transmission_buffer = [
    55, 12, 43, 9, 17, 8, 31, 6, 23, 14, 47, 19, 3, 7, 11, 5
]

# Decoy statistical tracker (not used in main flow)
stats_tracker = defaultdict(int)
for val in transmission_buffer:
    stats_tracker['even'] += 1 if val % 2 == 0 else 0
    stats_tracker['odd'] += 1 if val % 2 == 1 else 0
    stats_tracker['high'] += 1 if val > routing_table['threshold'] else 0

# Auxiliary transformation (never called)
compress_data = lambda x: [a for i, a in enumerate(x) if i % 3 == 0]

# Complex preprocessing with slicing and filtering
filtered_stream = transmission_buffer[1:-1]  # Remove edges
shifted_view = [v >> 1 for v in filtered_stream]  # Right shift all

# Conditional masking using bitwise and relational logic
masked_data = []
for val in shifted_view:
    if val < routing_table['threshold']:
        masked_val = val & routing_table['mask']
        if masked_val > 2:
            masked_data.append(masked_val)
    elif val == routing_table['threshold']:
        masked_data.append(7)

# Secondary filter using list comprehension and slicing
trimmed_set = masked_data[::2]  # Take every other element

# Decoy frequency analysis
freq_analysis = Counter(trimmed_set)
unique_values = len(freq_analysis)

# Dummy recursive function (never invoked)
def calculate_depth(n):
    return 1 if n <= 1 else n + calculate_depth(n - 2)

# Real processing path begins here
aggregated = 0
for x in trimmed_set:
    if x in routing_table['priority']:
        aggregated += x * 2
    else:
        aggregated += int(math.sqrt(x))

# Key conditional expression with short-circuiting
safe_mode = True and (routing_table['threshold'] > 40) or False

# Critical data transformation chain
intermediate_flow = aggregated >> 1
if safe_mode:
    adjustment_factor = 3 if unique_values < 5 else 2
    intermediate_flow *= adjustment_factor

# Final processing step (answer depends only on this)
def process_packet(buffer, config):
    base_value = sum(buffer[::3])  # Slice-based aggregation
    threshold_mask = config['mask']
    bonus = 0
    for v in buffer:
        # Nested condition with bitwise logic
        if (v & threshold_mask) == v and v in config['priority']:
            bonus += v
    return base_value + bonus

# Execution point of interest
optimized_flow = process_packet(transmission_buffer, routing_table)

# Print result as required
print(f"Result: {optimized_flow}")