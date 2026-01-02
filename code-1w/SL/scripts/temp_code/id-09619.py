def analyze_trends(data_slice):
    trend_sum = 0
    fluctuations = 0
    for i in range(1, len(data_slice)):
        if data_slice[i] > data_slice[i-1]:
            trend_sum += 1
        elif data_slice[i] < data_slice[i-1]:
            fluctuations += 1
    return trend_sum, fluctuations


def filter_outliers(raw_values):
    mean_val = sum(raw_values) / len(raw_values)
    std_dev = (sum((x - mean_val) ** 2 for x in raw_values) / len(raw_values)) ** 0.5
    filtered = [x for x in raw_values if abs(x - mean_val) <= 2 * std_dev]
    return filtered


def calculate_final_score(metrics):
    base_score = metrics['trend_strength']
    penalty = 0
    
    if metrics['volatility'] > 3:
        penalty += metrics['volatility'] * 0.5
    if metrics['data_gaps']:
        penalty += 2
    
    adjustment_factor = metrics['coverage_ratio'] * 1.5
    
    # Irrelevant intermediate computation (distractor)
    temp_analysis = [x * 0.1 for x in metrics['raw_sequence']]
    normalized_temp = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0
    
    # Unused but plausible variable (red herring)
    theoretical_max = len(metrics['raw_sequence']) * 2.5
    
    final_score = base_score - penalty + adjustment_factor
    return round(final_score, 4)

# Simulated sensor data over time
sensor_readings = [104, 106, 105, 107, 110, 108, 109, 115, 112, 111, 113, 114, 120, 118, 116, 117, 121, 123, 122, 125]

# Extract recent segment
recent_data = sensor_readings[10:]

# Detect upward trends and noise
trend_count, noise_level = analyze_trends(recent_data)

# Remove statistical outliers
cleaned_data = filter_outliers(sensor_readings)

data_loss = len(sensor_readings) - len(cleaned_data)

gap_exists = data_loss > 0

drift_compensation = sum(abs(a - b) for a, b in zip(cleaned_data, cleaned_data[1:])) / len(cleaned_data)

# Compute coverage ratio based on original vs cleaned
coverage = len(cleaned_data) / len(sensor_readings)

# Prepare metric dictionary
metrics_summary = {
    'trend_strength': trend_count,
    'volatility': noise_level,
    'data_gaps': gap_exists,
    'coverage_ratio': coverage,
    'raw_sequence': cleaned_data  # used in calculation
}

# Additional irrelevant transformations (distraction)
shifted_data = [x - 100 for x in sensor_readings]
scaled_data = [x * 1.05 for x in shifted_data]
aggregated_stats = {
    'avg_shifted': sum(shifted_data) / len(shifted_data),
    'max_scaled': max(scaled_data),
    'min_scaled': min(scaled_data)
}

# Key execution point
final_score = calculate_final_score(metrics_summary)
print(f"Result: {final_score}")