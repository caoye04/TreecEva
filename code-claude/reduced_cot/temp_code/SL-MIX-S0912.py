def calculate_final_altitude(flight_data, correction):
    base_altitude = 10000
    weather_adjustments = [120, -80, 50, -30, 10]
    traffic_density = {'low': 500, 'medium': 0, 'high': -500}
    
    # Apply flight path adjustments
    adjusted_altitude = base_altitude
    for i, (segment, weather) in enumerate(zip(flight_data, weather_adjustments)):
        if segment > 0:
            adjusted_altitude += segment * 100
        else:
            # Descending segments
            adjusted_altitude += segment * 110
        
        # Weather adjustments only apply to segments 1, 2, and 4
        if i in [0, 1, 3]:
            adjusted_altitude += weather
    
    # Calculate fuel efficiency metric (not used for altitude)
    fuel_efficiency = sum(flight_data) * 0.8 + correction * 2
    
    # Traffic adjustment based on last digit of adjusted altitude
    traffic_level = 'medium'
    last_digit = adjusted_altitude % 10
    if last_digit > 7:
        traffic_level = 'high'
    elif last_digit < 3:
        traffic_level = 'low'
    
    # Apply traffic adjustment
    adjusted_altitude += traffic_density[traffic_level]
    
    # Regulatory ceiling check (irrelevant to final calculation)
    max_altitude = 12000
    min_altitude = 8000
    is_within_limits = min_altitude <= adjusted_altitude <= max_altitude
    
    # Apply final correction factor
    result = adjusted_altitude + (correction * 5)
    
    # Log flight metrics (not affecting result)
    flight_duration = sum([abs(x) for x in flight_data]) * 2.5
    flight_code = f"FL{int(result/100)}"
    
    return result

# Flight data: [climb1, climb2, cruise, descent1, descent2]
flight_data = [3, 2, 0, -2, -1]
correction_factor = 15

# Calculate final altitude with correction
final_altitude = calculate_final_altitude(flight_data, correction_factor)
print(f"Final altitude: {final_altitude}")