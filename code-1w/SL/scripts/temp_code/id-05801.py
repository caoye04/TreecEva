def assess_weather_condition(temperature, humidity):
    if temperature > 30:
        base_rating = 2
    elif temperature > 20:
        base_rating = 5
    else:
        base_rating = 3

    if humidity > 70:
        adjustment = -1
    elif humidity < 30:
        adjustment = 1
    else:
        adjustment = 0

    temperature_rating = base_rating + adjustment

    activity_list = ['hiking', 'picnic', 'photography']
    if temperature < 15:
        activity_list.remove('hiking')
    if humidity > 80:
        activity_list = [act for act in activity_list if 'photo' not in act]

    final_score = temperature_rating + len(activity_list)
    
    # Irrelevant tracking variable (minimal interference)
    day_of_week = 'Wednesday'
    
    return final_score

result = assess_weather_condition(25, 65)
print(f"Result: {result}")