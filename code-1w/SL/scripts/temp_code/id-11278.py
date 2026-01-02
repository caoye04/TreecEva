import math

# Irrelevant helper function (dead code path)
def unused_diagnostic_check(data):
    return sum(x ** 2 for x in data if x > 0) % 7

# Misleading performance estimator (not actually used in final calculation)
def legacy_metric(v):
    accumulator = 0
    for i in range(len(v)):
        accumulator += v[i] * (0.9 ** i)
    return accumulator * 1.5

# Core system variables
default_weights = [0.1, 0.2, 0.3, 0.4]
scaling_factor = 2.718
temp_buffer = [0] * 10

# Simulated telemetry stream (distractor data)
telemetry_log = [
    {'time': 1, 'value': 100, 'flag': False},
    {'time': 2, 'value': 105, 'flag': True},
    {'time': 3, 'value': 103, 'flag': False}
]

# Actual processing begins here
raw_inputs = [8, 12, 16, 20, 24]

# Irrelevant transformation chain
shifted_values = [x + 5 for x in raw_inputs]
filtered_shifted = [y for y in shifted_values if y % 2 == 0]
decoy_aggregate = sum(filtered_shifted) // len(filtered_shifted)

# Real data pipeline
base_metrics = list(map(lambda x: math.sqrt(x * 2), raw_inputs))  # [4, ~4.899, ~5.657, ~6.325, ~6.928]

# Set operations to mask real logic
unique_bases = set(base_metrics)
adjusted_bases = unique_bases.union({scaling_factor})
purged_bases = adjusted_bases.difference({min(adjusted_bases)})

# Slicing distraction
windowed_slice = base_metrics[1:4]  # middle three elements
rolling_avg = sum(windowed_slice) / len(windowed_slice)

# Critical data structure
benchmark_data = {
    'readings': raw_inputs,
    'derived': base_metrics,
    'size': len(raw_inputs)
}

# Complex conditional mask with red herring logic
if len(purged_bases) > 3 and rolling_avg > 5.0:
    activation_flag = 1
else:
    activation_flag = 0

# Unused but plausible-looking aggregator
class PerformanceEstimator:
    def __init__(self, factor):
        self.factor = factor
    
    def compute(self, vals):
        return sum(vals) * self.factor  # never instantiated

# Decoy assignment
placeholder_result = None
for item in telemetry_log:
    if item['flag']:
        placeholder_result = item['value'] * 2

# Real control flow with nested conditions
def evaluate_performance(metrics_set, dataset):
    readings = dataset['readings']
    derived = dataset['derived']
    n = dataset['size']
    
    # Key computation buried in conditionals
    if n >= 4:
        subset = derived[::2]  # slicing every other element
        processed = [math.floor(x) for x in subset]  # [4, 5, 6]
        
        # Bit manipulation to obscure arithmetic
        bitmasked_sum = 0
        for val in processed:
            bitmasked_sum += val ^ 3  # XOR with 3
        
        # Logical combination with activation flag
        temp_result = bitmasked_sum * activation_flag  # still uses outer scope
        
        # Final adjustment using modular arithmetic
        checksum = sum(readings[:3]) % 11  # (8+12+16)=36 % 11 = 3
        final = temp_result + checksum  # ( (4^3)+(5^3)+(6^3) ) + 3 = (7+6+5)+3 = 21
        
        # Red herring: this line looks important but doesn't affect output
        final = final if final > 10 else -1 * final
        
        return final
    
    return -999

# Auxiliary state tracker (irrelevant)
current_state = {
    'stage': 'initialized',
    'counter': 42
}

# Trigger execution
metric_set = {"mode": "enhanced", "level": 3}
final_score = evaluate_performance(metric_set, benchmark_data)

print(f"Result: {final_score}")