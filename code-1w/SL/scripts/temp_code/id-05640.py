import math

# Simulated system diagnostics (irrelevant data)
def analyze_diagnostics(logs):
    error_count = sum(1 for log in logs if 'ERROR' in log)
    warning_count = sum(1 for log in logs if 'WARN' in log)
    health_status = 'OK' if error_count == 0 else 'CRITICAL'
    return {'errors': error_count, 'warnings': warning_count, 'status': health_status}

diag_logs = ['INFO: startup', 'DEBUG: module init', 'ERROR: timeout', 'WARN: deprecated call']
system_health = analyze_diagnostics(diag_logs)

# Data preprocessing pipeline (partially relevant, contains red herrings)
def preprocess_data(raw_input):
    cleaned = [x.strip().lower() for x in raw_input if isinstance(x, str)]
    tokenized = [word for text in cleaned for word in text.split()]
    freq_map = {}
    for word in tokenized:
        freq_map[word] = freq_map.get(word, 0) + 1
    
    # Distractor: N-gram generation (not used later)
    ngrams = [' '.join(tokenized[i:i+2]) for i in range(len(tokenized)-1)]
    vocabulary_size = len(set(tokenized))
    
    return {
        'tokens': tokenized,
        'frequency': freq_map,
        'vocab_size': vocabulary_size,
        'ngrams': ngrams  # Dead field
    }

raw_data = ['  Optimization Complete ', 'Memory Usage High', 'Optimization Complete']
processed = preprocess_data(raw_data)

# Benchmark configuration with decoy parameters
benchmark_config = {
    'version': '2.1-alpha',
    'active': True,
    'thresholds': {
        'latency_ms': 150,
        'throughput_min': 1000,
        'accuracy_target': 0.95
    },
    'scoring_weights': {
        'efficiency': 0.4,
        'consistency': 0.3,
        'rare_impact': 0.2,  # Not actually used
        'baseline_adjustment': 0.1
    },
    'flags': ['validate', 'log_trace'],
    'temp_override': False  # Unused
}

# Core metric calculator (contains key logic amid distractions)
def compute_efficiency_metric(records):
    total_ops = 0
    idle_cycles = 0
    peak_memory = 0
    memory_snapshots = []
    
    for record in records:
        op_count = record.get('ops', 0)
        mem_usage = record.get('memory', 0)
        is_active = record.get('active', True)
        
        if is_active:
            total_ops += op_count
        else:
            idle_cycles += op_count  # Misleading: idle cycles don't contribute
        
        memory_snapshots.append(mem_usage)
        
    if memory_snapshots:
        peak_memory = max(memory_snapshots)
    
    avg_memory = sum(memory_snapshots) / len(memory_snapshots) if memory_snapshots else 0
    
    # Efficiency formula (only this part matters)
    efficiency = (total_ops / (peak_memory + 1)) * 100 if peak_memory > 0 else 0
    
    # Distractor: unused derived metrics
    stability_score = (min(memory_snapshots) / max(memory_snapshots)) if memory_snapshots else 0
    
    return {
        'efficiency': efficiency,
        'total_ops': total_ops,
        'idle_cycles': idle_cycles,
        'peak_memory': peak_memory,
        'avg_memory': avg_memory,
        'stability_score': stability_score  # Red herring
    }

# Simulated performance records (mixed relevance)
performance_records = [
    {'ops': 120, 'memory': 40, 'active': True},
    {'ops': 150, 'memory': 60, 'active': True},
    {'ops': 80, 'memory': 100, 'active': True},
    {'ops': 200, 'memory': 85, 'active': True}
]

efficiency_metrics = compute_efficiency_metric(performance_records)

# Log structure for evaluation (key input)
metrics_log = [
    {'type': 'runtime', 'value': 235.0},
    {'type': 'efficiency', 'value': efficiency_metrics['efficiency']},
    {'type': 'consistency', 'value': processed['vocab_size'] * 10},
    {'type': 'baseline', 'value': 85.0}
]

# Advanced scoring engine with multiple layers and distractions
def evaluate_performance(log, config):
    # Extract weights (only efficiency and consistency are used)
    weights = config['scoring_weights']
    
    # Build score map using dictionary comprehension and slicing
    score_map = {entry['type']: entry['value'] for entry in log}
    
    # Irrelevant transformation chain
    transformed_scores = {
        k: v * 1.05 if k == 'runtime' else v * 0.95 for k, v in score_map.items()
    }
    
    # Decoy normalization (not applied to final result)
    max_val = max(transformed_scores.values()) if transformed_scores else 1
n    normalized = {k: v / max_val for k, v in transformed_scores.items()}
    
    # Critical calculation path
    base_efficiency = score_map.get('efficiency', 0)
    consistency_bonus = score_map.get('consistency', 0)
    baseline_ref = score_map.get('baseline', 0)
    
    # Apply actual weights (only two are relevant)
    weighted_efficiency = base_efficiency * weights['efficiency']
    weighted_consistency = consistency_bonus * weights['consistency']
    baseline_component = baseline_ref * weights['baseline_adjustment']
    
    # Final aggregation
    raw_score = weighted_efficiency + weighted_consistency + baseline_component
    
    # Artificial cap (not triggered here)
    capped_score = min(raw_score, 100.0)
    
    # Distractor: hypothetical adjustment using lambda (never called)
    apply_penalty = lambda x, p: x * (1 - p) if x > 90 else x
    
    # Real answer computed here
    return raw_score

# Execute main evaluation
evaluation_result = evaluate_performance(metrics_log, benchmark_config)

# Secondary analysis (dead code path)
def generate_audit_trace(result):
    trace = []
    if result > 90:
        trace.append('PERFORMANCE_EXCELLENT')
    elif result > 70:
        trace.append('PERFORMANCE_ACCEPTABLE')
    else:
        trace.append('PERFORMANCE_LOW')
    return '|'.join(trace)

audit_flag = generate_audit_trace(evaluation_result)  # Unused

# Key variable assignment
final_score = evaluation_result

# Print result as required
print(f"Result: {final_score}")