import itertools

# Simulated sensor array diagnostics with noise filtering and health scoring
def analyze_sensor_health(raw_readings, baseline, mode='strict'):
    readings = [x for x in raw_readings if isinstance(x, (int, float)) and x >= 0]
    adjusted = [abs(x - baseline) for x in readings]
    
    # Irrelevant transformation: frequency harmonics (unused later)
    harmonic_series = [round((i + 1) * 1.5) for i in range(7)]
    derived_weights = [w ** 0.5 for w in harmonic_series if w % 2 == 0]
    weight_sum = sum(derived_weights)  # Dead computation

    # Real signal processing path
    noise_floor = sum(adjusted) / len(adjusted) if adjusted else 0
    filtered = [val for val in adjusted if val < noise_floor * 2.3]

    # Decoy health metric (never used in final logic)
    decoy_risk_score = 0
    if len(filtered) > 5:
        decoy_risk_score += 10
    if max(filtered) > 15:
        decoy_risk_score += 25

    # Actual normalization
    normalized = [min(max(val, 0), 100) for val in filtered]

    # Conditional expression for stability classification
    stability = 'stable' if all(x < 12 for x in normalized) else 'unstable'
    
    # Early return red herring: only applies in loose mode
    if mode == 'loose' and stability == 'stable':
        return sum(normalized) // 3

    return normalized

# Secondary processing function with bit manipulation distraction
def compress_signal(data_list):
    if not data_list:
        return 0
    
    # Bit manipulation decoy (looks important but unused)
    bit_accum = 0
    for val in data_list[:5]:
        bit_accum ^= int(val) & 0xFF
        bit_accum = (bit_accum << 1) | (bit_accum >> 7)
    checksum = bit_accum & 0xFFFF  # Unused result

    # Real accumulation
    total_energy = sum(x ** 0.8 for x in data_list)
    return round(total_energy / len(data_list), 3) if data_list else 0

# Main diagnostic processor combining multiple concepts
def process_readings(signal_data, sensitivity_threshold):
    # Tuple unpacking with distractor variables
    (primary, secondary, *_rest) = (signal_data[:4], signal_data[4:8], signal_data[8:12], signal_data[12:])
    
    # Destructuring with irrelevant assignment
    peak_primary = max(primary) if primary else 0
    avg_secondary = sum(secondary) / len(secondary) if secondary else 0
    
    # Sorting distraction
    sorted_vals = sorted(itertools.chain(primary, secondary))
    mid_quartile = sorted_vals[len(sorted_vals)//4 : 3*len(sorted_vals)//4]
    outlier_ratio = (len(sorted_vals) - len(mid_quartile)) / len(sorted_vals) if sorted_vals else 0

    # Real logic begins: detect anomalies above threshold
    anomalies = list(itertools.filterfalse(lambda x: x < sensitivity_threshold, mid_quartile))
    
    # Conditional expression with logical short-circuiting
    base_score = 100 if len(anomalies) == 0 else (50 if len(anomalies) <= 2 else 10)
    
    # Accumulation through multiple steps
    penalty = 0
    for a in anomalies:
        if a > sensitivity_threshold * 1.8:
            penalty += 7
        elif a > sensitivity_threshold * 1.5:
            penalty += 4
        else:
            penalty += 2
    
    final_score = base_score - penalty
    return max(final_score, 0)

# Simulation setup
baseline_offset = 23.7
threshold = 14.5
raw_input_stream = [
    35.2, 24.1, 'error', -5, 30.0, 18.3, 27.9, 22.0,
    19.1, 41.5, 26.8, 15.2, None, 33.0, 29.7, 21.4
]

# Apply initial filtering and processing
filtered_data = analyze_sensor_health(raw_input_stream, baseline=baseline_offset, mode='strict')

# Signal compression (result not directly used but looks critical)
compressed_diagnostic = compress_signal(filtered_data)  # Distractor value

# Key statement: main evaluation logic
final_diagnostic = process_readings(filtered_data, threshold)

# Print target result
print(f"Target result: {final_diagnostic}")