import math

# Irrelevant helper function (dead code path)
def unused_diagnostic(data):
    return sum(x ** 2 for x in data if x > 0) // len(data) + 7

def analyze_throughput(latency_data, threshold=50):
    # Distractor computation with misleading intermediate result
    adjusted = [x + 10 for x in latency_data if x < 100]
    avg = sum(adjusted) / len(adjusted) if adjusted else 0
    outliers = [x for x in latency_data if x > threshold * 1.5]
    return avg > threshold and len(outliers) < 5

# Unused but plausible-looking configuration
test_profile = {
    'version': '2.1',
    'mode': 'stress',
    'timeout': 300,
    'retries': 3,
    'payload_size': 1024
}

# Core system metrics log with mixed data types
metrics_log = [
    {'type': 'request', 'duration': 45, 'bytes': 256, 'success': True},
    {'type': 'request', 'duration': 52, 'bytes': 512, 'success': True},
    {'type': 'request', 'duration': 61, 'bytes': 128, 'success': False},
    {'type': 'request', 'duration': 48, 'bytes': 384, 'success': True},
    {'type': 'heartbeat', 'interval': 10},  # Irrelevant record type
    {'type': 'request', 'duration': 55, 'bytes': 256, 'success': True}
]

# Benchmark configuration with red herring parameters
benchmark_config = {
    'target_rps': 100,
    'allowed_failure_rate': 0.05,
    'warmup_cycles': 3,
    'cooldown_delay': 0.5,
    'weighting': {
        'latency': 0.6,
        'throughput': 0.3,
        'accuracy': 0.1
    },
    'calibration': lambda x: x * 1.05 if x < 50 else x * 0.95,  # Unused lambda
    'baseline_adjustment': math.log(1 + 0.1 * 50)  # Distractor constant
}

# Auxiliary function that looks important but is only partially used
def compute_efficiency_factor(records):
    durations = [r['duration'] for r in records if r.get('type') == 'request']
    bytes_transferred = [r['bytes'] for r in records if r.get('type') == 'request']
    success_flags = [r['success'] for r in records if r.get('type') == 'request']
    
    avg_duration = sum(durations) / len(durations)
    total_bytes = sum(bytes_transferred)
    success_rate = sum(success_flags) / len(success_flags)
    
    # Real component used later
    base_efficiency = (total_bytes / (avg_duration + 1)) * success_rate
    
    # Dead-end transformations
    penalty = 0
    for d in durations:
        if d > 60:
            penalty += 5
    
    return base_efficiency - penalty  # Only base_efficiency matters

# Main evaluation logic with critical nesting and distractors
def evaluate_performance(log_entries, config):
    request_only = [e for e in log_entries if e.get('type') == 'request']
    
    if not request_only:
        return 0
    
    # Extract key metrics
    durations = [r['duration'] for r in request_only]
    successes = [r['success'] for r in request_only]
    
    avg_latency = sum(durations) / len(durations)
    failure_count = len([s for s in successes if not s])
    failure_rate = failure_count / len(successes)
    
    # Simulated throughput calculation (partially relevant)
    effective_rps = len(request_only) / (sum(durations) / 1000)
    meets_throughput = effective_rps >= config['target_rps'] * 0.8
    
    # Accuracy component
    meets_accuracy = failure_rate <= config['allowed_failure_rate']
    
    # Use dictionary operations and set logic to obscure real path
    criteria_met = set()
    if avg_latency <= 55:
        criteria_met.add('low_latency')
    if meets_throughput:
        criteria_met.add('high_throughput')
    if meets_accuracy:
        criteria_met.add('high_accuracy')
    
    # Weighted scoring — actual answer depends on this
    weights = config['weighting']
    score_components = {
        'latency': 100 * (55 / max(avg_latency, 1)),
        'throughput': 90 if meets_throughput else 60,
        'accuracy': 100 * (1 - failure_rate)
    }
    
    # Final weighted aggregation — this determines the answer
    raw_score = (
        score_components['latency'] * weights['latency'] +
        score_components['throughput'] * weights['throughput'] +
        score_components['accuracy'] * weights['accuracy']
    )
    
    # Apply efficiency factor (only this uses the auxiliary function)
    efficiency = compute_efficiency_factor(request_only)
    scaling_factor = 1 + (efficiency / 1000)  # Minimal impact
    
    # Dead-end conditional with early return that won't trigger
    if 'debug_mode' in config:
        return -1  # Never reached
    
    # Final adjustment using modular arithmetic (distraction)
    checksum = sum(len(str(int(sc))) for sc in score_components.values()) % 7
    
    return int(raw_score + checksum)  # deterministic final score

# Decoy function that looks like it might be called
def generate_report(data):
    return {"status": "skipped", "reason": "evaluation_complete"}

# Key execution point
final_score = evaluate_performance(metrics_log, benchmark_config)

# Output result as required
print(f"Target result: {final_score}")