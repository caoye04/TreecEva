import itertools

# Simulate sensor data with noise and metadata
def generate_sensor_data():
    raw_values = [i * 1.5 for i in range(20)]
    timestamps = list(range(20))
    statuses = ['active'] * 12 + ['idle'] * 8
    return list(zip(raw_values, timestamps, statuses))

data_stream = generate_sensor_data()

# Irrelevant utility: computes average of first n even squares (unused later)
def dummy_metric(n):
    return sum(x**2 for x in range(2*n) if x % 2 == 0) / n if n > 0 else 0

# Decoy transformation chain
class DataObfuscator:
    def __init__(self, shift):
        self.shift = shift
    
    def obscure(self, val):
        return val ^ self.shift  # Bitwise red herring

obfuscator = DataObfuscator(shift=7)

# Misleading intermediate: processes only status tags, no impact on result
def analyze_status_pattern(stream):
    active_count = sum(1 for _, _, s in stream if s == 'active')
    idle_transitions = 0
    for i in range(1, len(stream)):
        if stream[i-1][2] == 'active' and stream[i][2] == 'idle':
            idle_transitions += 1
    return {'active_ratio': active_count / len(stream), 'transitions': idle_transitions}

status_analysis = analyze_status_pattern(data_stream)  # Dead-end analysis

# Real processing begins here — hidden among distractions
def extract_valid_readings(stream):
    # Filter only 'active' state readings
    filtered = [val for val, ts, st in stream if st == 'active']
    # Apply fake obfuscation that's immediately undone (distraction)
    obscured = [int(f * 10) ^ 7 for f in filtered]
    deobscured = [float(o ^ 7) / 10 for o in obscured]  # Reversal cancels effect
    return deobscured

# Chain transformations with list comprehension and slicing
filtered_data = extract_valid_readings(data_stream)

# Use of itertools: group by integer part (only for appearance)
grouped = {k: list(g) for k, g in itertools.groupby(filtered_data, key=int)}
dummy_groups = len(grouped)  # Unused metric

# Compute rolling max over window size 3 (red herring computation)
rolling_maxes = [max(filtered_data[i:i+3]) for i in range(len(filtered_data)-2)]
spurious_peak_count = sum(1 for m in rolling_maxes if m > 10)  # Not used

# Actual signal refinement: invert values, take every second one using slicing
inverted_slice = [round(1 / x, 6) for x in filtered_data if x != 0][::2]

# Recursion-based summation (simple but masked by complexity)
def recursive_sum(lst, idx=0):
    if idx >= len(lst):
        return 0.0
    return lst[idx] + recursive_sum(lst, idx + 1)

sum_inverted = recursive_sum(inverted_slice)

# Final combinatorics distraction: count all pairs in original stream
pair_count = sum(1 for _ in itertools.combinations(data_stream, 2))  # Huge irrelevant number

# Core logic: normalize sum by number of valid processed elements
normalization_factor = len([x for x in filtered_data if x > 0])  # Slightly different set

# Critical assignment: this is the real answer path
def process_pipeline(input_data):
    valids = extract_valid_readings(input_data)
    inv_slice = [round(1 / x, 6) for x in valids if x != 0][::2]
    total = recursive_sum(inv_slice)
    divisor = len(valids)
    return round(total / divisor, 6)

final_output = process_pipeline(data_stream)
print(f"Result: {final_output}")