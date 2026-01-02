from collections import defaultdict, Counter

# Simulate sensor data aggregation and diagnostic analysis with red herrings
def collect_sensor_data():
    raw_readings = [73, 45, 73, 92, 45, 11, 92, 73, 64, 11, 45, 64, 73, 92]
    frequency = Counter(raw_readings)
    return [r for r in raw_readings if frequency[r] > 1]

def filter_outliers(data, limit=50):
    # Irrelevant filtering (not actually used in final path)
    return [x for x in data if x >= limit]

def transform_readings(data):
    shifted = [d ^ 15 for d in data]  # Bit manipulation red herring
    scaled = [s * 1.5 for s in shifted]  # Decoy transformation
    return [int(s) for s in scaled]  # Not used

def generate_checksum(values):
    # Dead function: looks important but unused
    chk = 0
    for v in values:
        chk = (chk + v) * 3 % 17
    return chk

def decode_pattern(sequence):
    # Distractor logic with recursion
    if len(sequence) <= 1:
        return sequence
    mid = len(sequence) // 2
    return decode_pattern(sequence[mid:]) + decode_pattern(sequence[:mid])

# Misleading intermediate variables
temp_buffer = [100, 200, 300]
activation_key = sum(temp_buffer) / 100  # Result: 6.0, irrelevant
flag_state = activation_key > 5  # True, distractor

# Core processing chain
raw_data = collect_sensor_data()  # Returns [73, 73, 73, 45, 45, 45, 92, 92, 92]
processed_data = [x * 2 for x in raw_data if x != 11]  # Doubles non-11 values → many duplicates

# Create complex threshold map with unused entries
types = ['A', 'B', 'C']
threshold_map = defaultdict(int)
for i, t in enumerate(types):
    threshold_map[t] = (i + 1) * 25
threshold_map['X'] = 999  # Red herring entry
threshold_map['Y'] = -1   # Another decoy

# Auxiliary function that appears essential but only one branch matters
def validate_entry(value, mode='strict'):
    if mode == 'strict':
        return value > 50
    elif mode == 'lenient':
        return value > 25  # Unused
    else:
        return False  # Unused

# Critical recursive function involved in actual computation
def recursive_reduce(lst):
    if len(lst) == 1:
        return lst[0]
    return recursive_reduce([lst[i] - lst[i+1] for i in range(0, len(lst)-1, 2)])

# Simulated multi-step processing with distraction
working_set = []
for val in processed_data:
    if validate_entry(val):  # Only strict mode used
        working_set.append(val + 5)

# Apply bit shift distraction (result not saved)
shifted_set = [w >> 1 for w in working_set]

# Actual critical transformation
transformed = [v // 3 for v in working_set]  # Integer division

# Use recursion on aggregated counts
count_vals = list(Counter(transformed).values())
reduction_seed = sorted([r * 2 for r in count_vals], reverse=True)

# Final diagnostic depends on recursive reduction of transformed frequencies
final_component = recursive_reduce(reduction_seed)

# Dummy aggregation to obscure logic
diagnostic_log = []
diagnostic_log.append(('base', sum(working_set)))
diagnostic_log.append(('check', final_component))  # Only this matters indirectly

# Key assignment statement
final_diagnostic = final_component * 3  # Final answer derived here

print(f"Result: {final_diagnostic}")