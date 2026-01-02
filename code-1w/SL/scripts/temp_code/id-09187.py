import itertools

def analyze_pattern(sequence):
    # Irrelevant function - dead code path
    return sum(a * b for a, b in zip(sequence, sequence[1:]))

def decode_signal(signal_str):
    # Distractor: complex string decoding with no impact on final result
    rotated = ''.join([chr((ord(c) - ord('a') + 3) % 26 + ord('a')) for c in signal_str if c.isalpha()])
    return rotated[::-1]

def evaluate_stability(index, readings):
    # Misleading intermediate computation
    base = sum(readings) / len(readings)
    variance = sum((x - base) ** 2 for x in readings) / len(readings)
    return variance < 5.0

def extract_features(data_stream):
    # Unused feature extractor - red herring
    chunks = [data_stream[i:i+4] for i in range(0, len(data_stream), 4)]
    features = {}
    for i, chunk in enumerate(chunks):
        features[f'chunk_{i}'] = sum(ord(c) for c in chunk)
    return features

def main():
    # Simulated system telemetry log
    log_entries = [
        {'timestamp': 1001, 'power_draw': 230, 'temp_core': 67, 'fan_speed': 2100},
        {'timestamp': 1002, 'power_draw': 235, 'temp_core': 68, 'fan_speed': 2150},
        {'timestamp': 1003, 'power_draw': 240, 'temp_core': 66, 'fan_speed': 2200},
        {'timestamp': 1004, 'power_draw': 250, 'temp_core': 70, 'fan_speed': 2300},
        {'timestamp': 1005, 'power_draw': 260, 'temp_core': 72, 'fan_speed': 2400}
    ]

    # Real-time sensor buffer - irrelevant to final answer but looks important
    sensor_buffer = []
    for entry in log_entries:
        if entry['temp_core'] > 65:
            sensor_buffer.append(entry['fan_speed'])

    # Construct diagnostic snapshot (this is where relevant data starts)
    log_snapshot = []
    for entry in log_entries:
        status_flag = 0
        if entry['power_draw'] > 245:
            status_flag |= 0b1000  # High power draw
        if entry['temp_core'] > 70:
            status_flag |= 0b0100  # Overheating
        if entry['fan_speed'] > 2250:
            status_flag |= 0b0010  # High fan activity
        log_snapshot.append(status_flag)

    # System health vector - derived from real conditions
    system_health = []
    for entry in log_entries:
        if entry['power_draw'] > 255:
            system_health.append(3)
        elif entry['temp_core'] > 71:
            system_health.append(2)
        elif entry['fan_speed'] > 2350:
            system_health.append(1)
        else:
            system_health.append(0)

    # DEAD CODE PATH - misleading complexity
    signal_input = "xqrsabct"
    decoded = decode_signal(signal_input)
    pattern_data = [1, 1, 2, 3, 5, 8]
    stability = evaluate_stability(42, pattern_data)

    # REAL COMPUTATION STARTS HERE ---
    def process_metrics(snapshot, health_levels):
        cumulative_risk = 0
        # Bit analysis of log flags
        for flag in snapshot:
            # Count set bits in status flag (complex-looking but straightforward)
            bit_count = bin(flag).count('1')
            cumulative_risk += bit_count * 10

        # Apply health multipliers
        multiplier = 1
        for level in health_levels:
            if level == 3:
                multiplier *= 1.5
            elif level == 2:
                multiplier *= 1.2

        intermediate = cumulative_risk * multiplier

        # Final transformation using dictionary mapping (actual key step)
        severity_map = {0: 1, 1: 3, 2: 7, 3: 15}
        adjustment = 0
        for level in health_levels:
            if level in severity_map:
                adjustment += severity_map[level]

        # Combine with string-derived constant (but string part is fixed)
        metadata_tag = "SYSLOG-2024"
        version_salt = int(metadata_tag.split('-')[1])  # 2024

        # Core formula - only this produces the answer
        result = (intermediate + adjustment) - (version_salt // 100)

        # Introduce unused variables for distraction
        anomaly_score = list(itertools.accumulate([adjustment, intermediate]))
        baseline_ref = analyze_pattern([1, 2, 3, 4])

        return int(result)

    # Execution point of interest
    final_diagnostic = process_metrics(log_snapshot, system_health)
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()