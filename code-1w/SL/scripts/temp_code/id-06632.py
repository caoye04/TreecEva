from collections import defaultdict, Counter

# System telemetry simulation for distributed node monitoring
def simulate_node_health(nodes):
    health_map = defaultdict(int)
    for i, node in enumerate(nodes):
        health_map[node] = (i * 3 + 7) % 5
    return health_map

def transform_signal(raw_data, mode='encode'):
    # Irrelevant transformation path (dead code path)
    if mode == 'encode':
        return [x ^ 255 for x in raw_data]
    else:
        return [x & 127 for x in raw_data]

def evaluate_stability(health_readings):
    cumulative = 0
    for reading in health_readings.values():
        if reading > 2:
            cumulative += reading * 1.5
        elif reading == 2:
            cumulative += reading * 0.8
        else:
            cumulative -= 1.2
    return round(cumulative, 4)

def analyze_phase_shift(frequencies):
    # Distractor function: looks important but unused in final result
    shift_log = []
    for i in range(1, len(frequencies)):
        shift_log.append(frequencies[i] - frequencies[i-1])
    return sum(shift_log)

def detect_resonance(channels):
    # Another red herring: complex logic with no downstream impact
    total = 0
    for a, b in zip(channels[:-1], channels[1:]):
        total += (a + b) * (a ^ b)
    return total // 2 if total > 0 else 0

def compute_entropy(sequence):
    counts = Counter(sequence)
    entropy = 0
    length = len(sequence)
    for count in counts.values():
        p = count / length
        entropy -= p * __import__('math').log2(p)
    return round(entropy, 4)

def aggregate_metrics(states, importance_weights):
    base_score = 0
    for idx, (state, weight) in enumerate(zip(states, importance_weights)):
        contribution = 0
        if state > 3:
            contribution = (state * weight) + 2.5
        elif state == 3:
            contribution = state * weight * 0.9
        else:
            contribution = weight * 0.4
        base_score += contribution

    # Secondary adjustment using entropy of states
    state_entropy = compute_entropy(states)
    adjusted_score = base_score * (1 + state_entropy / 10)

    # Final non-linear calibration
    if adjusted_score > 50:
        adjusted_score = adjusted_score * 0.85 + 5
    elif adjusted_score > 30:
        adjusted_score = adjusted_score * 0.92
    else:
        adjusted_score = adjusted_score * 1.05

    return int(round(adjusted_score))

# Main execution flow
if __name__ == '__main__':
    # Initialize sensor array and configuration
    node_ids = ['N1', 'N2', 'N3', 'N4', 'N5']
    sensor_data = [128, 192, 64, 220, 100]
    frequency_band = [440, 452, 460, 475]
    channel_power = [18, 23, 19, 27, 33]

    # Execute health simulation
    node_health = simulate_node_health(node_ids)
    
    # Extract state levels from health readings
    network_states = [v for k, v in sorted(node_health.items())]
    
    # Assign dynamic weights based on position (critical for final result)
    weights = [1.1, 1.3, 0.9, 1.4, 1.2]
    
    # Apply signal transform (irrelevant to final answer)
    encrypted_signal = transform_signal(sensor_data, 'encode')
    
    # Perform stability evaluation (distractor computation)
    raw_stability = evaluate_stability(node_health)
    
    # Analyze phase shift (dead-end analysis)
    delta_analysis = analyze_phase_shift(frequency_band)
    
    # Detect resonance pattern (misleading intermediate)
    resonance_peak = detect_resonance(channel_power)
    
    # Compute auxiliary metrics (partially relevant via side-channel)
    _ = compute_entropy(network_states)
    
    # Key statement: aggregate final diagnostic score
    final_diagnostic = aggregate_metrics(network_states, weights)
    
    # Output target result
    print(f"Result: {final_diagnostic}")