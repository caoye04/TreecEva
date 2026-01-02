def analyze_system_health():
    # Real-time telemetry data from distributed sensors
    raw_signals = [234, 567, 123, 890, 456, 789, 321, 654]
    calibration_offsets = [12, -5, 8, 0, -3, 10, 7, -6]
    
    # Irrelevant signal smoothing (distractor)
    smoothed = [raw_signals[i] + calibration_offsets[i] for i in range(len(raw_signals))]
    normalized = [x / max(smoothed) for x in smoothed]
    energy_sum = sum(x**2 for x in normalized)

    # Sensor metadata (partially relevant)
    sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']
    locations = ['North', 'South', 'East', 'West', 'Core', 'Edge', 'Hub', 'Node']
    
    # Mapping with enumerate and zip (required feature)
    sensor_map = {sid: {'idx': i, 'loc': loc} for i, (sid, loc) in enumerate(zip(sensor_ids, locations))}

    # Decoy transformation chain (dead path)
    def transform_readings(data, factor=1.1):
        return [int(x * factor) % 1000 for x in data]
    
    enhanced_signals = transform_readings(raw_signals)  # Unused

    # Critical diagnostic logs (core data)
    log_entries = [
        {'time': 1001, 'code': 'ERR', 'value': 234, 'sensor': 'S1'},
        {'time': 1003, 'code': 'OK',  'value': 567, 'sensor': 'S2'},
        {'time': 1005, 'code': 'WARN','value': 123, 'sensor': 'S3'},
        {'time': 1007, 'code': 'ERR', 'value': 890, 'sensor': 'S4'},
        {'time': 1009, 'code': 'OK',  'value': 456, 'sensor': 'S5'},
        {'time': 1011, 'code': 'WARN','value': 789, 'sensor': 'S6'},
        {'time': 1013, 'code': 'ERR', 'value': 321, 'sensor': 'S7'},
        {'time': 1015, 'code': 'OK',  'value': 654, 'sensor': 'S8'}
    ]

    # Threshold policy configuration (relevant)
    system_thresholds = {
        'critical': 800,
        'elevated': 600,
        'normal': 400
    }

    # Misleading aggregation (distractor)
    error_count = len([e for e in log_entries if e['code'] == 'ERR'])
    avg_value = sum(e['value'] for e in log_entries) / len(log_entries)
    status_flags = [1 if e['code'] == 'OK' else 0 for e in log_entries]

    # String-based event tagging (required string method)
    for entry in log_entries:
        tags = []
        if 'ERR' in entry['code']:
            tags.append('failure')
        if str(entry['value']).endswith('4'):
            tags.append('terminal_alert')
        entry['tags'] = ','.join(tags)  # Use of string join

    # Core processing function with bit manipulation red herring
    def evaluate_anomaly(value, base_threshold):
        # Bitwise decoy: manipulate bits but only use modulo result
        shifted = (value << 2) ^ 0xFF
        masked = shifted & 0xFFFF
        synthetic = (masked >> 3) + (value & 0x0F)
        return value > base_threshold or (synthetic % 7 == 0)  # Only first condition matters

    # Secondary decoy: set operations with no impact
    critical_codes = {'ERR', 'CRIT'}
    active_warnings = {'WARN', 'ERR'}
    transient_states = {'OK', 'STANDBY'}
    volatile_set = critical_codes | transient_states

    # Main metric processor (key logic)
    def process_metrics(entries, thresholds):
        high_severity = 0
        mid_severity = 0
        
        # Nested control flow with distractors
        for idx, entry in enumerate(entries):
            val = entry['value']
            sensor_info = sensor_map[entry['sensor']]
            
            # Red herring: location-based weighting (unused)
            weight = 1.0
            if sensor_info['loc'] in ['Core', 'Hub']:
                weight = 1.25
            
            # Actual logic hidden among distractions
            if val > thresholds['critical']:
                high_severity += 1
            elif val > thresholds['elevated']:
                mid_severity += 1

            # Dead computation branch
            checksum = 0
            for c in entry['tags']:
                checksum ^= ord(c)  # Computed but not used
            
        # Complex formula with irrelevant components
        base_score = (high_severity * 100) + (mid_severity * 10)
        adjustment = len([e for e in entries if 'terminal_alert' in e['tags']]) * 5
        penalty = sum(1 for e in entries if evaluate_anomaly(e['value'], 999))  # Always false
        
        # Final diagnostic is based only on high/mid severity counts
        result = base_score - adjustment  # adjustment cancels out due to only one terminal_alert
        
        # Irrelevant final transformation
        binary_rep = bin(result)
        parity = binary_rep.count('1') % 2
        
        return int(result)  # Only this matters

    # Execution point of interest
    final_diagnostic = process_metrics(log_entries, system_thresholds)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

analyze_system_health()