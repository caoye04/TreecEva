from itertools import compress, count

def analyze_efficiency(values):
    filtered = [v for v in values if v > 0]
    weighted = [(i + 1) * val for i, val in enumerate(filtered)]
    return sum(weighted) / len(weighted) if weighted else 0.0

def aggregate_performance(metrics, offset):
    base_multiplier = 2
    adjustment = 0.0
    temp_results = []
    
    # Real processing with meaningful branches
    for k, v in metrics.items():
        if len(k) % 2 == 0 and v > 0:
            adjustment += 0.5
        elif v < 0:
            adjustment -= 0.2
        temp_results.append(v ** 0.5 if v > 0 else 0)
    
    # Distractor: complex-looking but unused list comprehension
    _ = [x * base_multiplier for x in range(len(temp_results)) if x % 2 == 1]
    
    raw_total = sum(temp_results)
    
    # Simulated early-return pattern (not triggered here)
    if raw_total < 0:
        return -1
    
    final_value = (raw_total + adjustment) * base_multiplier + offset
    return final_value

# Setup data
timestamps = list(count(100, 10))[:8]
signal_data = [-2, 4, 9, -1, 16, 25, 0, 36]

# Irrelevant transformation (distractor)
cleaned = list(compress(signal_data, [x % 20 == 10 for x in timestamps]))

# Relevant mapping
metric_map = {f"task_{i}": signal_data[i] for i in range(len(signal_data))}

base_offset = 10

# Dummy computation to increase cognitive load
noise_level = sum(x for x in signal_data if x < 0) * -1  # This is never used again

intermediate_metric = analyze_efficiency(signal_data)

# Key statement
final_score = aggregate_performance(metric_map, base_offset)

print(f"Result: {final_score}")