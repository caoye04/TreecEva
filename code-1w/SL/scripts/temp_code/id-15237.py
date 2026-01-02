def analyze_growth_pattern(data):
    trend = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend.append(1)
        elif data[i] < data[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    return trend

# Simulated weekly plant growth in cm (irrelevant for final result but adds distraction)
growth_data = [2.1, 2.3, 2.3, 2.6, 3.0, 3.1, 3.2]
trend_analysis = analyze_growth_pattern(growth_data)

# Daily water intake in ml (distractor)
water_intake = [80, 85, 90, 95, 100, 110, 120]
avg_water = sum(water_intake) / len(water_intake)

# Key operational data: daily crop output in kg
base_output = [45, 52, 48, 55, 60, 53, 50]

# Apply adjustment based on temperature fluctuation (some irrelevant processing)
temperature_offset = [-0.5, 0.2, 0.0, 0.8, -0.3, 0.1, 0.4]
adjusted_output = [base_output[i] + temperature_offset[i] * 0.9 for i in range(len(base_output))]

# Normalize using min-max scaling (semi-relevant but not directly used later)
normalized = [(x - min(adjusted_output)) / (max(adjusted_output) - min(adjusted_output)) for x in adjusted_output]

# Actual critical computation path begins
filtered_output = [x for x in adjusted_output if x >= 50]

# Introduce slicing distraction
slice_peak = filtered_output[1:3]
slice_avg = sum(slice_peak) / len(slice_peak)

# Compute rolling 3-day average (only one value used later)
rolling_avg = []
for i in range(2, len(adjusted_output)):
    rolling_avg.append(sum(adjusted_output[i-2:i+1]) / 3)

# Use only last element of rolling average in final logic
bias_correction = 1.05 if rolling_avg[-1] > 52 else 0.98

# Core calculation function
def calculate_harvest_efficiency(output_list):
    total = sum(output_list)
    peak = max(output_list)
    days_above_mean = len([x for x in output_list if x > (total / len(output_list))])
    
    # Dummy computations with dead variables
    efficiency_score = 0.0
    stability_index = 0.0
    volatility_ratio = 0.0
    
    # Real formula
    base_efficiency = (total * 0.87) / len(output_list)
    peak_bonus = 1.5 if peak >= 58 else 0.5
    day_weight = days_above_mean * 0.3
    
    return base_efficiency + peak_bonus + day_weight

# Final assignment
final_yield = calculate_harvest_efficiency(filtered_output)
print(f"Result: {final_yield}")