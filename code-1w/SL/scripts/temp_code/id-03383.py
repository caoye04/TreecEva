def main():
    # Sensor data simulation with noise
    raw_readings = [145, 203, 176, 198, 215]
    
    # Irrelevant transformation: amplitude modulation (not used in final result)
    modulated = list(map(lambda x: (x * 1.05) + 12, raw_readings))
    avg_modulated = sum(modulated) / len(modulated)

    # Core processing pipeline
    filtered = [x for x in raw_readings if x > 160]  # Only high-intensity readings
    squared = [x ** 2 for x in filtered]
    summed_squares = sum(squared)
    
    # Checksum for data integrity (distractor)
    checksum = sum([x % 10 for x in raw_readings]) * 2
    expected_checksum = 44
    is_valid = checksum == expected_checksum

    # Secondary filter based on modular condition
    processed_data = [val for val in squared if (val // 100) % 3 == 2]

    # Conditional transformation using lambda
    transform = lambda x: x - 100 if x > 30000 else x + 50
    
    # Apply transformation only to elements meeting criteria
    transformed_list = [transform(val) for val in processed_data]

    # Final aggregation
    base_result = sum(transformed_list) // len(transformed_list) if transformed_list else 0

    # Final nonlinear adjustment
    def final_transform(data):
        if not data:
            return 0
        product = 1
        for val in data:
            product *= (val % 25)  # Focus on remainder space
        return base_result + (product % 100)

    result = final_transform(processed_data)
    print(f"Target result: {result}")

if __name__ == "__main__":
    main()