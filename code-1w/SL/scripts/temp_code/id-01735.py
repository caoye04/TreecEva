def analyze_sensor(network_state):
    if not network_state:
        return 0
    return sum(ord(c) for c in network_state[:3]) % 7

def decode_signal(signal):
    base = 0
    for i, val in enumerate(signal):
        base += val * (2 ** (i % 4))
    return base % 13

def shift_buffer(buffer, offset):
    return [buffer[(i + offset) % len(buffer)] for i in range(len(buffer))]

def generate_checksum(data_list):
    total = 0
    for item in data_list:
        if isinstance(item, int):
            total += item ^ 5
    return total % 1000

def validate_entry(record):
    return record.get('status') == 'active' and record['value'] > 0

# Irrelevant telemetry processing (red herring)
telemetry_logs = [
    {'node': 'A1', 'signal': [1, 0, 1], 'timestamp': 1623456789},
    {'node': 'B2', 'signal': [0, 1, 1], 'timestamp': 1623456790}
]

for log in telemetry_logs:
    decoded = decode_signal(log['signal'])
    delay_comp = (log['timestamp'] * decoded) % 11

# Real input data
raw_readings = [18, 22, 15, 30, 12, 25, 14, 20]

# Distractor: unused transformation
shifted_readings = shift_buffer(raw_readings, 3)
sorted_readings = sorted(shifted_readings, reverse=True)

# Threshold configuration map (used later)
threshold_map = {
    'low_power': 18,
    'overload': 25,
    'critical': 30
}

# Filtering logic with string-based flags
filter_flags = ['valid', 'active', 'primary']
flag_summary = ''.join(filter_flags).upper().replace('I', '1')

filtered_data = []
for val in raw_readings:
    flag_char = chr(val % 26 + ord('A'))
    if flag_char in 'ABCDEFGHIJKLMNOPQR':
        filtered_data.append(val)

# Dead code path - never called
def deprecated_analysis(x):
    return x * 17 % 19

# Another red herring: checksum on irrelevant list
auxiliary_data = [5, 9, 14, 8, 2]
generate_checksum(auxiliary_data)  # result unused

# Conditional mutation based on dummy network state
network_status = 'STANDBY'
diag_code = analyze_sensor(network_status)

if diag_code > 4:
    filtered_data = [x + 2 for x in filtered_data]
elif diag_code == 2:
    filtered_data = [x - 1 for x in filtered_data]

# Key function combining dictionary and list operations
def process_readings(data, thresholds):
    result = 0
    stats = {}
    
    # Dictionary accumulation
    for key, thresh in thresholds.items():
        count = len([v for v in data if v >= thresh])
        stats[key] = count
    
    # String manipulation side computation (distractor)
    stat_keys = ''.join(sorted(stats.keys()))
    magic_shift = sum(ord(c) for c in stat_keys) % 5
    
    # Core arithmetic logic
    overload_events = stats['overload']
    baseline = stats['low_power'] * 7
    critical_load = stats['critical'] * 15
    
    intermediate = baseline + overload_events * 12
    
    # Final computation
    result = intermediate - critical_load + magic_shift
    
    # Dead branch (never executes due to values)
    if len(data) < 5 and 'X' in stat_keys:
        result *= 2  
    
    return result

# Trigger point: this assignment determines the answer
final_diagnostic = process_readings(filtered_data, threshold_map)

print(f"Result: {final_diagnostic}")