def preprocess_signal(raw_values):
    filtered = [x for x in raw_values if x > 0]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized


def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq


def evaluate_stability(ratios):
    if len(ratios) < 2:
        return 0
    variance = sum((ratios[i] - ratios[i-1]) ** 2 for i in range(1, len(ratios)))
    return round(variance, 4)


def analyze_pattern(data, limit):
    subset = data[:limit]
    if len(subset) == 0:
        return -1
    product = 1
    for val in subset:
        product *= int(val * 100) % 7
    return product + len(subset)

# Irrelevant signal processing chain (distractor)
raw_sensor_data = [0.1, -0.3, 0.5, 0.2, -0.7, 0.9, 1.1, -0.2]
processed = preprocess_signal(raw_sensor_data)
stability_score = evaluate_stability(processed)

# Decoy combinatorics (dead path)
def count_combinations(n, r):
    if r > n or r < 0:
        return 0
    result = 1
    for i in range(min(r, n - r)):
        result = result * (n - i) // (i + 1)
    return result

combination_test = count_combinations(10, 3)

# Core misleading transformation chain (red herring)
fibonacci_tail = generate_sequence(7)
inverted_map = {i: float(f'{1/(v+1):.3f}') for i, v in enumerate(fibonacci_tail)}
sum_inverse = sum(inverted_map.values())

# String-based filtering distraction
data_tags = ['A1', 'B2', 'C3', 'D4', 'E5']
valid_tags = [tag for tag in data_tags if tag.endswith('2') or tag.startswith('C')]
encoded_reference = ''.join([t[0] for t in valid_tags])  # evaluates to 'BC'

# Actual relevant computation path
base_stream = [3.2, 1.8, 4.5, 2.1, 3.9, 0.7, 2.4]
transformed_data = []
for x in base_stream:
    temp_val = (x ** 2) / 2
    if temp_val > 3:
        transformed_data.append(round(temp_val, 3))

# Misleading conditional check (unused)
if len(transformed_data) > 5:
    transformed_data = [x for x in transformed_data if x < 5]

threshold = 5
final_diagnostic = analyze_pattern(transformed_data, threshold)

print(f'Result: {final_diagnostic}')