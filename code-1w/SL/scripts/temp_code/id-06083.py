import itertools

# Simulated sensor data stream with redundant and irrelevant fields
data_stream = [
    {'id': 101, 'temp_raw': 23.5, 'vibration': 0.45, 'status_flag': 1, 'checksum': 'A1'},
    {'id': 102, 'temp_raw': -19.2, 'vibration': 0.38, 'status_flag': 0, 'checksum': 'B2'},
    {'id': 103, 'temp_raw': 31.8, 'vibration': 0.67, 'status_flag': 1, 'checksum': 'C3'},
    {'id': 104, 'temp_raw': 27.1, 'vibration': 0.41, 'status_flag': 1, 'checksum': 'D4'},
    {'id': 105, 'temp_raw': -22.0, 'vibration': 0.72, 'status_flag': 0, 'checksum': 'E5'}
]

# Irrelevant auxiliary mappings (distractor)
status_interpretation = {0: 'inactive', 1: 'active', 2: 'standby'}
flag_weights = {'A1': 0.1, 'B2': 0.2, 'C3': 0.3, 'D4': 0.4, 'E5': 0.5}

# Preprocessing: extract and clean relevant temperature values
temp_filter = lambda x: x['temp_raw'] > 0
valid_entries = list(filter(temp_filter, data_stream))

# Misleading transformation chain (partly irrelevant)
raw_temps = [entry['temp_raw'] for entry in data_stream]
avg_temp = sum(raw_temps) / len(raw_temps)
adjusted_temps = [t * 1.05 if t > 0 else t * 0.95 for t in raw_temps]

# Core signal extraction (relevant)
positive_temps = [entry['temp_raw'] for entry in valid_entries]
squared_offsets = [(t - avg_temp) ** 2 for t in positive_temps]
mean_variance = sum(squared_offsets) / len(squared_offsets) if squared_offsets else 0

# Red herring: complex checksum analysis (dead path)
def analyze_checksum(entries):
    return sum(ord(entry['checksum'][0]) for entry in entries)

# Unused but plausible-looking diagnostic
checksum_score = analyze_checksum(data_stream)

# Real processing begins: transform data using meaningful operations
def transform_entry(entry):
    val = entry['temp_raw']
    # Nonlinear response curve simulation
    if val > 30:
        return val * 0.8 + 5
    elif val > 20:
        return val * 1.1 + 2
    else:
        return val * 1.3

decoy_mapping = {i: round(100 * 1.07**i) for i in range(10)}  # unused growth table

transformed_data = [transform_entry(e) for e in valid_entries]

# Threshold logic with lambda (required feature)
threshold_fn = lambda x: x > 25

# Decoy statistical function (never called)
def compute_entropy(vals):
    from math import log
    total = sum(vals)
    probs = [v / total for v in vals]
    return -sum(p * log(p) for p in probs if p > 0)

# Real metric processor with nested logic and early returns
def process_metrics(metrics, predicate):
    if not metrics:
        return -999
    
    # First stage: filter by dynamic threshold
    passed = list(filter(predicate, metrics))
    if len(passed) < 2:
        return -1
    
    # Second stage: pairwise difference analysis
    pairwise_diffs = []
    for a, b in itertools.combinations(passed, 2):
        pairwise_diffs.append(abs(a - b))
    
    if not pairwise_diffs:
        return 0
    
    # Third stage: weighted aggregation
    max_diff = max(pairwise_diffs)
    diff_avg = sum(pairwise_diffs) / len(pairwise_diffs)
    
    if max_diff > 10:
        return round(diff_avg * 1.5)
    elif max_diff > 5:
        return round(diff_avg * 1.2)
    else:
        return round(diff_avg)

# Critical execution point
final_diagnostic = process_metrics(transformed_data, threshold_fn)

# Output result as required
print(f"Result: {final_diagnostic}")