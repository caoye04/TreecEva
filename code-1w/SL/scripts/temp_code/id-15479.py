from collections import defaultdict, Counter

# Simulated system metrics with irrelevant and relevant data
def collect_metrics():
    raw_data = [150, 200, 175, 180, 210]
    extra_logs = [0.1, 0.3, 0.5, 0.7]  # Distractor: not used
    status_flags = {'active': True, 'debug': False, 'mode': 'prod'}
    
    metrics = defaultdict(float)
    metrics['latency'] = sum(raw_data) / len(raw_data)
    metrics['throughput'] = raw_data[-1] * 1.5
    metrics['errors'] = 0
    metrics['retries'] = 3  # Red herring: used in decoy function

    # Irrelevant transformations
    temp_result = [x ** 0.5 for x in raw_data if x > 160]
    adjustment_factor = len(temp_result) * 0.2  # Not actually used

    return metrics

# Decoy function with dead logic
def calculate_health(data):
    if data.get('errors', 0) > 5:
        return -1
    elif data.get('retries', 0) > 2:
        return data['retries'] * 10  # Looks important but unused
    return 100

# Real evaluation logic
def apply_weight(x, w):
    return x * w

def recursive_transform(val, depth=0):
    if depth >= 3:
        return val
    return recursive_transform((val + 10) * 0.9, depth + 1)

def evaluate_performance(metrics, weights):
    score = 0.0
    components = []
    
    # Key calculation branch
    if metrics['latency'] < 185:
        components.append(apply_weight(metrics['throughput'], weights['perf']))
        
        # Nested conditional red herring
        temp_debug = metrics['retries'] > 1
        debug_boost = 5 if temp_debug else 0  # Unused boost
        
        base_error_penalty = 0
        if metrics['errors'] == 0:
            base_error_penalty -= 15
        
        # Critical distractor block — looks like it modifies score but doesn't
        shadow_score = 0
        for i in range(2):
            for j in range(2):
                shadow_score += (i + j) * 10
        # End of irrelevant nested loop
        
        # Actual score accumulation
        score += recursive_transform(components[0])
        score += base_error_penalty
        
        # Another decoy: uses list comprehension but result discarded
        _ = [x * 2 for x in [score, score + 10] if x < 0]  # Dead path
    
    # Final adjustments using correct logic
    adjustment = weights['stability'] * (1 if metrics['errors'] == 0 else 0.5)
    score *= adjustment
    
    # Irrelevant final check
    if score > 1000:
        print('Optimal performance detected')  # Never reached
    
    return int(score)

# Main execution with mixed concerns
def main():
    # Unused counters
    log_counter = Counter(['init', 'load', 'run', 'run', 'save'])
    phase_weights = {'init': 1, 'run': 2}  # Distractor

    metrics = collect_metrics()
    
    # Weight configuration — only these two keys matter
    weights = {
        'perf': 1.2,
        'stability': 0.8,
        'availability': 1.0,  # Unused
        'bandwidth': 0.5     # Unused
    }
    
    # Dummy variable to mislead
    temp_output = calculate_health(metrics)  # Called but result ignored
    
    # Critical statement
    final_score = evaluate_performance(metrics, weights)
    
    # Print required output
    print(f"Result: {final_score}")
    
    return final_score

# Execute
main()