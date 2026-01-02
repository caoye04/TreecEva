def analyze_pattern(sequence, base_mod):
    accumulator = 0
    for i in range(len(sequence)):
        if i % 2 == 0:
            accumulator += (sequence[i] ** 2) % base_mod
        else:
            accumulator -= (sequence[i] + 1) // 3
    return accumulator

# Irrelevant helper function (dead code path)
def deprecated_calc(x, y):
    return (x << 2) | (y >> 1)

# Unused transformation
temp_shift = lambda a, b: (a + b) * 5 % 7

# Core data structures
log_set = {x**2 for x in range(1, 10) if x % 3 != 0}  # Set comprehension with filtering
reference_pool = [x for x in range(15) if x % 4 != 0]

# Distractor variables
dummy_mask = 0b10101010
padding_factor = sum([i * 0.5 for i in range(8)])  # Unused float computation

# Threshold inventory with modular arithmetic and integer division
t_threshold = (37 * 2) // 5
critical_floor = 44 % 9
threshold_inventory = {
    'low': critical_floor,
    'high': t_threshold,
    'mode': 'safe'
}

# Misleading intermediate processing
shadow_copy = set()
for item in reference_pool:
    if item in log_set:
        shadow_copy.add(item * 2)  # Dead-end transformation

# Simulated telemetry stream (unused)
telemetry_data = []
for i in range(6):
    telemetry_data.append((i, (i**3) % 11))

# Conditional red herring
activation_key = None
if len(log_set) > 5:
    activation_key = sum(log_set) & dummy_mask  # Bitwise decoy

# Real processing begins here
working_pairs = [(x, x+1) for x in log_set if x < 50]

# Tuple unpacking and filtering
cleaned_metrics = []
for val_a, val_b in working_pairs:
    temp_result = val_a * 2 + val_b // 4
    if temp_result % 2 == 0:
        cleaned_metrics.append(temp_result)

# Auxiliary counting (partially relevant)
frequency_map = {}
for num in cleaned_metrics:
    frequency_map[num] = frequency_map.get(num, 0) + 1

# Key distraction: complex but irrelevant sorting operation
sorted_diags = sorted(frequency_map.items(), key=lambda x: (-x[1], x[0]))

# Decoy function call preparation
placeholder_args = tuple(sorted_diags[:2]) if len(sorted_diags) > 2 else (0, 0)

# Actual core logic hidden among noise
def process_metrics(logs, thresholds):
    base_score = 0
    high_limit = thresholds['high']
    
    # Relevant nested logic
    for entry in logs:
        if entry < high_limit * 2:
            base_score += entry // 3
        elif entry % 5 == 0:
            base_score -= entry % 7
    
    # Additional valid step: set symmetry check
    mirror_val = len(logs.intersection({1, 4, 9, 16, 25, 36}))
    
    # Final computation combining multiple concepts
    adjustment = analyze_pattern([base_score, mirror_val], 17)
    return base_score * 2 + mirror_val - abs(adjustment)

# Execution point of interest
final_diagnostic = process_metrics(log_set, threshold_inventory)

# Output requirement
print(f"Result: {final_diagnostic}")