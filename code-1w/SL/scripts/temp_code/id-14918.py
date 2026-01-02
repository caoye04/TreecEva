def analyze_sequence(data):
    temp_result = 0
    for i in range(len(data)):
        if i % 2 == 0:
            temp_result += data[i] * 2
        else:
            temp_result -= data[i] // 3
    return temp_result

# Irrelevant helper function (dead code path)
def deprecated_calculate(x):
    return (x ** 2 + 3 * x + 1) % 7

# Unused transformation table
decoy_table = {k: (k * k) % 13 for k in range(15)}

# Main processing pipeline
base_offset = 417
raw_inputs = [12, 8, 25, 17, 33, 42]
processed = [val % 9 + 1 for val in raw_inputs]

# Distractor: complex-looking but unused bitwise cascade
cascade_key = 0
for x in raw_inputs:
    cascade_key ^= (x << 1) ^ (x >> 2)
cascade_key = cascade_key & 0xFF

# Real computation begins: transform with side-channel filtering
filtered = []
for val in processed:
    if val > 5:
        filtered.append(val * 3)
    elif val == 3:
        filtered.append(99)  # red herring value, never triggered
    else:
        filtered.append(val + 4)

# Dictionary-based weight mapping (relevant)
weight_map = {
    'w': 3, 'x': -2, 'y': 7, 'z': 1
}

# Construct metric map using filtered results and dictionary operations
metric_map = {}
for idx, char in enumerate(weight_map.keys()):
    if idx < len(filtered):
        metric_map[char] = filtered[idx] * weight_map[char]
    else:
        metric_map[char] = 0

# Additional noise: unused recursive sum
def rec_sum(n):
    if n <= 1:
        return n
    return n + rec_sum(n - 2)

unused_total = rec_sum(20)

# Decoy control flow with misleading intermediate
status_flags = [True, False, True]
aggregated = 0
for flag in status_flags:
    if flag:
        aggregated += 100  # irrelevant to final result

# Critical operation: score evaluation using dictionary values
metric_map['x'] += metric_map['w'] // 5  # modifies 'x' based on 'w'

# Final scoring logic (depends only on 'x', 'y', 'z')
def evaluate_performance(metrics, offset):
    score = offset
    score += metrics.get('x', 0)
    score -= metrics.get('w', 0) // 10  # uses 'w' indirectly
    score *= (metrics.get('y', 1) // 7)  # scales by y/7
    if metrics.get('z', 0) > 0:
        score += 5
    return score

# Execute critical statement
temp_data = [6, 3, 8]
analyze_sequence(temp_data)  # called but result ignored

final_score = evaluate_performance(metric_map, base_offset)
print(f"Target result: {final_score}")