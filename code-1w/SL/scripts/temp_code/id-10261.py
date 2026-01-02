from itertools import compress

def calculate_final_score():
    # Simulate sensor readings with thresholds
    temperatures = [23.5, 24.1, 19.8, 22.0, 25.3, 18.7, 20.9]
    thresholds = [t > 20 for t in temperatures]
    
    # Use itertools to filter valid readings
    valid_readings = list(compress(temperatures, thresholds))
    
    # Calculate base average
    base_avg = sum(valid_readings) / len(valid_readings)
    
    # Bonus adjustment based on count
    bonus = 2.0 if len(valid_readings) >= 5 else 0.5
    
    # Final score with conditional expression
    result = base_avg + (bonus if base_avg < 24 else 0)
    
    return result

# Execute and print result
result = calculate_final_score()
print(f"Result: {result}")