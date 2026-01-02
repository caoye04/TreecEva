from collections import defaultdict, Counter

# Simulate system benchmark data with multiple metrics
def generate_synthetic_benchmark():
    data = defaultdict(list)
    for i in range(10):
        data['latency'].append((i + 1) * 3.5)
        data['throughput'].append(100 + (i * 2))
        data['errors'].append(1 if i % 4 == 0 else 0)
    return data

def analyze_stability(metrics):
    # Irrelevant stability analysis (distractor)
    outlier_count = 0
    for val in metrics['latency']:
        if val > 20:
            outlier_count += 1
    return outlier_count > 3

def filter_noisy_runs(raw_data):
    # Remove runs with errors (has real effect)
    clean_data = {key: [] for key in raw_data}
    error_indices = [i for i, e in enumerate(raw_data['errors']) if e == 0]
    
    for key in raw_data:
        clean_data[key] = [raw_data[key][i] for i in error_indices]
    
    # Introduce misleading intermediate
    temp_avg = sum(clean_data['throughput']) / len(clean_data['throughput'])
    adjustment_factor = 1.0 if temp_avg > 105 else 0.9
    
    # Apply adjustment (actually used later)
    adjusted_throughput = [t * adjustment_factor for t in clean_data['throughput']]
    clean_data['throughput'] = adjusted_throughput
    
    # Dead code path (never accessed)
    if False:
        clean_data['latency'] = [x for x in clean_data['latency'] if x < 100]
    
    return clean_data

def compute_efficiency_ratio(proc_times, outputs):
    # Efficiency metric based on harmonic mean concept
    total_time = sum(proc_times)
    total_output = sum(outputs)
    if total_time == 0:
        return 0
    return (2 * total_output * total_time) / (total_output + total_time)

def calculate_performance(benchmark_data):
    # Preprocess and filter
    processed = filter_noisy_runs(benchmark_data)
    
    # Extract relevant time and output metrics
    execution_times = processed['latency']
    throughput_values = processed['throughput']
    
    # Compute composite efficiency (real contribution)
    base_efficiency = compute_efficiency_ratio(execution_times, throughput_values)
    
    # Secondary metric - jitter calculation (distractor)
    jitter = 0.0
    for i in range(1, len(execution_times)):
        jitter += abs(execution_times[i] - execution_times[i-1])
    average_jitter = jitter / (len(execution_times) - 1) if len(execution_times) > 1 else 0
    
    # Red herring: count occurrences of specific pattern (unused)
    cycle_counter = Counter()
    for t in throughput_values:
        bucket = int(t // 10)
        cycle_counter[bucket] += 1
    high_utilization_cycles = sum(count for bucket, count in cycle_counter.items() if bucket >= 11)
    
    # Actual performance score computation
    peak_throughput = max(throughput_values)
    avg_latency = sum(execution_times) / len(execution_times)
    latency_penalty = avg_latency * 0.8
    
    # Final formula combining multiple factors
    raw_score = (base_efficiency * 1.2) + (peak_throughput * 0.5) - latency_penalty
    
    # Normalize using a constant derived from data length (subtle but valid)
    normalization_constant = len(execution_times) + len(throughput_values)
    final_normalized_score = raw_score / (normalization_constant / 15)
    
    # This variable is the actual answer
    final_score = int(round(final_normalized_score))
    
    # Spurious assignment (dead store)
    final_score = final_score + 0  # No-op
    
    return final_score

# Main execution flow
benchmark_data = generate_synthetic_benchmark()
stable_system = analyze_stability(benchmark_data)  # Used to mislead about importance

# Key statement
final_score = calculate_performance(benchmark_data)

print(f"Result: {final_score}")