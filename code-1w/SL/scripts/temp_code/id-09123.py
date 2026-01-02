import math

# Simulated system metrics for a distributed computing task
def collect_metrics(node_count, load_factor):
    raw_data = {}
    for i in range(node_count):
        cpu_load = (i * 7 + load_factor) % 13
        mem_usage = (i * 11 + load_factor * 2) % 17
        net_latency = abs((cpu_load - mem_usage) * 1.5)
        raw_data[f'node_{i}'] = {
            'cpu': cpu_load,
            'memory': mem_usage,
            'latency': net_latency,
            'active': cpu_load < 10 and mem_usage < 12
        }
    return raw_data

# Irrelevant auxiliary function - dead code path
def calculate_checksum(data_dict):
    checksum = 0
    for key, val in data_dict.items():
        if isinstance(val, dict):
            for v in val.values():
                if isinstance(v, int):
                    checksum ^= v
    return checksum

# Data transformation pipeline
def normalize_metrics(raw):
    normalized = {}
    max_cpu = max(entry['cpu'] for entry in raw.values())
    max_mem = max(entry['memory'] for entry in raw.values())
    max_lat = max(entry['latency'] for entry in raw.values())

    for node_id, metrics in raw.items():
        norm_cpu = metrics['cpu'] / max_cpu if max_cpu > 0 else 0
        norm_mem = metrics['memory'] / max_mem if max_mem > 0 else 0
        norm_lat = metrics['latency'] / max_lat if max_lat > 0 else 0
        isActive = metrics['active']

        # Decoy computation - looks important but unused
        efficiency_score = (norm_cpu * 0.6 + norm_mem * 0.3) / (norm_lat + 0.1)
        
        normalized[node_id] = {
            'n_cpu': round(norm_cpu, 4),
            'n_mem': round(norm_mem, 4),
            'n_lat': round(norm_lat, 4),
            'flag': isActive
        }
    
    # More red herring variables
    summary_stats = {
        'nodes': len(normalized),
        'avg_lat': sum(v['n_lat'] for v in normalized.values()) / len(normalized),
        'healthy_nodes': sum(1 for v in normalized.values() if v['flag'])
    }
    
    return normalized, summary_stats

# Weight configuration (some entries are irrelevant)
def get_weights(strategy='balanced'):
    all_weights = {
        'balanced': {'w_cpu': 0.4, 'w_mem': 0.3, 'w_lat': 0.3, 'w_dummy1': 0.0, 'w_extra': 0.0},
        'performance': {'w_cpu': 0.5, 'w_mem': 0.2, 'w_lat': 0.3, 'w_dummy1': 0.0, 'w_extra': 0.0},
        'efficiency': {'w_cpu': 0.3, 'w_mem': 0.4, 'w_lat': 0.3, 'w_dummy1': 0.0, 'w_extra': 0.0}
    }
    return all_weights[strategy]

# Core evaluation logic
def evaluate_performance(metrics_log, weights):
    composite_scores = []
    
    # Intermediate decoy accumulator
    temp_aggregate = {'sum_sq': 0.0, 'count_valid': 0}
    
    for node_id, data in metrics_log.items():
        n_cpu = data['n_cpu']
        n_mem = data['n_mem']
        n_lat = data['n_lat']
        
        # Actual scoring formula used
        score = n_cpu * weights['w_cpu'] + n_mem * weights['w_mem'] + (1 - n_lat) * weights['w_lat']
        
        # Distractor calculation - looks like it contributes but doesn't
        squared_term = score ** 2
        temp_aggregate['sum_sq'] += squared_term
        temp_aggregate['count_valid'] += 1 if score > 0.5 else 0
        
        composite_scores.append(score)
    
    # Final result computed deterministically
    base_avg = sum(composite_scores) / len(composite_scores) if composite_scores else 0
    
    # Additional misleading transformation (unused)
    adjusted = base_avg * (1 + 0.1 * math.sin(len(composite_scores)))
    
    # Critical point: final_score derived here
    final_score = round(base_avg * 10000)  # Scale for integer output
    
    # Irrelevant print statements (simulating debugging noise)
    # print(f'Debug: temp_aggregate={temp_aggregate}')
    # print(f'Debug: adjusted_score={adjusted}')
    
    return final_score

# Unused utility - distractor
def generate_report(nodes, score):
    return f"System Report:\nNodes: {nodes}\nScore: {score:.2f}\nStatus: OK"

# Main execution flow
if __name__ == '__main__':
    # Initialize parameters
    num_nodes = 8
    current_load = 5
    
    # Step 1: Collect raw metrics
    raw_metrics = collect_metrics(num_nodes, current_load)
    
    # Step 2: Normalize and extract stats (summary_stats is not used later)
    processed_metrics, summary_stats = normalize_metrics(raw_metrics)
    
    # Step 3: Retrieve weighting scheme
    config_weights = get_weights('balanced')
    
    # Step 4: Evaluate overall performance
    final_score = evaluate_performance(processed_metrics, config_weights)
    
    # Output target result
    print(f"Result: {final_score}")