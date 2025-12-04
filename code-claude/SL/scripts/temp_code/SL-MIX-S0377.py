def calculate_device_metrics(readings):
    # Process device power readings
    base_values = [reading & 0xFF for reading in readings]
    scaled_values = [val * 2 for val in base_values]
    
    # Calculate potential efficiency metrics
    efficiency_factor = sum(base_values) // len(base_values)
    alternative_factor = max(base_values) - min(base_values)
    
    # Generate power combinations for XOR analysis
    primary_values = [val | 0x10 for val in base_values[:3]]
    secondary_values = [val & 0x3F for val in scaled_values[1:4]]
    
    # Track unused metrics for later analysis
    unused_metric = sum(scaled_values) / len(scaled_values)
    reference_point = (efficiency_factor + alternative_factor) // 2
    
    # Combine values using bitwise operations
    power_combinations = list(zip(primary_values, secondary_values))
    
    # Apply XOR operation to each combination
    total_power = sum(map(lambda x: x[0] ^ x[1], power_combinations))
    
    # Adjust based on efficiency threshold (unused in final calculation)
    if unused_metric > 100:
        adjustment = 15
    else:
        adjustment = 10
        
    # Calculate alternative power (not used in result)
    alt_power = sum(primary_values) - sum(secondary_values)
    
    print(f"Result: {total_power}")
    return total_power

# Device power readings from sensors
readings = [78, 92, 107, 65, 82]
result = calculate_device_metrics(readings)