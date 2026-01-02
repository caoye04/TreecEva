import math

# Simulated system metrics from a distributed computing environment
def collect_metrics():
    raw_data = [
        {'node': 'A', 'load': 85, 'errors': 2, 'uptime': 99.8, 'tasks': 142},
        {'node': 'B', 'load': 63, 'errors': 0, 'uptime': 98.7, 'tasks': 118},
        {'node': 'C', 'load': 91, 'errors': 5, 'uptime': 96.5, 'tasks': 135},
        {'node': 'D', 'load': 72, 'errors': 1, 'uptime': 99.2, 'tasks': 127}
    ]
    return raw_data

# Irrelevant helper: computes geometric mean (not used in final logic)
def geometric_mean(vals):
    product = 1
    for v in vals:
        product *= v
    return product ** (1 / len(vals))

# Noise function: generates unused statistical summaries
def generate_summary_stats(data_list):
    total_load = sum(d['load'] for d in data_list)
    avg_errors = sum(d['errors'] for d in data_list) / len(data_list)
    min_uptime = min(d['uptime'] for d in data_list)
    max_tasks = max(d['tasks'] for d in data_list)
    
    # Dead code path - never accessed
    if False:
        return {
            'total_load': total_load,
            'avg_errors': round(avg_errors, 2),
            'min_uptime': min_uptime,
            'max_tasks': max_tasks
        }
    return None

# Decoy scoring function that looks important but is unused
def legacy_score(node):
    score = 0
    score += node['load'] * 0.3
    score -= node['errors'] * 10
    score += node['uptime'] * 0.5
    return int(score)

# Core processing: extract key performance indicators
def extract_kpis(metrics):
    kpi_list = []
    for entry in metrics:
        efficiency = entry['tasks'] / (entry['load'] + 1)
        reliability = entry['uptime'] - entry['errors'] * 2.5
        kpi_list.append({
            'node': entry['node'],
            'efficiency': round(efficiency, 2),
            'reliability': round(reliability, 2)
        })
    return kpi_list

# Set-based filtering: identify high-performing nodes using set operations
def filter_elite_nodes(kpi_data):
    all_nodes = {item['node'] for item in kpi_data}
    efficient_nodes = {item['node'] for item in kpi_data if item['efficiency'] > 1.7}
    reliable_nodes = {item['node'] for item in kpi_data if item['reliability'] > 90}
    
    # Intersection identifies elite nodes meeting both criteria
    elite_candidates = efficient_nodes & reliable_nodes
    
    # Red herring: symmetric difference (unused)
    outlier_group = efficient_nodes ^ reliable_nodes
    if len(outlier_group) > 2:
        pass  # Dead logic branch
    
    return elite_candidates

# Auxiliary transformation: character frequency analysis on node IDs (distractor)
def analyze_node_labels(node_set):
    label_text = ''.join(sorted(node_set))
    freq_map = {}
    for char in label_text:
        freq_map[char] = freq_map.get(char, 0) + 1
    # Returns something irrelevant
    return sum(freq_map.values())

# Central evaluation logic with multiple steps
def evaluate_performance(metric_set, benchmark_data):
    # Step 1: Extract KPIs from raw metrics
    kpis = extract_kpis(metric_set)
    
    # Step 2: Filter elite nodes using set intersection
    elite_nodes = filter_elite_nodes(kpis)
    
    # Step 3: Compute aggregate efficiency (only for elite nodes)
    total_efficiency = 0
    for item in kpis:
        if item['node'] in elite_nodes:
            total_efficiency += item['efficiency']
    
    # Step 4: Apply benchmark multiplier based on size
    base_multiplier = len(elite_nodes) or 1
    adjusted_benchmark = benchmark_data * 1.5 if base_multiplier >= 2 else benchmark_data * 0.8
    
    # Step 5: Calculate entropy-like penalty for non-uniform distribution
    raw_efficiencies = [item['efficiency'] for item in kpis]
    mean_eff = sum(raw_efficiencies) / len(raw_efficiencies)
    variance = sum((e - mean_eff) ** 2 for e in raw_efficiencies) / len(raw_efficiencies)
    stability_penalty = math.sqrt(variance) * 10
    
    # Step 6: Combine components into final score
    raw_score = total_efficiency * adjusted_benchmark
    penalized_score = raw_score - stability_penalty * 5
    
    # Step 7: Final adjustment using character count red herring
    dummy_count = analyze_node_labels(elite_nodes)
    final_adjustment = dummy_count * 0.1  # Minor influence to maintain plausible deniability
    
    # Critical statement
    final_score = int(penalized_score + final_adjustment)
    
    # Debug print (simulates logging, not part of output)
    # print(f'Debug: final_score={final_score}')
    return final_score

# Orchestration block
if __name__ == '__main__':
    metrics = collect_metrics()
    baseline_ref = 42  # Benchmark anchor
    metric_set = metrics
    benchmark_data = baseline_ref
    
    # Key execution point
    final_score = evaluate_performance(metric_set, benchmark_data)
    
    print(f"Result: {final_score}")