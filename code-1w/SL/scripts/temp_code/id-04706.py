def analyze_trend(temps):
    avg = sum(temps) / len(temps)
    deviation = [t - avg for t in temps]
    squared_dev = [d ** 2 for d in deviation]
    variance = sum(squared_dev) / len(squared_dev)
    return variance < 5

# Simulate environmental data
soil_conditions = [0.8, 0.6, 0.9, 0.7, 0.5]
temperature_weekly = [22, 23, 21, 24, 22, 23, 25]
humidity_levels = [60, 65, 63, 67, 66, 64, 68]

# Misleading auxiliary calculation (irrelevant to final result)
external_factor = 0
for h in humidity_levels:
    if h > 65:
        external_factor += 0.05

# Extract key climate windows using slicing
climate_data = temperature_weekly[1:6:2]  # [23, 22, 23]

# Secondary processing with distractor variables
temp_avg = sum(climate_data) / len(climate_data)
dummy_score = 0
for i in range(len(soil_conditions)):
    if soil_conditions[i] > 0.7:
        dummy_score += 1

# Conditional optimization path
def optimize_harvest(temps, soil):
    yield_base = 0
    boost_factor = 1.0
    
    # Logical and arithmetic chain
    if len(temps) >= 3 and analyze_trend(temps):
        yield_base += 120
        boost_factor *= 1.2
    else:
        yield_base += 80
    
    # Multiple assignments and destructuring
    good_zones = [s for s in soil if s > 0.65]
    primary, *remaining = good_zones  # tuple unpacking
    
    # Irrelevant recursion (dead-end path)
    def calculate_depth(n):
        if n <= 1:
            return 1
        return n + calculate_depth(n - 2)
    
    irrelevant_call = calculate_depth(5)  # not used
    
    # Actual yield logic
    if primary > 0.75:
        yield_base += 30
    elif sum(remaining) > 1.0:
        yield_base += 15
    
    # Final adjustment via slicing-based check
    recent_temps = temps[-2:]
    if recent_temps[0] < recent_temps[1]:
        yield_base += 10
    
    final_yield = int(yield_base * boost_factor)
    
    # Early return simulation (not triggered)
    if final_yield > 200:
        return final_yield - 5
        
    return final_yield

# Execute main logic
final_yield = optimize_harvest(climate_data, soil_conditions)
Result: {final_yield}