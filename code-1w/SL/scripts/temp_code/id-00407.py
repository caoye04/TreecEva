def process_system_diagnostics(raw_data, threshold=0.75):
    # Irrelevant preprocessing: string cleaning
    sanitized = ''.join(filter(str.isalnum, raw_data.lower()))
    tokens = [sanitized[i:i+4] for i in range(0, len(sanitized), 4)]
    token_lengths = list(map(len, tokens))

    # Distractor: unused checksum calculation
    checksum = 0
    for char in raw_data:
        if char.isdigit():
            checksum = (checksum * 31 + int(char)) % 97

    # Real data structures
    timing_log = []
    error_flags = []
    warnings_issued = 0

    # Simulated parsing of diagnostic entries
    lines = raw_data.strip().split('\n')
    for line in lines:
        parts = line.split(',')
        if len(parts) < 3:
            continue

        try:
            latency = float(parts[1])
            cpu_load = float(parts[2])
            status = parts[0]

            # Relevant conditional logic with nesting
            if 'ERR' in status:
                if latency > 200:
                    error_flags.append(3)
                elif cpu_load > 85:
                    error_flags.append(2)
                else:
                    error_flags.append(1)
            elif 'WARN' in status and cpu_load > 75:
                warnings_issued += 1

            # Accumulate only successful or monitored timings
            if latency > 0:
                timing_log.append(latency)

            # Dead code path - never accessed due to structure
            if False:
                backup_entry = {'latency': latency, 'flag': 'none'}
                timing_log.append(backup_entry)  # Would break type consistency

        except (ValueError, IndexError):
            pass  # Silent ignore - realistic but distracting

    # Distractor: complex unused lambda
    severity_rank = lambda x: sum(1 for v in x if v > threshold * max(x)) if x else 0
    rank_score = severity_rank([len(error_flags), warnings_issued * 2])

    # Another red herring: bitwise obfuscation (unused)
    obfuscated = 0
    for val in token_lengths:
        obfuscated ^= (val << 2) | (val >> 1)

    # Core logic: count significant errors
    errors_detected = sum(flag for flag in error_flags if flag >= 2)

    # Critical function with meaningful computation
    def aggregate_metrics(times, errors):
        if not times:
            return 0
        avg_time = sum(times) / len(times)
        peak = max(times)
        penalty = errors * 17
        score = int((avg_time / (peak + 1e-5)) * 100) - penalty
        return abs(score)  # Final deterministic scalar

    final_diagnostic = aggregate_metrics(timing_log, errors_detected)
    print(f"Result: {final_diagnostic}")

# Simulated input resembling system logs
data_input = """
OK,120.5,65.2
ERR,210.0,90.1
WARN,180.3,78.4
ERR,80.0,88.0
OK,95.7,60.1
UNKNOWN,50.0,55.0
ERR,300.2,40.0
"""

process_system_diagnostics(data_input)