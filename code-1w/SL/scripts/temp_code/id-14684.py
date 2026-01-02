import math

# Irrelevant physics constants (distractors)
gravitational_constant = 6.67430e-11
planck_constant = 6.62607015e-34
boltzmann_constant = 1.380649e-23
avogadro_number = 6.02214076e23
elementary_charge = 1.602176634e-19

# Misleading energy calculations (dead code path)
def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def calculate_potential_energy(mass, height):
    return mass * 9.81 * height

# Unused recursive red herring
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Character frequency counter (seemingly relevant but mostly distraction)
def count_characters(text):
    return {char: text.count(char) for char in set(text)}

# Real computational chain begins here — deeply nested logic
initial_entropy = 150
scaling_factor = 2.5
adjustment_threshold = 37.2

state_vector = [12, 8, 19, 44, 3, 7]
state_log = []

for idx in range(len(state_vector)):
    val = state_vector[idx]
    transformed = (val ** 1.5) / scaling_factor
    
    # Conditional expression with side-effect logging
    status_flag = 'high' if transformed > adjustment_threshold else 'low'
    state_log.append({
        'index': idx,
        'raw': val,
        'transformed': round(transformed, 4),
        'flag': status_flag,
        'checksum': (idx + val) % 4 == 0
    })

# Decoy accumulation (looks important but unused later)
total_accumulator = sum(entry['raw'] for entry in state_log)
weighted_sum = sum(entry['transformed'] for entry in state_log if entry['flag'] == 'high')

# Lambda-based filter predicate (key concept)
valid_entry = lambda x: x['checksum'] and x['raw'] % 2 == 1

# Actual critical data extraction
filtered_indices = [
    entry['index'] for entry in state_log 
    if valid_entry(entry)
]

# Bit manipulation red herring
bitmask_result = 0
for i in filtered_indices:
    bitmask_result ^= (i << 2) | (i >> 1)

# Core thermodynamic simulation (uses only filtered indices)
entropy_offset = initial_entropy
for i in filtered_indices:
    entropy_offset += math.log(i + 5) * scaling_factor

# Secondary adjustment using character analysis of labels (distractor integration)
flag_string = ''.join(entry['flag'][0] for entry in state_log)
char_freq = count_characters(flag_string)
h_correction = char_freq.get('h', 0) * 10.5  # 'h' from 'high'

# Final processing function with conditional expression
def process_state_variables(log):
    base_potential = entropy_offset + h_correction
    
    # Complex conditional expression involving multiple concepts
    adjustment = (
        sum(1 for x in log if x['flag'] == 'low') * 3.2 
        if len(filtered_indices) > 1 
        else scaling_factor * 2.1
    )
    
    # Tertiary interference: unused nested structure
    summary_tree = {
        'level_1': {
            'entries': len(log),
            'details': {
                'sub_level': {
                    'max_raw': max(x['raw'] for x in log),
                    'computed_x': [fibonacci(x['index']) for x in log[:3]]  # Dead recursion
                }
            }
        }
    }
    
    # The real answer computation — subtle and buried
    raw_sum = sum(entry['raw'] for entry in log if entry['index'] in filtered_indices)
    return base_potential - adjustment + raw_sum

# Execution point of interest
final_output = process_state_variables(state_log)

# Key variable assignment
thermodynamic_potential = int(round(final_output))

# Print required output
print(f"Result: {thermodynamic_potential}")