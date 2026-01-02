from collections import defaultdict, Counter
import math

# Simulated system telemetry processing with extensive distractors
def analyze_subsystem_health(sensor_data, thresholds):
    temp_readings = []
    pressure_peaks = []
    checksum = 0
    anomaly_count = 0  # Distractor: not used in final result

    for entry in sensor_data:
        temp_readings.append(entry['temp'])
        if entry['pressure'] > thresholds['pressure']:
            pressure_peaks.append(entry['pressure'])
        # Red herring computation
        checksum ^= int(entry['temp'] * 10) % 256

    avg_temp = sum(temp_readings) / len(temp_readings)
    high_pressure_count = len(pressure_peaks)
    return {'avg_temp': avg_temp, 'high_pressure_count': high_pressure_count}

# Legacy function - dead code path (never called)
def deprecated_diagnostic(sequence):
    bit_pattern = 0
    for x in sequence:
        bit_pattern |= (1 << (x % 8))
    return bin(bit_pattern).count('1')

# Core signal analysis with multiple distractions
def extract_timing_signature(raw_signal):
    window_size = 4
    filtered = []
    noise_floor = 0.05
    spike_count = 0

    for i in range(len(raw_signal) - window_size + 1):
        segment = raw_signal[i:i+window_size]
        energy = sum(x**2 for x in segment)
        if energy > noise_floor:
            filtered.append(energy ** 0.5)
            if energy > 0.2:
                spike_count += 1  # Distractor

    # Meaningless transformation
    normalized = [max(0, math.log(f + 1e-8)) for f in filtered]
    return filtered  # Actual return used downstream

# Complex data transformation with decoy logic
def compute_phase_offset(buffers):
    offset_map = defaultdict(int)
    total_swaps = 0

    for buf in buffers:
        arr = list(buf)
        swaps = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1
        total_swaps += swaps
        offset_map[swaps % 5] += 1

    mode_class = max(offset_map, key=lambda k: offset_map[k])
    return mode_class * 0.25  # Unused in final flow

# Primary metric aggregator - this contains the real logic path
def aggregate_metrics(log_entries, flags):
    timing_values = []  
    flag_summary = Counter(flags)
    base_score = 0
    intermediate_result = 0

    # Real processing begins here
    for record in log_entries:
        timestamp_str = record['time']
        seconds_part = int(timestamp_str.split('.')[1][:3])  # milliseconds
        micro_shift = seconds_part % 7  # meaningful variation
        
        duration = record['duration']
        # Key calculation embedded in noise
        if duration > 0:
            normalized = math.log(duration) * (micro_shift + 1)
            timing_values.append(normalized)

        # Distractor block: irrelevant flag analysis
        if flag_summary.get('critical', 0) > 3:
            base_score += 10
        elif flag_summary.get('warning', 0) > 10:
            base_score -= 5

    # Decoy data structure manipulation
    history = set()
    running = []
    for v in timing_values:
        truncated = int(v * 100) % 100
        history.add(truncated)
        if truncated % 3 == 0:
            running.append(truncated / 10)

    # Actual answer computation (non-obvious)
    accumulator = 0
    weight_sequence = [1, 2, 1, 3, 1]
    for i, val in enumerate(timing_values):
        w = weight_sequence[i % len(weight_sequence)]
        accumulator += val * w

    final_adjustment = len(history) % 4  # minor modifier
    intermediate_result = accumulator + final_adjustment

    # Final transformation using string slicing red herring
    hex_rep = hex(int(intermediate_result * 100) % 256)[2:]
    padded = ('0' + hex_rep)[-2:]  # always 2 chars
    # But actual answer doesn't use this

    # Answer is here - derived purely from weighted sum + history size
    result = round(intermediate_result, 4)

    # Irrelevant tuple unpacking distraction
    metadata = ('SYS_DIAG_7', 'v2.1', 'UTC')
    system_id, version, tz = metadata

    return result

# Generate test input data
if __name__ == '__main__':
    # Construct realistic telemetry stream
    timing_log = [
        {'time': '12:34:56.123', 'duration': 2.718},
        {'time': '12:34:57.234', 'duration': 3.141},
        {'time': '12:34:58.345', 'duration': 1.414},
        {'time': '12:34:59.456', 'duration': 0.577},
        {'time': '12:35:00.567', 'duration': 1.732}
    ]

    fault_flags = ['info'] * 4 + ['warning'] * 6 + ['critical'] * 2 + ['debug'] * 8

    # Execute core analysis
    signal_data = [0.01, 0.06, 0.25, 0.08, 0.02, 0.35, 0.15]  # unused but looks important
    processed_signal = extract_timing_signature(signal_data)

    # Fake subsystem buffer data
    test_buffers = [
        [3, 1, 4, 2],
        [5, 9, 2, 6],
        [1, 1, 8, 3]
    ]
    phase_shift = compute_phase_offset(test_buffers)

    # Real diagnostic execution
    sensor_telemetry = [
        {'temp': 23.5, 'pressure': 101.3},
        {'temp': 24.1, 'pressure': 102.0},
        {'temp': 22.8, 'pressure': 99.7}
    ]
    health_report = analyze_subsystem_health(
        sensor_telemetry,
        {'pressure': 100.0}
    )

    # Critical statement: where the answer is determined
    final_diagnostic = aggregate_metrics(timing_log, fault_flags)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")