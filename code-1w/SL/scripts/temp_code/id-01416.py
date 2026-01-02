def calculate_efficiency(load_profile):
    base_capacity = 150
    peak_multiplier = 1.2
    off_peak_discount = 0.85
    
    # Determine time-based load factor using conditional expression
    load_factor = 1.1 if sum(load_profile) > base_capacity else 0.9
    
    # Simulate dynamic pricing adjustment with lambda
    adjust_price = lambda x, t: x * peak_multiplier if t > 17 else x * off_peak_discount
    
    # Generate adjusted hourly rates using list comprehension
    adjusted_rates = [adjust_price(hour, i) for i, hour in enumerate(load_profile)]
    
    # Calculate final efficiency score
    efficiency_score = sum(adjusted_rates) * load_factor
    
    return efficiency_score

# Grid load data (hourly measurements)
hourly_load = [65, 70, 72, 68, 75, 80, 85, 90, 95, 100, 105, 110,
              112, 115, 118, 120, 119, 117, 115, 110, 105, 100, 95, 90]

# Secondary irrelevant variable (minor distraction - intervention level 4)
temperature_log = [22, 21, 20, 19, 18, 17, 16, 16, 17, 18, 20, 22,
                    23, 24, 25, 26, 25, 24, 23, 22, 21, 20, 19, 18]

# Key computation
energy_threshold = calculate_efficiency(hourly_load)

print(f"Target result: {energy_threshold}")