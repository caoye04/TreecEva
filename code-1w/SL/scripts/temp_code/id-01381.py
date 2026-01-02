def evaluate_performance(data, config):
    # Normalize metrics using lambda for dynamic scaling
    normalizer = lambda x, base: round(x / (base + 1e-5), 4)
    normalized = [normalizer(val, sum(data)) for val in data]

    # Apply weight transformation with modular arithmetic twist
    transformed_weights = [(w ** 2) % 7 for w in config]

    # Misleading intermediate: entropy calculation (not used in final score)
    import math
    shannon_entropy = 0
    for n in normalized:
        if n > 0:
            shannon_entropy -= n * math.log(n)
    shannon_entropy = round(shannon_entropy, 4)

    # Track cumulative product for no reason (dead computation)
    cumprod = 1
    for n in normalized:
        cumprod *= max(n, 0.1)
        if cumprod > 100:
            cumprod = 1  # reset condition (never triggers)

    # Core logic: weighted harmonic mean with filtering
    filtered_pairs = [(n, w) for n, w in zip(normalized, transformed_weights) if n > 0.05]
    if not filtered_pairs:
        return 0
    
    harmonic_sum = 0
    total_weight = 0
    for n, w in filtered_pairs:
        harmonic_sum += w / n
        total_weight += w
    
    if harmonic_sum == 0:
        return 0
    
    # Final performance metric
    raw_score = total_weight / harmonic_sum
    
    # Additional irrelevant smoothing
    smoothed = raw_score
    for _ in range(2):
        smoothed = (smoothed + raw_score * 1.1) / 2.1
    
    return round(smoothed, 4)

# Main execution block
metrics = [85, 90, 78, 92, 88]
weights = [3, 4, 2, 5, 4]

# Preprocessing distraction: reverse mapping (unused)
metric_map = {i: m for i, m in enumerate(metrics)}
inverse_lookup = [metric_map[i] for i in sorted(metric_map.keys(), reverse=True)]

# Secondary distractor: string-based weight encoding (irrelevant)
token_weights = ''.join([chr(97 + w) for w in weights])
split_tokens = token_weights.split('b')
joined_token = ''.join(split_tokens)

# Data reshaping that goes nowhere
reshaped = [[metrics[i], weights[i]] for i in range(len(metrics))]
doubled_reshaped = [row * 2 for row in reshaped][:3]  # truncated and unused

# Critical statement
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")