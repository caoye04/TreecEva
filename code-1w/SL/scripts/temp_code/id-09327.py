import math

# Irrelevant helper function (dead code path)
def analyze_sentiment(text):
    return sum(ord(c) for c in text) % 7

def transform_data(values):
    # Distractor: complex-looking but unused transformation
    shifted = [(v << 2) ^ 0xA for v in values]
    processed = [math.sin(x / 10.0) for x in shifted if x > 5]
    return [round(p * 100) for p in processed]

# Unused bitwise mixer (red herring)
mixer = lambda a, b: (a ^ b) + ((a & b) << 1)

# Real data used in computation
event_log = [12, 15, 22, 8, 43]

# Irrelevant string manipulation block
domain_hint = "perf_analysis_v2"
encoded_hint = ''.join(chr(ord(ch) + (i % 3)) for i, ch in enumerate(domain_hint))

# Core metrics and weights
metrics = {
    'latency': 45,
    'throughput': 88,
    'consistency': 67,
    'reliability': 91
}

weights = {
    'latency': 0.2,
    'throughput': 0.35,
    'consistency': 0.15,
    'reliability': 0.3
}

# Misleading intermediate calculation (not part of final logic)
temp_bias = 0
for k in metrics:
    temp_bias += len(k) % 5

# Decoy aggregate using bit operations (unused)
bit_aggregate = 0
for val in metrics.values():
    bit_aggregate ^= (val & 0xF) << 1

# Conditional branch with plausible but irrelevant adjustment
adjustment_factor = 0.9
if sum(metrics.values()) > 250:
    adjustment_factor = 1.05  # This looks important but isn't used later

# Lambda-based combinator (used in real logic)
combiner = lambda m, w: sum(m[k] * w[k] for k in m)

# Simulated load adjustment (distractor)
load_profile = [x * 0.8 + 2 for x in event_log if x > 10]

# Primary evaluation logic buried among noise
def evaluate_performance(m, w):
    base = combiner(m, w)
    
    # Extra logic layer: penalty for imbalance
    values = list(m.values())
    variance = sum((v - sum(values)/len(values))**2 for v in values) / len(values)
    penalty = math.sqrt(variance) * 0.1
    
    # Hidden offset from string hint (subtle but valid)
    offset = sum(1 for c in domain_hint if c in 'aeiou') * 0.5
    
    result = base - penalty + offset
    
    # Dead code inside function
    if result < 0:
        result = abs(result)
    
    return result

# Unused recursive function (decoy)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)

# Another red herring: matrix-like structure
snapshot_grid = [[i + j for j in range(4)] for i in range(4)]

# Key execution point
final_score = evaluate_performance(metrics, weights)

# Output requirement
print(f"Result: {final_score}")