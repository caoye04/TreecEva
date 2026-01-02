def analyze_temperature_trends(raw_readings):
    daily_averages = []
    for i in range(0, len(raw_readings), 24):
        day_block = raw_readings[i:i+24]
        if len(day_block) == 24:
            avg_temp = sum(day_block) / len(day_block)
            daily_averages.append(round(avg_temp, 2))n
    return daily_averages


def filter_outliers(temps):
    mean_val = sum(temps) / len(temps)
    std_dev = (sum((t - mean_val) ** 2 for t in temps) / len(temps)) ** 0.5
    lower_bound = mean_val - 1.5 * std_dev
    upper_bound = mean_val + 1.5 * std_dev
    filtered = [t for t in temps if lower_bound <= t <= upper_bound]
    outlier_count = len(temps) - len(filtered)  # distractor
    return filtered


def extract_peak_info(temp_list):
    max_temp = max(temp_list)
    min_temp = min(temp_list)
    peak_index = temp_list.index(max_temp)
    temp_range = max_temp - min_temp
    normalized_peaks = [round((t - min_temp) / temp_range, 3) for t in temp_list]  # semi-relevant
    return max_temp, peak_index, normalized_peaks


def calculate_final_score(data):
    score_components = []
    for record in data:
        trend_value = record['trend']
        stability = record.get('stability', 1.0)
        weight = record['weight']
        adjusted = abs(trend_value) * weight * stability
        score_components.append(adjusted)
    
    base_score = sum(score_components)
    penalty_factor = 0.9 if len(data) < 5 else 1.0
    final_score = int(round(base_score * penalty_factor))
    return final_score

# Simulated sensor data processing pipeline
raw_sensor_data = [
    22.1, 22.3, 22.0, 21.8, 21.7, 21.9, 22.5, 23.1,
    23.6, 24.0, 24.2, 24.5, 24.3, 24.1, 23.9, 23.7,
    23.5, 23.4, 23.6, 23.8, 24.0, 24.2, 24.1, 23.9,
    25.0, 25.2, 24.8, 24.6, 24.4, 24.5, 24.7, 24.9,
    25.1, 25.3, 25.5, 25.4, 25.2, 25.0, 24.8, 24.6
]

# Step 1: Compute daily averages from hourly readings
averages_per_day = analyze_temperature_trends(raw_sensor_data)

# Step 2: Filter statistical outliers
cleaned_averages = filter_outliers(averages_per_day)

# Step 3: Extract peak characteristics (index used later)
max_avg, peak_day_index, norm_vals = extract_peak_info(cleaned_averages)

# Step 4: Prepare metadata with some irrelevant fields
metadata_records = []
for idx, avg in enumerate(cleaned_averages):
    deviation = round(abs(avg - max_avg), 2)
    category_tag = 'high' if avg > 24.0 else 'normal'
    fake_checksum = (idx + 1) * 17 % 13  # irrelevant
    stability_metric = 1.0 - (deviation / 100)  # slightly affects final result
    metadata_records.append({
        'day': idx + 1,
        'trend': avg - 20.0,
        'weight': 2 if idx == peak_day_index else 1,
        'stability': stability_metric,
        'checksum': fake_checksum,
        'tag': category_tag
    })

# Step 5: Process using slicing and zip to align with auxiliary indices
aux_indices = list(range(len(metadata_records)))
paired_data = list(zip(metadata_records, aux_indices))
processed_data = []
for item, pos in paired_data:
    item_copy = item.copy()
    item_copy['offset'] = pos * 0.1  # dead feature
    if pos % 2 == 0:
        item_copy['trend'] += 0.5  # minor modification
    processed_data.append(item_copy)

# Introduce distractor computation with sets
unique_tags = {r['tag'] for r in processed_data}
duplicate_flags = [0 for _ in range(len(processed_data))]  # unused array
buffer_slice = raw_sensor_data[::3]  # every 3rd reading - not used

# Key execution point
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")