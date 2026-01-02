from collections import defaultdict
import math

# Simulate sensor data aggregation and health scoring for IoT devices
def collect_sensor_data():
    raw_data = [
        {'device': 'D1', 'temp': 23.5, 'humidity': 45, 'vibration': 0.4},
        {'device': 'D2', 'temp': 26.1, 'humidity': 52, 'vibration': 0.8},
        {'device': 'D1', 'temp': 22.9, 'humidity': 47, 'vibration': 0.3},
        {'device': 'D3', 'temp': 30.2, 'humidity': 60, 'vibration': 1.4},
        {'device': 'D2', 'temp': 25.8, 'humidity': 50, 'vibration': 0.7},
        {'device': 'D3', 'temp': 31.0, 'humidity': 63, 'vibration': 1.6}
    ]
    return raw_data

def group_by_device(data_list):
    grouped = defaultdict(list)
    for record in data_list:
        grouped[record['device']].append(record)
    return grouped

def calculate_stability_index(readings):
    if len(readings) < 2:
        return 0.0
    temp_variation = sum(
        abs(readings[i]['temp'] - readings[i+1]['temp'])
        for i in range(len(readings)-1)
    )
    # Irrelevant computation (distractor)
    dummy_calc = sum(r['humidity'] for r in readings) / len(readings)
    return round(temp_variation / (len(readings) - 1), 3)

def assess_vibration_risk(vib_seq):
    high_threshold = 1.0
    count_high = sum(1 for v in vib_seq if v > high_threshold)
    risk_factor = count_high / len(vib_seq) if vib_seq else 0
    return risk_factor

def normalize(value, min_val, max_val):
    # Dummy normalization function used only once
    return (value - min_val) / (max_val - min_val) if max_val != min_val else 0

def process_metrics(data, weight_config):
    device_groups = group_by_device(data)
    scores = {}
    stability_log = []  # Dead storage (not used later)

    for dev_id, records in device_groups.items():
        # Extract sequences
        temps = [r['temp'] for r in records]
        vibrations = [r['vibration'] for r in records]
        
        # Compute primary metrics
        avg_temp = sum(temps) / len(temps)
        base_score = 100 - abs(avg_temp - 25) * 2  # Ideal temp: 25°C
        
        stability = calculate_stability_index(records)
        stability_penalty = stability * 5
        
        vibration_risk = assess_vibration_risk(vibrations)
        vibration_penalty = vibration_risk * 30
        
        # Apply weights from config
        w1, w2, w3 = weight_config['temp'], weight_config['stability'], weight_config['vibration']
        composite_penalty = (
            w1 * stability_penalty * 0.1 + 
            w2 * vibration_penalty * 0.2 + 
            w3 * abs(avg_temp - 20)  # Artificially inflates effect
        )
        
        final_dev_score = base_score - composite_penalty
        scores[dev_id] = max(final_dev_score, 0)  # Clamp to non-negative
        
        # Distractor: store unused log entry
        stability_log.append(f"{dev_id}: {stability:.3f} ({len(records)} samples)")
    
    # Aggregate final score across devices using lambda
    aggregator = lambda s: sum(s.values()) / len(s)
    fleet_health = aggregator(scores)
    
    # Secondary irrelevant transformation
    temp_str = "".join([f"{t:.1f}" for t in sorted(temps)])
    checksum = sum(ord(c) for c in temp_str[:5]) % 100  # Unused
    
    # Final weighted adjustment (only one path matters)
    adjustment_factor = 1.1 if fleet_health < 80 else 1.0
    final_score = round(fleet_health * adjustment_factor, 2)
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Main execution
sensor_data = collect_sensor_data()
data = sensor_data  # Redundant assignment (distractor)
weights = {'temp': 0.6, 'stability': 0.3, 'vibration': 0.1}

# Dead code block (conditionally unreachable)
if False:
    debug_out = defaultdict(int)
    for d in data:
        debug_out[d['device']] += d['humidity']

final_score = process_metrics(data, weights)