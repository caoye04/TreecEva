def preprocess_items(raw_list):
    # Irrelevant transformation: converts strings to lengths
    return [len(item) for item in raw_list if isinstance(item, str)]


def validate_sequence(seq):
    # Dead function - never called with meaningful data
    return all(x > 0 for x in seq) if seq else False

# Distractor variables
temp_buffer = [x**2 for x in range(15) if x % 3 != 0]
offset_map = {i: (i * 3) % 7 for i in range(10)}
useless_total = sum(offset_map.values()) - 12

# Real data disguised among noise
raw_input_data = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
feature_flags = [True, False, True, True, False]

# Key data structures
primary_indices = [i for i, flag in enumerate(feature_flags) if flag]
masked_data = [len(raw_input_data[i]) for i in primary_indices]

# Weight configuration (some irrelevant entries)
weights = {
    'base': 1.5,
    'bonus': 0.8,
    'penalty': 0.3,
    'decay': 0.95,
    'unused_factor': 2.1  # Never used
}

# Auxiliary function with red herring logic
def compute_adjustment(arr, mode='legacy'):
    if mode == 'legacy':
        return sum(x % 4 for x in arr) * 0.1
    else:
        return max(arr) - min(arr)  # Not triggered

# Decoy calculation chain
shadow_accumulator = 0
for i in range(len(temp_buffer)):
    if temp_buffer[i] > 10:
        shadow_accumulator += temp_buffer[i] // 4

# Core logic buried in noise
def calculate_component_a(values):
    return sum(v * 2 for v in values)

def calculate_component_b(values, w):
    bonus = sum(values) * w['bonus']
    penalty = len([v for v in values if v < 6]) * w['penalty']
    return bonus - penalty

def exponential_decay(value, steps, rate):
    for _ in range(steps):
        value *= rate
    return value

# Main scoring function with distractions
def calculate_final_score(data, config):
    # Step 1: Base component from transformed data
    base_value = calculate_component_a(data)
    
    # Step 2: Add conditional adjustment (uses distractor function but harmless)
    adj = compute_adjustment(data, mode='legacy')
    adjusted_base = base_value + adj
    
    # Step 3: Apply bonus/penalty logic
    b_value = calculate_component_b(data, config)
    intermediate = adjusted_base + b_value
    
    # Step 4: Decay over number of active features (real dependency)
    active_count = len(data)
    decayed = exponential_decay(intermediate, active_count, config['decay'])
    
    # Step 5: Final scaling
    final = int(decayed * config['base'])  # Truncate to integer
    
    # Irrelevant rounding branch (never taken)
    if final < 0:
        final = round(final, 2)
    
    return final

# Spurious control flow block (dead path)
current_state = 'initialized'
if current_state == 'processed':
    masked_data = [x + 100 for x in masked_data]

# Critical execution point
final_score = calculate_final_score(masked_data, weights)

# Output result as required
print(f"Result: {final_score}")