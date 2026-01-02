def transform_signal(raw_values, scaling_factor):
    """Apply non-linear transformation to sensor signal (distractor function)"""
    transformed = []
    for v in raw_values:
        if v > 0:
            transformed.append(v ** 0.5 * scaling_factor)
        else:
            transformed.append(-1 * (abs(v) ** 0.3))
    return transformed


def validate_checksum(data_str):
    """Compute checksum for data integrity (irrelevant but plausible)
    This function is never called but looks important.
    """
    chk = 0
    for char in data_str:
        chk ^= ord(char)
    return chk == 0xFF

# Simulated sensor readings (some real, some decoy)
sensor_a_readings = [144, 225, 196, 361, 400, 529]  # Perfect squares: 12², 15², 14², 19², 20², 23²
sensor_b_readings = [111, 222, 333, 444]  # Distractor sequence

# Preprocessing step that matters
def extract_features(values):
    result = []
    for val in values:
        root = int(val ** 0.5)
        if root * root == val:  # Is perfect square?
            digit_sum = sum(int(d) for d in str(root))
            if digit_sum % 2 == 0:
                result.append(root + digit_sum)
            else:
                result.append(root - digit_sum)
        else:
            result.append(0)  # Non-square contributes nothing
    return result

# Secondary transformation with red herring logic
def perturb_sequence(seq, noise_level=0.1):
    """Add controlled noise (never used in final path)"""
    return [x + (i * noise_level) for i, x in enumerate(seq)]

# Core logic: group and filter based on dynamic criteria
def build_summary(features):
    summary = {}
    for idx, val in enumerate(features):
        key = 'even' if val % 2 == 0 else 'odd'
        if key not in summary:
            summary[key] = []
        summary[key].append(val * (idx + 1))  # Weight by position
    return summary

# Another distraction: recursive checksum (unused)
def recursive_reduce(n):
    if n < 10:
        return n
    return recursive_reduce(sum(int(d) for d in str(n)))

# Real processing begins here
processed_raw = [x for x in sensor_a_readings if x % 2 == 0]  # Filter even squares only

feature_vector = extract_features(processed_raw)

# Introduce irrelevant string manipulation (plausible metadata)
current_mode = "diagnostic_v2"
mode_prefix = current_mode.split('_')[0]
version_tag = ''.join([c for c in current_mode if c.isdigit()])

# Create complex control flow with dead branches
def apply_filters(data_dict):
    filtered = []
    for k, values in data_dict.items():
        temp = []
        threshold = 50
        for v in values:
            # Misleading condition that appears significant
            if k == 'even' and v > threshold:
                temp.append(v // 2)
            elif k == 'odd':
                temp.append(v + 10)
            else:
                temp.append(v)  # Default case actually used
        filtered.extend(temp)
    return filtered

summary_groups = build_summary(feature_vector)

# Dead code path: masked by similar name
apply_filter = lambda x: [e for e in x if e > 0]  # Unused

filtered_diagnostics = apply_filters(summary_groups)

# Define threshold map with fake and real components
threshold_map = {
    'normal': 42,
    'elevated': 85,
    'critical': 200,
    'debug_mode': False,
    'override_key': None
}

# Actual answer derivation buried in complexity
def analyze_readings(diag_list, limits):
    base = 1000
    adjustment = 0
    for i, val in enumerate(diag_list):
        if val < limits['elevated']:
            adjustment += val // (i + 1) if i % 2 == 0 else -(val % 13)
        else:
            base *= 1.1  # Not triggered
    
    # Final computation: depends on prior steps
    temp_var = base + adjustment
    
    # Additional misdirection: unused conditional expression
    status_flag = 'OK' if temp_var < 900 else 'ALERT' if temp_var > 1100 else 'MONITOR'
    
    # The real assignment
    final_score = int(temp_var - 37)  # Offset applied
    
    return final_score

# Critical execution point
final_diagnostic = analyze_readings(filtered_diagnostics, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")