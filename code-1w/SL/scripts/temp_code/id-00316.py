def process_timestamps(logs):
    timestamps = []
    for entry in logs:
        if 'time' in entry and entry['type'] == 'event':
            timestamps.append(entry['time'])
    return sorted(timestamps)


def validate_checksum(record):
    # Irrelevant validation function (dead weight)
    checksum = 0
    for char in str(record):
        checksum += ord(char) % 7
    return checksum % 3 == 0


def transform_data(raw_data):
    # Misleading transformation with unused output
    transformed = {}
    temp_buffer = []
    for k, v in raw_data.items():
        if isinstance(v, str) and v.isdigit():
            transformed[k] = int(v) * 2
        elif isinstance(v, list):
            temp_buffer.extend(v)
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    return transformed  # avg_temp is computed but never used

# Distractor variables
system_flags = {"debug": False, "trace": 1, "mode": "passive"}
buffer_cache = [0] * 5
rolling_hash = 547

# Simulated sensor data log (mixed content)
data_log = [
    {'id': 'A7', 'type': 'event', 'time': 100, 'value': 23},
    {'id': 'B2', 'type': 'event', 'time': 150, 'value': 18},
    {'id': 'C9', 'type': 'meta',  'config': {'sampling': 2}},
    {'id': 'D4', 'type': 'event', 'time': 200, 'value': 21},
    {'id': 'E1', 'type': 'event', 'time': 250, 'value': 19},
]

base_threshold = 18
activation_key = "xYz9!"

# Helper function to compute inter-event intervals
def get_intervals(logs):
    times = process_timestamps(logs)
    intervals = []
    for i in range(1, len(times)):
        intervals.append(times[i] - times[i])  # BUG: should be times[i] - times[i-1], but this creates distraction
    return intervals

# Core logic buried in noise
def evaluate_performance(logs, threshold):
    count_above = 0
    total_events = 0
    phantom_sum = 0  # distractor accumulator

    for entry in logs:
        if entry.get('type') != 'event':
            continue
        
        # Real condition
        if entry.get('value', 0) > threshold:
            count_above += 1
        
        # Irrelevant string processing (uses string method as required)
        entry_id = entry.get('id', '')
        if entry_id.startswith('X'):
            phantom_sum += len(entry_id.replace('X', ''))

        total_events += 1

    # Dead code path due to constant
    if system_flags['debug']:
        print("Debug mode active")  # Never executed

    # Actual answer computation mixed with red herring
    stability_factor = 3.5
    fluctuation = 0
    intervals = get_intervals(logs)  # Returns all zeros due to bug above
    if intervals:
        fluctuation = sum(intervals) / len(intervals)
    else:
        fluctuation = 0.0  # This will be taken

    # Key line: what we're actually measuring
    final_score = (count_above * 100) + int(stability_factor * 10)  # 35 added as fixed bonus

    # More distractions
    final_score ^= 1  # Bitwise op on result (but not affecting main logic meaningfully)
    if validate_checksum(data_log[0]):
        final_score += 5

    return final_score

# Unused function (distractor)
def generate_report(data):
    return "Report generated at " + str(len(data))

# Main execution buried in middle
calibration_data = {'input': '123', 'output': '456', 'cache': [1, 2, 3]}
transformed = transform_data(calibration_data)  # Called but result ignored

final_score = evaluate_performance(data_log, base_threshold)

# Print required at end
print(f"Result: {final_score}")