import math

# Simulated sensor network data processing with diagnostic analysis
def collect_sensor_readings():
    raw_readings = [
        (1001, [23.4, 25.1, 24.8, 26.0, 22.9]),
        (1002, [19.5, 18.7, 19.0, 18.2, 19.8]),
        (1003, [31.2, 33.5, 30.8, 32.1, 31.9]),
        (1004, [17.6, 18.1, 17.3, 17.9, 18.0])
    ]
    return raw_readings

# Irrelevant helper - decoy function
def normalize_strings(str_list):
    return [s.upper().strip() for s in str_list if len(s) > 2]

# Data transformation with red herring operations
def transform_coordinates(coords):
    # Complex but irrelevant coordinate math
    transformed = []
    for x, y in coords:
        r = math.sqrt(x*x + y*y)
        theta = math.atan2(y, x)
        new_x = r * math.cos(theta + math.pi/4)
        new_y = r * math.sin(theta + math.pi/4)
        transformed.append((new_x * 0.1, new_y * 0.1))
    return transformed

# Unused but plausible-looking preprocessing step
def filter_outliers(data, factor=1.5):
    # Not actually used in main flow
    result = []
    for entry in data:
        sensor_id, readings = entry
        median_val = sorted(readings)[len(readings)//2]
        filtered = [r for r in readings if abs(r - median_val) < factor]
        result.append((sensor_id, filtered))
    return result

# Core processing with distractors
threshold_map = {
    'critical': 30.0,
    'warning': 25.0,
    'normal': 20.0,
    'info': 15.0
}

status_codes = {
    200: 'OK',
    400: 'Bad Request',
    500: 'Internal Error'
}

# This function is called and relevant
def process_readings(raw_data):
    processed = {}
    temp_aggregates = []  # Red herring collection
    
    for sensor_id, readings in raw_data:
        avg = sum(readings) / len(readings)
        deviation = math.sqrt(sum((r - avg)**2 for r in readings) / len(readings))
        
        # Real logic branch
        if sensor_id == 1001:
            category = 'urban'
        elif sensor_id == 1002:
            category = 'suburban'
        else:
            category = 'rural'
        
        # Store real result
        if category not in processed:
            processed[category] = []
        processed[category].append(avg)
        
        # Dead-end computation
        max_jump = 0
        for i in range(1, len(readings)):
            jump = abs(readings[i] - readings[i-1])
            if jump > max_jump:
                max_jump = jump
        temp_aggregates.append({'sensor': sensor_id, 'max_jump': max_jump})
        
    # More irrelevant transformations
    code_lookup = {v: k for k, v in status_codes.items()}
    code_lookup['Timeout'] = 599
    
    return processed

# Another decoy function dealing with unrelated data format
def parse_timestamps(ts_list):
    total_seconds = 0
    for ts in ts_list:
        parts = ts.split(':')
        hours, minutes, seconds = [float(p) for p in parts]
        total_seconds += hours*3600 + minutes*60 + seconds
    return total_seconds

# Critical analysis function that produces the answer
def analyze_readings(data, thresholds):
    diagnostics = []
    
    # Real computation path
    for region_type, values in data.items():
        region_avg = sum(values) / len(values)
        
        # Apply threshold logic
        level = 'normal'
        if region_avg >= thresholds['critical']:
            level = 'critical'
        elif region_avg >= thresholds['warning']:
            level = 'warning'
        elif region_avg <= thresholds['info']:
            level = 'info'
            
        # Compute severity score
        base_score = 0
        if level == 'critical':
            base_score = 85
        elif level == 'warning':
            base_score = 65
        elif level == 'normal':
            base_score = 45
        else:
            base_score = 25
        
        # Adjustment based on variation (real but subtle)
        variance = sum((v - region_avg)**2 for v in values) / len(values)
        adjustment = int(variance * 2)
        final_score = base_score + adjustment
        
        diagnostics.append(final_score)
    
    # Final aggregation - this is the key value
    aggregate_diagnostic = sum(diagnostics) * len(diagnostics)
    
    # Multiple distractions below
    metadata_log = []
    for i, d in enumerate(diagnostics):
        metadata_log.append(f"D{i}:{d}")
    
    # Unused nested structure
    summary_tree = {
        'root': {
            'branch_a': {f'score_{i}': d for i, d in enumerate(diagnostics)},
            'branch_b': {'count': len(diagnostics), 'total': sum(diagnostics)}
        }
    }
    
    # THIS IS THE TARGET VARIABLE
    final_diagnostic = aggregate_diagnostic + 10  # Final adjustment
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Simulate auxiliary string processing (irrelevant)
def format_region_names(names):
    formatted = []
    for name in names:
        words = name.split(' ')
        capitalized = [w.capitalize() for w in words]
        formatted.append('_'.join(capitalized))
    return formatted

# Main execution flow
if __name__ == "__main__":
    # Collect real data
    sensor_data = collect_sensor_readings()
    
    # Irrelevant coordinate list
    coordinates = [(1.0, 2.0), (3.5, 4.2), (5.1, 6.8)]
    transformed_coords = transform_coordinates(coordinates)
    
    # String list for decoy processing
    regions = ["northern zone", "east district", "south area"]
    formatted_regions = format_region_names(regions)
    
    # Timestamp parsing (dead end)
    timestamps = ["01:23:45", "02:15:30", "00:45:12"]
    total_time = parse_timestamps(timestamps)
    
    # Process the actual sensor data
    processed_data = process_readings(sensor_data)
    
    # Generate final diagnostic (answer produced here)
    final_diagnostic = analyze_readings(processed_data, threshold_map)