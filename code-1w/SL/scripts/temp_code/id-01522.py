def process_telemetry_chunk(chunk_data, threshold=0.75):
    cumulative_score = 0
    anomaly_count = 0
    for item in chunk_data:
        raw_value = item.get('signal', 0)
        normalized = abs(raw_value) / (1 + abs(raw_value))
        if normalized > threshold:
            anomaly_count += 1
    return anomaly_count > len(chunk_data) * 0.3

# Irrelevant telemetry preprocessing (dead path)
def preprocess_signal_stream(stream):
    filtered = []
    for s in stream:
        if s > 0:
            filtered.append(s ** 0.5)
    return [f * 0.1 for f in filtered]

# Unused scoring function (distractor)
def compute_health_score(metrics):
    base = sum(m.get('value', 0) for m in metrics)
    penalty = len([m for m in metrics if m.get('error')]) * 10
    return max(0, base - penalty)

# Core system state analyzer
def analyze_system_state(log_entries, flags):
    state_vector = []
    temp_cache = {}
    
    # Process logs using enumerate and build intermediate states
    for idx, entry in enumerate(log_entries):
        code = entry.get('code', 0)
        severity = entry.get('severity', 1)
        timestamp = entry.get('ts', 0)
        
        # Bit manipulation on code (relevant only if even index)
        if idx % 2 == 0:
            transformed = (code ^ 255) & 0xFF
            state_vector.append(transformed * severity)
        else:
            state_vector.append(code + severity)

    # Build flag map with zip (mixed relevance)
    flag_keys = ['FATAL', 'CRITICAL', 'WARNING', 'INFO']
    flag_values = [flags & 1, (flags >> 1) & 1, (flags >> 2) & 1, (flags >> 3) & 1]
    flag_interpretation = dict(zip(flag_keys, flag_values))
    
    # Decoy aggregation (unused)
    total_flags = sum(flag_values)
    if total_flags > 2:
        consistency_check = False
    else:
        consistency_check = True
    
    # Critical path: conditional recursion based on state length
    def recursive_diagnose(vector, depth=0):
        if depth >= 3 or len(vector) == 0:
            return 404  # Default fail-safe
        if len(vector) == 1:
            return vector[0] % 97
        
        # Pairwise reduction with XOR and sum
        reduced = []
        for i in range(0, len(vector) - 1, 2):
            combined = (vector[i] ^ vector[i+1]) + depth
            reduced.append(combined)
        if len(vector) % 2 == 1:
            reduced.append(vector[-1])
        
        return recursive_diagnose(reduced, depth + 1)
    
    # Distractor: dictionary-based lookup table (never accessed)
    diagnostic_codes = {
        10: "SensorTimeout",
        23: "BusCollision",
        42: "CalibrationError",
        99: "ClockDrift",
        204: "BufferOverflow"
    }
    
    # Actual computation
    initial_diagnosis = recursive_diagnose(state_vector)
    
    # Secondary adjustment using flag INTERSECTION logic
    adjustment_factor = 0
    if flag_interpretation['CRITICAL'] and not flag_interpretation['INFO']:
        adjustment_factor += 3
    if flag_interpretation['FATAL']:
        adjustment_factor += 5
    
    # Final computation (answer point)
    final_diagnostic = (initial_diagnosis * 7 + adjustment_factor * 13) % 10000
    
    # Dead code branch (misleading)
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic) * 2
    
    return final_diagnostic

# Simulated input data (structured realistically)
log_entries = [
    {'code': 88, 'severity': 3, 'ts': 1678886400},
    {'code': 104, 'severity': 2, 'ts': 1678886401},
    {'code': 55, 'severity': 4, 'ts': 1678886402},
    {'code': 201, 'severity': 1, 'ts': 1678886403}
]
system_flags = 11  # Binary: 1011 -> FATAL=1, CRITICAL=1, WARNING=0, INFO=1

# Orchestration with red herring call
telemetry_snapshot = [{'signal': 850}, {'signal': 920}, {'signal': 700}]
_ = process_telemetry_chunk(telemetry_snapshot)  # Result ignored

# Actual target execution
final_diagnostic = analyze_system_state(log_entries, system_flags)
print(f"Result: {final_diagnostic}")