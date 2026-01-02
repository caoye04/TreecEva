def preprocess_values(raw):
    # Irrelevant preprocessing (distractor)
    offset = sum([x % 7 for x in raw if x > 0]) // 3
    normalized = [(val + offset) * 0.95 for val in raw]
    return [n for n in normalized if n > 0]

# Decoy function – never called but looks important
def evaluate_fitness(x):
    total = 0
    for i in range(len(x)):
        if i % 3 == 0:
            total += x[i] ** 2
    return total / (len(x) + 1)

# Unused helper with misleading logic
def transform_sequence(seq):
    result = []
    for idx, val in enumerate(seq):
        if idx % 2 == 0:
            result.append(val << 2)
        else:
            result.append(val | 7)
    return result

# Core recursive summation (used)
def recursive_sum(seq, index=0):
    if index >= len(seq):
        return 0
    return seq[index] + recursive_sum(seq, index + 1) if seq[index] > 0 else recursive_sum(seq, index + 1)

# Weighted accumulation with zip and conditional scaling
def apply_weighting(values, factors):
    adjusted = []
    for v, f in zip(values, factors):
        temp_val = v * f
        if temp_val > 100:
            temp_val = 100  # Cap mechanism
        elif temp_val < -50:
            temp_val = -50
        adjusted.append(round(temp_val, 4))
    return adjusted

# Main scoring logic
def calculate_final_score(entries, multipliers):
    base_scores = [e * 1.1 for e in entries]
    capped_scores = [min(max(s, 10), 90) for s in base_scores]  # Bound between 10 and 90

    # Apply weighting using zip
    weighted = apply_weighting(capped_scores, multipliers)

    # Accumulate only positive contributions
    net_total = 0
    for score in weighted:
        if score > 20:
            net_total += score * 0.7
        else:
            net_total += score * 0.3

    # Secondary adjustment based on enumeration logic
    bonus = 0
    for i, w in enumerate(weighted):
        if i % 3 == 0 and w > 30:
            bonus += w * 0.1
    net_total += bonus

    # Final non-linear transformation
    final = int((net_total ** 0.5) * 3.2) if net_total > 0 else 0
    return final

# Irrelevant data arrays (red herrings)
dummy_data = [12, -5, 8, 21, 33, 0, 14]
noise_seq = [x ^ 5 for x in dummy_data]

# Actual input datadata = [23, 15, 45, 10, 38]
weights = [0.8, 1.2, 0.9, 1.5, 1.1]

# Dead code path (never executed)
if len(data) > 10:
    data = preprocess_values(data)

# Key execution pointfinal_score = calculate_final_score(data, weights)
print(f"Result: {final_score}")