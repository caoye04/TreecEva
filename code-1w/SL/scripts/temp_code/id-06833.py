from itertools import combinations
from math import log, sin

# Simulated system metrics from a distributed sensor network
def collect_telemetry():
    return {
        'latency_ms': [12.5, 14.2, 13.1, 16.8, 9.7],
        'packet_loss': [0.002, 0.003, 0.001, 0.004, 0.002],
        'throughput_mbps': [842, 796, 889, 763, 912],
        'jitter_ms': [0.8, 1.1, 0.7, 1.3, 0.9]
    }

def calculate_entropy(data):
    # Irrelevant entropy calculation (dead-end function)
    total = sum(data)
    probs = [x / total for x in data]
    return -sum(p * log(p) for p in probs if p > 0)

def apply_noise_filter(signal, threshold=0.5):
    # Distractor: signal processing that isn't used in final path
    return [x for x in signal if abs(x - sum(signal)/len(signal)) < threshold]

def generate_combinations(values):
    # Creates red herring combinations not used in main logic
    return list(combinations(values, 3))

def validate_checksum(data_dict):
    # Misleading validation that computes but doesn't affect final result
    checksum = 0
    for key, values in data_dict.items():
        for v in values:
            checksum ^= int(v * 100)
    return checksum % 17 == 0

def normalize_metrics(raw):
    # Relevant: Normalize metrics to 0-1 scale
    normalized = {}
    normalized['latency'] = 1 - (sum(raw['latency_ms']) / len(raw['latency_ms'])) / 20
    normalized['loss'] = 1 - max(raw['packet_loss'])
    normalized['throughput'] = sum(raw['throughput_mbps']) / len(raw['throughput_mbps']) / 1000
    normalized['jitter'] = 1 - (sum(raw['jitter_ms']) / len(raw['jitter_ms'])) / 2
    return normalized

def compute_diagnostic_flag(metrics):
    # Dead-end diagnostic logic
    if metrics['latency'] < 0.6 and metrics['jitter'] < 0.8:
        return 0b1010
    elif metrics['loss'] > 0.99:
        return 0b1100
    else:
        return 0b0011

def evaluate_resilience(latency_vals, loss_vals):
    # Complex-looking but unused resilience score
    paired = zip(latency_vals, loss_vals)
    score = 0.0
    for lat, loss in paired:
        score += (1 / (1 + lat)) * (1 - loss)
    return score * 10

def evaluate_performance(weights, raw_data):
    # Core function with relevant logic buried in distractions
    norm_metrics = normalize_metrics(raw_data)
    
    # Spurious intermediate calculations
    temp_a = sin(norm_metrics['latency']) * 100
    temp_b = log(1 + norm_metrics['throughput'] * 100)
    
    # Actual scoring logic
    base_score = 0.0
    base_score += norm_metrics['latency'] * weights.get('latency', 0.25)
    base_score += norm_metrics['loss'] * weights.get('loss', 0.20)
    base_score += norm_metrics['throughput'] * weights.get('throughput', 0.35)
    base_score += norm_metrics['jitter'] * weights.get('jitter', 0.20)
    
    # Final adjustment - only this matters
    final_adjustment = base_score * 1000
    
    # Decoy return paths
    if final_adjustment < 0:
        return int(final_adjustment) ^ 0xFF
    elif final_adjustment > 900:
        return int(final_adjustment) >> 2
    else:
        return int(final_adjustment)  # This is the actual path taken

# Irrelevant data structures
ERROR_CODES = {102: 'Timeout', 205: 'HandshakeFail', 301: 'AuthReject'}
DEPLOY_CONFIGS = [
    {'region': 'us-east', 'nodes': 8},
    {'region': 'eu-west', 'nodes': 6}
]

# Unused transformation pipeline
pipeline_stages = ['ingest', 'filter', 'enrich', 'encode', 'transmit']
stage_weights = {stage: 1 + i*0.1 for i, stage in enumerate(pipeline_stages)}

# Main execution flow
if __name__ == '__main__':
    # Collect real data
    telemetry_data = collect_telemetry()
    
    # Generate irrelevant combinatorial analysis
    latency_triplets = generate_combinations(telemetry_data['latency_ms'])
    loss_combos = generate_combinations(telemetry_data['packet_loss'])
    
    # Compute meaningless checksum (distractor)
    is_valid = validate_checksum(telemetry_data)
    
    # Prepare metric weights - only this dictionary matters
    metric_weights = {
        'latency': 0.25,
        'loss': 0.20,
        'throughput': 0.35,
        'jitter': 0.20
    }
    
    # Apply fake noise filter on irrelevant copy
    filtered_jitter = apply_noise_filter(telemetry_data['jitter_ms'], threshold=1.0)
    
    # Compute unused resilience metric
    resilience_score = evaluate_resilience(
        telemetry_data['latency_ms'],
        telemetry_data['packet_loss']
    )
    
    # Diagnostic flag not used
    diag_flag = compute_diagnostic_flag(normalize_metrics(telemetry_data))
    
    # Critical statement: this determines the answer
    final_score = evaluate_performance(metric_weights, telemetry_data)
    
    # Print result as required
    print(f"Target result: {final_score}")