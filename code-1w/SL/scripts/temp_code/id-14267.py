import math

# Simulated telemetry data from a distributed sensor network
def fetch_telemetry():
    return [
        {'sensor': 'A1', 'temp': 23.5, 'status': 'active', 'reads': [22, 24, 25, 23]},
        {'sensor': 'B2', 'temp': -19.1, 'status': 'idle', 'reads': [18, 17, 16, 15]},
        {'sensor': 'C3', 'temp': 31.7, 'status': 'active', 'reads': [30, 32, 31, 33]},
        {'sensor': 'D4', 'temp': 0.0, 'status': 'failed', 'reads': []},
        {'sensor': 'E5', 'temp': 15.3, 'status': 'active', 'reads': [14, 15, 16, 15]}
    ]

# Legacy function - not actually used in current logic (dead path)
def legacy_calibrate(x):
    return [val * 1.05 for val in x if val > 0]

# Irrelevant signal processing mock-up
def enhance_signal(strength):
    if strength < 0:
        return abs(strength) ** 0.5
    return strength * 1.2 + 4.1

# Auxiliary function to compute moving average (not directly used)
def moving_avg(readings, window=2):
    if len(readings) < window:
        return 0
    return sum(readings[-window:]) / window

# Complex preprocessing with red herring operations
def preprocess_data(raw):
    processed = []
    baseline_shift = 0.7
    noise_floor = 0.02
    
    for entry in raw:
        raw_temp = entry['temp']
        adjusted = raw_temp + baseline_shift
        
        # Distractor: signal quality metric not used later
        signal_quality = 'high' if abs(adjusted) > 5 else 'low'
        
        # Real transformation: normalize and flag extremes
        normalized = abs(adjusted) % 100
        is_critical = normalized > 30 and entry['status'] == 'active'
        
        # Decoy calculation with string manipulation (irrelevant)
        sensor_code = entry['sensor']
        code_sum = sum(ord(c) for c in sensor_code) % 100
        
        processed.append({
            'id': sensor_code,
            'value': normalized,
            'critical': is_critical,
            'meta': f"{signal_quality}-{code_sum}"
        })
    
    return processed

# Secondary load analysis with conditional expression distraction
def analyze_load(config):
    levels = [len(node) for node in config.values()]
    avg_level = sum(levels) / len(levels) if levels else 0
    
    # Use of lambda and conditional expression (partially relevant)
    classify = lambda x: 'over' if x > 2.5 else 'normal'
    return {
        'magnitude': avg_level * 1.8,
        'state': classify(avg_level),
        'peak': max(levels) if levels else 0
    }

# Core metric processor combining multiple concepts
def process_metrics(metrics, load_profile):
    # Extract active critical sensors
    critical_count = len([m for m in metrics if m['critical']])
    
    # Bit manipulation red herring
    magic_flag = (critical_count << 2) ^ 0b1010
    if magic_flag & 0b1000:
        magic_flag = magic_flag >> 1
    
    # Real computation: aggregate values using string method distraction
    all_ids = ','.join([m['id'] for m in metrics])
    id_checksum = sum(ord(c) for c in all_ids if c in 'AEIOU') - 3 * critical_count
    
    # Primary arithmetic chain
    base_score = 0
    for m in metrics:
        base_score += m['value']
        if m['critical']:
            base_score += 10.5  # Criticality bonus
    
    # Load influence via trigonometric distraction (only magnitude matters)
    load_factor = load_profile['magnitude']
    dampened = load_factor * math.cos(math.pi / 4)  # Constant factor
    
    # Final composition with conditional expression
    final_modifier = 0.85 if load_profile['state'] == 'over' else 1.15
    
    # Key statement: what is the value of final_diagnostic here?
    final_diagnostic = int(base_score * final_modifier - id_checksum + dampened)
    
    # Dead code path - never executed but looks important
    if final_diagnostic < 0:
        recovery_mode = True
        final_diagnostic = abs(final_diagnostic) // 2
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    # Simulated system configuration (distractor structure)
    network_config = {
        'nodes': ['A1', 'C3'],
        'gateways': ['G7'],
        'repeaters': ['R2', 'R5']
    }
    
    # Fetch and preprocess real data
    raw_data = fetch_telemetry()
    data_snapshot = preprocess_data(raw_data)
    
    # Generate system load profile (used in main logic)
    system_load = analyze_load(network_config)
    
    # Execute key computation
    final_diagnostic = process_metrics(data_snapshot, system_load)
    
    # Output result
    print(f"Result: {final_diagnostic}")