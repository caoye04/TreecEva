def calculate_crop_yield(temperatures, rainfall_levels):
    threshold_temp = 20
    min_rainfall = 80
    
    suitable_days = 0
    total_production = 0
    
    for i in range(len(temperatures)):
        temp = temperatures[i]
        rain = rainfall_levels[i]
        if temp >= threshold_temp and rain >= min_rainfall:
            suitable_days += 1
            total_production += temp * (rain / 100)

    average_production = total_production / suitable_days if suitable_days > 0 else 0
    
    status_messages = ['Optimal', 'Suboptimal', 'Poor']
    message_code = len(status_messages)  # irrelevant variable
    
    efficiency_factor = 0.9 if average_production > 25 else 0.7
    final_yield = average_production * efficiency_factor
    
    return final_yield

# Input data
temp_data = [22, 25, 19, 24, 27, 23, 20]
rain_data = [85, 90, 70, 95, 88, 83, 78]

result = calculate_crop_yield(temp_data, rain_data)
print(f"Target result: {result}")