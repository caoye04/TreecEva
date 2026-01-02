import math

# Simulated system telemetry and performance metrics
technical_metrics = {
    'latency_ms': [120, 85, 93, 110, 98],
    'bandwidth_mbps': [480, 510, 495, 520, 475],
    'cpu_load': [78, 82, 75, 88, 80],
    'memory_mb': [3200, 3350, 3100, 3400, 3250]
}

# User experience survey results (irrelevant for final score but looks important)
survey_data = {
    'satisfaction': [4.2, 4.5, 4.0, 4.7, 4.3],
    'usability': [4.1, 4.6, 4.2, 4.8, 4.4],
    'interface_rating': [4.3, 4.4, 4.1, 4.5, 4.2]
}

# Legacy system thresholds (distractor data)
thresholds_v1 = {
    'critical_latency': 150,
    'max_cpu': 95,
    'min_bandwidth': 400
}

# Weights for current scoring model
weights = {'latency': 0.35, 'throughput': 0.40, 'stability': 0.25}

# Historical anomaly records (unused but plausible)
anomaly_log = [
    {'timestamp': '2023-01-15', 'type': 'latency_spike', 'severity': 2},
    {'timestamp': '2023-02-03', 'type': 'packet_loss', 'severity': 1}
]

# Auxiliary function that appears relevant but isn't used in main calculation
def calculate_user_satisfaction_index(survey_dict):
    avg_scores = []
    for key in survey_dict:
        avg_scores.append(sum(survey_dict[key]) / len(survey_dict[key]))
    return sum(avg_scores) / len(avg_scores)

# Function to mask real logic with similar-looking alternative
def legacy_evaluation(metrics, thresh):
    score = 100
    if max(metrics['latency_ms']) > thresh['critical_latency']:
        score -= 20
    if max(metrics['cpu_load']) > thresh['max_cpu']:
        score -= 15
    if min(metrics['bandwidth_mbps']) < thresh['min_bandwidth']:
        score -= 10
    return score  # Dead end - never called in execution path

# Real processing begins here
system_events = ['startup', 'calibration', 'sync', 'processing', 'idle']
event_codes = {event: idx * 17 for idx, event in enumerate(system_events)}

def preprocess_sequence(raw_metrics):
    processed = {}
    for key in raw_metrics:
        # Normalize using z-score (but only some are actually used)
        values = raw_metrics[key]
        mean_val = sum(values) / len(values)
        variance = sum((x - mean_val) ** 2 for x in values) / len(values)
        std_dev = math.sqrt(variance)
        processed[key] = [round((x - mean_val) / std_dev, 3) for x in values]
    return processed

# Throughput derived from bandwidth (key transformation)
def extract_throughput_norm(bandwidth_list):
    # Convert Mbps to normalized efficiency score
    base = sum(bandwidth_list) / len(bandwidth_list)
    efficiency = (base - 400) / 100  # Assume 400 is baseline
    return round(efficiency, 3)

# Stability metric based on latency variance
def compute_stability_score(latency_list):
    n = len(latency_list)
    if n == 0:
        return 0
    mean_lat = sum(latency_list) / n
    ss = sum((x - mean_lat) ** 2 for x in latency_list)
    variance = ss / n
    # Lower variance = higher stability
    stability_base = 100 - (variance / 10)
    return round(stability_base, 3)

# Main data processing pipeline
def process_metrics(metrics, weight_map):
    # Preprocess all technical metrics (only some will be used)
    cleaned = preprocess_sequence(metrics)
    
    # Extract relevant features
    avg_latency = sum(metrics['latency_ms']) / len(metrics['latency_ms'])
    latency_normalized = (100 - avg_latency) / 100  # Higher score for lower latency
    
    # Compute actual components
    throughput_score = extract_throughput_norm(metrics['bandwidth_mbps'])
    stability_score = compute_stability_score(metrics['latency_ms'])
    
    # Apply weights - this is where final_score is determined
    weighted_sum = (
        latency_normalized * weight_map['latency'] +
        throughput_score * weight_map['throughput'] +
        stability_score * weight_map['stability']
    )
    
    # Additional distraction: modify unused dictionary
    cleaned['cpu_load'][0] = 0  # Meaningless mutation
    
    # Final scaling to 0-100 range
    final = round(weighted_sum * 10, 3)
    
    # Dead logic branch that looks like it affects result
    if final > 90:
        flag = ''.join([chr(ord(c) - 1) for c in 'Bpnnfs!Tdvttf'])  # "Answer Success" obfuscated
    elif final < 60:
        recovery_vector = [i**2 for i in range(5) if i % 2 == 0]
    
    return final

# Initialization vector (looks important)
init_vector = [0x1F, 0x0A, 0x0D, 0x0E]

# Execution starts here
data_log = {
    'latency_ms': technical_metrics['latency_ms'],
    'bandwidth_mbps': technical_metrics['bandwidth_mbps'],
    'cpu_load': technical_metrics['cpu_load']
}

# Unused transformation that looks critical
encoded_weights = {k: int(v * 100) for k, v in weights.items()}
decoded_back = {k: v / 100 for k, v in encoded_weights.items()}

# Critical execution point
final_score = process_metrics(data_log, weights)

# Print result as required
print(f"Result: {final_score}")