def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if x > 0]
    normalized = [round(x ** 0.5, 3) for x in filtered]
    return normalized


def generate_sequence(length):
    seq = [1, 1]
    for i in range(2, length):
        seq.append(seq[i-1] + seq[i-2])
    return seq[:length]


def shift_window(data, offset):
    return [data[i] + offset for i in range(len(data)) if i % 2 == 0] + [data[i] for i in range(len(data)) if i % 2 != 0]


def evaluate_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)


def analyze_pattern(dataset, adjustment):
    temp_state = []
    for val in dataset:
        if val > adjustment:
            temp_state.append(int(val * 1.2) % 7)
        else:
            temp_state.append(int(val * 0.8) % 5)
    
    # Irrelevant entropy calculation (red herring)
    _ = evaluate_entropy(temp_state)
    
    mapping = {i: temp_state.count(i) for i in set(temp_state)}
    
    # Decoy logic with unused branching
    if sum(mapping.values()) > 10:
        scaling_factor = 2.5
    else:
        scaling_factor = 1.8  # Never used
    
    result = 0
    for k, v in mapping.items():
        result += k * v
    
    # Additional distraction: complex but irrelevant set operations
    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}
    _ = s1.union(s2).intersection({2, 4, 6})
    _ = len(s1.symmetric_difference(s2))
    
    return result

# Unused recursive function (dead code path)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Simulated sensor data (initial input)
sensor_readings = [-5, 10, 15, -3, 20, 25, 8, 0, 12]

# Step 1: Preprocess signal to remove noise and normalize
processed = preprocess_signal(sensor_readings)

# Generate auxiliary sequence (distractor)
fib_seq = generate_sequence(10)

# Apply window shift with arbitrary offset (partially relevant)
shifted_readings = shift_window(processed, 1.5)

# Transform data using conditional expression chain
transformed_data = [
    x * 1.1 if i % 3 == 0 else \
    x * 0.95 if i % 3 == 1 else \
    x * 1.05 \
    for i, x in enumerate(shifted_readings)
]

# Baseline adjustment calculated via min/max stats (relevant)
baseline_shift = (min(transformed_data) + max(transformed_data)) / 2

# Core analysis function call — critical execution point
final_diagnostic = analyze_pattern(transformed_data, baseline_shift)

# Print final result
print(f"Result: {final_diagnostic}")