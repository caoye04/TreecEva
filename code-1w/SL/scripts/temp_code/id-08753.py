from collections import defaultdict, Counter
import math

# Simulated system performance monitoring with irrelevant metrics
def collect_diagnostics():
    diagnostics = defaultdict(lambda: 'N/A')
    diagnostics['cache_misses'] = 217
    diagnostics['thread_count'] = 12
    diagnostics['io_wait'] = 3.4
    diagnostics['thermal_throttle'] = False
    return dict(diagnostics)

def generate_test_sequence(n):
    # Irrelevant recursive sequence generation (Fibonacci-like but unused)
    if n <= 1:
        return n
    seq = [0, 1]
    for i in range(2, n + 1):
        seq.append(seq[i-1] + seq[i-2])
    return seq

def deprecated_normalizer(x):
    # Dead code path - never called
    return (x - min(x)) / (max(x) - min(x))

# Core data transformation pipeline
def preprocess_metrics(raw):
    processed = {}
    scaling_factor = 1.75
    
    # Distractor: complex but unused transformation
    noise_floor = sum([math.sin(i * 0.1) for i in range(10)]) * 0.01
    
    for k, v in raw.items():
        if isinstance(v, int):
            processed[f'{k}_norm'] = v * scaling_factor
        elif isinstance(v, float) and v > 1.0:
            processed[f'{k}_adj'] = v ** 0.9
    return processed

# Misleading performance model (never invoked)
def legacy_evaluation(data):
    score = 0
    for val in data.values():
        if isinstance(val, float):
            score += math.log(abs(val) + 1) * 0.3
    return round(score, 4)

# Real evaluation logic buried among distractions
def calculate_efficiency_ratio(exec_time, cpu_load, memory_usage):
    # Key formula used in final computation
    base = (exec_time ** -0.5) * (cpu_load + 10)
    penalty = memory_usage * 0.015
    return (base - penalty) * 100

def filter_outliers(data_list, threshold=2.0):
    # Unused utility function
    mean_val = sum(data_list) / len(data_list)
    std_val = math.sqrt(sum((x - mean_val) ** 2 for x in data_list) / len(data_list))
    return [x for x in data_list if abs(x - mean_val) <= threshold * std_val]

# Central logic with embedded distractions
def evaluate_performance(metrics, reference):
    temp_results = []
    accumulator = defaultdict(int)
    
    # Red herring: bit manipulation with no effect on result
    magic_key = 0xABC
    for i, val in enumerate(metrics.values()):
        if isinstance(val, (int, float)):
            obfuscated = (hash(str(val)) ^ magic_key) & 0xFFFF
            accumulator['checksum'] += obfuscated % 100
    
    # Irrelevant string processing
    labels = ['sys', 'io', 'proc', 'net', 'vm']
    encoded = ''.join([label[0].upper() for label in labels if len(label) > 2])
    
    # Actual critical computation hidden in list comprehension
    raw_times = [reference['baseline'], reference['peak'], metrics['duration']]
    adjusted_times = [t * 0.95 for t in raw_times if t > 0.1]
    
    # Decoy aggregation
    dummy_agg = sum([len(str(t)) for t in adjusted_times])
    
    efficiency = calculate_efficiency_ratio(
        exec_time = metrics['duration'],
        cpu_load = metrics['cpu_avg'],
        memory_usage = metrics['mem_peak_kb']
    )
    
    # Complex conditional expression with partial relevance
    stability_bonus = 10 if (metrics['errors'] == 0 and 
                            metrics['timeout'] < 5 and 
                            efficiency > 65) else 0
    
    # Distractor: unused lambda and higher-order operation
    transform = lambda x: x ** 2 if x > 50 else x ** 0.5
    hypotheticals = list(map(transform, [efficiency, stability_bonus]))
    
    # Critical intermediate value disguised as part of a counter
    metric_counter = Counter()
    metric_counter['efficiency'] = round(efficiency)
    metric_counter['bonus'] = stability_bonus
    
    # Final computation
    base_score = metric_counter['efficiency'] * 7.3
    final_adjustment = (base_score * 0.12) if metric_counter['bonus'] > 0 else 0
    final_score = int(base_score + final_adjustment + metric_counter['bonus'])
    
    # Output required result
    print(f'Result: {final_score}')
    return final_score

# Simulated input data
if __name__ == '__main__':
    benchmark_data = {
        'baseline': 0.45,
        'peak': 0.82,
        'version': 'v2.1'
    }
    
    system_metrics = {
        'duration': 0.38,
        'cpu_avg': 78,
        'mem_peak_kb': 4250,
        'errors': 0,
        'timeout': 3,
        'retries': 2,
        'timestamp': 1712345678
    }
    
    # Call the key function
    final_score = evaluate_performance(system_metrics, benchmark_data)