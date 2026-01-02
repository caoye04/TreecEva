def analyze_component(x, threshold=5):
    if x < threshold:
        return x * 1.5
    else:
        return x * 0.9

# Simulate sensor readings with noise filtering
temp_readings = [3, 7, 4, 9, 2]
corrected = []
for val in temp_readings:
    adjusted = val + 0.1
    normalized = adjusted * 0.98
    corrected.append(normalized)

# Irrelevant transformation (distractor)
distorted = [x ** 0.5 for x in corrected if x > 5]

# Core data for evaluation
benchmark_data = [5, 8, 6, 7, 4, 9]

# Weighted contribution calculation with conditional scaling
weights = []
for i, val in enumerate(benchmark_data):
    weight = 1.1 if i % 2 == 0 else 0.9
    scaled = val * weight
    weights.append(scaled)

# Secondary derived metric (semi-relevant)
accumulated = 0
for idx, (raw, w) in enumerate(zip(benchmark_data, weights)):
    accumulated += abs(raw - w) * 0.5

# Noise margin adjustment (dead code path - distractor)
margin_tracker = 0
for _ in range(3):
    margin_tracker += 0.05
    if margin_tracker > 1:
        break

# Main performance model
def calculate_performance(data):
    base_total = sum(data)
    bonus = 0
    penalty = 0
    
    # Apply component-wise analysis
    for item in data:
        analyzed = analyze_component(item)
        if analyzed > 6:
            bonus += 1.5
        else:
            penalty += 0.8
    
    # Conditional adjustment using modular arithmetic
    if len(data) % 3 == 0:
        adjustment = bonus * 1.2
    else:
        adjustment = penalty * 0.7

    # Final composition with summation and accumulation
    raw_score = base_total + bonus - penalty
    final_adjustment = adjustment if raw_score > 30 else -adjustment
    
    # Key execution point
    final_score = raw_score + final_adjustment
    
    # Extra unused tracking (distractor)
    stats_summary = {
        'count': len(data),
        'peak': max(data),
        'bonus_applied': bonus,
        'penalty_incurred': penalty
    }
    
    return int(final_score)

# Execute main logic
result_value = calculate_performance(benchmark_data)
final_score = result_value
print(f"Target result: {final_score}")