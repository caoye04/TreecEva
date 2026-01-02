from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and redundant readings
data = [
    {'sensor': 'A', 'reading': 12.5, 'status': 'active', 'timestamp': 1001},
    {'sensor': 'B', 'reading': 8.3, 'status': 'active', 'timestamp': 1002},
    {'sensor': 'A', 'reading': 13.1, 'status': 'active', 'timestamp': 1003},
    {'sensor': 'C', 'reading': 9.7, 'status': 'inactive', 'timestamp': 1004},
    {'sensor': 'B', 'reading': 7.9, 'status': 'active', 'timestamp': 1005},
    {'sensor': 'D', 'reading': 11.2, 'status': 'active', 'timestamp': 1006},
    {'sensor': 'C', 'reading': 10.1, 'status': 'inactive', 'timestamp': 1007},
    {'sensor': 'A', 'reading': 12.8, 'status': 'active', 'timestamp': 1008}
]

# Weight configuration for active sensors only
weights = {'A': 0.4, 'B': 0.35, 'D': 0.25}  # Sensor C is excluded due to inactivity

# Irrelevant accumulators (distractors)
total_readings = 0
valid_sensors = set()
status_counter = defaultdict(int)
reading_history = []

for entry in data:
    total_readings += 1
    status_counter[entry['status']] += 1
    if entry['status'] == 'active':
        valid_sensors.add(entry['sensor'])
    reading_history.append(entry['reading'])

# Misleading intermediate computation (dead path)
avg_all_time = sum(reading_history) / len(reading_history) if reading_history else 0
median_reading = sorted(reading_history)[len(reading_history)//2]
deviation_sq = sum((x - avg_all_time)**2 for x in reading_history)
std_deviation = math.sqrt(deviation_sq / len(reading_history)) if reading_history else 0

# Another red herring: frequency analysis of timestamps
freq = Counter(d['timestamp'] % 10 for d in data)
common_digit = freq.most_common(1)[0][0] if freq else 0

# Core logic: aggregate only active sensor readings by weighted average
def process_results(sensor_data, weight_map):
    weighted_sum = 0.0
    weight_accumulator = 0.0
    processed_sensors = set()
    
    # Secondary distraction inside function
    debug_info = defaultdict(list)
    outlier_count = 0
    
    for record in sensor_data:
        s_id = record['sensor']
        value = record['reading']
        status = record['status']
        
        # Only process active sensors that are in weight map
        if status == 'active' and s_id in weight_map:
            if s_id not in processed_sensors:
                # First occurrence weighting
                weighted_sum += value * weight_map[s_id]
                weight_accumulator += weight_map[s_id]
                processed_sensors.add(s_id)
            else:
                # Subsequent readings contribute half weight (smoothing)
                weighted_sum += (value * 0.5) * weight_map[s_id]
                weight_accumulator += (0.5 * weight_map[s_id])
            
            # Dead code: logging not used downstream
            debug_info[s_id].append(value)
        else:
            # Distractor: count ignored entries
            outlier_count += 1

    # Irrelevant normalization attempt
    if weight_accumulator > 0:
        preliminary_avg = weighted_sum / weight_accumulator
    else:
        preliminary_avg = 0
    
    # Final adjustment based on number of unique active sensors
    adjustment_factor = len(processed_sensors) * 0.1
    final_result = preliminary_avg + adjustment_factor
    
    return final_result

# Execute main logic
temp_var = [x['reading'] for x in data if x['sensor'] == 'Z']  # Unused list comprehension
baseline_shift = math.sin(math.pi / 4)  # Meaningless constant

final_score = process_results(data, weights)

# Output result as required
print(f"Target result: {final_score}")