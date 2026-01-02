import math

def analyze_signal_strength(signal, threshold=0.7):
    return [s * 1.8 + 0.2 for s in signal if s > threshold]


def compute_phase_shift(frequency, time_offset):
    # Irrelevant trigonometric transformation (distractor)
    return math.sin(2 * math.pi * frequency * time_offset) + math.cos(frequency)


def filter_anomalies(data_stream):
    anomalies = []
    baseline = sum(data_stream) / len(data_stream)
    for point in data_stream:
        deviation = abs(point - baseline)
        if deviation > 0.5 * baseline and point > 1.2:
            anomalies.append(point * 0.9)
    return anomalies  # Unused return (dead path)


def transform_node_load(load_value):
    if load_value < 30:
        return load_value * 1.6
    elif load_value < 70:
        return load_value * 1.3
    else:
        return load_value * 0.85


def evaluate_stability_metric(raw_scores):
    adjusted = [math.sqrt(s) * 1.1 for s in raw_scores]
    penalty = 0
    for score in adjusted:
        if score > 8:
            penalty += 0.4
    return sum(adjusted) - penalty

# Simulated sensor network node data (real data)
network_nodes = {
    'node_alpha': {'load': 65, 'health': 0.88, 'signals': [0.62, 0.71, 0.93, 0.55]},
    'node_beta': {'load': 44, 'health': 0.76, 'signals': [0.81, 0.69, 0.95]},
    'node_gamma': {'load': 78, 'health': 0.92, 'signals': [0.53, 0.88, 0.91, 0.49]},
    'node_delta': {'load': 29, 'health': 0.64, 'signals': [0.77, 0.83]}
}

# Decoy function that appears important but is never called
def encrypt_transmission(data):
    encrypted = ''
    for c in str(data):
        encrypted += chr(ord(c) + 3)
    return encrypted

# Unused global variables (distractors)
critical_threshold = 90.5
emergency_protocol_active = False
fallback_sequence = [1, 1, 2, 3, 5, 8]

# Secondary processing chain with misleading intermediate values
intermediate_diagnostics = {}
total_health = 0
valid_nodes = 0

for node_id, attrs in network_nodes.items():
    total_health += attrs['health']
    if attrs['health'] > 0.75:
        valid_nodes += 1

average_health = total_health / len(network_nodes)
health_factor = 1.0 if average_health >= 0.8 else 0.85

# Real processing begins: extract and transform relevant features
transformed_loads = []
signal_contributions = []

for name, config in network_nodes.items():
    # Transform load using non-linear scaling
    transformed_load = transform_node_load(config['load'])
    transformed_loads.append(transformed_load)

    # Analyze only strong signals above threshold
    strong_signals = analyze_signal_strength(config['signals'])
    signal_impact = sum(strong_signals) * 0.3
    signal_contributions.append(signal_impact)

    # Compute phase shift (red herring - calculated but unused)
    shift = compute_phase_shift(50, config['load'] / 100)

# Aggregate metrics with weighted combination
load_baseline = sum(transformed_loads) / len(transformed_loads)
signal_potential = sum(signal_contributions)

# Simulate fallback logic (never triggered due to condition)
if len(network_nodes) < 3:
    fallback_mode = True
    final_diagnostic = 0
else:
    stability_vector = evaluate_stability_metric(transformed_loads)
    # Core computation path
    base_score = load_baseline * 0.6 + signal_potential * 0.4
    final_diagnostic = base_score * health_factor + (stability_vector * 0.1)

# Print result as required
print(f"Result: {final_diagnostic}")