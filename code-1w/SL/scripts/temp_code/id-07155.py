from itertools import combinations

def analyze_trends(data, mode):
    trend_scores = []
    for i in range(2, len(data) + 1):
        for group in combinations(data, i):
            if mode == 'sum':
                trend_scores.append(sum(group))
            elif mode == 'xor':
                result = 0
                for x in group:
                    result ^= x
                trend_scores.append(result)
    return max(trend_scores) if trend_scores else 0

# Simulate sensor readings over time
readings = [3, 7, 4, 8]
noise_floor = 2
adjusted_readings = [x - noise_floor for x in readings if x > noise_floor]

# Extract statistical features
mean_val = sum(readings) / len(readings)
peak = max(readings)
valid_count = len([x for x in readings if x > mean_val])

# Secondary analysis with irrelevant transformations
transformed = []
for x in readings:
    temp = (x ** 2) >> 1
    if temp % 3 == 0:
        transformed.append(temp)
dummy_aggregate = sum(transformed) // len(transformed) if transformed else 0

# Core evaluation logic
metrics = {
    'base': sum(adjusted_readings),
    'trend': analyze_trends(adjusted_readings, 'xor'),
    'stability': len(readings) - len(adjusted_readings),
    'bonus': 5 if valid_count >= 2 else 0
}

threshold = 10
def evaluate_performance(m, thresh):
    score = 0
    if m['base'] > thresh:
        score += m['base']
    if m['trend'] > 0:
        score += m['trend'] * 2
    if m['stability'] == 0:
        score += 10
    score += m['bonus']
    
    # Distractor: complex adjustment not affecting final logic
    adjustment_chain = 1
    for i in range(3):
        adjustment_chain = (adjustment_chain * 2) + 1
    unused_penalty = adjustment_chain if m['stability'] > 1 else 0
    
    return score

final_score = evaluate_performance(metrics, threshold)
print(f"Target result: {final_score}")