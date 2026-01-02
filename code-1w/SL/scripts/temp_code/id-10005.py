import math

# Irrelevant helper function (dead code path)
def analyze_bandwidth(data):
    return sum(x * 0.1 for x in data if x > 50)

# Misleading performance indicator (distractor)
class LegacySystem:
    def __init__(self):
        self.score = 999
        self.active = False

legacy = LegacySystem()

# Real computation begins here
baseline = {
    'latency': 40,
    'throughput': 250,
    'error_rate': 0.05,
    'jitter': 8
}

metrics = [
    {'latency': 35, 'throughput': 275, 'error_rate': 0.03, 'jitter': 6},
    {'latency': 45, 'throughput': 240, 'error_rate': 0.07, 'jitter': 10},
    {'latency': 38, 'throughput': 260, 'error_rate': 0.04, 'jitter': 7}
]

# Decoy metric transformation (irrelevant)
transformed = [{k: v * 1.1 if k == 'throughput' else v for k, v in m.items()} for m in metrics]

# Unused intermediate result (misleading)
avg_latency = sum(m['latency'] for m in metrics) / len(metrics)

# Bit manipulation red herring (no effect on final result)
flag = 0b101010
flag ^= 0b111111
flag &= ~0b100000

# Conditional decoy with short-circuit evaluation
is_optimal = legacy.active and legacy.score > 500 or False

# Core logic: compute geometric mean of normalized improvements
def normalize_reading(val, base, invert=False):
    ratio = val / base
    return 1 / ratio if invert else ratio

# Actual relevant processing
improvements = []
for reading in metrics:
    latency_norm = normalize_reading(reading['latency'], baseline['latency'], invert=True)
    throughput_norm = normalize_reading(reading['throughput'], baseline['throughput'])
    error_norm = normalize_reading(reading['error_rate'], baseline['error_rate'], invert=True)
    jitter_norm = normalize_reading(reading['jitter'], baseline['jitter'], invert=True)
    
    # Composite improvement score per reading
    composite = (latency_norm + throughput_norm + error_norm + jitter_norm) / 4
    improvements.append(composite)

# Use list comprehension to filter noise (valid use)
effective_improvements = [imp for imp in improvements if imp >= 0.95]

# Set operation as distractor (unused)
unique_improvements = set(round(x, 3) for x in improvements)

# Dictionary-based weighting (red herring)
weights = {i: w for i, w in enumerate([1.0, 0.85, 1.1])}  # Not actually used

# Final evaluation using harmonic mean (key reasoning step)
def evaluate_performance(imps, _):
    n = len(imps)
    reciprocal_sum = sum(1 / x for x in imps)
    return n / reciprocal_sum

# Critical execution point
final_score = evaluate_performance(improvements, baseline)

# Output the target result
print(f"Target result: {final_score}")