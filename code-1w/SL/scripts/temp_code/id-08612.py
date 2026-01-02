def analyze_efficiency(ratio):
    if ratio > 0.75:
        return ratio * 1.2
    elif ratio > 0.5:
        return ratio * 1.1
    else:
        return ratio * 0.9

process_flow = [0.68, 0.72, 0.81, 0.45, 0.77, 0.63, 0.88, 0.51]
segment_flags = [True if x > 0.7 else False for x in process_flow]

# Irrelevant transformation (distractor)
flow_squared = [x**2 for x in process_flow]

valid_segments = []
for i, val in enumerate(process_flow):
    if segment_flags[i] and analyze_efficiency(val) > 0.75:
        valid_segments.append(i)

# Misleading intermediate calculation (dead path)
baseline_offset = sum([x for x in process_flow if x < 0.6]) * 0.1

process_segments = process_flow[valid_segments[0]:valid_segments[-1]+1]

# Extraneous list processing (semi-relevant)
shifted_values = []
for j in range(len(process_segments)):
    shifted_values.append(process_segments[j] + 0.05 * (j % 2))

# Early termination condition (adds logic complexity)
def calculate_thermal_output(segments):
    total = 0.0
    threshold = 0.78
    for seg in segments:
        if seg > threshold:
            total += seg * 1.3
        else:
            total += seg * 0.95
        if total > 3.0:  # early break
            total -= 0.4
            break
    return total * 1.1  # final scaling

thermal_capacity = calculate_thermal_output(process_segments)

# Unused variables to increase cognitive load
redundant_sum = sum(flow_squared)
placeholder_flag = False

Result: {thermal_capacity}