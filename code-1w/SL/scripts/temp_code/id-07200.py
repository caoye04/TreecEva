import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return (x ** 2 + 3 * x + 1) % 100

# Distractor variables
temp_cache = [0] * 10
backup_flag = False
junk_sum = 0
for i in range(10):
    junk_sum += (i * i) % 7

# Real data initialization
data_stream = [5, -3, 12, 8, 0, 15, 7]

# Misleading pre-processing (partially unused)
processed = []
for val in data_stream:
    if val > 10:
        processed.append(val ^ 5)
    elif val < 0:
        processed.append(abs(val) << 1)
    else:
        processed.append(val)

# Decoy transformation chain
decoy = [x + 2 for x in processed if x % 2 == 0]
decoy_avg = sum(decoy) / len(decoy) if decoy else 0

# Actual pipeline functions
def transform_chunk(chunk, key_offset):
    # Bit manipulation and arithmetic mix
    shifted = [(x << 1) ^ key_offset for x in chunk]
    return [s % 17 for s in shifted]

def evaluate_stability(seq):
    # Boolean logic and comparisons
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1)) or len(seq) < 2

def aggregate_metrics(values):
    # Conditional expression and slicing
    mid = len(values) // 2
    left_half = values[:mid]
    right_half = values[mid:]
    
    left_score = sum(left_half) * 0.9 if left_half else 0
    right_score = sum(x * 1.1 for x in right_half) if right_half else 0
    
    return math.floor(left_score + right_score)

# Dictionary-based state tracking (red herring with partial use)
state_registry = {
    'active': True,
    'mode': 'legacy',
    'version': 2,
    'buffer': [transform_chunk(data_stream[:3], 3)]
}

if state_registry['mode'] == 'debug':
    state_registry['buffer'].append([0,0])

# Core processing pipeline
def process_pipeline(stream):
    # Step 1: Apply bit transformation
    transformed = transform_chunk(stream, 7)
    
    # Step 2: Sort and check stability
    sorted_vals = sorted(transformed)
    stable = evaluate_stability(transformed)
    
    # Step 3: Slice based on condition
    use_vals = sorted_vals if stable else transformed
    
    # Step 4: Aggregate final metric
    score = aggregate_metrics(use_vals)
    
    # Step 5: Final adjustment using dictionary default
    flags = {'adjust': True, 'factor': 1.05}
    adjusted = score * flags.get('factor') if flags.get('adjust') else score
    
    # Step 6: Integer conversion
    return int(adjusted)

# Execution point of interest
final_output = process_pipeline(data_stream)

# Output result
print(f"Target result: {final_output}")