from itertools import compress

def calculate_final_score(records):
    # Extract valid temperature readings above threshold
    temperatures = [r[1] for r in records if r[2] == 'sensor_ok']
    threshold = 18.5
    valid_readings = list(compress(temperatures, (t >= threshold for t in temperatures)))
    
    # Calculate average of valid readings
    avg_temp = sum(valid_readings) / len(valid_readings) if valid_readings else 0
    
    # Scoring logic: points based on rounded average
    base_points = int(avg_temp)
    bonus = 5 if avg_temp > 20.0 else 2
    penalty = 3 if len(valid_readings) < 4 else 0
    
    final_score = base_points + bonus - penalty
    return final_score

# Simulated sensor data: (timestamp, temp, status)
data = [
    ('t0', 17.2, 'sensor_ok'),
    ('t1', 19.5, 'sensor_ok'),
    ('t2', 20.1, 'sensor_ok'),
    ('t3', 18.9, 'sensor_ok'),
    ('t4', 21.3, 'sensor_ok'),
    ('t5', 16.7, 'sensor_error'),  # invalid due to error
    ('t6', 22.0, 'sensor_ok'),
    ('t7', 18.4, 'sensor_ok')  # below threshold
]

result = calculate_final_score(data)
print(f"Result: {result}")