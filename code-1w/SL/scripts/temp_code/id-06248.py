from collections import defaultdict
import math

# Simulate system benchmark data with multiple metrics
def generate_test_data():
    data = defaultdict(list)
    for i in range(1, 6):
        data['latency'].append(100 * math.exp(-i / 3) + 5 * i)
        data['throughput'].append(200 - 8 * (i - 1)**1.5)
        data['errors'].append(max(0, 15 - 3 * i))
    return data

def analyze_stability(logs):
    # Irrelevant helper function - distractor
    stability = 0
    for val in logs['latency']:
        stability += math.sin(val / 50) ** 2
    return round(stability, 2)

def calculate_performance(metrics):
    size_factor = len(metrics['latency'])
    base_latency_score = sum([1000 / (1 + lat) for lat in metrics['latency']])
    throughput_bonus = sum([t / 10 for t in metrics['throughput'] if t > 100])
    
    # Conditional expression for adaptive scaling
    scale = 1.5 if sum(metrics['throughput']) > 700 else 1.2
    
    reliability_penalty = 0
    total_errors = sum(metrics['errors'])
    if total_errors > 0:
        reliability_penalty = 10 * math.log(total_errors + 1)
    
    # Dummy computations - misleading intermediate values
    dummy_aggr = 0
    temp_vals = []
    for i in range(len(metrics['latency'])):
        dummy_val = metrics['latency'][i] * metrics['throughput'][i]
        temp_vals.append(dummy_val / (i + 1))
        dummy_aggr += dummy_val
    
    # Unused lambda - red herring
    adjust = lambda x: x * 0.95 if x > 50 else x * 1.05
    
    # Core logic hidden among distractions
    raw_score = (base_latency_score + throughput_bonus) * scale - reliability_penalty
    
    # Additional irrelevant normalization
    max_possible = 1200 * scale
    normalized = raw_score / max_possible if max_possible > 0 else 0
    
    # Final score computed here — this is the key line
    final_score = int(raw_score - 50 * normalized)
    
    return final_score

# Main execution flow
test_run = True
if test_run:
    benchmark_data = generate_test_data()
    
    # Distractor: unused analysis
    stability_index = analyze_stability(benchmark_data)
    
    # Key statement: this determines the answer
    final_score = calculate_performance(benchmark_data)
    
    # Print result in required format
    print(f"Result: {final_score}")