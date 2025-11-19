import math

def calculate_sensor_coverage(sensors):
    covered_arcs = []
    
    for sensor in sensors:
        center = sensor['angle']
        width = sensor['range']
        start = center - width/2
        end = center + width/2
        
        # Normalize angles to [0, 360)
        start = start % 360
        end = end % 360
        
        # Handle wrap-around cases where arc crosses 0°
        if start > end:
            covered_arcs.append((start, 360))
            covered_arcs.append((0, end))
        else:
            covered_arcs.append((start, end))
    
    # Merge overlapping intervals
    if not covered_arcs:
        return 0
        
    covered_arcs.sort()
    merged = [covered_arcs[0]]
    
    for current in covered_arcs[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # Overlapping
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    
    # Calculate total coverage
    total = 0
    for start, end in merged:
        total += end - start
    
    return total

# Sensor configuration
park_sensors = [
    {'angle': 0, 'range': 90},
    {'angle': 60, 'range': 60},
    {'angle': 180, 'range': 120},
    {'angle': 300, 'range': 60}
]

total_coverage_degrees = calculate_sensor_coverage(park_sensors)
print(f"Result: {total_coverage_degrees}")