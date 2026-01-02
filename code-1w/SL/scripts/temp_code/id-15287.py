from itertools import compress, cycle

# Simulate sensor data validation and weighted performance scoring
def analyze_readings(readings):
    valid_mask = [r > 0 and r % 2 == 1 for r in readings]  # Only odd positive values are valid
    filtered = list(compress(readings, valid_mask))
    adjusted = [r * 1.1 if r < 50 else r * 0.95 for r in filtered]
    baseline = sum(adjusted) / len(adjusted) if adjusted else 0
    
    # Distractor: irrelevant trend analysis
    trends = []
    for i in range(1, len(readings)):
        if readings[i] > readings[i-1]:
            trends.append(1)
        elif readings[i] < readings[i-1]:
            trends.append(-1)
    avg_trend = sum(trends) / len(trends) if trends else 0

    return baseline, len(filtered)

def calculate_stability(indices):
    diffs = [abs(indices[i+1] - indices[i]) for i in range(len(indices)-1)]
    stability = 1 / (sum(diffs) / len(diffs) + 1) if diffs else 1
    return stability

# Main processing pipeline
def evaluate_performance(metrics, weights):
    base_value = metrics['baseline']
    count = metrics['count']
    stability = metrics['stability']
    
    # Irrelevant intermediate computation
    temp_factor = 0
    for w in weights:
        temp_factor += w ** 2
    temp_factor = temp_factor ** 0.5 if temp_factor > 1 else 1
    
    # Core logic: weighted composite score
    raw_score = base_value * weights[0]
    raw_score += count * weights[1] * 100
    raw_score += stability * weights[2] * 50
    
    # Normalization using slicing of hypothetical history
    history = [raw_score - i*5 for i in range(10)]
    recent = history[-3:]  # Last three simulated past scores
    final_adjustment = sum(recent) / len(recent)
    
    final_score = raw_score * 0.8 + final_adjustment * 0.2
    
    # Dead code branch (never executed due to constant condition)
    if False:
        fallback = sum(history[:5])
        final_score = fallback
    
    return final_score

# Input data
sensor_data = [45, -10, 67, 22, 81, 0, 13, 94, 33, 76]
indices = [1, 3, 4, 6, 8]

# Extract features
base, count = analyze_readings(sensor_data)
stability = calculate_stability(indices)

# Compile metrics
dummy_padding = [0] * 5  # Unused padding
metrics = {
    'baseline': base,
    'count': count,
    'stability': stability,
    'extra': dummy_padding  # Irrelevant field
}
weights = [0.6, 0.3, 0.1]

# Critical execution point
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")