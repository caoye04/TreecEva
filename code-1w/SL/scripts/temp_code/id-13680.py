import math

# Simulated sensor readings from a distributed environmental monitoring system
def generate_sensor_data():
    base_values = [12.4, 15.1, 9.8, 22.0, 17.3, 8.5, 14.2]
    timestamps = [1634567890 + i*60 for i in range(len(base_values))]
    locations = ['north', 'south', 'east', 'west', 'central', 'northeast', 'southwest']
    
    # Misleading: complex packaging with irrelevant metadata
    metadata_map = {loc: {'id': idx+100, 'active': True, 'version': '2.1'} 
                   for idx, loc in enumerate(locations)}
    
    readings = []
    for val, ts, loc in zip(base_values, timestamps, locations):
        noise = (math.sin(ts / 10000) * 0.1)
        corrupted_val = val + noise + (0.05 if loc == 'east' else 0)  # minor perturbation
        readings.append({
            'value': corrupted_val,
            'timestamp': ts,
            'location': loc,
            'meta': metadata_map[loc],
            'status': 'ok'
        })
    return readings

# Decoy function: looks important but unused in final path
def analyze_trend(readings):
    values = [r['value'] for r in readings]
    diffs = [values[i+1] - values[i] for i in range(len(values)-1)]
    return sum(diffs) / len(diffs) if diffs else 0

# Another red herring: advanced calibration model that isn't used
class RedundantCalibrator:
    def __init__(self, order=3):
        self.order = order
        self.coefs = [0.98 + i*0.01 for i in range(order)]
    
    def apply(self, x):
        return sum(c * (x ** i) for i, c in enumerate(self.coefs))

# Real calibration matrix (simplified lookup)
def build_calibration_matrix():
    # Complex-looking structure with irrelevant entries
    raw_matrix = {
        'north':      {'gain': 1.02, 'offset': -0.3, 'weight': 0.85},
        'south':      {'gain': 0.99, 'offset': 0.1,  'weight': 0.92},
        'east':       {'gain': 1.05, 'offset': -0.6, 'weight': 0.78},
        'west':       {'gain': 0.97, 'offset': 0.4,  'weight': 0.88},
        'central':    {'gain': 1.00, 'offset': 0.0,  'weight': 1.00},
        'northeast':  {'gain': 1.01, 'offset': -0.2, 'weight': 0.81},
        'southwest':  {'gain': 0.98, 'offset': 0.3,  'weight': 0.90},
        # Extra decoy locations not present in data
        'up':         {'gain': 1.10, 'offset': -1.0, 'weight': 0.50},
        'down':       {'gain': 0.90, 'offset': 0.8,  'weight': 0.60}
    }
    return raw_matrix

# Core processing logic — where actual computation happens
def process_readings(readings, calib_matrix):
    adjusted_values = []
    weights = []
    
    # Distractor: use of enumerate and zip in a slightly convoluted way
    for idx, reading in enumerate(readings):
        loc = reading['location']
        raw_val = reading['value']
        
        # Only these fields are used; others are distractions
        gain = calib_matrix[loc]['gain']
        offset = calib_matrix[loc]['offset']
        weight = calib_matrix[loc]['weight']
        
        # Actual transformation
        corrected = (raw_val * gain) + offset
        
        # Irrelevant intermediate calculation (dead-end)
        normalized = corrected / (weight * 1.5)  # never used
        
        adjusted_values.append(corrected)
        weights.append(weight)
    
    # Final weighted diagnostic index
    total_weight = sum(weights)
    weighted_sum = sum(val * w for val, w in zip(adjusted_values, weights))
    
    # The real answer
    final_index = weighted_sum / total_weight if total_weight else 0
    
    # Misleading: secondary diagnostics that aren't returned
    variance = sum((v - final_index)**2 for v in adjusted_values) / len(adjusted_values)
    outlier_count = sum(1 for v in adjusted_values if abs(v - final_index) > 2)
    
    # This is the only returned value
    return final_index

# Unused helper — creates illusion of more complexity
def validate_consistency(data_list):
    for d in data_list:
        assert d['status'] == 'ok', "Data corruption detected"
    return True

# Main execution block
if __name__ == '__main__':
    # Generate realistic input
    sensor_data = generate_sensor_data()
    
    # Build calibration parameters
    calibration_matrix = build_calibration_matrix()
    
    # Dead code path: looks important but unused
    if len(sensor_data) > 5:
        trend = analyze_trend(sensor_data)  # computed but ignored
        calibrator_v2 = RedundantCalibrator(order=3)
        enhanced_data = [calibrator_v2.apply(r['value']) for r in sensor_data]  # unused
    
    # Critical statement
    final_diagnostic = process_readings(sensor_data, calibration_matrix)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")