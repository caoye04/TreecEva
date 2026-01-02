import math

# Simulated system metrics with irrelevant and relevant data
def collect_diagnostics():
    return {
        'cpu_load': 78,
        'memory_usage': 4321,
        'disk_reads': 950,
        'network_latency_ms': 42,
        'packet_loss_rate': 0.003,
        'temperature_c': 67,
        'fan_speed_rpm': 2300,
        'uptime_hours': 127
    }

def collect_behavioral_data():
    return [
        {'action': 'read', 'priority': 1, 'size_kb': 128},
        {'action': 'write', 'priority': 3, 'size_kb': 64},
        {'action': 'read', 'priority': 2, 'size_kb': 256},
        {'action': 'exec', 'priority': 5, 'size_kb': 4},
        {'action': 'read', 'priority': 1, 'size_kb': 512}
    ]

def compute_health_factor(data):
    # Irrelevant health computation
    base = data['cpu_load'] * 0.3
    if data['temperature_c'] > 60:
        base += 12
    if data['memory_usage'] > 4000:
        base += 8
    return min(base, 100)

def extract_patterns(logs):
    # Distractor: processes logs but result not used in final score
    priorities = [entry['priority'] for entry in logs]
    sizes = [entry['size_kb'] for entry in logs]
    avg_priority = sum(priorities) / len(priorities)
    total_bandwidth = sum(sizes)
    critical_actions = sum(1 for p in priorities if p >= 4)
    return {
        'avg_priority': avg_priority,
        'total_bandwidth': total_bandwidth,
        'critical_count': critical_actions,
        'pattern_entropy': math.log(len(priorities)) if priorities else 0
    }

def transform_metrics(raw):
    # Relevant transformation with embedded red herrings
    transformed = {
        'latency_norm': 100 - (raw['network_latency_ms'] * 2),
        'stability': 100 - raw['packet_loss_rate'] * 10000,
        'efficiency': max(0, 100 - raw['cpu_load'] * 0.5),
        'thermal_rating': max(0, 70 - (raw['temperature_c'] - 50)),
        # Following fields look important but are unused in final calculation
        'disk_io_score': max(0, 100 - raw['disk_reads'] // 10),
        'uptime_bonus': min(30, raw['uptime_hours'] // 10)
    }
    return transformed

def calculate_reliability_index(values):
    # Complex but partially irrelevant function
    score = 0
    weights = {'a': 0.4, 'b': 0.3, 'c': 0.2, 'd': 0.1}
    temp_vals = {
        'a': values['latency_norm'],
        'b': values['stability'],
        'c': values['thermal_rating'],
        'd': values.get('disk_io_score', 0)
    }
    for k, v in temp_vals.items():
        score += v * weights[k] * (0.95 if k == 'd' else 1.0)  # slight penalty for disk
    return score * 0.85  # artificial scaling

def adjust_for_efficiency(base, efficiency):
    # Efficiency impacts final score through non-linear adjustment
    if efficiency > 80:
        return base * 1.2
    elif efficiency > 60:
        return base * 1.1
    elif efficiency > 40:
        return base * 1.05
    else:
        return base * 0.9

def apply_curve(corrupted_input, factor=1.05):
    # Misleading function that appears important but is not called in main flow
    acc = 0
    for i in range(8):
        acc += math.sin(i * factor) * 10
    return acc % 100

def generate_weight_map():
    # Returns fixed weights; looks dynamic but is static
    return {
        'reliability': 0.6,
        'efficiency': 0.4
        # Note: 'latency_norm' and others are already folded into reliability
    }

def evaluate_performance(metrics, weight_map):
    reliability = calculate_reliability_index(metrics)
    efficiency = metrics['efficiency']
    adjusted_efficiency = adjust_for_efficiency(efficiency, efficiency)
    
    # Final weighted combination
    final = (
        reliability * weight_map['reliability'] + 
        adjusted_efficiency * weight_map['efficiency']
    )
    
    # Dead code branch - never executed due to logic
    if final < 0:
        final = 0
    elif final > 100:
        # This branch is actually reachable
        final = 97.6  # hard cap override
    
    return final

# --- Main Execution with Distractions ---
if __name__ == "__main__":
    # Collect system data
    diagnostics = collect_diagnostics()
    logs = collect_behavioral_data()
    
    # Extract patterns (unused later - distractor)
    pattern_analysis = extract_patterns(logs)
    
    # Transform metrics for scoring
    processed_metrics = transform_metrics(diagnostics)
    
    # Compute auxiliary health factor (not used in final score)
    health_factor = compute_health_factor(diagnostics)
    
    # Generate static weight map
    weights = generate_weight_map()
    
    # Evaluate overall performance
    final_score = evaluate_performance(processed_metrics, weights)
    
    # Irrelevant lambda - computes something not used
    diagnostic_summary = lambda d: f"CPU:{d['cpu_load']}%, Temp:{d['temperature_c']}C"
    summary_str = diagnostic_summary(diagnostics)
    
    # Output the target result
    print(f"Result: {final_score}")