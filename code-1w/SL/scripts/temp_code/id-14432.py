def analyze_temperatures(temp_readings):
    high_threshold = 30
    low_threshold = 10
    hot_days = 0
    cold_days = 0
    moderate_days = 0

    for temp in temp_readings:
        if temp > high_threshold:
            hot_days += 1
        elif temp < low_threshold:
            cold_days += 1
        else:
            moderate_days += 1

    # Distractor calculations
    total_anomalies = abs(hot_days - cold_days) + 2  # Irrelevant offset
    adjustment_factor = 1.5 if hot_days > cold_days else 0.8
    pseudo_stability = (moderate_days + 1) / (len(temp_readings) + 1)

    return {'hot': hot_days, 'cold': cold_days, 'moderate': moderate_days, 'factor': adjustment_factor}


def filter_outliers(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    cleaned = [x for x in data if abs(x - mean_val) <= 2 * std_dev]

    # Dead code path - never used
    if len(cleaned) == 0:
        cleaned = [int(mean_val)]

    outlier_count = len(data) - len(cleaned)  # Computed but not returned
    return cleaned


def calculate_final_score(data_dict):
    base_score = data_dict['hot'] * 3
    penalty = data_dict['cold'] * 2
    bonus = data_dict['moderate']

    # Extra distraction
    hypothetical_max = (data_dict['hot'] + data_dict['moderate']) * 3
    efficiency_ratio = (base_score - penalty) / hypothetical_max if hypothetical_max > 0 else 0

    raw_score = base_score - penalty + bonus
    adjusted = int(raw_score * data_dict['factor'])

    # Final irrelevant transformation
    normalized = round(adjusted / 1.7, 2)
    return int(normalized)


# Main execution
raw_temperatures = [35, 32, 8, 5, 29, 27, 31, 36, 40, 3, 12, 15, 28, 33, 9]

# Step 1: Filter statistical outliers
filtered_temps = filter_outliers(raw_temperatures)

# Step 2: Analyze temperature trends
temp_analysis = analyze_temperatures(filtered_temps)

# Step 3: Process data with set operations (ensure uniqueness)
unique_categories = set(temp_analysis.keys())
disregarded_keys = {'factor'}  
used_keys = unique_categories - disregarded_keys
key_count_tracker = {k: len(k) for k in used_keys}  # Semi-relevant distractor

# Step 4: Build processed data structure
processed_data = {
    'hot': temp_analysis['hot'],
    'cold': temp_analysis['cold'],
    'moderate': temp_analysis['moderate'],
    'factor': temp_analysis['factor']
}

# Step 5: Calculate final score
final_score = calculate_final_score(processed_data)

# Output result
print(f"Result: {final_score}")