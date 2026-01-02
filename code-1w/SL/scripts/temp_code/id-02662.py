def analyze_pattern(sequence):
    count = 0
    for ch in sequence:
        if ch.isupper():
            count += 1
    return count

# Simulate sensor data validation and transformation
raw_data = [3, 7, 2, 8, 5, 6, 4]
data_flags = [True, False, True, True, False, True, False]
checksum = 0

for i in range(len(raw_data)):
    if i % 2 == 0:
        checksum ^= raw_data[i]  # Bitwise XOR for even indices

# Misleading intermediate processing
buffer = set()
for val in raw_data:
    buffer.add(val * 2)
    buffer.discard(4)  # Irrelevant mutation

# Auxiliary computation with string-based tagging
tagged_data = []
for x in raw_data:
    tag = "HIGH" if x > 5 else "LOW"
    tagged_data.append((x, tag.lower()))

def process_metrics(values, conditions):
    temp_sum = 0
    activation_count = 0
    history = []  # Unused tracking

    for v, flag in zip(values, conditions):
        if flag:
            temp_sum += v ** 2
            activation_count += 1
        else:
            temp_sum -= v  # Penalty for inactive

        # Distractor: complex but unused logic
        snapshot = f"{v}:{'A' if flag else 'I'}"
        mirror = snapshot[::-1]
        if mirror.startswith('A'):
            pass  # Dead code path

    # Core logic contribution
    avg = temp_sum / (activation_count or 1)
    stability = len(set(values))
    score = int(avg) + (stability & 7)  # Bitwise AND with small mask

    # Final adjustment based on string pattern analysis
    pattern_str = "".join([t for _, t in tagged_data])
    uppercase_count = analyze_pattern(pattern_str.upper())
    score += uppercase_count

    return score

# Key execution point
final_score = process_metrics(raw_data, data_flags)
Result: {final_score}