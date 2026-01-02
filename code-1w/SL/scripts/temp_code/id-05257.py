import itertools

# Simulated sensor data with noise and redundant fields
data_stream = [
    {'id': 1, 'val': 3.5, 'meta': 'A', 'err': 0.1},
    {'id': 2, 'val': -2.0, 'meta': 'B', 'err': 0.3},
    {'id': 3, 'val': 7.2, 'meta': 'A', 'err': 0.05},
    {'id': 4, 'val': 0.0, 'meta': 'C', 'err': 0.2},
    {'id': 5, 'val': -5.8, 'meta': 'A', 'err': 0.15}
]

# Irrelevant helper that looks important but is unused
def legacy_transform(x):
    return [i ** 2 for i in x if i > 0]

# Distractor: complex-looking normalization with no real impact
class Normalizer:
    def __init__(self, factor=1.0):
        self.factor = factor

    def apply(self, x):
        return x * self.factor

# Another decoy function that computes something irrelevant
def compute_entropy(values):
    from math import log
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * log(p) for p in probs)

# Misleading intermediate calculation with side-effect-like structure but no real use
temp_aggregates = []
for entry in data_stream:
    temp_aggregates.append(entry['val'] ** 2 + entry['err'])

# Dead code path: never invoked
disabled_filter = lambda x: x['meta'] in ['X', 'Y']

# Real processing begins here — buried under distractions
def extract_valid_vals(stream):
    # Extract only entries with meta == 'A' and positive val
    filtered = [s['val'] for s in stream if s['meta'] == 'A' and s['val'] > 0]
    return filtered

# Bit manipulation red herring
def obscure_shift(value):
    shifted = value << 3
    masked = shifted & 0xFF
    return masked ^ 0x5A  # Looks cryptic but unused

# Core transformation pipeline using itertools and lambda
# Uses relevant concepts: filtering, accumulation, min/max, arithmetic

# Auxiliary useless generator that mimics real work
def generate_parity_pairs(n):
    return list(itertools.takewhile(lambda x: x[0] < n, 
                                  enumerate(itertools.cycle([1, 0]))))

# Actual critical function
def process_pipeline(stream):
    # Step 1: extract valid values
    valid_vals = extract_valid_vals(stream)
    
    # Step 2: compute rolling average using itertools pairwise (manual zip)
    paired = [(valid_vals[i], valid_vals[i+1]) for i in range(len(valid_vals)-1)]
    rolling_avg = [sum(pair)/2 for pair in paired]
    
    # Step 3: apply artificial gain (looks like calibration)
    calibrated = list(map(lambda x: x * 1.5, rolling_avg))
    
    # Step 4: accumulate total deviation from mean
    if not calibrated:
        return 0.0
    mean_val = sum(calibrated) / len(calibrated)
    deviations = [abs(x - mean_val) for x in calibrated]
    total_deviation = sum(deviations)
    
    # Step 5: combine with count via tuple unpacking distraction
    count = len(valid_vals)
    _, final_component = (count * 2, total_deviation * count)
    
    # Step 6: inject a modular arithmetic step (relevant)
    mod_factor = (len(stream) % 4) or 1
    adjusted_result = final_component / mod_factor
    
    # Step 7: use itertools.chain to flatten a nested structure (unnecessary but plausible)
    chained_inputs = list(itertools.chain([adjusted_result], [0]*2))
    
    # Step 8: final output derived from chained input
    final_output = sum(x * (i+1) for i, x in enumerate(chained_inputs))
    
    return final_output

# Execution point of interest
final_output = process_pipeline(data_stream)
print(f"Target result: {final_output}")