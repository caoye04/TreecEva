import itertools

# Simulated sensor array diagnostics with interference

def collect_readings():
    # Real data source
    base_signals = [12, 15, 18, 21, 24]
    return [x * 2 for x in base_signals if x > 16]

# Irrelevant preprocessing function (dead path)
def preprocess_legacy(signal):
    temp_buffer = []
    for s in signal:
        if s % 3 == 0:
            temp_buffer.append(s // 3)
    return sorted(temp_buffer, reverse=True)

# Unused transformation chain
def transform_signal(x):
    return (x + 5) * 3

def validate_checksum(data):
    # Distractor: looks important but unused
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= (val + i) % 7
    return checksum == 4

# Core logic disguised among red herrings
def generate_sequence(limit):
    seq = []
    a, b = 1, 1
    while a < limit:
        seq.append(a)
        a, b = b, a + b
    return seq

def filter_anomalies(readings, tolerance=2):
    avg = sum(readings) / len(readings)
    return [r for r in readings if abs(r - avg) / avg < tolerance / 10]

def merge_diagnostic(patterns):
    combined = set()
    for p in patterns:
        combined.update(p)
    return sorted(list(combined))

def analyze_pattern(data, config):
    # Key computation hidden in complex logic
    phase_shift = config['phase'] * 2
    amplitude = len(data) * config['gain']
    
    # Bit manipulation distraction
    masked = 0
    for d in data:
        masked |= (d & 0b1100)
    
    # Actual answer derivation
    cycle_sum = 0
    for i in range(len(data)):
        if i % 2 == 0:
            cycle_sum += data[i] * phase_shift
        else:
            cycle_sum -= data[i] // 2
    
    # Red herring: unused complex structure
    diagnostic_map = {}
    for idx, val in enumerate(data):
        diagnostic_map[f'node_{idx}'] = {
            'raw': val,
            'flagged': (val ^ idx) % 5 == 0,
            'checksum': (val * 3) & 0xF
        }
    
    # Critical result computed here
    result = (cycle_sum * amplitude) // 4
    return result

# Irrelevant data generation
def build_lookup_table():
    table = {}
    for i in range(5):
        table[f'key_{i}'] = list(itertools.permutations([1,2,3]))[:i+1]
    return table

# Unused recursive validator
def verify_hierarchy(node_id, depth=0):
    if depth > 3:
        return False
    if node_id.endswith('9'):
        return True
    return verify_hierarchy(f'{int(node_id)+1}', depth+1)

# Main execution with distractions
if __name__ == '__main__':
    # Initialization of real and fake variables
    raw_input = collect_readings()  # [36, 42, 48]
    processed = preprocess_legacy(raw_input)  # Dead path
    
    # Distractor: complex-looking but irrelevant data
    legacy_modes = ['A', 'B', 'C']
    mode_combinations = list(itertools.product(legacy_modes, repeat=2))
    priority_set = set(itertools.chain.from_iterable(mode_combinations))
    
    # Real processing begins
    filtered_data = filter_anomalies(raw_input, tolerance=3)
    fibonacci_template = generate_sequence(50)
    
    # Transformation using set operations (required feature)
    base_indices = set(range(len(filtered_data)))
    offset_mask = {i for i in base_indices if filtered_data[i] % 6 == 0}
    shifted_indices = set(itertools.islice(itertools.cycle([2,4,6]), len(filtered_data)))
    index_overlap = offset_mask.intersection(shifted_indices)
    
    # Data mutation
    transformed_data = []
    for i, val in enumerate(filtered_data):
        if i in index_overlap:
            transformed_data.append(val + 10)
        else:
            transformed_data.append(val)
    
    # Configuration with misleading fields
    thresholds = {
        'gain': 3,
        'phase': 4,
        'timeout': 999,  # unused
        'retries': 3,     # unused
        'debug_mode': False  # unused
    }
    
    # Decoy function call
    _ = build_lookup_table()
    
    # Key statement containing the answer
    final_diagnostic = analyze_pattern(transformed_data, thresholds)
    
    # Print required output
    print(f"Result: {final_diagnostic}")