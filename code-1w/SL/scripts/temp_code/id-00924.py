import math

# Irrelevant helper function (dead code path)
def unused_diagnostic(data):
    return sum([x ** 2 for x in data if x > 5])

# Distractor: complex-looking but unused transformation
twin_primes = [i for i in range(2, 50) if all(i % p != 0 for p in range(2, int(i**0.5)+1))]
prime_offset = sum(twin_primes[:10]) // 10

# Misleading intermediate calculation (not used in final result)
class PerformanceTracker:
    def __init__(self):
        self.history = []
        self.baseline = 75.0

    def update(self, val):
        self.history.append(val)

    def get_trend(self):
        return sum(self.history) / len(self.history) if self.history else 0

# Unused recursive decoy function
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Real logic starts here — subtle and buried among distractions
raw_inputs = [12, 8, 15, 3, 9, 6]
filter_fn = lambda x: x > 7
filtered = list(filter(filter_fn, raw_inputs))  # [12, 8, 15, 9]

# Secondary processing with distractors
offset_value = 4
shifted = [x - offset_value for x in filtered]  # [8, 4, 11, 5]

dummy_stats = {
    'mean': sum(shifted) / len(shifted),
    'max_deviation': max(shifted) - min(shifted),
    'padding': [0]*len(raw_inputs)  # red herring
}

# Another layer of misdirection: bitwise decoy
data_key = 0
for x in shifted:
    data_key ^= x << 1  # produces some large number, never used later

# Core metric computation (obscured)
def transform(x):
    if x % 3 == 0:
        return x * 2
    elif x % 2 == 0:
        return x + 5
    else:
        return x - 1

transformed = [transform(x) for x in shifted]  # [8->13, 4->9, 11->10, 5->4] => [13,9,10,4]

# Conditional aggregation with short-circuit logic
safe_avg = lambda a, b: (a + b) / 2 if a >= 0 and b >= 0 else 0
running_total = 0
for i in range(len(transformed) - 1):
    running_total += safe_avg(transformed[i], transformed[i+1])

# Additional noise: unused list comprehension
even_squared = [x**2 for x in raw_inputs if x % 2 == 0]  # [144, 64, 36]

# Tuple unpacking distraction
config = (100, 'strict', False)
threshold, mode, debug = config

# Real evaluation logic deeply nested
metric_data = {
    'samples': transformed,
    'total': running_total,
    'version': '2.1b'
}

def evaluate_performance(data):
    samples = data['samples']
    base = data['total']
    
    # Nested conditional with logical operations
    if len(samples) > 3 and all(s > 0 for s in samples):
        adjustment = 10 if any(s % 5 == 0 for s in samples) else 5
        
        # Bitwise manipulation that actually matters
        flag = 0
        for s in samples:
            flag |= (s & 3)  # collects lower 2 bits across samples
        
        # Core formula hidden here
        core_metric = sum(samples) + base
        final_modifier = adjustment ^ flag  # XOR adjustment with bit flag
        
        # Final score calculation
        result = int(core_metric - final_modifier)
        
        # Dead comparison (distractor)
        if result > 1000:
            result //= 2
            
        return result

    return -1

# Execution point of interest
final_score = evaluate_performance(metric_data)

# Irrelevant cleanup
tracker = PerformanceTracker()
for val in raw_inputs:
    tracker.update(val * 0.8)

dummy_sum = sum([prime_offset, len(even_squared), tracker.baseline])  # unused

print(f"Target result: {final_score}")