def analyze_pattern(logs):
    cumulative_shift = 0
    temp_buffer = []
    for i in range(len(logs)):
        entry = logs[i]
        if i % 2 == 0:
            shifted = entry * (i + 1)
            temp_buffer.append(shifted)
            cumulative_shift += shifted
        else:
            adjusted = entry + (i - 1)
            temp_buffer.append(adjusted)

    # Irrelevant smoothing pass (distractor)
    smoothed = [sum(temp_buffer[j:j+3]) / 3 for j in range(len(temp_buffer) - 2)] if len(temp_buffer) > 2 else temp_buffer

    # Key slicing operation: only consider last 4 entries of original buffer
    relevant_segment = temp_buffer[-4:]

    # Secondary processing with dictionary frequency tracking
    freq_map = {}
    for val in relevant_segment:
        rounded = int(round(val))
        freq_map[rounded] = freq_map.get(rounded, 0) + 1

    # Misleading entropy-like calculation (not used in final result)
    import math
    entropy = 0
    total = len(relevant_segment)
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)

    # Core logic: sum of squared indices-weighted values
    weighted_sum = 0
    for idx, value in enumerate(relevant_segment):
        weight = (idx + 1) ** 2
        weighted_sum += weight * value

    # Final transformation
    final_diagnostic = int(weighted_sum // 1.5)
    return final_diagnostic

# Simulated diagnostic readings from sensor array
diagnostics = [3, 7, 2, 8, 4, 6]

# Extraneous data structures (dead weight)
baseline_readings = {k: v for k, v in enumerate([1, 1, 1, 1, 1, 1])}
calibration_sequence = diagnostics[::-1]
outlier_flags = [x > 5 for x in diagnostics if x != 4]

# Critical computation point
final_diagnostic = analyze_pattern(diagnostics)

# Output result
print(f"Result: {final_diagnostic}")