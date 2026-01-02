from collections import defaultdict

# Simulated system performance metrics with noise data
def get_raw_metrics():
    return {
        'latency_ms': 120,
        'throughput_ops': 850,
        'error_rate': 0.004,
        'memory_usage_mb': 470,
        'cpu_utilization': 0.78,
        'queue_depth': 23,
        'timeout_count': 5,
        'retry_attempts': 12
    }

# Irrelevant decoy function - looks important but unused
def analyze_quantum_efficiency(qubits):
    total = 0
    for i in range(len(qubits)):
        total += qubits[i] * (i + 1) % 7
    return total // 3

# Distractor data - quantum-inspired but irrelevant
decoherence_data = [3, 7, 1, 8, 2, 9, 5]
noise_floor = sum([x**2 for x in decoherence_data if x % 2 == 1])

# Benchmark weight configuration (real)
benchmark_weights = {
    'latency_ms': 0.25,
    'throughput_ops': 0.30,
    'error_rate': 0.20,
    'memory_usage_mb': 0.15,
    'stability_factor': 0.10  # derived, not raw
}

# Fake transformation path - dead end
legacy_mapping = defaultdict(lambda: 0)
for k, v in get_raw_metrics().items():
    legacy_mapping[f"old_{k}"] = v * 0.95

# Red herring computation chain
phantom_score = 0
for i in range(1, 10):
    phantom_score += (i * noise_floor) % 17
phantom_score = (phantom_score + 99) // 10  # misleading intermediate result

# Stability factor calculation (used later)
def calculate_stability(cpu, errors, retries):
    transient = retries / (errors * 100) if errors > 0 else 0.0
    return (1 - cpu) * 100 - transient

# Core evaluation logic
def normalize_latency(latency):
    return max(0, 100 - (latency / 2))

def normalize_throughput(tput):
    return min(100, tput / 10)

def normalize_error_rate(err):
    return max(0, 100 - (err * 10000))

def normalize_memory(mem):
    return max(20, 100 - (mem / 5))

def evaluate_performance(metrics, weights):
    # Extract relevant values
    lat = metrics['latency_ms']
    tput = metrics['throughput_ops']
    err = metrics['error_rate']
    mem = metrics['memory_usage_mb']
    cpu = metrics['cpu_utilization']
    
    # Compute derived metric
    stability = calculate_stability(cpu, metrics['timeout_count'], metrics['retry_attempts'])
    
    # Normalize all components to 0-100 scale
    n_lat = normalize_latency(lat)
    n_tput = normalize_throughput(tput)
    n_err = normalize_error_rate(err)
    n_mem = normalize_memory(mem)
    n_stab = max(0, min(100, stability))  # clamp to range
    
    # Debug inspection (distractor output - looks important)
    diagnostics = {
        'component_health': [
            'latency_ok' if n_lat > 60 else 'latency_degraded',
            'tput_ok' if n_tput > 60 else 'tput_degraded'
        ],
        'priority_flags': ['high_load']
    }
    
    # Spurious secondary weighting (unused)
    alternative_weights = {k: w * 1.1 for k, w in weights.items()}
    alt_result = 0
    for comp in alternative_weights:
        alt_result += 1  # meaningless accumulation
    
    # Final weighted score calculation (ACTUAL ANSWER PATH)
    final_score = (
        n_lat * weights['latency_ms'] +
        n_tput * weights['throughput_ops'] +
        n_err * weights['error_rate'] +
        n_mem * weights['memory_usage_mb'] +
        n_stab * weights['stability_factor']
    )
    
    # Additional distraction: update diagnostics with phantom
    diagnostics['phantom_baseline'] = phantom_score
    
    return round(final_score, 4)

# Main execution flow
raw_data = get_raw_metrics()

# Dead code branch - never reached but looks like error handling
if raw_data.get('unknown_flag', False):
    fallback_weights = {k: 0.1 for k in raw_data}
    exit(1)

# Actual computation
final_score = evaluate_performance(raw_data, benchmark_weights)

# Output required result
print(f"Target result: {final_score}")