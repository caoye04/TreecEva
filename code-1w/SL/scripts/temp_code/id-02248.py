import itertools

# System for evaluating algorithmic trading strategy performance with distractions
def simulate_market_conditions(days):
    trend = [1.0 + i * 0.001 for i in range(days)]
    noise = [0.01 * (i % 5 - 2) for i in range(days)]
    return [t + n for t, n in zip(trend, noise)]

# Irrelevant helper: computes factorial (not used in final calculation)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Distractor function: looks important but unused
def compute_volatility(prices):
    mean_price = sum(prices) / len(prices)
    variance = sum((p - mean_price) ** 2 for p in prices) / len(prices)
    return variance ** 0.5

# Another red herring: dead code path
INVALID_CODES = {x: factorial(x % 7) for x in range(100) if x % 11 == 0}

# Core logic disguised among noise
def normalize(values):
    min_val, max_val = min(values), max(values)
    if max_val == min_val:
        return [0.5] * len(values)
    return [(v - min_val) / (max_val - min_val) for v in values]

# Misleading intermediate transformation
def apply_risk_filter(metrics, threshold=0.7):
    return [m for m in metrics if m > threshold]  # Unused later

# Key function buried in abstractions
def evaluate_strategy_health(metrics):
    sorted_metrics = sorted(metrics, reverse=True)
    top_quartile = sorted_metrics[:len(sorted_metrics)//4]
    return sum(top_quartile) / len(top_quartile)

# Real computation chain
raw_data = [3, 7, 1, 9, 2, 8, 4]
shifted_data = [x << 1 for x in raw_data]  # Bit shift: doubles values
filtered_data = [x for x in shifted_data if x > 10]  # Keep only large values

# Create decoy variables
baseline = sum(raw_data) / len(raw_data)
deviation_map = {i: abs(v - baseline) for i, v in enumerate(raw_data)}
scaling_factor = 2.718  # Looks scientific, not critical

# Primary evaluation pipeline
metric_weights = [0.4, 0.3, 0.2, 0.1]
raw_outcomes = [
    sum(filtered_data) % 17,                    # Modular arithmetic
    len(list(itertools.combinations(raw_data, 3))) % 13,  # Combinatorics via itertools
    (sum(shifted_data[::2]) - sum(shifted_data[1::2])) % 11,  # Slicing + diff
    len([x for x in deviation_map.values() if x > 2])         # Count filtered
]

# Normalize outcomes using min-max scaling
normalized_outcomes = normalize(raw_outcomes)

# Apply weighted scoring - actual answer determined here
def evaluate_performance(weights, outcomes):
    # Conditional expression mix
    adjusted_weights = [w if o > 0.5 else w * 0.5 for w, o in zip(weights, outcomes)]
    total_weight = sum(adjusted_weights)
    
    # Ensure no division by zero
    if total_weight == 0:
        return 0.0
        
    # Final weighted average
    score = sum(w * o for w, o in zip(adjusted_weights, outcomes)) / total_weight
    
    # Additional transformation that doesn't change outcome due to data properties
    final_adjustment = score * (1 + 0.0 ** len([x for x in weights if x > 0.25]))
    return final_adjustment

# Dead code: looks like post-processing but unused
def aggregate_results(results_list):
    return [evaluate_strategy_health(r) for r in results_list]

# Irrelevant data structure manipulation
cyclic_buffer = [0]*5
for i in range(12):
    cyclic_buffer[i % 5] += i * 2

# Critical execution point
final_score = evaluate_performance(metric_weights, normalized_outcomes)

# Print result as required
print(f"Target result: {final_score}")