def analyze_signal(samples):
    magnitude = [abs(x) for x in samples]
    normalized = [m / max(magnitude) for m in magnitude]
    threshold = 0.5
    peaks = [i for i, v in enumerate(normalized) if v > threshold]
    peak_count_metric = len(peaks) * 1.5
    return peak_count_metric

samples_x = [-0.2, 0.8, -0.9, 0.1, 0.95, -0.7, 0.3]

# Distractor: irrelevant signal analysis
def frequency_scan(sig):
    count = 0
    for s in sig:
        if s > 0.5 or s < -0.5:
            count += 1
    ratio = count / len(sig)
    adjusted = ratio * 100
    return adjusted

resultant = frequency_scan(samples_x)

# Real data path begins
raw_data = [3, 7, 2, 9, 4]
weight_map = [0.1, 0.3, 0.2, 0.3, 0.1]

# Misleading transformation chain
shadow_data = [(x ** 2 + 1) // 2 for x in raw_data]
decoy_weights = [w + 0.05 for w in weight_map]
temp_product = [a * b for a, b in zip(shadow_data, decoy_weights)]
baseline_offset = sum(temp_product) / len(temp_product)

# Actual relevant computation (obscured by distractors)
def preprocess(seq, factors):
    indexed = []
    for idx, val in enumerate(seq):
        adjusted_val = val * factors[idx]
        if idx % 2 == 0:
            adjusted_val -= 0.1
        else:
            adjusted_val += 0.05
        indexed.append((idx, round(adjusted_val, 4)))
    return [item[1] for item in indexed]

cleaned = preprocess(raw_data, weight_map)

# Secondary distraction: unused recursive function
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fib_series = [fibonacci(i) for i in range(6)]
fib_sum = sum(fib_series)
fib_ratio = fib_series[-1] / fib_series[-2] if len(fib_series) > 1 else 0

# Core logic buried in distractions
def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0
    probabilities = [v / total for v in values]
    import math
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)

entropy_value = compute_entropy(cleaned)

# Another red herring: string-based encoding
status_codes = ['A', 'B', 'C']
encoded = ''.join([s.lower() for s in status_codes])
length_code = len(encoded) * 10

# Main processing function (decoy name, but actually used)
def process_metrics(data, weights):
    # Heavily interwoven with noise
    temp_results = []
    for i, (d, w) in enumerate(zip(data, weights)):
        if i == 0:
            temp_results.append(d * w - 0.1)
        elif i % 3 == 0:
            temp_results.append(d * w + 0.2)
        else:
            temp_results.append(d * w + 0.05)
    
    base_metric = sum(temp_results)
    
    # Additional distraction: tuple unpacking that isn't critical
    extras = (1.5, 2.3, 0.9)
    alpha, beta, gamma = extras
    adjustment = alpha * 0.1 if base_metric > 2 else gamma * 0.2
    
    # Final computation
    score = base_metric + adjustment + entropy_value
    
    # Dead code branch (never reached due to logic)
    if len(data) > 10:
        fallback = 0
        for x in data:
            fallback += x * 2
        score = fallback
    
    return round(score, 4)

# Critical execution point
final_score = process_metrics(data=raw_data, weights=weight_map)
print(f"Target result: {final_score}")