# Weather data analysis system
# Processing temperature readings from multiple stations

# Temperature readings for each station (in Celsius)
station_data = {
    'north': [12, 14, -3, 8, 15, 22],
    'south': [24, 28, 31, 27, 22, 35],
    'east': [18, 19, 17, 21, 16, 15],
    'west': [14, 16, 12, 13, 11, 10]
}

# Configuration parameters
config = {
    'outlier_threshold': 30,
    'calibration_factor': 1.2,
    'humidity_adjustment': 0.5,
    'precision': 2
}

# Data processing
def calculate_metrics(data_dict, settings):
    all_temps = []
    station_averages = {}
    
    # Process each station's data
    for station, readings in data_dict.items():
        # Apply calibration to raw readings
        calibrated = [temp * settings['calibration_factor'] for temp in readings]
        
        # Calculate station average (not directly used in final result)
        station_avg = sum(calibrated) / len(calibrated)
        station_averages[station] = round(station_avg, settings['precision'])
        
        # Add to combined dataset
        all_temps.extend(calibrated)
    
    # Create some distractor metrics that aren't used in the final calculation
    max_temp = max(all_temps)
    min_temp = min(all_temps)
    temp_range = max_temp - min_temp
    
    # Filter out extreme values based on threshold
    filtered_temps = [t for t in all_temps if t < settings['outlier_threshold']]
    
    # Calculate average of filtered temperatures
    average_temperature = sum(filtered_temps) / len(filtered_temps)
    
    # This humidity adjustment isn't actually used in the final result
    humidity_adjusted = average_temperature + settings['humidity_adjustment']
    
    return {
        'station_averages': station_averages,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'range': temp_range,
        'average': average_temperature,
        'adjusted': humidity_adjusted
    }

# Run the analysis
results = calculate_metrics(station_data, config)

# Extract key metrics for reporting
max_reading = results['max_temp']
min_reading = results['min_temp']
average_temperature = round(results['average'], config['precision'])

# Some additional calculations that don't affect the final answer
daily_variation = max_reading - average_temperature
is_extreme_weather = daily_variation > 20

print(f"Result: {average_temperature}")