# Agricultural Soil Moisture Analysis System

def calculate_nutrient_score(ph_level, organic_matter):
    # Higher score means better growing conditions
    if ph_level < 5.5:
        return organic_matter * 0.7  # Too acidic
    elif ph_level > 8.0:
        return organic_matter * 0.6  # Too alkaline
    else:
        return organic_matter * 1.2  # Optimal pH range

# Weather data from multiple stations (temperature, humidity, rainfall)
weather_stations = {
    'north': (28.5, 65, 42.3),
    'south': (32.1, 58, 12.7),
    'east': (29.8, 72, 38.6),
    'west': (27.3, 61, 29.4),
    'central': (30.2, 67, 31.5)
}

# Soil moisture readings from sensors (percentage)
moisture_levels = [18.7, 24.3, 31.5, 22.8, 16.9, 28.4]

# Get average temperature across stations
temperatures = [data[0] for data in weather_stations.values()]
avg_temperature = sum(temperatures) / len(temperatures)

# Calculate potential evaporation based on temperature
potential_evaporation = 0.35 * (avg_temperature - 20) if avg_temperature > 20 else 0.15 * avg_temperature

# Select the station with highest rainfall
max_rainfall_station = max(weather_stations.items(), key=lambda x: x[1][2])[0]
max_rainfall = weather_stations[max_rainfall_station][2]

# Process soil data
ph_readings = [6.2, 5.8, 7.1, 8.2, 6.5]
organic_content = [3.2, 2.8, 4.1, 1.9, 3.7]

# Calculate nutrient scores
nutrient_scores = []
for i in range(len(ph_readings)):
    score = calculate_nutrient_score(ph_readings[i], organic_content[i])
    nutrient_scores.append(score)

# Find optimal growing area
optimal_area_index = nutrient_scores.index(max(nutrient_scores))
optimal_ph = ph_readings[optimal_area_index]

# Calculate rainfall factor - this affects moisture retention
rainfall_factor = 1.0
if max_rainfall > 40:
    rainfall_factor = 1.5
elif max_rainfall > 30:
    rainfall_factor = 1.25
elif max_rainfall > 20:
    rainfall_factor = 1.1
else:
    rainfall_factor = 0.9

# Determine which sensor to use based on nutrient scores
total_score = sum(nutrient_scores)
average_score = total_score / len(nutrient_scores)
quality_threshold = average_score * 1.1

# This would normally be used but we'll take another approach
unused_best_sensors = [i for i, score in enumerate(nutrient_scores) if score > quality_threshold]

# Calculate a sensor index based on optimal pH
sensor_index = int((optimal_ph - 5.5) * 10) % len(moisture_levels)

# Determine if the selected sensor reading is valid
is_valid = moisture_levels[sensor_index] > 15 and moisture_levels[sensor_index] < 35

# Base moisture level calculation - unused in final result but looks important
base_moisture = (sum(moisture_levels) / len(moisture_levels)) * 0.8

# Apply seasonal adjustment factor - this is a distraction
seasonal_factors = {'spring': 1.2, 'summer': 0.8, 'fall': 1.0, 'winter': 1.4}
current_season = 'summer'  # Assume it's summer
seasonal_adjustment = seasonal_factors.get(current_season, 1.0)

# Adjust moisture levels based on weather conditions - another distraction
adjusted_moisture_levels = [level * seasonal_adjustment / potential_evaporation 
                           for level in moisture_levels]

# Calculate irrigation needs - also not used for final result
irrigation_threshold = 25.0
irrigation_needs = [max(0, irrigation_threshold - level) for level in moisture_levels]

# Determine final soil moisture based on selected sensor and rainfall
final_soil_moisture = moisture_levels[sensor_index] * rainfall_factor if is_valid else base_moisture

# This would modify the result but it's after our target statement
if False:  # This never executes
    if potential_evaporation > 5:
        final_soil_moisture *= 0.85

print(f"Result: {final_soil_moisture}")