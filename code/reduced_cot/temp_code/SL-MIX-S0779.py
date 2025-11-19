from functools import reduce

def process_sensor_data():
    # Raw sensor readings
    raw_readings = [127, 64, 33, 98, 255, 1, 42]
    
    # Apply transformation using list comprehension and modular arithmetic
    transformed_values = [
        (value * 3 + 7) % 256 
        for value in raw_readings 
        if value > 32 and value < 200
    ]
    
    # Create mapping dictionary using dictionary comprehension
    sensor_map = {
        idx: val 
        for idx, val in enumerate(transformed_values)
    }
    
    # Apply bitwise operations using functional programming
    xor_results = list(map(
        lambda x: x[1] ^ (x[0] << 2) & 255,
        sensor_map.items()
    ))
    
    # Filter values using logical operations
    filtered_values = [
        val for val in xor_results
        if (val > 50) and not (val & 1)  # Even numbers greater than 50
    ]
    
    # Calculate checksum using modular arithmetic and reduce
    checksum_base = reduce(
        lambda acc, val: (acc + val * 17) % 1000,
        filtered_values,
        0
    )
    
    # Final adjustment with logical conditions
    checksum_result = (
        checksum_base + 42 
        if len(filtered_values) >= 3 
        else checksum_base - 100
    ) % 1000
    
    return checksum_result

# Execute processing
final_checksum = process_sensor_data()
print(f"Result: {final_checksum}")