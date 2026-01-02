def analyze_pattern(sequence):
    """Irrelevant helper function for pattern analysis."""
    count = 0
    for i in range(len(sequence)):
        if sequence[i] % 2 == 0 and i % 2 == 1:
            count += 1
    return count


def validate_checksum(items):
    """Decoy function that computes a checksum but is never used."""
    checksum = 0
    for idx, val in enumerate(items):
        checksum ^= (val + idx) % 7
    return checksum

# Unused but misleading initialization
temp_buffer = [x ** 2 for x in range(15) if x % 3 != 0]
shadow_map = {k: k * 1.5 for k in temp_buffer[:10]}

# Real data used in computation
data = [14, 8, 22, 36, 41, 9, 17]
weights = [0.1, 0.2, 0.15, 0.25, 0.1, 0.05, 0.1]

# Distractor: complex-looking but unused transformation
decoy_data = list(zip(temp_buffer, [x // 3 for x in temp_buffer if x > 20]))
deep_offset = sum([len(str(x)) for x in shadow_map.values()]) // 2

# Auxiliary metric with partial relevance
status_flags = ['HIGH', 'LOW', 'MID', 'HIGH', 'MID', 'LOW', 'HIGH']
flag_values = {'HIGH': 3, 'MID': 2, 'LOW': 1}

# Secondary computation - appears important but only one value is used
aggregated_risk = 0
for i, flag in enumerate(status_flags):
    aggregated_risk += flag_values[flag] * (i + 1)

# Key intermediate: only 'penalty_factor' derived from this is used later
penalty_factor = aggregated_risk % 5

# Another red herring: string-based encoding that doesn't affect result
encoded_tags = []
for i, d in enumerate(data):
    tag = f"DAT{d}-{i}".replace('0', 'X')
    if 'X' in tag:
        encoded_tags.append(tag)

# Real processing begins here — heavy distraction up to this point
def normalize(values):
    total = sum(values)
    return [v / total for v in values] if total else values

normalized_weights = normalize(weights)

# Core logic wrapped in misleading context
def compute_moment(arr, w):
    """Weighted moment calculation; only this part matters."""
    moment = 0.0
    for i in range(len(arr)):
        # Introduce modular arithmetic twist
        adjusted_index = (i * 3) % len(arr)
        contribution = arr[adjusted_index] * w[i]
        # Integer division side-path
        if i > 0 and arr[i] % 2 == 0:
            contribution -= (arr[i] // 4) * w[i-1]
        moment += contribution
    return moment

# Distractor dictionary operation — looks like configuration
config_map = {
    'version': '2.1',
    'active': True,
    'thresholds': [penalty_factor, 2.5, 3.7],
    'scale': 1.0 + (deep_offset / 100)
}

# Fake control flow with dead branches
mode_flag = 'standard'
scaling_factor = 1.0
if mode_flag == 'debug':
    scaling_factor = 0.9
elif mode_flag == 'legacy':
    scaling_factor = 1.1  # Never reached
else:
    pass  # Real path does nothing

# Main processing function — actual core logic
def process_metrics(readings, importance):
    base_moment = compute_moment(readings, importance)
    
    # Use only penalty_factor from earlier computation
    adjusted_moment = base_moment * (1 - penalty_factor * 0.05)
    
    # Final adjustment using string-derived length (only one element actually contributes)
    tag_count_bonus = len(encoded_tags) * 0.02  # Only depends on prior string ops
    final_raw = adjusted_moment + tag_count_bonus
    
    # Round to nearest integer using floor logic
    result = int(final_raw) if final_raw >= 0 else int(final_raw - 0.5)
    
    # One last decoy: tuple unpacking with irrelevant use
    aux_data = (result, result * 1.01, result * 0.99)
    primary, _, _ = aux_data  # Unpack but ignore extras
    
    return primary

# Execution point of interest
final_score = process_metrics(data, normalized_weights)

# Output required format
print(f"Target result: {final_score}")