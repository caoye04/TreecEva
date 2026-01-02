def process_metrics(entries, importance):
    final_score = 0
    temp_offset = 0
    base_shift = len(entries) % 7

    # Irrelevant tracking variables
    anomaly_count = 0
    cumulative_xor = 0
    debug_trace = []

    for idx, (val, weight) in enumerate(zip(entries, importance)):
        # Primary logic branch
        if val < 0:
            temp_val = abs(val) ** 0.5
        else:
            temp_val = val + base_shift

        # Bitwise manipulation with semi-relevant effect
        shifted_weight = weight << 1
        weighted_contribution = temp_val * shifted_weight

        # Core accumulation
        final_score += int(weighted_contribution)

        # Distractor: XOR chain that doesn't impact result
        cumulative_xor ^= int(temp_val)
        if temp_val > 10:
            anomaly_count += 1
            debug_trace.append(idx)

        # Extra distraction: nested conditional with dead-end logic
        if idx % 3 == 0:
            adjustment = 0
            for _ in range(2):
                adjustment += (idx + 1) // 2
            temp_offset -= adjustment  # never used later

    # Secondary processing on irrelevant path
    alternate_sum = sum([x | 3 for x in importance])  # unused
    scaling_factor = round(alternate_sum / (len(importance) or 1), 3)  # computed but irrelevant

    # Final adjustment using only meaningful variable
    final_score -= base_shift * anomaly_count

    return final_score

# Input data
data = [4, -9, 16, 25, 8]
weights = [1, 2, 1, 3, 2]

# Execution point
final_score = process_metrics(data, weights)
print(f"Result: {final_score}")