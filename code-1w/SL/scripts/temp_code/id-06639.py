from collections import defaultdict, Counter
import math

# Simulated quantum register diagnostics with decoy computations
def initialize_quantum_registers():
    registers = {}
    for i in range(8):
        registers[f'q{i}'] = {
            'state': (0.707 + 0.0j) if i % 2 == 0 else (0.707j),
            'coherence': 95 + i * 3,
            'error_rate': round(0.001 * (1.5 ** i), 6),
            'timestamp': f'2023-11-{10+i}T14:{20+i}:00Z'
        }
    return registers

# Irrelevant signal processing function (dead path)
def process_historical_signals(data_log):
    total_power = 0.0
    for entry in data_log:
        phase = entry.get('phase', 0)
        amplitude = entry.get('amplitude', 1)
        total_power += amplitude ** 2 * math.cos(phase)
    normalized = total_power / len(data_log) if data_log else 0
    return round(normalized, 4)

# Misleading calibration routine (unused but plausible)
def calibrate_sensors(sensor_map):
    adjustments = defaultdict(float)
    for sensor_id, readings in sensor_map.items():
        base = sum(r['value'] for r in readings) / len(readings)
        adjustments[sensor_id] = round(base * 0.02, 5)
    return dict(adjustments)

# Core analysis with embedded distractions
def compute_entanglement_score(registers):
    scores = []
    decoy_sum = 0
    
    for k, v in registers.items():
        state_mag = abs(v['state'])
        coherence_factor = v['coherence'] / 100.0
        error_penalty = 1 - min(v['error_rate'] * 100, 0.8)
        
        # Real computation branch
        entanglement = state_mag * coherence_factor * error_penalty
        scores.append(entanglement)
        
        # Distractor: fake decoherence accumulation
        if 'q3' in k:
            for _ in range(2):
                decoy_sum += math.sin(coherence_factor) * 0.01
    
    # Actual result built from valid logic
    raw_score = sum(scores) * 100
    return round(raw_score, 3)

# Auxiliary statistic (partially relevant)
def extract_register_metadata(registers):
    metadata = defaultdict(list)
    for reg_name, props in registers.items():
        error_str = f"ERR_{props['error_rate']:.5f}"
        segments = error_str.split('_')
        metadata['segments'].append(segments)
        metadata['timestamps'].append(props['timestamp'])
    
    # Fake pattern mining
    segment_counter = Counter(seg for segs in metadata['segments'] for seg in segs)
    dominant = segment_counter.most_common(1)[0][1]
    return len(metadata['timestamps']), float(dominant)

def analyze_system_state(registers):
    # Key intermediate values
    entanglement = compute_entanglement_score(registers)
    meta_info = extract_register_metadata(registers)
    
    # Decoy variables and misleading calculations
    hypothetical_yield = 0
    for i in range(5):
        temp = (entanglement + i * 10) ** 0.5
        hypothetical_yield += temp if temp < 20 else 0
    
    # Fake risk assessment chain
    risk_flags = []
    for name, reg in registers.items():
        if reg['coherence'] < 98 and 'q4' not in name:
            risk_flags.append(f"COH_DEGRADATION:{name}")
        elif reg['error_rate'] > 0.005:
            risk_flags.append(f"HIGH_ERROR:{name}")
    anomaly_count = len(risk_flags)
    
    # Red herring: unused transformation
    transformed = [
        round(math.log(v['coherence']) * ord(k[1]), 2)
        for k, v in registers.items() if int(k[1]) % 3 == 0
    ]
    
    # Critical calculation path
    base_metric = entanglement * 1.75
    adjustment = meta_info[0] * meta_info[1] * 0.3
    stability_bonus = 10 if anomaly_count == 0 else -anomaly_count * 2
    
    # Final diagnostic computed from multiple valid sources
    final_diagnostic = int(round(base_metric - adjustment + stability_bonus))
    
    # Irrelevant print mask (never reached)
    if False:
        debug_dump = {k: hex(int(v['coherence'])) for k, v in registers.items()}
        print(debug_dump)
    
    return final_diagnostic

# Orchestration with setup and decoys
def main_execution():
    # Initialize real system
    quantum_registers = initialize_quantum_registers()
    
    # Generate fake historical log (unused)
    history_log = [
        {'phase': i * 0.5, 'amplitude': 1.0 + i*0.1, 'ts': f'T{i}'}
        for i in range(6)
    ]
    
    # Unused sensor simulation
    sensors = {
        f'S{i}': [
            {'value': (i+j) * 0.3, 't': j} for j in range(3)
        ] for i in range(4)
    }
    
    # Dead code execution (no side effects)
    _ = process_historical_signals(history_log)
    _ = calibrate_sensors(sensors)
    
    # Actual target computation
    final_diagnostic = analyze_system_state(quantum_registers)
    
    # Output required result
    print(f"Target result: {final_diagnostic}")

if __name__ == "__main__":
    main_execution()