def analyze_trends(data, threshold=0.5):
    trend_data = []
    for i in range(1, len(data)):
        change = (data[i] - data[i-1]) / data[i-1]
        trend_data.append(change)
    return [t for t in trend_data if abs(t) > threshold]


def filter_outliers(values, factor=1.5):
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [v for v in values if lower_bound <= v <= upper_bound]


def compute_entropy(arr):
    from math import log2
    total = sum(arr)
    if total == 0:
        return 0
    probabilities = [x / total for x in arr if x > 0]
    return -sum(p * log2(p) for p in probabilities)


def shift_cipher(text, shift=3):
    # Irrelevant distraction: string encryption function
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def accumulate_pairs(seq):
    # Another red herring: accumulates adjacent products
    return [seq[i] * seq[i+1] for i in range(len(seq)-1)]


def generate_fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# Decoy dataset: financial noise
market_fluctuations = [0.01, -0.02, 0.05, 0.03, -0.01, 0.04, 0.02, -0.03]
distorted_signal = [x * 100 for x in market_fluctuations if x != 0]

# Fake processing path
transformed = list(map(lambda x: x ** 2, distorted_signal))
aggregated = sum(transformed) // len(transformed)
baseline_offset = 42

# Real input data (hidden among distractions)
sensor_readings = [85, 90, 78, 92, 88]
weight_map = {'precision': 0.3, 'recall': 0.2, 'latency': 0.1, 'throughput': 0.4}

# Simulated metric extraction with slicing and enumeration
metrics = []
for idx, val in enumerate(sensor_readings):
    if idx % 2 == 0:
        metrics.append(val * 0.1)
    else:
        metrics.append(val * 0.05)

# Introduce zip and set operations as distractors
labels = ['A', 'B', 'C', 'D', 'E']
pairs = list(zip(labels, sensor_readings))
unique_categories = set([label[0] for label in labels])

# More irrelevant transformations
sliced_pairs = pairs[1:4:2]
doubled_values = [x[1]*2 for x in sliced_pairs]

# Core logic embedded within noise
def evaluate_performance(met, wts):
    keys = ['precision', 'recall', 'latency', 'throughput']
    defaults = [0.8, 0.7, 0.9, 0.6]
    filled_metrics = []
    for i, k in enumerate(keys):
        if i < len(met):
            filled_metrics.append(met[i])
        else:
            filled_metrics.append(defaults[i])
    
    # Apply weights using list comprehension and enumeration
    weighted_sum = sum(filled_metrics[i] * wts[list(wts.keys())[i]] for i in range(len(keys)))
    adjustment_factor = compute_entropy([int(x*10) for x in filled_metrics])
    
    # Final calculation buried in logic
    temp_result = weighted_sum * (1 + adjustment_factor)
    
    # Use of slicing on intermediate result
    str_rep = str(round(temp_result, 4))
    decimal_part = str_rep.split('.')[1][:2]
    
    # Actual answer formation
    final_numeric = int(decimal_part) if decimal_part != '00' else 50
    
    # Dead code branch (never executed due to structure)
    if len(str_rep) > 100:
        backup = sum(int(d) for d in str_rep if d.isdigit())
        return float(backup)
    
    return final_numeric

# Unused recursive red herring
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

# Hidden call chain
intermediate_sequence = generate_fibonacci(len(sensor_readings))
processed = [x+y for x, y in zip(intermediate_sequence, sensor_readings)]

# Key execution point
weights = {'precision': 0.3, 'recall': 0.2, 'latency': 0.1, 'throughput': 0.4}
final_score = evaluate_performance(metrics, weights)

# Print required output
print(f"Result: {final_score}")