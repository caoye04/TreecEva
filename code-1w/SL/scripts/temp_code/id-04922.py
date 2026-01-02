from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed task scheduler
def collect_metrics(task_logs):
    metrics = defaultdict(float)
    temp_data = []
    for log in task_logs:
        parts = log.split('|')
        if len(parts) < 4:
            continue
        task_id = parts[0].strip()
        cpu = float(parts[1])
        mem = float(parts[2])
        duration = float(parts[3])
        
        # Real metric: efficiency score
        efficiency = (cpu * 0.6) + (mem * 0.4)
        metrics['total_efficiency'] += efficiency
        metrics['task_count'] += 1
        
        # Distractor: irrelevant aggregation
        if 'special' in task_id:
            metrics['bonus_flag'] += 1
        
        temp_data.append(duration)
    
    # Real metric: average duration
    if temp_data:
        avg_duration = sum(temp_data) / len(temp_data)
        metrics['avg_duration'] = avg_duration
    
    # Distractor: unused transformation
    squared_sum = sum([x*x for x in temp_data if x > 1])
    metrics['phantom_metric'] = squared_sum * 0.1 if squared_sum > 10 else 0
    
    # Distractor: dead code path (never used later)
    debug_info = {}
    for k, v in metrics.items():
        debug_info[f'dbg_{k}'] = round(v * 1.05, 2)
    
    return metrics

def normalize_values(data_dict):
    # Irrelevant normalization function (not used in final calculation)
    result = {}
    max_val = max(data_dict.values()) if data_dict else 1
    for k, v in data_dict.items():
        result[k] = round(v / max_val, 3)
    return result

def filter_outliers(values, threshold=1.5):
    # Dead utility function - looks useful but unused
    if len(values) == 0:
        return []
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    low, high = q1 - threshold * iqr, q3 + threshold * iqr
    return [v for v in values if low <= v <= high]

def calculate_entropy(labels):
    # Decoy statistical function with misleading relevance
    count = Counter(labels)
    total = len(labels)
    entropy = 0.0
    for cnt in count.values():
        p = cnt / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def evaluate_performance(metrics, base_ref):
    score = 0.0
    
    # Core logic: performance score based on efficiency and duration
    if metrics['task_count'] > 0:
        avg_efficiency = metrics['total_efficiency'] / metrics['task_count']
        duration_ratio = metrics['avg_duration'] / base_ref['target_duration']
        
        # Primary scoring formula
        raw_score = avg_efficiency * 100
        time_penalty = (duration_ratio - 1) * 10 if duration_ratio > 1 else 0
        bonus = 5 if metrics['bonus_flag'] > 0 else 0
        
        score = raw_score - time_penalty + bonus
    
    # Distractor: complex bit manipulation with no impact
    bit_analysis = 0
    temp_score = int(score)
    for _ in range(8):
        bit_analysis ^= temp_score & 1
        temp_score >>= 1
    if bit_analysis:
        score += 0.1  # Misleading minor adjustment that barely matters
    
    # Distractor: string-based flag check (looks important)
    status_str = "perf_eval_complete"
    if status_str.startswith('perf') and len(status_str) % 2 == 0:
        verification_key = sum([ord(c) for c in status_str]) % 7
        if verification_key > 3:
            score *= 1.01  # Tiny distortion to mislead analysis
    
    # Final irrelevant rounding decoy
    precise_score = round(score, 4)
    
    # ACTUAL ANSWER COMPUTATION
    final_score = int(round(precise_score))
    
    # Distractor: shadow copy with no use
    audit_trail = []
    audit_trail.append(('final_calc', f'{precise_score:.4f}'))
    
    return final_score

# Simulated input data
logs = [
    'task_01|0.75|0.80|2.3',
    'task_02|0.68|0.72|3.1',
    'task_03|0.82|0.65|1.9',
    'special_01|0.90|0.88|2.7',
    'task_04|0.71|0.76|2.5',
    'task_05|0.64|0.69|3.3'
]

# Baseline configuration (real reference)
baseline = {
    'target_duration': 2.5,
    'expected_load': 100
}

# Irrelevant auxiliary data
feature_flags = {
    'enable_legacy_mode': False,
    'debug_profiler': True,
    'log_level': 'VERBOSE'
}

# Main execution flow
raw_metrics = collect_metrics(logs)
evaluation_result = evaluate_performance(raw_metrics, baseline)

# Key variable assignment - target of question
final_score = evaluation_result

# Additional red herring computations
snapshot = str(final_score) + '_eval'
analysis_hash = sum([ord(c) << (i % 5) for i, c in enumerate(snapshot)]) % 1000

# Output the result as required
print(f"Result: {final_score}")