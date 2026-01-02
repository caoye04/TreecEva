import math

# System diagnostic simulation with heavy distractions

# Irrelevant sensor arrays (distractor data)
sensor_readings_a = [0.1, 0.4, 0.9, 1.3, 2.1]
sensor_readings_b = [x ** 2 for x in sensor_readings_a if x > 0.5]
buffer_cache = {i: sensor_readings_a[i] * 17 for i in range(len(sensor_readings_a))}

# Decoy function - looks important but unused
def calculate_fusion_score(data):
    return sum([math.sin(x) * 2 for x in data]) // len(data)

# Unused calibration map (dead code path)
calibration_map = {
    'alpha': 0.91,
    'beta': 1.03,
    'gamma': 0.87,
    'delta': None  # Invalid entry
}

# Simulated telemetry stream (partially relevant)
telemetry_stream = [
    {'time': 1001, 'val': 42, 'type': 'temp'},
    {'time': 1002, 'val': 38, 'type': 'temp'},
    {'time': 1003, 'val': 45, 'type': 'pressure'}
]

# Extract temperature values (only partially used)
temps = [entry['val'] for entry in telemetry_stream if entry['type'] == 'temp']
avg_temp = sum(temps) / len(temps) if temps else 0

# Core system status dictionary (critical)
system_status = {
    'core_health': 89,
    'subsystem_flag': 0b1010,
    'uptime_days': 367,
    'version_hash': 0xDEADBEEF
}

# Red herring variables
legacy_mode_active = False
debug_override = None
fallback_threshold = float('inf')

# Bit manipulation decoy (looks computational but irrelevant)
masked_flag = system_status['subsystem_flag'] & 0b1100
shifted_flag = masked_flag << 4
inverted_flag = ~shifted_flag & 0xFFFF  # 16-bit inversion

# Spurious mathematical transformations
baseline_offset = math.log(1 + avg_temp, 2) * 100
noise_factor = math.sin(0.1 * system_status['uptime_days'])

# Unused health formula variant
effective_health_v1 = (
    system_status['core_health'] * 0.9 + 
    (100 - abs(noise_factor * 10)) * 0.1
)

# Dictionary-based conditional routing (some branches dead)
routing_table = {
    89: 'PATH_A',
    90: 'PATH_B',
    91: 'PATH_C'
}

execution_path = routing_table.get(system_status['core_health'], 'DEFAULT_PATH')

# Health multiplier determined by core health (relevant logic starts)
if system_status['core_health'] > 90:
    health_multiplier = 1.2
elif system_status['core_health'] == 89:
    health_multiplier = 1.1  # Critical branch
else:
    health_multiplier = 0.95

# Secondary correction factor based on uptime (distractor)
if system_status['uptime_days'] > 365:
    annual_degradation = 0.01
else:
    annual_degradation = 0.005

# Offset correction using modular arithmetic (relevant)
offset_seed = system_status['version_hash'] % 1000
offset_correction = (offset_seed - 941)  # (0xDEADBEEF % 1000) = 975 → 975 - 941 = 34

# Final diagnostic computation (key statement)
final_diagnostic = system_status.get('core_health', 0) * health_multiplier + offset_correction

# Print result as required
print(f"Result: {final_diagnostic}")