def process_system_state(raw_data, config):
    # Irrelevant preprocessing block (dead path)
    temp_buffer = []
    for item in raw_data:
        if isinstance(item, str) and 'ERR' in item:
            temp_buffer.append(item.lower())
    
    # Distractor: complex but unused transformation
    encoded_stream = {i: format(ord(c), 'b') for i, c in enumerate('system_snapshot')}
    checksum = sum(len(b) for b in encoded_stream.values()) % 7

    # Real data path begins
    event_timeline = [x for x in raw_data if isinstance(x, int)]
    critical_events = set()
    for tick in event_timeline:
        if tick % 13 == 0 and tick > 0:
            critical_events.add(tick)

    # Simulated sensor mask (misleading intermediate)
    sensor_mask = [1 if i % 5 == 0 else 0 for i in range(256)]
    masked_sum = sum(i * v for i, v in enumerate(sensor_mask) if v)

    # Core logic disguised among noise
    threshold = config.get('threshold', 100)
    filtered_ticks = [t for t in event_timeline if t > threshold]
    spike_count = len([t for t in filtered_ticks if t in critical_events])

    # Auxiliary decoy function (never called)
    def decrypt_handshake(token):
        return ''.join(chr((ord(c) - 3) % 95 + 32) for c in reversed(token))

    # Data structure cross-reference
    diagnostic_log = {
        'events': event_timeline,
        'spikes': spike_count,
        'baseline': min(event_timeline) if event_timeline else 0,
        'anomalies': critical_events
    }

    active_sensors = set(range(1, 50, 3)) | {len(event_timeline)}
    backup_sensors = {x for x in range(100) if x % 7 == 0}
    active_sensors.discard(42)  # Red herring removal

    # Decoy calculation with realistic-looking metrics
    health_score = 100.0
    for s in active_sensors:
        if s in backup_sensors:
            health_score -= 0.7
    health_score = round(health_score, 2)

    # Key analysis function
    def analyze_fault_sequence(log, sensors):
        sequence = log['events']
        spike_flag = log['spikes'] > 5
        size_factor = len(sensors) // 4
        
        # Misleading use of set operations
        intersection_risk = len(sensors & log['anomalies'])
        risk_adjustment = intersection_risk * 2 if intersection_risk < 10 else 10
        
        # Actual answer derivation hidden in multiple steps
        base = log['baseline']
        for i in range(3):
            base = (base * 7 + 31) % 10007
        base += size_factor
        
        if spike_flag:
            base += 50
        else:
            base -= 25
        
        # Final adjustment using dictionary lookup
        modifier_map = {k: k*2 % 13 for k in range(15)}
        final_mod = modifier_map.get(size_factor % 15, 0)
        
        result = base + risk_adjustment + final_mod
        return int(result)

    # Execution point of interest
    final_diagnostic = analyze_fault_sequence(diagnostic_log, active_sensors)
    
    # Unused cleanup (distraction)
    del temp_buffer, encoded_stream, sensor_mask
    
    # Output requirement
    print(f"Target result: {final_diagnostic}")

# Input setup
raw_input_data = [15, 0, 'ERR_INIT', 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 200, 300, 400]
config_params = {'threshold': 50}

# Entry point
process_system_state(raw_input_data, config_params)