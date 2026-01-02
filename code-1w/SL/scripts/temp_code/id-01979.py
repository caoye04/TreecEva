from collections import defaultdict, Counter
from itertools import zip_longest, cycle

def preprocess_signal(raw_samples):
    # Irrelevant preprocessing: applies noise filtering (not used in final result)
    filtered = [x * 0.9 for x in raw_samples if x > -50]
    stats = {'mean': sum(filtered) / len(filtered), 'count': len(filtered)}
    return [int(x + 1.5) for x in filtered]  # Only this transformed part is used

def generate_reference_grid(dim):
    # Distractor function: creates a grid but only one value is extracted
    grid = [[i ** 2 - j * 2 for j in range(dim)] for i in range(dim)]
    diagonal = [grid[i][i] for i in range(dim)]
    return diagonal  # Partially used later as red herring

def compute_entropy(seq):
    # Dead function — looks important but unused
    counts = Counter(seq)
    total = len(seq)
    entropy = -sum((count / total) * (count / total).__log__ for count in counts.values())
    return entropy

def shift_sequence(seq, key_offset):
    # Useful transformation: circular shift based on offset
    offset = key_offset % len(seq)
    return seq[offset:] + seq[:offset]

def build_lookup(keys, values):
    # Creates mapping, some entries are decoys
    lookup = defaultdict(lambda: -1)
    for k, v in zip(keys, values):
        lookup[k] = v * 2 if k % 3 == 0 else v  # Some transformation applied
    return lookup

def evaluate_stability(indices):
    # Complex but mostly irrelevant stability check
    cumulative = 0
    for i, idx in enumerate(indices):
        if i % 2 == 0:
            cumulative += idx ** 1.5
        else:
            cumulative -= idx ** 0.5
    return int(cumulative % 100)

def analyze_pattern(data, config):
    # Core logic: pattern analysis with distractors
    temp_result = 0
    for i, val in enumerate(data):
        if i in config['critical_indices']:
            temp_result += val * config['weight_factor']
        elif val > config['threshold']:
            temp_result += val // 2
    # Injecting misleading dependency on external-looking state
    adjustment = config.get('bonus', 0) - config.get('penalty', 0)
    return temp_result + adjustment

# --- Main Execution with High Interference ---
raw_sensor_data = list(range(10, 40, 3))  # [10, 13, 16, 19, 22, 25, 28, 31, 34, 37]

# Step 1: Preprocess signal (only return value matters)
processed_frames = preprocess_signal(raw_sensor_data)

# Step 2: Generate reference grid (only one element used as red herring)
ref_diagonal = generate_reference_grid(8)
red_herring_value = ref_diagonal[5]  # Used to mislead in threshold_map

# Step 3: Shift sequence using complex cycle
shifted_indices = shift_sequence(processed_frames, key_offset=17)

# Step 4: Build dummy lookup table with irrelevant mappings
key_set = [2, 4, 6, 8, 10]
value_set = [3, 7, 5, 9, 11]
dummy_lookup = build_lookup(key_set, value_set)  # Never used

# Step 5: Evaluate stability (result appears important but is not directly used)
stability_score = evaluate_stability(shifted_indices)  # Printed but not affecting answer

# Step 6: Create transformed data with zip and cycle
extended_weights = list(zip_longest(shifted_indices, cycle([2, -1]), fillvalue=0))
transformed_data = [a + b for a, b in extended_weights]  # Actual input to analyzer

# Step 7: Construct threshold map with decoy keys and misleading values
threshold_map = {
    'critical_indices': {1, 4, 7},
    'threshold': 20,
    'weight_factor': 3,
    'bonus': red_herring_value,  # Looks important but overcompensated
    'penalty': ref_diagonal[2],  # Offset bonus; net zero effect
    'debug_mode': False,
    'version': '2.1-alpha'
}

# Step 8: Analyze pattern — this is the critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")