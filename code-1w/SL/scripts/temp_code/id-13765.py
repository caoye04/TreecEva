import math

# Simulated system telemetry data
temperature_readings = [23.5, 24.1, 25.0, 26.8, 27.3, 25.9, 24.7]
humidity_levels = [45, 47, 50, 55, 60, 58, 52]
error_flags = [False, False, True, False, False, True, False]

# Irrelevant auxiliary data (distraction)
color_palette = ['#FF5733', '#33FF57', '#3357FF']
user_preferences = {'theme': 'dark', 'notifications': True}

# System state with nested structure (mix of relevant and irrelevant fields)
system_state = {
    'core_temp': 67.4,
    'voltage_stable': True,
    'fan_speed_rpm': 1200,
    'uptime_hours': 873,
    'last_reboot_cause': 'overheat',
    'debug_mode': False,
    'cache_health': 'optimal',
    'bandwidth_usage': 74.2
}

# Log entries containing mixed operational events
log_entries = [
    {'timestamp': 1680001, 'level': 'INFO', 'msg': 'System booted successfully'},
    {'timestamp': 1680002, 'level': 'WARN', 'msg': 'High temp detected in sector 3'},
    {'timestamp': 1680003, 'level': 'ERROR', 'msg': 'Sensor failure: humidity'},
    {'timestamp': 1680004, 'level': 'INFO', 'msg': 'Fan speed increased'},
    {'timestamp': 1680005, 'level': 'DEBUG', 'msg': 'Memory pressure low'},
    {'timestamp': 1680006, 'level': 'INFO', 'msg': 'Stabilization achieved'}
]

# Decoy function - looks important but unused (dead code path)
def analyze_color_scheme(palette):
    return sum([int(c[1:3], 16) for c in palette]) // len(palette)

# Auxiliary transformation with partial relevance
def extract_severity_level(msg: str) -> int:
    if 'ERROR' in msg.upper():
        return 3
    elif 'WARN' in msg.upper():
        return 2
    elif 'CRITICAL' in msg.upper():
        return 4
    return 1

# Bit manipulation for checksum simulation (partial red herring)
def compute_checksum(data_list):
    chk = 0
    for entry in data_list:
        chk ^= hash(entry['msg']) & 0xFFFF  # Only use lower 16 bits
    return chk % 1000

# Real processing begins here — complex logic chain

# Step 1: Count uppercase letters across all log messages (string method usage)
total_caps = sum(len([c for c in entry['msg'] if c.isupper()]) for entry in log_entries)

# Step 2: Compute average temperature from sensor array (arithmetic)
avg_temp = sum(temperature_readings) / len(temperature_readings)

# Step 3: Determine stability flag using conditional expression
system_stable = system_state['voltage_stable'] and avg_temp < 26.5
status_flag = 1 if system_stable else 0

# Step 4: Count error occurrences in logs using list comprehension and string matching
error_count = len([e for e in log_entries if e['level'] == 'ERROR'])

# Step 5: Extract message lengths and apply bitwise AND with severity
length_severity_product = 1
for entry in log_entries:
    severity = extract_severity_level(entry['msg'])
    length = len(entry['msg'])
    # Use XOR to obfuscate relevance
    masked = (length ^ severity) & 0xFF
    length_severity_product *= min(masked, 50)  # Prevent overflow

# Step 6: Apply logarithmic scaling only if conditions met
if error_count > 0 and not system_stable:
    scaled_score = math.log(length_severity_product) * 0.8
else:
    scaled_score = math.sqrt(length_severity_product) * 0.3

# Step 7: Analyze timestamp deltas (control flow + arithmetic)
timestamps = [entry['timestamp'] for entry in log_entries]
deltas = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
avg_delta = sum(deltas) / len(deltas)

# Step 8: Generate diagnostic weight based on uptime and fan speed
hours = system_state['uptime_hours']
speed = system_state['fan_speed_rpm']
weight_factor = (hours // 100) + (speed // 400)

# Step 9: Combine multiple metrics into composite index
raw_index = (total_caps * 100) + (error_count * 500) + int(scaled_score)

# Step 10: Apply conditional adjustment based on system state
adjustment = -1000 if system_state['last_reboot_cause'] == 'overheat' else 500
adjusted_index = raw_index + adjustment

# Step 11: Final transformation involving dictionary lookup and case conversion (string method)
level_map = {'INFO': 0, 'WARN': 1, 'ERROR': 2, 'DEBUG': -1}
first_msg_type = log_entries[0]['level'].upper()  # Redundant .upper()
base_offset = level_map.get(first_msg_type, 0)

# Step 12: Critical statement — final computation
final_diagnostic = adjusted_index + base_offset * 100 + weight_factor * 25

# Print result for evaluation
print(f"Result: {final_diagnostic}")