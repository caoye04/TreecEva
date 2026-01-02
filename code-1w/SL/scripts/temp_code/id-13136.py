def analyze_growth_pattern(sequence):
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    return trend

# Simulate soil nutrient levels over weeks (irrelevant to final result)
soil_nutrients = [45, 47, 46, 48, 50, 49, 47]
growth_trend = analyze_growth_pattern(soil_nutrients)

# Field data representing weekly crop measurements in cm
field_data = {
    'plot_A': [12.3, 15.1, 18.7, 23.5, 29.8],
    'plot_B': [10.2, 14.8, 17.9, 22.1, 28.4],
    'plot_C': [11.5, 16.0, 19.2, 24.0, 30.1]
}

# Misleading auxiliary calculation (distractor)
def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

variance_check = {key: round(compute_variance(val), 3) for key, val in field_data.items()}

# Core logic: calculate growth acceleration per plot using differences of differences
accelerations = {}
for name, values in field_data.items():
    diffs = [round(values[i] - values[i-1], 2) for i in range(1, len(values))]
    accels = [diffs[i] - diffs[i-1] for i in range(1, len(diffs))]
    accelerations[name] = accels

# Determine consistency score based on string patterns in plot names (semi-relevant)
consistency_score = 0
for plot_name in field_data.keys():
    if plot_name.startswith('p') and 'o' in plot_name:
        consistency_score += 1
    if len(plot_name) == 5 and plot_name.isalpha():
        consistency_score += 0.5

# Threshold determined from median initial growth (actual relevant computation)
initial_growths = [(data[-1] - data[0]) for data in field_data.values()]
threshold = sum(initial_growths) / len(initial_growths) * 0.65  # 65% of average total growth

# Helper function that appears complex but has simplified effective behavior
def calculate_harvest_efficiency(data_dict, thresh):
    efficiency_scores = []
    adjustment_factor = 0.9
    
    for key, readings in data_dict.items():
        total_increase = readings[-1] - readings[0]
        
        # Apply non-linear scaling (distraction with minor effect)
        if total_increase > thresh:
            scaled = total_increase * adjustment_factor
        else:
            scaled = total_increase * (1 + 0.1 * len(readings))
        
        # Real key computation: count how many readings exceed midpoint baseline
        midpoint_baseline = (readings[0] + readings[-1]) / 2
        above_mid = len([r for r in readings if r > midpoint_baseline])
        stability_bonus = above_mid / len(readings)
        
        # Efficiency is combination of scaled increase and stability
        efficiency = scaled * stability_bonus
        efficiency_scores.append(efficiency)
    
    # Final yield determined by sorted index of first plot (Plot A)
    sorted_efficiencies = sorted(efficiency_scores)
    plot_a_efficiency = efficiency_scores[0]  # corresponds to plot_A
    rank_based_multiplier = (sorted_efficiencies.index(plot_a_efficiency) + 1) / len(sorted_efficiencies)
    
    # Actual answer computed here
    final_yield = int(plot_a_efficiency * rank_based_multiplier * 10)
    
    # Print required output
    print(f"Result: {final_yield}")
    return final_yield

# Execute main logic
calculate_harvest_efficiency(field_data, threshold)