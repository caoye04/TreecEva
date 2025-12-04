# Solar panel production monitoring system

def calculate_energy_stats(daily_outputs, weather_conditions):
    # Process weather impact factors
    impact_factors = {}
    for day, condition in weather_conditions.items():
        if condition == 'Sunny':
            impact_factors[day] = 1.0
        elif condition == 'Cloudy':
            impact_factors[day] = 0.6
        elif condition == 'Rainy':
            impact_factors[day] = 0.3
        else:
            impact_factors[day] = 0.8  # Default for other conditions
    
    # Calculate normalized outputs
    normalized_outputs = {day: output / impact_factors.get(day, 0.5) 
                         for day, output in daily_outputs.items()}
    
    # Analyze maintenance periods (not directly relevant to final calculation)
    maintenance_days = [day for day, condition in weather_conditions.items() 
                      if condition == 'Maintenance']
    maintenance_impact = len(maintenance_days) * 50
    
    # Calculate operational metrics
    total_production = sum(daily_outputs.values())
    potential_production = sum(normalized_outputs.values())
    efficiency_drop = potential_production - total_production
    
    # Calculate operating hours (only weekdays count)
    weekday_count = len([day for day in daily_outputs.keys() if int(day) % 7 not in [0, 6]])
    operating_hours = weekday_count * 8
    
    # Unused variable calculations (distraction)
    peak_production = max(daily_outputs.values()) if daily_outputs else 0
    lowest_production = min(daily_outputs.values()) if daily_outputs else 0
    production_range = peak_production - lowest_production
    
    # Calculate final efficiency ratio
    efficiency_ratio = total_production / (operating_hours * 100)
    
    # Generate report metrics (distraction)
    report_data = {
        'total': total_production,
        'peak': peak_production,
        'efficiency': efficiency_ratio * 100,
        'maintenance_impact': maintenance_impact
    }
    
    return efficiency_ratio

# Production data (kWh)
daily_outputs = {
    '1': 750, '2': 820, '3': 640, '4': 710, '5': 890,
    '8': 760, '9': 800, '10': 720, '11': 750, '12': 830
}

# Weather conditions
weather_conditions = {
    '1': 'Sunny', '2': 'Sunny', '3': 'Cloudy', '4': 'Cloudy', '5': 'Sunny',
    '8': 'Rainy', '9': 'Sunny', '10': 'Maintenance', '11': 'Cloudy', '12': 'Sunny'
}

efficiency = calculate_energy_stats(daily_outputs, weather_conditions)
print(f"Result: {efficiency}")