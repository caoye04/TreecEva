import math

# Irrelevant constants and decoy variables
temperature_offset = 273.15
data_buffer = [0] * 100
scaling_factor = 1.8
log_table = {i: round(math.log(i), 4) for i in range(1, 21)}

# Real input data structures
production_data = [
    (500, 'A', 'Q1'), (700, 'B', 'Q1'), (600, 'A', 'Q2'),
    (800, 'C', 'Q2'), (900, 'B', 'Q3'), (400, 'D', 'Q4')
]
efficiency_map = {'A': 0.85, 'B': 0.78, 'C': 0.92, 'D': 0.65}

# Decoy function - never called
def calculate_entropy(data):
    total = sum(data)
    probs = [x / total for x in data]
    return -sum(p * math.log2(p) for p in probs if p > 0)

# Unused transformation
reversed_map = {v: k for k, v in efficiency_map.items()}

# Distractor list comprehension with side effects (but no real impact)
buffer_analysis = [x for x in data_buffer if x > 50]

# Real processing logic buried in distractions
def preprocess_records(raw_data):
    # Extract valid entries based on category and quarter
    filtered = [entry for entry in raw_data if entry[1] in efficiency_map]
    stats = {}
    for amount, category, quarter in filtered:
        if category not in stats:
            stats[category] = []
        stats[category].append(amount)
    
    # Compute geometric mean per category (relevant)
    geometric_means = {}
    for cat, values in stats.items():
        product = 1
        for v in values:
            product *= v
        geometric_means[cat] = product ** (1 / len(values))
    
    return geometric_means

# Another decoy function with misleading name
def assess_volatility(series):
    mean_val = sum(series) / len(series)
    variance = sum((x - mean_val) ** 2 for x in series) / len(series)
    return math.sqrt(variance) / mean_val if mean_val != 0 else 0

# Core function that computes the final result
def harvest_results(data, efficiency):
    base_stats = preprocess_records(data)
    
    # Irrelevant aggregation
    total_entries = len(data)
    unique_categories = len(set(cat for _, cat, _ in data))
    score_metric = total_entries * unique_categories / 10.0
    
    # Real computation path
    weighted_sum = 0
    total_efficiency_weight = 0
    
    for category, base_value in base_stats.items():
        if category in efficiency:
            weight = efficiency[category]
            # Apply diminishing returns using logarithmic scale
            adjusted = base_value * math.log(1 + weight * 10)
            weighted_sum += adjusted
            total_efficiency_weight += weight
    
    # Dead code path - unreachable due to logic
    if False and total_efficiency_weight == 0:
        fallback = 0
        for val in base_stats.values():
            fallback += val * 0.1
        return fallback
    
    # Final calculation
    aggregate_index = weighted_sum / (total_efficiency_weight or 1)
    
    # Additional distraction: complex but unused bitwise operation
    magic_key = 0
    for c in "harvest":
        magic_key ^= ord(c) << 2
    
    # Final adjustment based on index size
    final_output = int(aggregate_index) + (score_metric % 7)
    
    return final_output

# Misleading pre-execution
interim_test = [assess_volatility([100, 200, 300]), assess_volatility([50, 150])]  # Unused

# Critical execution point
final_yield = harvest_results(production_data, efficiency_map)

# Output the required result
print(f"Target result: {final_yield}")