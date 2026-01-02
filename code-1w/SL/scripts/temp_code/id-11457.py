import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return x ** 3 + 2 * x - 1

# Misleading transformation chain
def transform_value(v):
    if v < 0:
        return abs(v) * 2
    elif v == 0:
        return 100
    else:
        return int(math.sqrt(v)) if v > 10 else v + 10

# Distractor: complex but unused data structure
class DataBuffer:
    def __init__(self):
        self.buffer = [0] * 100
        self.pointer = 0

    def reset(self):
        self.pointer = 0

# Another red herring function
def calculate_checksum(arr):
    chk = 0
    for i in range(len(arr)):
        chk ^= arr[i] * (i + 1)
    return chk % 256

# Real processing begins here — heavily masked by noise
def decode_sequence(seq):
    temp = 0
    for item in seq:
        if item % 2 == 0:
            temp += item // 2
        else:
            temp -= item // 3
    return temp

# Core logic buried in abstraction
def apply_filter(data):
    filtered = []
    for d in data:
        # Conditional expression used as required
        adjusted = d * 2 if d < 50 else d - 10
        if adjusted % 7 == 0:
            filtered.append(adjusted)
    return filtered

# Higher-level wrapper with decoy operations
def build_hierarchy(elements):
    tree = {}
    for idx, val in enumerate(elements):
        tree[idx] = {'value': val, 'flag': (val % 4 == 0)}
    # This part is never used downstream
    for k in tree:
        if tree[k]['flag']:
            tree[k]['bonus'] = tree[k]['value'] * 0.5
    return tree  # distractor return

# Actual critical pipeline
def process_pipeline(raw_data):
    step1 = decode_sequence(raw_data)  # -15
    step2 = apply_filter([abs(step1) + 5])  # [20] -> filtered if divisible by 7?
    
    # Simulated intermediate check (misleading)
    status_flag = True if len(step2) > 0 else False
    temp_cache = {'interim': step2[0] if step2 else 0, 'active': status_flag}
    
    # Real computation hidden among distractions
    adjustment = 0
    for i in range(3):
        if i == 1:
            adjustment += temp_cache['interim'] * 3  # 20 * 3 = 60
            break  # early break to obscure flow

    # Final transformation using conditional expression
    base_result = adjustment if adjustment > 0 else -1
    final_correction = base_result + 7
    
    # Key assignment — target variable
    final_output = final_correction
    
    # Irrelevant logging block (distractor)
    log_entry = f"Processed {len(raw_data)} items with output {final_output}"
    debug_mode = False
    if debug_mode:
        print(log_entry)
    
    return final_output

# Main execution with seeded structure
data_chunk = [12, -8, 15, 22, 9]

# Unused variables and side computations (red herrings)
shadow_copy = data_chunk[:]
scaling_factor = 1.75
offset_lookup = {x: x*scaling_factor for x in range(10)}

# Trigger the real computation
final_output = process_pipeline(data_chunk)

# Output must follow exact format
print(f"Result: {final_output}")