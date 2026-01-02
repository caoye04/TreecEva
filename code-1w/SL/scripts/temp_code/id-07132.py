def main():
    # Simulate sensor data calibration and transformation
    raw_readings = [240, 180, 360, 90]
    
    # Irrelevant distraction: unused variable (minimal interference)
    calibration_offset = 0.5  

    # Step 1: Filter valid range using lambda
    filtered_readings = list(filter(lambda x: x % 90 == 0, raw_readings))
    
    # Step 2: Scale down by factor of 2 via mapping
    scaled_readings = list(map(lambda x: x // 2, filtered_readings))
    
    # Step 3: Compute XOR checksum of scaled values
    checksum = 0
    for val in scaled_readings:
        checksum ^= val
    
    # Step 4: Simple transformation function
    def transform(data):
        return sum(data) + checksum
    
    # Step 5: Process final result
    processed_data = scaled_readings[1:-1]  # Middle elements only
    result = transform(processed_data)
    
    print(f"Result: {result}")

main()