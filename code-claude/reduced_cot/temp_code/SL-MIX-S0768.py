def calculate_power_efficiency(turbines, hours):
    # Calculate the efficiency of wind turbines
    base_output = sum(t['capacity'] for t in turbines)
    
    # Track maintenance impact
    maintenance_factor = 0.95
    weather_impact = [0.8, 1.2, 0.9, 1.0, 1.1]
    
    # Calculate theoretical maximum output
    theoretical_max = base_output * hours
    
    # Environmental adjustments that don't affect efficiency calculation
    altitude_factors = [1.02, 0.98, 1.03, 0.97, 1.01]
    temperature_impact = sum(altitude_factors) / len(altitude_factors)
    
    # Calculate actual power generation with losses
    actual_output = 0
    for i, turbine in enumerate(turbines):
        # Apply weather effects cyclically
        weather_idx = i % len(weather_impact)
        weather_modifier = weather_impact[weather_idx]
        
        # Calculate turbine contribution with maintenance factor
        contribution = turbine['capacity'] * turbine['uptime'] * maintenance_factor
        
        # Apply weather effects
        contribution *= weather_modifier
        
        # Track unused diagnostic data
        diagnostic = turbine.get('diagnostic', 0)
        sensor_readings = [diagnostic + i for i in range(3)]
        
        # Add to total output
        actual_output += contribution
    
    # Calculate efficiency as percentage
    return round((actual_output / theoretical_max) * 100, 2)

# Wind turbine data
turbines = [
    {'id': 'T1', 'capacity': 2.5, 'uptime': 0.92, 'diagnostic': 3},
    {'id': 'T2', 'capacity': 2.0, 'uptime': 0.88, 'diagnostic': 5},
    {'id': 'T3', 'capacity': 3.0, 'uptime': 0.95, 'diagnostic': 2},
    {'id': 'T4', 'capacity': 2.8, 'uptime': 0.90, 'diagnostic': 4}
]

# Calculate total capacity for reporting
total_capacity = sum(t['capacity'] for t in turbines)
max_theoretical = total_capacity * 24 * 30  # Monthly maximum

# Historical data (not used in final calculation)
historical_efficiencies = [82.5, 78.9, 85.2, 80.1, 83.7]
avg_historical = sum(historical_efficiencies) / len(historical_efficiencies)

# Operational parameters
operational_hours = 720  # Hours in a month
power_price = 0.12  # $ per kWh

# Calculate current efficiency
efficiency = calculate_power_efficiency(turbines, operational_hours)

# Calculate potential revenue (not affecting efficiency)
potential_revenue = (total_capacity * operational_hours * efficiency / 100) * power_price

print(f"Wind farm efficiency: {efficiency}%")
