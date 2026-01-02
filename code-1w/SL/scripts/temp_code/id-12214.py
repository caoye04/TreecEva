def analyze_system_health(raw_logs, config):
    # Irrelevant preprocessing block (dead code path)
    temp_buffer = []
    for entry in raw_logs:
        if 'DEBUG' in entry and len(entry) > 50:
            temp_buffer.append(entry.lower().replace('debug', ''))
    
    # Distractor: complex but unused transformation
    encoded_stream = [sum([ord(c) for c in log[:8]]) % 256 for log in raw_logs if 'ERROR' not in log]
    checksum = 0
    for val in encoded_stream:
        checksum = (checksum ^ val) << 1
        if checksum > 255:
            checksum -= 255

    # Actual relevant data extraction
    log_entries = []
    for log in raw_logs:
        if 'ERROR' in log or 'CRITICAL' in log:
            timestamp = int(log.split('|')[0])
            level = log.split('|')[2]
            message = log.split('|')[3]
            log_entries.append({'ts': timestamp, 'lvl': level, 'msg': message})

    # Misleading statistical aggregation (not used in final result)
    avg_length = sum(len(e['msg']) for e in log_entries) / max(len(log_entries), 1)
    error_density = len([e for e in log_entries if 'disk' in e['msg'].lower()]) * 1000
    
    # System state initialization with red herring values
    system_state = {
        'core_temp': 67.4,
        'fan_speed': 2200,
        'voltage_rail': 3.28,
        'uptime_hours': 142,
        'packet_loss': 0.07,
        'dummy_flag': True,
        'cache_misses': 9812,
        'last_reset': 1684321098
    }

    # Decoy function that's defined but never called
    def simulate_failure_mode(state, threshold=0.5):
        import random
        random.seed(state['uptime_hours'])
        return [random.random() > threshold for _ in range(10)]

    # Another distractor: irrelevant bit manipulation on sensor data
    temp_word = int(system_state['core_temp'] * 100) & 0xFF
    voltage_word = int(system_state['voltage_rail'] * 100) | 0x3A
    fused_diagnostics = (temp_word << 8) | voltage_word
    fused_diagnostics = (fused_diagnostics ^ 0xABCD) & 0xFFFF

    # Conditional branch with misleading side computation
    if system_state['fan_speed'] < 2000:
        corrective_action = 'INCREASE'
        expected_rpm = system_state['fan_speed'] * 1.2
    else:
        corrective_action = 'STABLE'
        decay_factor = 0.91
        predicted_temp = system_state['core_temp'] * decay_factor  # Not used later

    # Real processing begins here
    severity_map = {'WARNING': 1, 'ERROR': 3, 'CRITICAL': 5}
    recent_alerts = [e for e in log_entries if e['ts'] > 1684300000]
    
    weighted_score = 0
    for alert in recent_alerts:
        base_severity = severity_map.get(alert['lvl'], 0)
        length_factor = len(alert['msg'].split())
        keyword_bonus = 2 if 'failure' in alert['msg'].lower() else 0
        weighted_score += base_severity * (1 + keyword_bonus) * min(length_factor, 5)
    
    # Key variable used in answer
    system_state['alert_score'] = weighted_score

    # Critical function containing final computation
    def process_metrics(entries, state):
        score = state['alert_score']
        uptime_penalty = 0
        
        # Uptime-based degradation factor
        if state['uptime_hours'] > 100:
            uptime_penalty = int(state['uptime_hours'] // 25)
        
        # Bitwise anomaly detection on log count
        log_count = len(entries)
        anomaly_flag = (log_count & (log_count - 1)) == 0  # Is power of two
        anomaly_multiplier = 3 if anomaly_flag else 1
        
        # Final diagnostic calculation
        base_diagnostic = (score * 17) + 42
        if state['core_temp'] > 65:
            base_diagnostic += 25
        intermediate = (base_diagnostic ^ 0xFF) + uptime_penalty
        final_diagnostic = (intermediate * anomaly_multiplier) - 13
        
        # Dead code branch (never reached due to prior logic)
        if len(entries) == 0:
            return -999  
        
        return final_diagnostic

    # Execution point of interest
    final_diagnostic = process_metrics(log_entries, system_state)
    print(f"Target result: {final_diagnostic}")