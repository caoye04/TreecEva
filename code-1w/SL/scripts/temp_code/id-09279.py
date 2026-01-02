import itertools

# Simulated system metrics from a distributed computing environment
def collect_metrics():
    return {
        'latency_ms': 142,
        'throughput_ops': 893,
        'error_rate': 0.023,
        'cpu_util': 76.4,
        'memory_gb': 18.7,
        'disk_io': 211,
        'network_latency': 43,
        'packet_loss': 0.0012
    }

def calculate_efficiency(latency, throughput, errors):
    # Irrelevant efficiency calculation (dead logic path)
    base = (throughput / (latency + 1)) * (1 - errors)
    bonus = 1.1 if latency < 150 else 0.9
    return base * bonus

def assess_stability(cpu, memory, disk, network):
    # Misleading stability score (not actually used in final logic)
    thresholds = [80, 20, 250, 50]
    values = [cpu, memory, disk, network]
    score = 100
    for v, t in zip(values, thresholds):
        if v > t:
            score -= (v - t) * 0.5
    return max(score, 0)

def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0

def apply_weighting(metrics, weights):
    # Correct but obfuscated path: only specific keys are actually used
    used_keys = ['latency_ms', 'throughput_ops', 'error_rate', 'cpu_util']
    normalized = {}
    ranges = {
        'latency_ms': (50, 200),
        'throughput_ops': (100, 1000),
        'error_rate': (0.0, 0.05),
        'cpu_util': (0.0, 100.0)
    }
    
    for key in used_keys:
        if key in metrics and key in ranges:
            norm_val = normalize(metrics[key], *ranges[key])
            # Invert for desirable traits (lower latency, lower error better)
            if key in ['latency_ms', 'error_rate']:
                norm_val = 1 - norm_val
            normalized[key] = norm_val
    
    # Dead assignment - looks important but unused
    completeness_ratio = len(normalized) / len(ranges)
    
    weighted_sum = 0.0
    for key, weight in weights.items():
        if key in normalized:
            weighted_sum += normalized[key] * weight
    
    return weighted_sum

def recursive_diagnostic(level, accumulator=0):
    # Distractor recursion with no impact on result
    if level <= 0:
        return accumulator
    return recursive_diagnostic(level - 1, accumulator + (level % 3))

def evaluate_performance(metrics, weights):
    # Key function that determines final answer
    temp_vals = []
    for k, v in metrics.items():
        if isinstance(v, (int, float)):
            temp_vals.append(abs(v) ** 0.5)
    
    # Real computation hidden among distractions
    core_weights = {k: w for k, w in weights.items() if k in metrics}
    
    # Actual scoring uses apply_weighting, but it's not obvious due to noise
    raw_score = apply_weighting(metrics, core_weights)
    
    # Final transformation: scale and shift
    final_raw = raw_score * 100  # Convert to percentage-like scale
    
    # Multiple candidate outputs - only one is printed
    debug_info = {
        'stability': assess_stability(metrics['cpu_util'], metrics['memory_gb'], 
                                   metrics['disk_io'], metrics['network_latency']),
        'efficiency': calculate_efficiency(metrics['latency_ms'], metrics['throughput_ops'], 
                                       metrics['error_rate']),
        'recursion_trace': recursive_diagnostic(7)
    }
    
    # Critical red herring: looks like final_score depends on debug_info
    adjustment = 0
    for val in debug_info.values():
        if val > 50:
            adjustment += 1
    
    # But in reality, final_score does NOT depend on adjustment
    final_score = final_raw  # Answer is purely based on weighted normalized metrics
    
    # Unused tuple unpacking - distractor
    _, _, _ = (1, 2, 3) if final_score > 50 else (4, 5, 6)
    
    return final_score

# Main execution flow
if __name__ == "__main__":
    # Collect real data
    system_metrics = collect_metrics()
    
    # Weight configuration (expert-defined priorities)
    importance_weights = {
        'latency_ms': 0.35,
        'throughput_ops': 0.30,
        'error_rate': 0.25,
        'cpu_util': 0.10
    }
    
    # Spurious data structure manipulation
    combinations = list(itertools.combinations(importance_weights.keys(), 2))
    combo_count = len(combinations)
    
    # Dummy dictionary operations
    shadow_copy = {k: v * 1.0 for k, v in importance_weights.items()}
    shadow_copy['placeholder'] = 999
    if 'placeholder' in shadow_copy:
        del shadow_copy['placeholder']
    
    # Another irrelevant conditional expression
    mode_flag = 'high_load' if system_metrics['cpu_util'] > 70 else 'normal'
    load_factor = 1.1 if mode_flag == 'high_load' else 1.0
    
    # This call contains the actual answer path
    final_score = evaluate_performance(system_metrics, importance_weights)
    
    # Print required output
    print(f"Result: {final_score}")