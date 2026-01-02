from collections import defaultdict, Counter
import itertools

# Simulated sensor network data processing with diagnostic analysis

def collect_readings():
    # Real data collection
    raw_streams = [
        [14, 17, 14, 23, 15, 14, 14, 19],
        [25, 22, 21, 22, 20, 22, 24],
        [8, 11, 9, 8, 12, 8, 8, 11, 9]
    ]
    
    # Irrelevant aggregation (distractor)
    stats_summary = {}
    for i, stream in enumerate(raw_streams):
        stats_summary[f'stream_{i}'] = {
            'min': min(stream),
            'max': max(stream),
            'range': max(stream) - min(stream)
        }
    
    # Misleading normalization attempt (dead path)
    normalized = []
    for stream in raw_streams:
        mean_val = sum(stream) / len(stream)
        norm_stream = [(x - mean_val) / mean_val for x in stream]
        normalized.append(norm_stream)
    
    # Actual relevant transformation
    flattened = list(itertools.chain.from_iterable(raw_streams))
    return flattened

# Decoy function - looks important but unused
def analyze_pattern(sequence):
    freq_pairs = {}
    for i in range(len(sequence) - 1):
        pair = (sequence[i], sequence[i+1])
        freq_pairs[pair] = freq_pairs.get(pair, 0) + 1
    return freq_pairs

# Another red herring: complex bit analysis
def compute_entropy_signature(data):
    total_bits = 0
    for val in data:
        if val > 0:
            bin_rep = bin(val)[2:]
            total_bits += sum(1 for b in bin_rep if b == '1')
    return total_bits % 17

# Core processing pipeline
readings = collect_readings()

# Irrelevant character counting on stringified numbers (distractor)
counted_chars = defaultdict(int)
for num in readings:
    str_num = str(num)
    for char in str_num:
        counted_chars[char] += 1

# Actual filtering logic
noise_floor = 10
filtered_data = [x for x in readings if x > noise_floor]

# Complex threshold map setup (some entries are decoys)
threshold_map = defaultdict(lambda: 100)
threshold_map.update({
    'critical': 20,
    'warning': 15,
    'info': 5,
    'legacy_mode': 30  # unused parameter
})

# Secondary filter based on frequency (real logic)
freq_count = Counter(filtered_data)
high_freq_values = {k for k, v in freq_count.items() if v >= 2}

# Redundant data structure transformation
matrix_grid = [[val for val in filtered_data if val % 2 == 0],
               [val for val in filtered_data if val % 2 == 1]]

# Fake machine learning prep (misleading)
dataset_tensor = []
for row in matrix_grid:
    padded = row + [0] * (5 - len(row))
    dataset_tensor.append(padded)

# Main processing function
def process_readings(data, thresholds):
    base_limit = thresholds['critical']
    secondary_limit = thresholds['warning']
    
    # Real computation begins
    above_critical = [x for x in data if x >= base_limit]
    within_warning = [x for x in data if secondary_limit <= x < base_limit]
    
    # Complex weighted score
    critical_score = sum(x * 3 for x in above_critical)
    warning_score = sum(x * 2 for x in within_warning)
    normal_score = sum(x for x in data if x in high_freq_values and x < secondary_limit)
    
    # Combine using modular arithmetic
    aggregate = (critical_score + warning_score + normal_score) % 97
    
    # Final adjustment using bit manipulation
    bit_modified = aggregate ^ 0b1101  # XOR with 13
    
    # This is the actual answer variable
    final_diagnostic = bit_modified + 500
    
    # Dead code path (never executed)
    if False:
        backup_system = compute_entropy_signature(data)
        final_diagnostic = backup_system * 10
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_readings(filtered_data, threshold_map)
print(f"Result: {final_diagnostic}")