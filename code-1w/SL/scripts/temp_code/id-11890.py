from collections import defaultdict, Counter

# Simulated system telemetry data
timestamps = [100, 105, 112, 120, 125, 134, 140, 148]
fault_codes = [0, 1, 0, 1, 1, 0, 1, 0]
sensor_readings = [23.1, 24.5, 25.3, 26.0, 25.8, 27.1, 28.0, 29.2]

def analyze_sequence(times, codes, readings):
    # Irrelevant transformation: time deltas (used in decoy logic)
    time_deltas = []
    for i in range(1, len(times)):
        time_deltas.append(times[i] - times[i-1])
    
    # Decoy counter: tracks something meaningless
    decoy_counter = defaultdict(int)
    for delta in time_deltas:
        decoy_counter[delta % 3] += 1
    
    # Real processing starts: correlate faults with rising trends
    trend_breaks = 0
    for i in range(1, len(readings)):
        if readings[i] > readings[i-1]:
            if codes[i] == 1:
                trend_breaks += 1

    # Unused recursive helper (dead code path)
    def unused_recursive(n):
        if n <= 1:
            return 1
        return n * unused_recursive(n - 2)

    # Simulated timing log with metadata tags
    timing_log = []
    for idx, t in enumerate(timestamps):
        entry = {
            'tick': t,
            'phase': 'A' if t % 2 == 0 else 'B',
            'tag': (t // 10) ^ 7  # bitwise XOR red herring
        }
        timing_log.append(entry)
    
    # Fault flags with bit encoding (only one bit matters)
    fault_flags = []
    mask = 0b1101
    for code in fault_codes:
        encoded = (code << 3) | 5
        decoded_hint = (encoded & mask) >> 2  # misleading intermediate
        fault_flags.append(bool(encoded & 0b1000))
    
    # Redundant zip-enumerate loop with no side effects
    temp_accum = 0
    for i, (t, r) in enumerate(zip(timestamps, sensor_readings)):
        if i % 2 == 0:
            temp_accum += int(r) ^ i
    
    # Critical function buried in middle
    def aggregate_metrics(log_entries, faults):
        # Only this part matters
        valid_ticks = []
        for entry, flag in zip(log_entries, faults):
            if flag and entry['phase'] == 'A':
                valid_ticks.append(entry['tick'])
        
        # Real computation: sum of valid ticks mod 1000 plus number of faults
        base_sum = sum(valid_ticks) % 1000
        fault_count = sum(1 for f in faults if f)
        magic_offset = 0
        
        # Hidden adjustment: only when tick divisible by 7 occurs in phase A with fault
        for entry, f in zip(log_entries, faults):
            if f and entry['phase'] == 'A' and entry['tick'] % 7 == 0:
                magic_offset = 17
        
        return base_sum + fault_count + magic_offset
    
    final_diagnostic = aggregate_metrics(timing_log, fault_flags)
    return final_diagnostic

result = analyze_sequence(timestamps, fault_codes, sensor_readings)
print(f"Target result: {result}")