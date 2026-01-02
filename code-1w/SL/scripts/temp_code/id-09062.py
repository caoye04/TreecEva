import math

# Irrelevant helper function (decoy)
def useless_transform(x):
    return (x ** 2 + 3 * x + 1) % 17

# Distractor: unused complex structure
class DataBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0] * size
    def reset(self):
        self.buffer = [0] * self.size

# Misleading intermediate computation with red herring variables
temp_offset = 5
base_shift = 3
lookup_table = {i: (i * i + 2 * i + 1) for i in range(15)}

# Real logic starts here — deeply nested and mixed with noise
def decode_sequence(seq):
    accumulator = 0
    for val in seq:
        if val <= 0:
            continue
        # Bit manipulation mixed with modular arithmetic
        transformed = (val ^ temp_offset) & 0xFF
        if transformed % 2 == 0:
            accumulator += int(math.log(transformed + 1, 2))
        else:
            accumulator -= (transformed % 7)
    return accumulator

# Higher-level wrapper with lambda and string operations as distraction
def build_processor(mode):
    modes = {'fast': lambda x: x > 5, 'slow': lambda x: x <= 5}
    suffix_map = {1: 'A', 2: 'B', 3: 'C'}
    
    # Unused string processing path (dead code)
    def format_result(code):
        tag = ''.join([char.upper() for char in code if char.isalpha()])
        return f"RESULT-{tag}"
    
    return modes.get(mode, modes['fast'])

# Core data transformation pipeline
filter_func = build_processor('fast')

def apply_corrections(arr, threshold=4):
    corrected = []
    index = 0
    while index < len(arr):
        item = arr[index]
        if filter_func(item):
            # Early break in loop as optimization (real use)
            if item == 99:
                break
            shifted = item - base_shift
            corrected.append(shifted)
        else:
            # Dead branch with misleading operation
            dummy = lookup_table.get(item, 0) * 2  # never used
        index += 1
    return corrected

# Complex multi-stage pipeline with distractors
def process_pipeline(raw_data):
    # Step 1: Apply correction with conditional break
    stage_one = apply_corrections(raw_data)
    
    # Step 2: Decode using bitwise and logarithmic logic
    stage_two = decode_sequence(stage_one)
    
    # Step 3: Spurious dictionary usage (only one key matters)
    stats = {
        'count': len(stage_one),
        'sum': sum(stage_one),
        'magic': 42,
        'ignored_value': useless_transform(len(raw_data))
    }
    
    # Actual dependency: combine stage two with a derived constant
    modifier = stats['magic'] // 2  # 21
    
    # Final computation — depends only on stage_two and modifier
    result = stage_two * modifier
    
    # Critical assignment point
    final_output = result + 3  # This is the answer
    
    # Red herring: unused variable with complex derivation
    audit_token = f"SEC-{str(modifier * 1000)[::-1]}".replace('0', 'X')
    
    return final_output

# Input data crafted to trigger specific execution path
data_chunk = [6, 8, -1, 10, 99, 12, 4, 2]

# Execution point of interest
final_output = process_pipeline(data_chunk)
print(f"Target result: {final_output}")