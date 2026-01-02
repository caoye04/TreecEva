from collections import defaultdict, Counter
import math

# System health monitoring simulation with diagnostic computation

# Simulated sensor inputs (irrelevant to final result)
sensor_readings = [0.88, 0.91, 0.85, 0.93, 0.87, 0.89, 0.90]
smoothed_signal = sum(sensor_readings) / len(sensor_readings)
spike_detected = any(x > 0.92 for x in sensor_readings)

# Legacy calibration data — red herring
CALIBRATION_MAP = {
    'A': 0.1, 'B': 0.2, 'C': 0.15, 'D': 0.25, 'E': 0.18
}
legacy_adjustment = sum(CALIBRATION_MAP.values()) * 100

# Irrelevant string transformation chain
device_id = 'SYS-9X'
id_parts = device_id.split('-')
base_code = ord(id_parts[1][0]) * 2
temp_key = ''.join([chr(base_code + i) for i in range(3)])
key_hash = hash(temp_key) % 1000

# Core diagnostic logic disguised among distractions
def compute_stability_index(config): 
    base = config.get('threshold', 1) ** 2
    offset = config.get('damping', 1) * 3
    return (base + offset) % 7

def analyze_pattern(sequence):
    # Unused function — dead code path
    freq = defaultdict(int)
    for item in sequence:
        freq[item] += 1
    return max(freq.values())

# Bit manipulation decoy
flag_register = 0b101101
mask = 0b110011
masked_value = flag_register & mask
shifted_flag = masked_value << 2
is_active = bool(shifted_flag & 0b1000000)

# Primary data structure for analysis
failure_modes = [
    {'type': 'overload', 'severity': 3, 'timestamp': 1623456780},
    {'type': 'leak', 'severity': 2, 'timestamp': 1623456800},
    {'type': 'overload', 'severity': 4, 'timestamp': 1623456820},
    {'type': 'corrosion', 'severity': 1, 'timestamp': 1623456840}
]

# Distractor: unused aggregation
event_counter = Counter([mode['type'] for mode in failure_modes])
most_common_failure = event_counter.most_common(1)

# Relevant but obscured calculation chain
baseline_config = {'threshold': 5, 'damping': 4}
stability = compute_stability_index(baseline_config)  # Result: (25 + 12) % 7 = 37 % 7 = 2

# Complex tuple unpacking and transformation (partial red herring)
data_points = [(1, 4), (2, 5), (3, 6)]
processed = []
for a, b in data_points:
    processed.append((a * 2) + (b // 2))

# Real signal extraction via dictionary operation
diag_signals = {'stability': stability, 'load': 8, 'temp': 45}
active_signals = {k: v for k, v in diag_signals.items() if v > 3}  # {'load': 8, 'temp': 45}

# Core arithmetic hidden in min/max chain
extreme_vals = [diag_signals['stability'], 10, -5, 12]
adjusted_min = min(extreme_vals) + 7  # -5 + 7 = 2
adjusted_max = max(extreme_vals) - 4  # 12 - 4 = 8
aggregate_score = adjusted_min * adjusted_max  # 2 * 8 = 16

# Misleading offset from string operation
version_tag = 'v2.4-release'
version_digits = [int(c) for c in version_tag if c.isdigit()]
system_offset = version_digits[0] - version_digits[1] + 10  # 2 - 4 + 10 = 8

# Decoy list comprehension with side-effect-free mutation
_ = [x**2 for x in range(5) if x % 2 == 0]

# Key statement — target of query
final_diagnostic = aggregate_score + system_offset

# Output required format
print(f"Result: {final_diagnostic}")