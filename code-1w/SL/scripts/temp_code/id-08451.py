import math

# Simulated system telemetry logs with diagnostic flags
telemetry_logs = [
    {'timestamp': 1001, 'power_draw': 230.5, 'temp_core': 67.3, 'status_flag': 0b1010, 'checksum': 17},
    {'timestamp': 1002, 'power_draw': 235.1, 'temp_core': 69.1, 'status_flag': 0b1110, 'checksum': 19},
    {'timestamp': 1003, 'power_draw': 228.7, 'temp_core': 70.5, 'status_flag': 0b1011, 'checksum': 23},
    {'timestamp': 1004, 'power_draw': 245.3, 'temp_core': 72.8, 'status_flag': 0b1111, 'checksum': 29},
    {'timestamp': 1005, 'power_draw': 250.0, 'temp_core': 74.2, 'status_flag': 0b0111, 'checksum': 31},
    {'timestamp': 1006, 'power_draw': 260.8, 'temp_core': 76.9, 'status_flag': 0b1101, 'checksum': 37},
    {'timestamp': 1007, 'power_draw': 255.4, 'temp_core': 75.1, 'status_flag': 0b1001, 'checksum': 41},
    {'timestamp': 1008, 'power_draw': 248.9, 'temp_core': 73.6, 'status_flag': 0b1110, 'checksum': 43}
]

# Irrelevant auxiliary data (distractor)
system_matrix = [[i * j for j in range(5)] for i in range(5)]
compression_key = sum([sum(row) for row in system_matrix])
encoding_shift = (compression_key % 7) + 3

# Redundant checksum validator (unused path)
def validate_log_checksum(log):
    base = log['timestamp'] % 100 + int(log['power_draw'])
    return (base ^ 13) == log['checksum']

# Misleading transformation chain (dead code)
transformed_diagnostics = []
for log in telemetry_logs:
    temp_adj = (log['temp_core'] * 1.02) - 2.1
    power_factor = math.log(log['power_draw'], 10) * 100
    dummy_metric = (temp_adj ** 2) / (power_factor + 1)
    transformed_diagnostics.append({'adjusted_temp': temp_adj, 'efficiency': power_factor, 'score': dummy_metric})

# Decoy aggregation function (never called)
def compute_health_score(logs):
    score = 0
    for lg in logs:
        if lg['temp_core'] > 70:
            score += (lg['power_draw'] / lg['temp_core']) * 5
    return round(score, 3)

# Real processing begins here — filter logs where high temp and critical status overlap
active_alarms = []
for entry in telemetry_logs:
    temp_high = entry['temp_core'] > 70.0
    status_critical = (entry['status_flag'] & 0b1100) == 0b1100  # Checks bits 3 and 4 set
    recent = entry['timestamp'] > 1002
    if temp_high and status_critical and recent:
        active_alarms.append(entry)

# Further filtering using modular arithmetic on checksums (key logic)
valid_checksums = [p['checksum'] for p in telemetry_logs]
prime_like = [c for c in valid_checksums if all(c % n != 0 for n in range(2, int(math.sqrt(c)) + 1)) and c > 10]

# Distractor: simulate noise injection (unused)
noise_pattern = [(i * encoding_shift) % 11 for i in range(10)]
scrambled_indices = [abs(hash(str(np)) % 8) for np in noise_pattern]

# Actual filtering based on status and checksum criteria
filtered_logs = []
for log in telemetry_logs:
    meets_temp_power = log['power_draw'] > 240.0 and log['temp_core'] >= 72.0
    has_valid_status = (log['status_flag'] & 0b1110) >> 1 >= 5  # Right-shifted comparison
    correct_checksum = log['checksum'] in prime_like
    if meets_temp_power and has_valid_status and correct_checksum:
        filtered_logs.append(log)

# Auxiliary computation (distractor): average without usage
avg_power_surge = sum([l['power_draw'] for l in filtered_logs]) / len(filtered_logs) if filtered_logs else 0
projected_load = avg_power_surge * 1.15

# Core metric calculation: XOR of shifted checksums modulated by temperature
def aggregate_metrics(logs):
    if not logs:
        return -1
    raw_values = [l['checksum'] << 2 for l in logs]  # Left shift by 2
    shifted_sum = sum(raw_values)
    temp_mod = sum([int(l['temp_core']) for l in logs]) % 17
    combined = shifted_sum ^ temp_mod  # Bitwise XOR
    adjustment = math.sin(len(logs) * math.pi / 4)  # Periodic decimal factor
    final = combined * (1 + abs(adjustment))
    return int(final)

# Critical assignment point
final_diagnostic = aggregate_metrics(filtered_logs)

# Output result as required
print(f"Result: {final_diagnostic}")