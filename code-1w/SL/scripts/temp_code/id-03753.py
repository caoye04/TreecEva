def transform_sequence(seq, factor):
    """Irrelevant transformation function (dead code path)"""
    return [x * factor + 2 for x in seq if x % 2 == 0]

# Unused sensor calibration constants (distractor variables)
calibration_a = 0.87
offset_bias = -3.2
temporal_factor = 1.414
dummy_matrix = [[1, 0], [0, 1]]

# Simulated raw sensor readings (real data)
raw_readings = [
    12, 8, 15, 3, 9, 11, 7, 14, 5, 6,
    13, 10, 4, 16, 2, 1, 18, 19, 20, 17
]

# Misleading intermediate processing (red herring)
def filter_outliers(data, limit=10):
    return [x for x in data if x > limit]  # Only used once, not critical

# Unused recursive helper (decoy function)
def count_nodes(tree):
    if not tree:
        return 0
    return 1 + count_nodes(tree.get('left', {})) + count_nodes(tree.get('right', {}))

# Real processing begins here
threshold_map = {
    'low': lambda x: x < 6,
    'optimal': lambda x: 6 <= x <= 14,
    'high': lambda x: x > 14
}

status_flags = {
    'stable': 0,
    'warning': 0,
    'critical': 0
}

processed_data = []
for reading in raw_readings:
    processed = reading ^ 7  # Bit manipulation: XOR with 7
    if reading % 3 == 0:
        processed -= 2
    elif reading % 5 == 0:
        processed += 1
    else:
        processed = abs(processed // 2)  # Integer division, potential loss
    processed_data.append(processed)

# Secondary transformation (partially relevant)
shifted_data = [(val + 5) % 25 for val in processed_data]

# Character counting in status keys (irrelevant but plausible)
char_count = sum(len(key) for key in status_flags.keys())

# Determine status distribution (actual logic chain)
def evaluate_status(value):
    if threshold_map['high'](value):
        return 'critical'
    elif threshold_map['low'](value):
        return 'warning'
    else:
        return 'stable'

for val in shifted_data:
    flag = evaluate_status(val)
    status_flags[flag] += 1

# Early termination check (misleading conditional)
if status_flags['critical'] > 5:
    emergency_override = True
    correction_factor = 0.9
else:
    emergency_override = False
    correction_factor = 1.0  # Never used

# Complex conditional expression (required feature)
mode_selection = 'aggressive' if status_flags['warning'] > status_flags['stable'] else 'conservative'

# Dictionary-based mapping for diagnostics (required feature)
diagnostic_weights = {
    'stable': 1.0,
    'warning': 2.5,
    'critical': 5.0
}

weighted_score = sum(status_flags[k] * diagnostic_weights[k] for k in status_flags)

# Core analysis function with nesting and control flow
def analyze_readings(data, thresholds):
    total = 0
    history = {}
    for i, val in enumerate(data):
        if i % 4 == 0:
            if val in thresholds['optimal'](val):
                total += 3
            elif val > 10:
                total += 1
            else:
                total -= 2
        else:
            if val < 5:
                total += 4
                if i % 7 == 0:
                    total += 1
            elif val > 12:
                total -= 1
                break  # Early break creates non-obvious result
            else:
                total += 2
        history[i] = total  # Tracking but unused
    
    # Nested conditional expressions
    adjustment = 1.5 if total > 20 else (0.8 if total < 10 else 1.1)
    
    # Final computation
    final = int((total * adjustment) + len(history.keys()))
    
    # Dead code branch (never reached due to return)
    if final < 0:
        final = 0
        
    return final

# Key execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Irrelevant cleanup
del dummy_matrix
unused_sum = sum([calibration_a, offset_bias, temporal_factor])

# Output the target result
print(f"Result: {final_diagnostic}")