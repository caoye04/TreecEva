from collections import defaultdict
from itertools import combinations

# Simulate sensor data with noise and valid readings
def preprocess_sensor_readings(raw_readings):
    filtered = [x for x in raw_readings if x > 0]
    stats = defaultdict(int)
    
    for val in filtered:
        if val % 2 == 0:
            stats['even'] += 1
        else:
            stats['odd'] += 1
    
    # Irrelevant aggregation
    temp_analysis = []
    for i in range(len(filtered)):
        for j in range(i+1, len(filtered)):
            temp_analysis.append((filtered[i] + filtered[j]) // 2)
    
    # Distractor: unused computation
    peak_moments = []
    for idx, val in enumerate(filtered):
        if val > 50 and idx > 0 and filtered[idx-1] < val:
            peak_moments.append(idx)
    
    return filtered

# Analyze pattern transitions
def count_transitions(data):
    if not data:
        return 0
    
    transitions = 0
    trend = 0
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        new_trend = 1 if diff > 0 else (-1 if diff < 0 else 0)
        
        if trend != 0 and new_trend != 0 and trend != new_trend:
            transitions += 1
        trend = new_trend
    
    # Dead code path (never accessed in practice due to logic)
    if False:
        transitions = max(transitions, len(data) // 10)
    
    return transitions

# Core scoring logic
def calculate_final_score(data):
    base = sum(data)
    transition_penalty = count_transitions(data) * 2
    
    # Bitwise adjustment based on length parity
    size_factor = len(data) ^ 7 if len(data) % 2 else len(data) | 3
    
    # Conditional expression for stability bonus
    stability_bonus = 10 if all(abs(data[i] - data[i-1]) < 15 for i in range(1, len(data))) else -5
    
    # Red herring: complex but unused combinatorial analysis
    combo_risk = 0
    for combo in combinations(data, 3):
        if combo[0] < combo[1] > combo[2]:
            combo_risk += 1
    # This variable is never used

    final_score = base - transition_penalty + stability_bonus + size_factor
    return final_score

# Main execution
raw_sensor_data = [45, 22, 67, 68, 23, 24, 88, 89, 44, 12]
processed_data = preprocess_sensor_readings(raw_sensor_data)
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")