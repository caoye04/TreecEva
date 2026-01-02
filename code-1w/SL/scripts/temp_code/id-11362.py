def analyze_growth_potential(temp, moisture):
    if temp < 15 or moisture < 30:
        return 'LOW'
    elif temp > 35 or moisture > 90:
        return 'HIGH_STRESS'
    else:
        return 'OPTIMAL'

# Simulate sensor calibration offsets (irrelevant to final result)
calibration_factor_x = 1.05
calibration_factor_y = 0.98
offset_adjustment = (calibration_factor_x + calibration_factor_y) / 2

# Actual environmental data
base_temperatures = [22, 25, 18, 31, 27]
humidity_levels = [65, 70, 55, 80, 73]

# Derived temperature readings with fake noise injection and cleanup
raw_temp_data = [t * 1.02 + 0.3 for t in base_temperatures]
filtered_temps = [round(t, 1) for t in raw_temp_data]

# Redundant humidity transformation (not used later)
normalized_humidity = [h / 100.0 for h in humidity_levels]
dew_points = [round(241.2 * (h/100) * t / (17.67 + (h/100)*t), 2) for t, h in zip(filtered_temps, humidity_levels)]

# Soil moisture levels derived from humidity with artificial scaling
soil_moisture_levels = [int(h * 0.6) for h in humidity_levels]

# Temperature readings adjusted for elevation (mock correction)
elevation_compensation = [-1.8, -1.2, -2.1, -0.9, -1.5]
temperature_readings = [round(t + ec, 1) for t, ec in zip(filtered_temps, elevation_compensation)]

# Spurious intermediate calculation (dead-end path)
stress_index = sum(1 for t in temperature_readings if t > 30) * 1.5
theoretical_max_yield = 120.0 - stress_index * 2.3

# State tracker for growth phases (partially relevant)
growth_phase_status = []
for i, (t, m) in enumerate(zip(temperature_readings, soil_moisture_levels)):
    phase = analyze_growth_potential(t, m)
    growth_phase_status.append(f'Day_{i+1}:{phase}')

# Key function that determines final output
def calculate_optimal_harvest(temps, moisture_vals):
    valid_days = 0
    total_productivity = 0.0
    
    for t, m in zip(temps, moisture_vals):
        status = analyze_growth_potential(t, m)
        if status == 'OPTIMAL':
            # Productivity score based on proximity to ideal conditions
            temp_score = 10 - abs(t - 25)
            moisture_score = 10 - abs(m - 60)
            daily_yield = (temp_score + moisture_score) * 0.85
            total_productivity += daily_yield
            valid_days += 1
    
    if valid_days == 0:
        return 0.0
    
    average_yield_per_valid_day = total_productivity / valid_days
    total_estimated_yield = average_yield_per_valid_day * 10  # Projected over 10 units
    return round(total_estimated_yield, 2)

# Misleading secondary function (never called)
def predict_frost_risk(readings):
    return sum(1 for t in readings if t < 0)

# Critical statement
final_yield = calculate_optimal_harvest(temperature_readings, soil_moisture_levels)

# Print result as required
print(f"Result: {final_yield}")