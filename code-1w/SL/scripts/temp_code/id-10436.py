from collections import defaultdict, Counter
import math

# Irrelevant utility function (decoy)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v] if norm > 0 else v

def generate_sequence(n):
    # Generates Fibonacci-like sequence with noise
    seq = [1, 1]
    for i in range(2, n + 5):
        noisy_val = seq[-1] + seq[-2] + ((i % 3) - 1)  # red herring
        seq.append(noisy_val)
    return seq[:n]

def transform_values(data, key_offset=3):
    # Applies multiple transformations, some irrelevant
    shifted = [(x + key_offset) * 2 for x in data]
    filtered = [x for x in shifted if x % 2 == 0]
    mapped = {i: val ** 0.5 for i, val in enumerate(filtered)}
    # Dead code path - never used
    if len(mapped) > 100:
        mapped = {k: v * 1.5 for k, v in mapped.items()}
    return list(mapped.values())

def evaluate_stability(ratios):
    # Computes variance but only returns magnitude
    mean = sum(ratios) / len(ratios) if ratios else 0
    variance = sum((x - mean) ** 2 for x in ratios) / len(ratios) if ratios else 0
    return int(variance * 100) % 7  # misleading diagnostic

def compute_entropy(values):
    # Uses Counter to compute symbol frequency entropy
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def recursive_check(n):
    # Recursive bit counting (irrelevant side calculation)
    if n <= 0:
        return 0
    return (n & 1) + recursive_check(n >> 1)

def analyze_pattern(data, limit):
    # Core logic hidden among distractions
    temp_result = 0
    for i, val in enumerate(data):
        if i % 3 == 0 and val > 3:
            temp_result += int(val) * (i + 1)
    # Actual answer computation
    proxy_score = sum(1 for x in data if x > limit)
    adjustment = len([x for x in data if x < 2])
    final_diagnostic = proxy_score * 17 - adjustment * 5
    # Decoy operations below
    decoy_map = defaultdict(lambda: 0)
    for x in data:
        decoy_map[recursive_check(int(x))] += 1
    unused_entropy = compute_entropy([int(x) for x in data if x > 1])
    stability = evaluate_stability([data[i] / (data[i-1] + 1e-8) for i in range(1, len(data))])
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    raw_input = generate_sequence(12)
    # Apply transformation chain
    transformed_data = transform_values(raw_input, key_offset=4)
    threshold = compute_entropy([1, 1, 2, 2, 3]) * 10  # ~2.3219 * 10 → 23.219
    threshold = int(threshold)  # becomes 23
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    print(f"Result: {final_diagnostic}")