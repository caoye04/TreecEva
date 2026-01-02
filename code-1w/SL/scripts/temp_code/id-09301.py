def analyze_trends(data, threshold=0.5):
    trends = []
    for i, value in enumerate(data):
        if value > threshold:
            trends.append((i, value * 1.2))
        elif value < -threshold:
            trends.append((i, value * 0.8))
        else:
            trends.append((i, value))
    return trends

# Irrelevant helper (distractor)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v] if norm else v

# Unused function (dead code path)
def calculate_entropy(values):
    from math import log
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    return -sum(p * log(p) for p in probabilities)

# Core logic disguised among noise
def evaluate_performance(metrics, weights):
    adjusted = []
    temp_offset = 0
    
    # Bit manipulation red herring
    magic_key = 0b101010
    scramble = lambda x: (x ^ magic_key) + 1
    
    for idx, (metric, weight) in enumerate(zip(metrics, weights)):
        if idx % 2 == 0:
            # Apply artificial distortion (only some matter)
            processed = abs(metric) ** 0.5 * weight
            if processed > 3.0:
                processed -= scramble(int(processed // 2)) % 7  # Decoy adjustment
        else:
            processed = metric * weight + temp_offset
            temp_offset += 0.1  # Distracting accumulation
        
        # Only this condition contributes to final result
        if idx == len(metrics) - 1:
            processed = metric * weight * 2.5  # Critical operation
        
        adjusted.append(processed)
    
    # Real answer depends only on last element calculation
    base_result = sum(adjusted)
    
    # Fake complexity with dictionaries and irrelevant transformations
    stats = {
        'raw': metrics,
        'weighted': weights,
        'interim': adjusted,
        'count': len([x for x in adjusted if x > 0]),
        'peak': max(adjusted) if adjusted else 0
    }
    
    # Additional decoy logic
    if stats['count'] > 2:
        stats['bonus'] = stats['peak'] * 0.1
    else:
        stats['penalty'] = -1.5
    
    # Final score is actually just based on fixed transformation of base_result
    final_score = int(base_result * 100) / 100.0  # Truncate to 2 decimals
    return final_score

# Misleading data setup
dummy_data = [-2.1, 0.3, 1.8, -0.4, 2.2]
trend_analysis = analyze_trends(dummy_data, 0.6)

# Vector normalization distraction (unused)
noise_vector = [1.0, 2.0, 3.0]
normalized = normalize_vector(noise_vector)

# Actual input (hidden among noise)
metrics = [4.0, -1.5, 3.2, 0.8, 5.0]
weights = [0.1, 0.2, 0.3, 0.4, 0.5]

# The key statement
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")