import math

def analyze_phase_shift(frequency, amplitude, phase):
    # Irrelevant signal processing function (dead code path)
    return (amplitude * math.sin(2 * math.pi * frequency + phase)) ** 2

def validate_checksum(data_block):
    # Unused validation routine (distractor)
    checksum = 0
    for b in data_block:
        checksum = (checksum + b) % 257
    return checksum == 137

def transform_vector(coords):
    # Red herring: coordinate transformation not used in main logic
    x, y, z = coords
    x = (x + 3) % 10
    y = (y * 2) % 15
    z = int(math.sqrt(z + 1))
    return (z, y, x)

def aggregate_metrics(log_entries, flags):
    base_score = 0
    penalty = 0
    
    # Real logic begins: extract and filter timing events
    recent_events = log_entries[-5:]  # slicing operation
    event_types = {e['type'] for e in recent_events}  # set comprehension
    
    # Core calculation branch
    for entry in recent_events:
        if entry['status'] == 'OK' and flags['enable_enhanced_scoring']:
            base_score += int(entry['elapsed_ms'] // 10)
        elif entry['retried']:
            penalty += 5
    
    # Bit manipulation red herring
    encoded_flag = (flags['debug_mode'] << 3) | (flags['dry_run'] << 1)
    mask = 0b1101
    masked = encoded_flag & mask
    
    # Decoy dictionary update
    diagnostics = {
        'raw_count': len(log_entries),
        'unique_types': len(event_types),
        'overhead_flag': masked > 10
    }
    diagnostics['adjusted_score'] = base_score - penalty  # distractor assignment
    
    # Actual answer derivation buried here
    multiplier = 3 if flags['critical_path'] else 1
    temp_result = (base_score - penalty) * multiplier
    
    # More distractions: unused data structure transformations
    history_snapshot = log_entries[::2]  # every other entry
    cumulative = 0
    for h in history_snapshot:
        cumulative += h.get('payload_size', 0)
    average_load = cumulative / len(history_snapshot) if history_snapshot else 0
    
    # Final computation — depends only on temp_result and flag state
    final_adjustment = int(math.floor(average_load / 100)) if flags['adaptive'] else 0
    result = temp_result + final_adjustment
    
    # Critical assignment: this is the target variable
    final_diagnostic = result * 2  # double the aggregated metric
    
    # Dead print statements (no effect)
    if encoded_flag > 10:
        pass  # simulate debug output
    
    return final_diagnostic

# Main execution context
if __name__ == '__main__':
    # Simulated system telemetry
    timing_log = [
        {'type': 'auth', 'status': 'OK', 'elapsed_ms': 23.0, 'retried': False, 'payload_size': 120},
        {'type': 'route', 'status': 'ERR', 'elapsed_ms': 45.0, 'retried': True, 'payload_size': 200},
        {'type': 'db', 'status': 'OK', 'elapsed_ms': 67.0, 'retried': False, 'payload_size': 350},
        {'type': 'cache', 'status': 'OK', 'elapsed_ms': 12.0, 'retried': False, 'payload_size': 80},
        {'type': 'stream', 'status': 'OK', 'elapsed_ms': 89.0, 'retried': False, 'payload_size': 500},
        {'type': 'parse', 'status': 'OK', 'elapsed_ms': 34.0, 'retried': False, 'payload_size': 100}
    ]

    system_flags = {
        'enable_enhanced_scoring': True,
        'debug_mode': False,
        'dry_run': True,
        'critical_path': True,
        'adaptive': False
    }

    # Unused data structures to distract
    hardware_state = [0] * 8
    for i in range(len(hardware_state)):
        hardware_state[i] = (i * 17) % 255
    
    config_profile = {
        'version': '2.1.9',
        'timeout': 3000,
        'retries': 3,
        'burst_limit': 10
    }

    # Trigger decoy functions
    dummy_signal = analyze_phase_shift(50.0, 2.5, 1.2)
    dummy_vector = transform_vector((4, 7, 9))
    
    # Key statement: this determines the answer
    final_diagnostic = aggregate_metrics(timing_log, system_flags)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")