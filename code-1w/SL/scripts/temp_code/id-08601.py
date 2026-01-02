import math

def analyze_signal_strength(signal_packet, threshold=0.7):
    if not signal_packet:
        return 0
    avg_strength = sum([s['strength'] for s in signal_packet if s['type'] == 'primary']) / max(1, len([s for s in signal_packet if s['type'] == 'primary']))
    return avg_strength if avg_strength >= threshold else 0

def compute_orbital_correction(positions):
    corrections = []
    for i in range(1, len(positions)):
        dx = positions[i][0] - positions[i-1][0]
        dy = positions[i][1] - positions[i-1][1]
        correction = math.sqrt(dx**2 + dy**2) * 0.01
        corrections.append(correction)
    return sum(corrections)

def evaluate_comms_health(link_status):
    healthy_links = sum([1 for status in link_status if status == 'active'])
    return healthy_links >= 3

def filter_noisy_data(raw_readings):
    filtered = [x for x in raw_readings if abs(x - sum(raw_readings)/len(raw_readings)) < 2 * (max(raw_readings) - min(raw_readings)) / 2]
    return filtered if len(filtered) > 1 else [0]

def generate_telemetry_snapshot(timestamp, subsystems):
    snapshot = {}
    for sub in subsystems:
        snapshot[sub] = {
            'status': 'nominal',
            'timestamp': timestamp,
            'checksum': len(sub) * timestamp % 100
        }
    # Dead code path - irrelevant to final result
    if 'propulsion' in snapshot:
        snapshot['propulsion']['override'] = False
    return snapshot

def simulate_buffer_overflow(data_stream):
    buffer_size = 1024
    overflow_flag = len(data_stream) > buffer_size
    # This function does nothing meaningful
    temp_result = [x ^ 255 for x in data_stream[:10]] if data_stream else []
    return overflow_flag

def aggregate_diagnostics(log_entries, state_vector):
    base_score = 100
    
    # Irrelevant telemetry processing
    telemetry_snapshot = generate_telemetry_snapshot(12345, ['sensor_array', 'comms', 'power', 'nav'])
    overflow = simulate_buffer_overflow(list(range(50)))
    
    # Real logic begins
    position_history = [(10, 20), (15, 25), (18, 30), (20, 35)]
    orbital_correction = compute_orbital_correction(position_history)
    
    raw_emg_signals = [0.5, 0.8, 1.2, 0.9, 0.4, 1.1]
    filtered_signals = filter_noisy_data(raw_emg_signals)
    avg_filtered = sum(filtered_signals) / len(filtered_signals)
    
    signal_packets = [
        {'strength': 0.8, 'type': 'primary'},
        {'strength': 0.9, 'type': 'primary'},
        {'strength': 0.6, 'type': 'secondary'},
        {'strength': 0.75, 'type': 'primary'}
    ]
    signal_analysis = analyze_signal_strength(signal_packets)
    
    link_statuses = ['active', 'inactive', 'active', 'active', 'standby']
    comms_healthy = evaluate_comms_health(link_statuses)
    
    # Distractor: complex but unused calculation
    phase_angles = [math.sin(i * 0.5) for i in range(10)]
    coherence_index = sum([abs(phase_angles[i] - phase_angles[i-1]) for i in range(1, len(phase_angles))])
    normalized_coherence = coherence_index / len(phase_angles) if phase_angles else 0
    
    # Key logic with conditional expressions and set operations
    critical_subsystems = {'life_support', 'navigation', 'comms'}
    active_subsystems = {k for k, v in state_vector.items() if v == 'online'}
    redundancy_check = len(critical_subsystems & active_subsystems) == len(critical_subsystems)
    
    # Another red herring
    backup_protocols = tuple(['initiated' if i % 2 == 0 else 'pending' for i in range(5)])
    protocol_audit = len([p for p in backup_protocols if p == 'initiated'])
    
    # Final computation chain
    base_score -= int(orbital_correction * 10)
    base_score += int(avg_filtered * 20)
    base_score += 15 if signal_analysis > 0 else 0
    base_score += 20 if comms_healthy else -10
    base_score += 25 if redundancy_check else -30
    
    # This variable is key
    final_diagnostic = base_score + (state_vector.get('clock_drift', 0) * -5)
    
    # Print required at end
    return final_diagnostic

# Execution flow
system_telemetry = {
    'life_support': 'online',
    'navigation': 'online',
    'comms': 'online',
    'power': 'degraded',
    'thermal': 'online'
}
diagnostics_log = [{'event': 'startup', 'code': 200}, {'event': 'sync', 'code': 201}]
final_diagnostic = aggregate_diagnostics(diagnostics_log, system_telemetry)
print(f"Target result: {final_diagnostic}")