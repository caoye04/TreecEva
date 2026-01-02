def analyze_frequency(text):
    freq = {}
    for char in text:
        if char.isalpha():
            freq[char.lower()] = freq.get(char.lower(), 0) + 1
    return freq

# Irrelevant function: character frequency analysis (red herring)
def compute_entropy(frequency_dict):
    import math
    total = sum(frequency_dict.values())
    entropy = 0
    for count in frequency_dict.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

# Unused helper: calculates prime factors (dead code path)
def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

# Decoy data structure (misleading intermediate result)
benchmark_metadata = {
    'version': '3.1.4',
    'active_modules': ['parser', 'validator', 'scorer'],
    'weights': [0.2, 0.3, 0.5],
    'deprecated': False
}

# Simulated raw results from sub-benchmarks (some irrelevant)
raw_data = [
    {'task': 'arithmetic', 'result': 87, 'weight': 0.25},
    {'task': 'logic', 'result': 92, 'weight': 0.25},
    {'task': 'assignment', 'result': 78, 'weight': 0.15},
    {'task': 'control_flow', 'result': 85, 'weight': 0.20},
    {'task': 'data_structures', 'result': 90, 'weight': 0.15}
]

# Transform into flat lists for processing
tasks, results, weights = zip(*[(d['task'], d['result'], d['weight']) for d in raw_data])

# Distractor computation: normalized scores with unused scaling
normalized = [round(r / 100.0, 4) for r in results]
scaled_weights = [w * 1.1 for w in weights]  # unused scaled version

# Real weighting logic hidden among distractions
def weighted_average(values, weights):
    return sum(v * w for v, w in zip(values, weights))

partial_sum = sum(w for w in weights)  # red herring: appears important but redundant

# Set operations: filter high-performing tasks (only used conceptually)
high_performers = {t for t, r in zip(tasks, results) if r >= 85}
all_tasks = set(tasks)
ignored_tasks = all_tasks - high_performers  # calculated but unused

# Core metric logic buried in abstraction
def evaluate_performance(metrics, raw_results):
    # Nested conditional expression: actual answer derivation
    base = weighted_average(results, weights)
    adjustment = 5 if len(high_performers) >= 3 else -2
    bonus = 3 if 'arithmetic' in high_performers and 'logic' in high_performers else 0
    
    # Recursive depth counter (simple recursion red herring)
    def calculate_depth(n):
        return 1 + calculate_depth(n-1) if n > 0 else 0
    
    depth = calculate_depth(2)  # always returns 2, but looks complex
    
    # Actual formula
    temp_result = base + adjustment + bonus
    final = int(round(temp_result))
    
    # Multiple assignments (distractor)
    a = b = c = final // 3
    
    # Enumerate usage (required feature) - irrelevant traversal
    for i, task in enumerate(tasks):
        if i % 2 == 0:
            a += 1  # meaningless side-effect

    return final

# Dummy assignment to confuse data flow
interim_value = weighted_average(normalized, weights)

# Key statement
metric_set = {'precision', 'recall', 'f1'}
benchmark_results = raw_data
final_score = evaluate_performance(metric_set, benchmark_results)

print(f"Target result: {final_score}")