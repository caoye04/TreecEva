import math

# Simulated network node diagnostic system with interference

def analyze_node_health(signal, noise, threshold=0.7):
    snr = signal / (noise + 1e-9)
    return snr > threshold and signal > 5


def compute_entropy(data_stream):
    # Irrelevant entropy calculation (distractor)
    freq = {}
    for bit in data_stream:
        freq[bit] = freq.get(bit, 0) + 1
    probs = [f / len(data_stream) for f in freq.values()]
    return -sum(p * math.log2(p) for p in probs if p > 0)


def extract_timestamp_segments(log_entry):
    # Dead code path - never used in final computation
    parts = log_entry.split('.')
    if len(parts) > 2:
        return int(parts[1]) % 100
    return 0

# Misleading helper function that looks important but isn't used
def predict_failure_rate(usage_history):
    avg = sum(usage_history) / len(usage_history)
    variance = sum((x - avg) ** 2 for x in usage_history) / len(usage_history)
    return math.exp(-avg) * variance

# Core logic disguised among distractors
def evaluate_resilience(nodes):
    resilience_scores = []
    for node in nodes:
        base_score = node['capacity'] * 0.3
        if node['redundant']:
            base_score += 15
        if node['latency'] < 50:
            base_score += 10
        resilience_scores.append(base_score)
    return resilience_scores

# Distractor: complex-looking but unused bit manipulation
def obfuscate_id(node_id):
    transformed = 0
    for i, char in enumerate(str(node_id)):
        transformed ^= ord(char) << (i % 4)
    return transformed ^ 0xFFFF

# Real processing chain buried in noise
def filter_active_nodes(nodes):
    return [n for n in nodes if n['status'] == 'ACTIVE' and n['version'] >= 2]


def calculate_efficiency_metric(active_nodes, load):
    total_capacity = sum(node['capacity'] for node in active_nodes)
    avg_latency = sum(node['latency'] for node in active_nodes) / len(active_nodes)
    peak_ratio = load / (total_capacity + 1)
    efficiency = (total_capacity / (avg_latency + 1)) * (1 - peak_ratio)
    return efficiency

# Key aggregation function - the actual answer depends on this

def aggregate_metrics(nodes, current_load):
    filtered = filter_active_nodes(nodes)
    efficiency = calculate_efficiency_metric(filtered, current_load)
    
    # Secondary metric to obscure focus
    resilience_list = evaluate_resilience(filtered)
    average_resilience = sum(resilience_list) / len(resilience_list) if resilience_list else 0
    
    # Actual formula for final result
    adjustment_factor = 1.0
    if efficiency > 100:
        adjustment_factor = 0.9
    elif efficiency < 50:
        adjustment_factor = 1.1
    
    # Critical computation
    raw_diagnostic = efficiency * average_resilience * adjustment_factor
    
    # Normalize to integer scale
    final_score = int(round(raw_diagnostic / 2.5))
    
    # Decoy operations
    temp_results = set()
    for val in resilience_list:
        temp_results.add(int(val) % 7)
    _ = [math.sqrt(x + 1) for x in temp_results if x % 2 == 0]  # Unused list comprehension
    
    return final_score

# Simulated system state with realistic values
network_nodes = [
    {'id': 'N001', 'status': 'ACTIVE', 'capacity': 80,  'latency': 45, 'version': 2, 'redundant': True,  'signal': 8.2, 'noise': 0.3},
    {'id': 'N002', 'status': 'INACTIVE', 'capacity': 60, 'latency': 30, 'version': 1, 'redundant': False, 'signal': 4.1, 'noise': 0.5},
    {'id': 'N003', 'status': 'ACTIVE', 'capacity': 100, 'latency': 60, 'version': 3, 'redundant': True,  'signal': 9.0, 'noise': 0.4},
    {'id': 'N004', 'status': 'ACTIVE', 'capacity': 70,  'latency': 40, 'version': 2, 'redundant': False, 'signal': 6.5, 'noise': 0.6},
    {'id': 'N005', 'status': 'FAILED', 'capacity': 90,  'latency': 80, 'version': 2, 'redundant': True,  'signal': 3.0, 'noise': 1.2}
]

system_load = 180

# Dead assignment - misleading
health_logs = ['ERR.001.23', 'SYS.002.45', 'NET.003.67']
_ = [extract_timestamp_segments(log) for log in health_logs]  # Unused operation

# Critical execution point
final_diagnostic = aggregate_metrics(network_nodes, system_load)

# Output result as required
print(f"Result: {final_diagnostic}")