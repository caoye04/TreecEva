from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and metadata
data = [
    {'temp': 23.5, 'humidity': 45, 'status': 'active', 'sensor_id': 'S001'},
    {'temp': 25.1, 'humidity': 52, 'status': 'active', 'sensor_id': 'S002'},
    {'temp': 19.8, 'humidity': 60, 'status': 'idle',  'sensor_id': 'S003'},
    {'temp': 27.3, 'humidity': 41, 'status': 'active', 'sensor_id': 'S004'},
    {'temp': 22.0, 'humidity': 56, 'status': 'active', 'sensor_id': 'S005'}
]

# Irrelevant auxiliary mapping (distractor)
sensor_locations = {
    'S001': 'Room A', 'S002': 'Room B', 'S003': 'Storage',
    'S004': 'Hallway', 'S005': 'Lab'
}

# Weight configuration for scoring (only temp and humidity are used)
weights = {
    'temp': 0.6,
    'humidity': 0.4,
    'status_penalty': -5,
    'fake_param': 100  # Unused weight (red herring)
}

# Noise filter threshold (misleading computation)
noise_threshold = 0.5
filtered_readings = []
for entry in data:
    if abs(entry['temp'] - 22.0) > noise_threshold:
        filtered_readings.append(entry)  # Collected but never used

# Decoy transformation using string methods (dead path)
device_ids = [d['sensor_id'] for d in data]
encoded_ids = [sid.replace('S', 'X').lower() for sid in device_ids]
decoded_map = {enc: orig for enc, orig in zip(encoded_ids, device_ids)}

# Initialize aggregation structures
temp_sum = 0
humidity_sum = 0
active_count = 0
status_counter = defaultdict(int)

# Primary processing loop with enumerate (actual logic)
for i, record in enumerate(data):
    status = record['status']
    status_counter[status] += 1
    
    # Track active sensors
    if status == 'active':
        active_count += 1
        temp_sum += record['temp']
        humidity_sum += record['humidity']
    
    # Fake early exit condition (never triggers)
    if i > 10:
        break

# Compute averages only over active sensors
if active_count > 0:
    avg_temp = temp_sum / active_count
    avg_humidity = humidity_sum / active_count
else:
    avg_temp = 0
    avg_humidity = 0

# Auxiliary statistical distraction
median_temp = sorted([d['temp'] for d in data])[len(data)//2]
mode_humidity = Counter([d['humidity'] for d in data]).most_common(1)[0][0]

# Actual metric processing function
def process_metrics(sensor_data, config):
    # Secondary parsing of status (redundant but plausible)
    statuses = [item['status'] for item in sensor_data]
    status_freq = Counter(statuses)
    inactive_penalty = 0
    if 'idle' in status_freq:
        inactive_penalty = status_freq['idle'] * config.get('status_penalty', 0)
    
    # Real score computation
    raw_temp_score = avg_temp * config['temp']
    raw_humid_score = avg_humidity * config['humidity']
    base_composite = raw_temp_score + raw_humid_score
    
    # Apply penalty
    adjusted_score = base_composite + inactive_penalty
    
    # Fake nonlinear transform (unused branch)
    if adjusted_score < 0:
        adjusted_score = math.log(abs(adjusted_score) + 1) * -1
    
    # Final scaling based on number of sensors (actual use)
    final_multiplier = len(sensor_data) / 10.0
    final_score = adjusted_score * final_multiplier
    
    # Dead code: string-based flag check (never affects anything)
    flag_str = "normal_op"
    if 'critical' in flag_str.split('_'):
        final_score *= 0.5
    
    return final_score

# Execute main logic
total_entries = len(data)
baseline_offset = sum([len(d['status']) for d in data])  # Irrelevant sum

final_score = process_metrics(data, weights)
print(f"Target result: {final_score}")