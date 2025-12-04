# Water Conservation Tracking System
# Calculate water savings from various conservation methods

# Monthly rainfall data (in mm) - used for context but not essential
rainfall = [45, 32, 68, 75, 23, 12, 8, 5, 18, 42, 65, 80]

# Daily water usage reduction (in liters) for each implemented method
conservation_methods = {
    'low_flow_shower': 45.5,
    'rainwater_collection': 28.3,
    'efficient_irrigation': 67.2,
    'leak_repair': 15.9,
    'drought_plants': 33.0
}

# Track which methods were active each month (1=active, 0=inactive)
monthly_implementation = [
    {'low_flow_shower': 1, 'rainwater_collection': 0, 'efficient_irrigation': 0, 'leak_repair': 1, 'drought_plants': 0},
    {'low_flow_shower': 1, 'rainwater_collection': 0, 'efficient_irrigation': 0, 'leak_repair': 1, 'drought_plants': 1},
    {'low_flow_shower': 1, 'rainwater_collection': 1, 'efficient_irrigation': 0, 'leak_repair': 1, 'drought_plants': 1},
    {'low_flow_shower': 1, 'rainwater_collection': 1, 'efficient_irrigation': 1, 'leak_repair': 1, 'drought_plants': 1},
    {'low_flow_shower': 1, 'rainwater_collection': 1, 'efficient_irrigation': 1, 'leak_repair': 1, 'drought_plants': 1},
    {'low_flow_shower': 1, 'rainwater_collection': 1, 'efficient_irrigation': 1, 'leak_repair': 0, 'drought_plants': 1}
]

# Calculate efficiency factor based on rainfall (not used in final calculation)
efficiency_factors = []
for rain in rainfall[:6]:
    if rain > 60:
        efficiency_factors.append(0.8)  # Less savings when it rains a lot
    elif rain > 30:
        efficiency_factors.append(0.9)
    else:
        efficiency_factors.append(1.0)  # Maximum savings during dry periods

# Calculate daily savings for each month
daily_savings = []
for month, methods in enumerate(monthly_implementation):
    daily_amount = 0
    for method, is_active in methods.items():
        if is_active:
            daily_amount += conservation_methods[method]
    
    # Apply a seasonal modifier (not actually used in final calculation)
    season_modifier = 1.0 + (month % 3) * 0.05
    
    daily_savings.append(daily_amount)

# Calculate monthly savings (30 days per month for simplicity)
monthly_savings = []
for daily, _ in zip(daily_savings, efficiency_factors):
    monthly_amount = daily * 30
    monthly_savings.append(monthly_amount)

# Calculate potential yearly projection (not used in final calculation)
yearly_projection = sum(monthly_savings) * 2

# Calculate total water saved
total_water_saved = sum(monthly_savings)

# Display water conservation statistics
print(f"Average daily savings: {sum(daily_savings)/len(daily_savings):.2f} liters")
print(f"Total water saved: {total_water_saved:.1f} liters")
