import itertools

# System configuration constants (mostly irrelevant)
MAX_BUFFER_SIZE = 1024
DEBUG_MODE = False
DEFAULT_TIMEOUT = 30
RETRY_LIMIT = 3

# Irrelevant utility function (dead code path)
def validate_checksum(data):
    return sum(data) % 256 if data else 0

def generate_lookup_table():
    # This function is called but its result is only partially used
    table = {i: (i ** 2 + 3 * i + 7) % 101 for i in range(50)}
    return table

def analyze_pattern(sequence):
    # Complex logic with red herring intermediate values
    a = sum(1 for x in sequence if x % 3 == 0)
    b = sum(1 for x in sequence if x % 5 == 0)
    c = sum(1 for x in sequence if x % 15 == 0)  # Overlap
    score_harmonic = (a + b - c) * 1.5  # Misleading 'score'
    return a > 5 and b > 3

def apply_transformation(x, mode):
    if mode == 'A':
        return ((x ^ 217) + 13) & 255
    elif mode == 'B':
        return (x * 17) % 199
    else:
        return x

def process_transformations(pipeline_config, flags):
    # Core logic buried in distractions
    lookup = generate_lookup_table()
    base_sequence = [i * 4 + 2 for i in range(15) if i % 2 == 0]
    
    # Irrelevant filtering based on false condition
    if flags.get('enable_legacy', False):
        base_sequence = [x for x in base_sequence if x < 50]

    # Key transformation chain starts here
    temp_result = []
    for val in base_sequence:
        transformed = val
        if val in lookup:
            transformed = apply_transformation(transformed, 'A')
        if transformed > 100:
            transformed = apply_transformation(transformed, 'B')
        temp_result.append(transformed)
    
    # Decoy aggregation (never used)
    fake_aggregate = sum(temp_result[i] * (i+1) for i in range(len(temp_result))) % 1000
    
    # Real logic: find first triplet satisfying pattern condition
    valid_triplets = []
    for triplet in itertools.combinations(temp_result, 3):
        if triplet[0] < triplet[1] < triplet[2]:
            if analyze_pattern([triplet[0], triplet[1], triplet[2]]):
                valid_triplets.append(triplet)
    
    # Only one triplet will match due to constraints
    if valid_triplets:
        selected = valid_triplets[0]
        # Actual answer derivation
        raw_value = (selected[0] * selected[1] + selected[2])
        final_output = int((raw_value * 0.73) + 49)  # Final deterministic mapping
    else:
        final_output = -1  # Dead branch (not taken)
        
    return final_output

# Control flow setup
control_flags = {
    'enable_legacy': False,
    'debug_trace': True,
    'strict_mode': 'off',
    'timeout_override': None
}

# Data pipeline definition (only length matters, content misleading)
data_pipeline = [
    {'type': 'transform', 'mode': 'A', 'params': [1,2,3]},
    {'type': 'filter', 'mode': 'B', 'params': [4,5]},
    {'type': 'transform', 'mode': 'A', 'params': [6]}
]

# Execution point of interest
final_output = process_transformations(data_pipeline, control_flags)

# Output the target variable
print(f"Target result: {final_output}")