from collections import defaultdict, Counter

def analyze_efficiency(logs):
    efficiency_map = defaultdict(int)
    temp_counter = Counter()
    
    for entry in logs:
        level = entry.get('level', 1)
        duration = entry.get('duration', 0)
        category = entry.get('cat', 'unknown')
        
        if duration <= 0:
            continue
            
        efficiency_map[category] += duration * level
        temp_counter[category] += 1

    adjusted = {k: v / (temp_counter[k] + 1) for k, v in efficiency_map.items()}
    return sum(adjusted.values())


def compute_stress_factor(inputs):
    # Irrelevant helper that computes something not directly used
    total_xor = 0
    for val in inputs:
        total_xor ^= int(val % 7)
    return total_xor * 1.5


def evaluate_performance(metrics, risk_flag):
    base = 0
    modifier = 1.0
    
    if risk_flag > 3:
        modifier = 0.8
    elif risk_flag < 0:
        modifier = 1.2
    else:
        modifier = 1.0

    for val in metrics:
        if val < 0:
            base += val ** 2
        else:
            base += int(val) | 3  # bitwise OR with constant
    
    intermediate_result = base * modifier
    
    # Distractor computation
    shadow_accum = 0
    for i in range(5):
        shadow_accum += (intermediate_result - i) % 4
    
    final_score = int(intermediate_result + 0.5)
    
    # Dead code path (never reached due to logic)
    if False and shadow_accum > 1000:
        final_score -= 100
        
    return final_score

# Main execution block
log_data = [
    {'level': 2, 'duration': 10, 'cat': 'network'},
    {'level': 3, 'duration': 5, 'cat': 'io'},
    {'level': 1, 'duration': 8, 'cat': 'network'},
    {'level': 4, 'duration': 12, 'cat': 'cpu'},
    {'level': 2, 'duration': 0, 'cat': 'memory'},  # skipped due to duration=0
]

productivity = [4.2, -1.5, 6.8, 3.1, -2.0]
risk_levels = [5, 1, 3, 4, 2]
risk_factor = len([r for r in risk_levels if r >= 3])

# Unused but plausible-looking data structure
summary_stats = {
    'avg_risk': sum(risk_levels) / len(risk_levels),
    'peak': max(risk_levels),
    'flagged': any(r > 4 for r in risk_levels)
}

# Trigger analysis (not used in final score)
analysis_result = analyze_efficiency(log_data)
stress_test = compute_stress_factor([12, 14, 19, 22])

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")