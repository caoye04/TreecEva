from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and irrelevant entries
data_stream = [
    {'sensor': 'A', 'value': 12.5, 'status': 'ok', 'timestamp': 1648567200},
    {'sensor': 'B', 'value': 8.3, 'status': 'ok', 'timestamp': 1648567201},
    {'sensor': 'A', 'value': 13.1, 'status': 'ok', 'timestamp': 1648567202},
    {'sensor': 'C', 'value': 0.0, 'status': 'error', 'timestamp': 1648567203},
    {'sensor': 'B', 'value': 7.9, 'status': 'ok', 'timestamp': 1648567204},
    {'sensor': 'A', 'value': 11.8, 'status': 'ok', 'timestamp': 1648567205},
    {'sensor': 'D', 'value': -5.2, 'status': 'calibrating', 'timestamp': 1648567206},
    {'sensor': 'C', 'value': 14.0, 'status': 'ok', 'timestamp': 1648567207},
    {'sensor': 'B', 'value': 8.0, 'status': 'ok', 'timestamp': 1648567208},
    {'sensor': 'A', 'value': 12.2, 'status': 'ok', 'timestamp': 1648567209}
]

# Irrelevant mapping for distraction
type_mapping = {'A': 'primary', 'B': 'secondary', 'C': 'auxiliary', 'D': 'diagnostic'}

# Configuration with decoy parameters
config = {
    'threshold': 12.0,
    'gain': 1.5,
    'offset': -2.0,
    'max_records': 100,
    'debug_mode': True,
    'sampling_interval': 5,
    'use_enhancement': False  # This is never actually used
}

# Distractor function - looks important but unused
def enhance_signal(x, method='linear'):
    if method == 'linear':
        return x * 1.1
    elif method == 'exponential':
        return x * (1 + 0.1 * x)
    return x

def filter_noisy_data(stream, min_status='ok'):
    # Filter by status but include some red herrings
    valid_levels = {'ok', 'calibrating'}  # Note: calibrating is included but later ignored
    result = []
    temp_buffer = []  # Unused buffer - distractor

    for entry in stream:
        if entry['status'] not in valid_levels:
            continue
        if entry['sensor'] not in ['A', 'B', 'C']:  # Exclude diagnostic sensors
            continue
        if entry['value'] < 0:  # Drop negative values
            continue
        result.append(entry)
    
    # Dead code path - never reached due to above logic
    if len(temp_buffer) > 10:
        result.extend(temp_buffer[:2])

    return result

def aggregate_by_sensor(data_list):
    # Aggregate values by sensor with multiple steps
    raw_aggregates = defaultdict(list)
    stats_summary = {}  # Unused statistics

    for item in data_list:
        raw_aggregates[item['sensor']].append(item['value'])
    
    processed = {}
    for sensor, values in raw_aggregates.items():
        count = len(values)
        total = sum(values)
        avg = total / count
        # Apply gain and offset from config (only gain is actually used)
        adjusted_avg = avg * config['gain'] + config['offset']
        processed[sensor] = {
            'count': count,
            'average': avg,
            'adjusted': adjusted_avg,
            'variance': sum((x - avg) ** 2 for x in values) / count if count > 0 else 0
        }
    
    # Distractor: complex counter that isn't used
    distribution = Counter([s['sensor'] for s in data_list])
    
    return processed

def apply_correction_scheme(sensor_data, correction_type='dynamic'):
    # Apply non-linear correction based on sensor type
    corrected = {}
    base_weights = {'A': 1.2, 'B': 0.8, 'C': 1.0}
    
    for sensor_id, metrics in sensor_data.items():
        adj = metrics['adjusted']
        weight = base_weights.get(sensor_id, 1.0)
        
        if correction_type == 'static':
            corrected[sensor_id] = adj * weight
        else:  # dynamic - actual path
            # Complex formula with intermediate distractors
            exponent_factor = math.log(abs(adj) + 1) / 2.0
            temp_result = adj ** exponent_factor  # Distractor
            if adj > 10:
                corrected[sensor_id] = adj * weight * 0.95
            else:
                corrected[sensor_id] = adj * weight * 1.05
    
    return corrected

def finalize_output(corrections):
    # Final transformation with early return red herring
    if not corrections:
        return -1  # Dead path
    
    # Only sensor A and B are used in final output
    relevant_sensors = {k: v for k, v in corrections.items() if k in ['A', 'B']}
    
    # Key computation
    a_val = relevant_sensors.get('A', 0)
    b_val = relevant_sensors.get('B', 0)
    
    # Final mixing formula
    mixed = (a_val * 3 + b_val * 2) / 5
    
    # Apply floor only if above threshold
    if mixed > 10:
        mixed = math.floor(mixed * 10) / 10  # Round to 1 decimal
    
    return mixed

# Main execution chain
filtered_data = filter_noisy_data(data_stream)
aggregated_data = aggregate_by_sensor(filtered_data)
corrected_values = apply_correction_scheme(aggregated_data)
final_output = finalize_output(corrected_values)

# Print result as required
print(f"Result: {final_output}")