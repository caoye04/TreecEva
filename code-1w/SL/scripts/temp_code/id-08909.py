from itertools import compress

def analyze_sensor_data():
    # Simulated sensor readings (in Celsius)
    temperatures = [18, 21, 19, 25, 22, 17, 24, 20, 23, 26]
    
    # Threshold conditions
    above_threshold = [temp > 20 for temp in temperatures]
    below_critical = [temp < 25 for temp in temperatures]
    
    # Valid readings: between 20 and 25 (exclusive)
    valid_mask = [a and b for a, b in zip(above_threshold, below_critical)]
    
    # Extract valid temperatures using compress (like filtering)
    filtered_data = list(compress(temperatures, valid_mask))
    
    # Accumulate result
    total = 0
    for val in filtered_data:
        total += val
    
    result = sum(filtered_data)
    print(f"Result: {result}")

analyze_sensor_data()