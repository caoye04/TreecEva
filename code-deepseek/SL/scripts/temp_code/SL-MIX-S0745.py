def process_sensor_data(readings):
    # Process daily sensor readings
    daily_totals = [45, 23, 67, 89, 12, 56, 78, 34, 91, 15]
    
    # Get readings from day 3 to day 7 (inclusive)
    sliced_data = daily_totals[2:7]
    
    # Calculate sum of selected readings
    final_sum = sum(sliced_data)
    
    print(f"Target result: {final_sum}")
    return final_sum

# Execute the function
result = process_sensor_data([])