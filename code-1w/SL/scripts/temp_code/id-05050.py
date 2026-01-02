import math

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    signals = []
    for i in range(18):
        phase = i * 0.3
        signal_val = (math.sin(phase) * math.cos(phase * 1.5) + math.exp(-i / 20)) * 100
        signals.append(round(signal_val, 2))
    return signals

# Irrelevant helper: formats timestamps (not used in computation)
def format_timestamp(ts):
    hours = ts // 3600
    mins = (ts % 3600) // 60
    secs = ts % 60
    return f'{hours:02}:{mins:02}:{secs:02}'

# Decoy function: appears related but unused
validity_check = lambda x: all(v > -50 for v in x)

# Core pattern analyzer with red herrings and distractions
def analyze_pattern(logs, flags):
    # Irrelevant preprocessing block (dead path)
    temp_buffer = [x for x in logs if x > 10]
    if len(temp_buffer) < 5:
        temp_buffer.extend([0] * (5 - len(temp_buffer)))
    
    # Distractor: complex-looking but unused transformation
    transformed = list(map(lambda x: round(x ** 0.5 * 1.7, 3) if x > 0 else 0, logs))
    entropy_score = sum(math.log(abs(x) + 1) for x in transformed[:7])

    # Real computation begins here — subtle trigger condition
    critical_threshold = flags.get('activation_level', 0) > 3 and len(logs) % 2 == 0
    
    # Meaningful state accumulation
    state_vector = []
    for idx, val in enumerate(logs):
        if idx % 3 == 0:
            state_vector.append(val * 0.7)
        elif idx % 4 == 1 and val < 50:
            state_vector.append(val * 1.1)
    
    # Red herring: unused recursive counter
    def count_peaks(data, limit=10):
        if not data or limit <= 0:
            return 0
        return (1 if abs(data[0]) > 40 else 0) + count_peaks(data[1:], limit - 1)
    
    # Key branching logic — depends on flag combination
    mode_flag = flags.get('debug_mode') and flags.get('safe_override')
    base_accum = 0
    for v in state_vector:
        if mode_flag:
            base_accum += int(v) % 9
        else:
            base_accum += int(v * 0.9) % 7
    
    # Final calculation — only this matters
    adjustment = 0
    if critical_threshold:
        adjustment = 12
    elif flags.get('activation_level', 0) == 2:
        adjustment = 5

    # Real answer derived here
    result = int(sum(state_vector) % 1000) + adjustment

    # Distractor dictionary with plausible keys
    diagnostics = {
        'raw_count': len(logs),
        'peak_entropy': round(entropy_score, 3),
        'buffer_size': len(temp_buffer),
        'interim_total': sum(state_vector),
        'result_trace': base_accum,
        'final_diagnostic': result  # This is the actual output
    }
    
    return diagnostics['final_diagnostic']

# Unused set operations — red herring
exclusion_set = {x for x in range(5, 50, 7)}

# Main execution flow
if __name__ == '__main__':
    # Generate real data
    raw_signals = generate_telemetry()  # 18 elements, even length
    
    # Configuration with meaningful and misleading flags
    system_flags = {
        'activation_level': 4,           # Triggers critical_threshold
        'debug_mode': False,             # Affects base_accum path
        'safe_override': True,           # Paired with debug_mode
        'legacy_support': True,          # Unused
        'enable_audit': False          # Dead flag
    }
    
    # Dead code: string manipulation distraction
    log_id = "SYSLOG-2023"
    suffix = ''.join(sorted(set(log_id.split('-')[-1]), reverse=True))
    tag_code = int(suffix) % 13
    
    # Critical execution point
    final_diagnostic = analyze_pattern(raw_signals, system_flags)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")