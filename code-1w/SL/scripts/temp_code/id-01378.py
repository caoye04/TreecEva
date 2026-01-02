from collections import defaultdict

# Simulate system benchmark data with multiple metrics
def generate_synthetic_benchmark():
    data = defaultdict(list)
    for i in range(1, 6):
        data['latency'].append(100 // i)
        data['throughput'].append(i * 15)
        data['errors'].append(5 - i if i < 5 else 0)
    return data

def analyze_stability(metrics):
    # Irrelevant analysis path - distractor
    stability_log = []
    for val in metrics['latency']:
        if val < 50:
            stability_log.append(True)
    return len(stability_log) > 2

def compute_efficiency_ratio(data):
    # Semi-relevant computation - not used in final score but looks important
    total_throughput = sum(data['throughput'])
    total_latency = sum(data['latency'])
    if total_latency == 0:
        return 0
    return round(total_throughput / total_latency, 4)

def calculate_performance(benchmark):
    # Core logic begins
    base_score = 0
    adjustment_factor = 0
    
    # Process each iteration metric
    for i in range(len(benchmark['latency'])):
        latency = benchmark['latency'][i]
        throughput = benchmark['throughput'][i]
        error_count = benchmark['errors'][i]
        
        # Primary scoring mechanism
        if latency < 80 and error_count == 0:
            base_score += throughput * 0.8
        elif latency < 100:
            base_score += throughput * 0.5
        else:
            base_score += throughput * 0.2
        
        # Adjustment logic (only applies in specific case)
        if i % 2 == 0 and throughput > 20:
            adjustment_factor += 1
    
    # Misleading dead-end: this block never triggers due to data structure
    temp_offset = 0
    for err in benchmark['errors']:
        if err > 10:  # Never true
            temp_offset += err
    
    # Final calculation uses only base_score and adjustment_factor
    final_raw = base_score + (adjustment_factor * 5)
    
    # Normalize to prevent overflow (distractor comment)
    # No actual normalization needed
    return int(final_raw)

# Main execution flow
benchmark_data = generate_synthetic_benchmark()

# Perform auxiliary analyses (distractors)
diagnostic_flag = analyze_stability(benchmark_data)
efficiency_metric = compute_efficiency_ratio(benchmark_data)

# Key statement
final_score = calculate_performance(benchmark_data)

# Print result as required
print(f"Result: {final_score}")