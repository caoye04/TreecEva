import math

# Simulated system metrics over time
def collect_metrics():
    timestamps = list(range(10))
    cpu_load = [0.65, 0.72, 0.83, 0.77, 0.69, 0.74, 0.80, 0.85, 0.78, 0.70]
    memory_usage = [0.55, 0.60, 0.70, 0.75, 0.68, 0.64, 0.72, 0.78, 0.74, 0.66]
    disk_io = [120, 135, 110, 145, 130, 125, 140, 150, 132, 128]
    network_latency = [45, 52, 60, 55, 48, 50, 58, 62, 54, 49]
    
    # Irrelevant metric (distractor)
    irrelevant_temp_data = [23.4, 24.1, 22.8, 25.0, 23.9, 24.5, 26.1, 25.8, 24.7, 23.6]
    
    metrics_log = []
    for t in timestamps:
        entry = {
            'time': t,
            'cpu': cpu_load[t],
            'memory': memory_usage[t],
            'disk': disk_io[t],
            'latency': network_latency[t],
            'temp': irrelevant_temp_data[t]  # Red herring
        }
        metrics_log.append(entry)
    
    return metrics_log

# Unused function - dead code path (distractor)
def analyze_temperature(data_log):
    avg_temp = sum(entry['temp'] for entry in data_log) / len(data_log)
    risk_level = 'high' if avg_temp > 24.5 else 'normal'
    return risk_level

# Secondary helper with misleading intermediate (distractor)
def calculate_efficiency_index(logs):
    efficiency_scores = []
    for record in logs:
        raw_score = (record['cpu'] * 0.4 + record['memory'] * 0.3 + 
                    (1000 / record['latency']) * 0.001 * 0.3)
        # This transformation is unused later (red herring)
        normalized = 1 / (1 + math.exp(-raw_score))
        efficiency_scores.append(normalized)
    
    # Returns unused statistic
    return sum(efficiency_scores) / len(efficiency_scores)

# Core evaluation logic
def evaluate_stability(logs):
    spike_count = 0
    for i in range(1, len(logs)):
        cpu_change = abs(logs[i]['cpu'] - logs[i-1]['cpu'])
        if cpu_change > 0.1:
            spike_count += 1
    return spike_count < 3  # Stable if fewer than 3 spikes

# Key computation with dictionary operations and linear search
def find_baseline_reference(logs, key_metric='cpu'):
    baseline_ref = None
    for record in logs:
        if record['time'] == 5:  # Midpoint reference
            baseline_ref = record[key_metric]
            break
    return baseline_ref

# Main scoring with multiple concepts
def evaluate_performance(logs, threshold):
    # Extract baseline CPU at time=5
    base_cpu = find_baseline_reference(logs, 'cpu')
    base_mem = find_baseline_reference(logs, 'memory')
    
    # Compute averages (some used, some not)
    avg_cpu = sum(r['cpu'] for r in logs) / len(logs)
    avg_mem = sum(r['memory'] for r in logs) / len(logs)
    total_disk = sum(r['disk'] for r in logs)
    
    # Linear search for first high-latency occurrence (distractor)
    first_high_latency = None
    for r in logs:
        if r['latency'] > 60:
            first_high_latency = r['time']
            break  # Never triggered in this data
    
    # Stability check
    is_stable = evaluate_stability(logs)
    
    # Performance score components
    cpu_ratio = avg_cpu / base_cpu
    mem_ratio = avg_mem / base_mem
    
    # Primary decision logic
    base_score = 100.0
    if cpu_ratio > threshold:
        base_score -= 25
    if mem_ratio > 1.1:
        base_score -= 15
    if not is_stable:
        base_score -= 30
    
    # Complex adjustment using dictionary lookup and bit manipulation (distractor section)
    adjustments = {'low': -10, 'medium': 0, 'high': 10}
    load_category = 'medium'
    if avg_cpu > 0.75:
        load_category = 'high'
    elif avg_cpu < 0.6:
        load_category = 'low'
    
    # Bitwise red herring (irrelevant to final score)
    category_flag = 0b1000
    if load_category == 'high':
        category_flag |= 0b0110
    else:
        category_flag ^= 0b0011
    masked_flag = category_flag & 0b1101
    
    # Final score is NOT affected by flag, only by base_score
    final_score = int(base_score + adjustments[load_category])
    
    # Additional unused transformation (distractor)
    max_disk_period = 0
    current_sum = 0
    for i, r in enumerate(logs):
        current_sum += r['disk']
        if (i+1) % 3 == 0 or i == len(logs)-1:
            if current_sum > max_disk_period:
                max_disk_period = current_sum
            current_sum = 0
    
    return final_score

# Execution flow
def main():
    # Collect system metrics
    metrics_log = collect_metrics()
    
    # Baseline threshold for performance evaluation
    baseline_threshold = 1.05
    
    # Evaluate overall performance
    final_score = evaluate_performance(metrics_log, baseline_threshold)
    
    # Print result
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()