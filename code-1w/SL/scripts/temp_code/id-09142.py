def calculate_performance(temps):
    temp = sum(temps) // len(temps)
    performance_index = 0
    
    # Irrelevant string operation (minor distraction)
    status_msg = "Processing temperature batch...".upper()
    
    # Create mapping using dictionary comprehension and lambda
    temperature_map = {t: t * 2 + 5 for t in range(temp - 2, temp + 3)}
    
    # Logical check with comparison and assignment
    if temp > 20:
        performance_index += 10
    else:
        performance_index += 5
    
    # Key computational step
    final_score = temperature_map[temp] + performance_index
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
readings = [18, 22, 19, 21, 20]
calculate_performance(readings)