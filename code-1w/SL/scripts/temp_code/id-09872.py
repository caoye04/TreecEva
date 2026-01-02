from collections import defaultdict
import math

# Simulate system benchmark data with multiple metrics
def generate_test_data():
    data = {}
    for i in range(1, 6):
        data[f'test_{i}'] = {
            'latency_ms': [120/i, 89*i, 105 - i*5][i % 3],
            'success': i % 2 == 1,
            'payload_size': 1024 >> i,
            'timestamp': 1623456789 + i * 100
        }
    return data

def analyze_conditions(results):
    # Irrelevant analysis - distractor
    conditions_met = 0
    for k, v in results.items():
        if v['latency_ms'] < 100:
            conditions_met += 1
    return conditions_met

def dummy_transform(x):
    # Dead utility function - misleading
    return (x ** 2 + 3*x) // 2

def calculate_performance(data):
    score = 0
    penalty_factor = 1.0
    temp_log = []
    
    # Real logic begins: aggregate scores based on specific rules
    base_scores = defaultdict(lambda: 50)
    
    for test_id, metrics in data.items():
        latency = metrics['latency_ms']
        success = metrics['success']
        size = metrics['payload_size']
        
        # Primary scoring logic
        if success:
            score += 20
            if latency < 100:
                score += 15
            elif latency < 150:
                score += 5
        else:
            penalty_factor *= 0.9
        
        # Distractor: collect unused intermediate values
        adjusted_latency = latency * (1 + (size / 2048))
        temp_log.append(adjusted_latency)
    
    # Real: apply penalty
    score = int(score * penalty_factor)
    
    # Fake complex transformation - irrelevant
    noise_reduction = lambda x: (x + sum(temp_log) / len(temp_log)) if temp_log else x
    enhanced_score = noise_reduction(score)
    
    # Final computation using only part of the chain
    final_score = score + 10  # Core answer derivation
    
    return final_score

# Main execution flow
dataset = generate_test_data()

# Misleading pre-processing step
total_payload = sum(dataset[k]['payload_size'] for k in dataset)
condition_count = analyze_conditions(dataset)
effective_ratio = total_payload / (condition_count + 1) if condition_count else 0

# Key statement
final_score = calculate_performance(dataset)

print(f"Result: {final_score}")