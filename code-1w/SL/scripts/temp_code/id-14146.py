from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and redundant fields
def fetch_sensor_array():
    raw = [
        {'id': 'A7', 'val': 144, 'meta': {'q': 0.8}, 'temp': 22, 'flag': True},
        {'id': 'B2', 'val': 256, 'meta': {'q': 0.9}, 'temp': 19, 'flag': False},
        {'id': 'A7', 'val': 169, 'meta': {'q': 0.7}, 'temp': 23, 'flag': True},
        {'id': 'C5', 'val': 121, 'meta': {'q': 0.95}, 'temp': 20, 'flag': True},
        {'id': 'B2', 'val': 225, 'meta': {'q': 0.6}, 'temp': 18, 'flag': False}
    ]
    return raw

# Irrelevant transformation: converts to temperature map (not used in final result)
def build_temp_map(data):
    temp_map = defaultdict(list)
    for entry in data:
        temp_map[entry['temp']].append(entry['val'])
    avg_map = {k: sum(v)/len(v) for k, v in temp_map.items()}
    return {k: round(v, 2) for k, v in avg_map.items()}

# Misleading function that looks important but is unused
def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Core processing function with relevant logic
def extract_signals(data):
    signal_map = defaultdict(list)
    for item in data:
        signal_map[item['id']].append(item['val'])
    
    processed = {}
    for key, values in signal_map.items():
        # Compute mean squared magnitude
        ms_val = sum(x*x for x in values) / len(values)
        root = int(math.sqrt(ms_val))
        processed[key] = root if root % 2 == 1 else root + 1  # force odd
    return processed

# Auxiliary function - actually used
def correct_phase_offset(val_list):
    offset = 0
    for v in val_list:
        if v > 200:
            offset += 1
    return offset * 0.5

# Higher-level aggregator with red herring parameters
def integrate_diagnostics(primary, secondary_map, mode='strict'):
    base = sum(primary.values())
    bonus = 0
    # Dead branch - never executed due to mode
    if mode == 'relaxed':
        bonus = sum(len(v) for v in secondary_map.values())
    elif mode == 'hybrid':
        bonus = max(primary.values()) // 2
    # This path is taken
    else:
        bonus = len([v for v in primary.values() if v > 15]) * 2
    return base + bonus

# Decoy function using bitwise tricks (unused)
def scramble_bits(x):
    x ^= (x << 3) & 0xFF
    x ^= (x >> 4)
    x ^= (x << 2)
    return x & 0xFF

# Real computation chain
processed_data = []
dataset = fetch_sensor_array()

# Step 1: Extract core signals
temp_lookup = build_temp_map(dataset)  # irrelevant assignment
signal_roots = extract_signals(dataset)

# Step 2: Apply dynamic correction
offset_tune = correct_phase_offset(list(signal_roots.values()))
adjusted = {k: v + int(offset_tune) for k, v in signal_roots.items()}

# Step 3: Add dummy entries to create confusion
counterfeit_data = {'X1': 999, 'Y2': 888}  # decoy keys
adjusted.update(counterfeit_data)

# Step 4: Filter out fake ones using heuristic
filtered = {k: v for k, v in adjusted.items() if k in ['A7', 'B2', 'C5']}  # removes decoys

# Step 5: Count occurrences for no reason (distractor)
frequencies = Counter([item['id'] for item in dataset])

# Step 6: Recursive reduction to add complexity
def recursive_reduce(lst):
    if len(lst) <= 1:
        return lst[0] if lst else 0
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    return recursive_reduce([recursive_reduce(left), recursive_reduce(right)])

values_list = sorted(filtered.values())
reduced_core = recursive_reduce(values_list) if values_list else 0

# Step 7: Final integration with multiple inputs (some ignored)
def analyze_readings(data_dict):
    # Re-extract clean values
    clean_vals = [v for k, v in data_dict.items() if k in ['A7','B2','C5']]
    if not clean_vals:
        return -1
    
    # Mean and deviation proxy
    mean_val = sum(clean_vals) / len(clean_vals)
    deviant_count = sum(1 for v in clean_vals if abs(v - mean_val) > 5)
    
    # Conditional expression with actual impact
    adjustment = 5 if deviant_count >= 2 else 3
    
    # Use of defaultdict in non-critical way
    stats = defaultdict(int)
    stats['base'] = int(mean_val)
    stats['adjust'] = adjustment
    
    # Final formula
    result = stats['base'] * 2 + stats['adjust'] * reduced_core
    
    # Critical dead code - looks like it updates but doesn't affect
    if result < 0:
        result = abs(result)
    elif result > 1000:
        result = result // 3  # Not triggered here
    
    return int(result)

# Execute main analysis
final_diagnostic = analyze_readings(processed_data)  # placeholder call setup

# Actual execution flow continues...
final_diagnostic = analyze_readings(filtered)

print(f"Target result: {final_diagnostic}")