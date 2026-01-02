def analyze_pattern(sequence):
    """ Misleading function: appears relevant but is never called """
    count = 0
    for i in range(len(sequence)):
        if sequence[i] % 3 == 0:
            count += (i * 2) // sequence[i]
    return count

# Irrelevant constants
tolerance_threshold = 0.005
max_iterations = 1000
debug_mode = True

# Decoy data structures
auxiliary_map = {x: x**2 for x in range(15) if x % 2 == 1}
shadow_list = [i - 3 for i in range(20) if i in auxiliary_map]

# Actual input data
event_codes = [1, 0, 1, 1, 0, 1]
raw_data = [84, 72, 91, 65, 88, 77]
weights = {'alpha': 0.2, 'beta': 0.3, 'gamma': 0.5}

# Distractor: unused but plausible weighting scheme
legacy_weights = {
    'w1': 0.1,
    'w2': 0.4,
    'w3': 0.5
}

# Simulated calibration offset (unused)
calibration_factor = sum([x for x in raw_data if x > 80]) / 100.0

# Bit manipulation red herring
def apply_mask(value):
    masked = value & 0b11111111
    shifted = masked << 2
    return shifted ^ 0b10101010  # Never actually used

# Auxiliary helper that seems important but isn't invoked
def normalize_dataset(data):
    mean_val = sum(data) / len(data)
    return [round((x - mean_val) / mean_val, 4) for x in data]

# Core logic disguised among noise
def compute_baseline(x):
    if x < 70:
        return x + 5
    elif x < 85:
        return x + 3
    else:
        return x + 1

# Real processing chain
def evaluate_status(code_seq):
    status_flags = []
    for code in code_seq:
        if code == 1:
            status_flags.append('active')
        else:
            status_flags.append('inactive')
    return status_flags

def process_results(data, weight_dict):
    # Step 1: Apply baseline correction
    adjusted = [compute_baseline(val) for val in data]
    
    # Step 2: Extract active entries using event codes
    active_values = []
    statuses = evaluate_status(event_codes)
    for i, flag in enumerate(statuses):
        if flag == 'active':
            active_values.append(adjusted[i])
    
    # Step 3: Weighted aggregation
    alpha_part = active_values[0] * weight_dict['alpha']
    beta_part = active_values[1] * weight_dict['beta']
    gamma_part = active_values[2] * weight_dict['gamma']
    
    # Step 4: Final adjustment with modular arithmetic
    temp_sum = alpha_part + beta_part + gamma_part
    final_raw = temp_sum % 97
    
    # Step 5: Add fixed offset from bit count in third active value
    third_val_bin = bin(active_values[2])
    popcount = third_val_bin.count('1')
    final_score = int(final_raw + popcount)  # Key assignment point
    
    # Dead branch: unreachable but looks important
    if final_score < 0:
        final_score = abs(final_score)
    
    return final_score

# Execution begins here
baseline_check = [compute_baseline(x) for x in raw_data]

# This call looks like it might affect things but doesn't
_ = {k: v*1.05 for k, v in weights.items()}

# Critical execution point
final_score = process_results(raw_data, weights)

# Output result as required
print(f"Result: {final_score}")