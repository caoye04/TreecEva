def analyze_temperature_readings():
    # Daily temperature readings over 7 days
    temperature_data = [23.5, 25.1, 19.8, 28.3, 22.7, 26.4, 20.9]
    
    # Filter readings above 22 degrees using conditional expression
    filtered_data = [temp for temp in temperature_data if temp > 22]
    
    # Calculate average of filtered readings (integer division)
    target_value = sum(filtered_data) // len(filtered_data)
    
    print(f"Result: {target_value}")
    return target_value

# Execute the function
if __name__ == "__main__":
    analyze_temperature_readings()