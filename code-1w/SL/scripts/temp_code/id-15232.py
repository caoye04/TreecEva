def analyze_trends(data, threshold=0.5):
    trends = []
    for i in range(1, len(data)):
        change = (data[i] - data[i-1]) / data[i-1] if data[i-1] != 0 else 0
        trends.append(1 if change > threshold else 0)
    return trends

# Simulated sensor readings over time
temperature_readings = [22.1, 23.5, 24.8, 25.3, 24.9, 26.1, 27.5, 28.0, 27.3, 26.8]

# Irrelevant transformation - distractor
normalized_readings = [round((x - min(temperature_readings)) / (max(temperature_readings) - min(temperature_readings)), 3) for x in temperature_readings]

# Extract increasing trend indicators
upward_trend = analyze_trends(temperature_readings, threshold=0.05)

# Secondary processing with slicing - relevant operation
windowed_analysis = upward_trend[1:6]  # Focus on middle segment

# Misleading accumulation - does not affect final result
phantom_accumulator = 0
for val in normalized_readings:
    phantom_accumulator += val * 0.1

# Calculate volatility using absolute differences - semi-relevant preprocessing
volatility = sum(abs(temperature_readings[i] - temperature_readings[i-1]) for i in range(1, len(temperature_readings)))

# Noise filter level - irrelevant constant
filter_level = 1.34

# Core performance metric calculation
def calculate_performance(raw_data):
    base_reference = raw_data[::2]  # Use even-indexed samples only
    reference_avg = sum(base_reference) / len(base_reference)
    
    # Additional filtering based on trend context
    trend_influence = sum(windowed_analysis) * 10
    adjustment_factor = 1.0 + (trend_influence / 100)
    
    # Introduce auxiliary variable that looks important but is unused
    deprecated_metric = max(raw_data) - min(raw_data)
    
    # Final score computation
    raw_score = reference_avg * adjustment_factor
    penalty = 0.5 * sum(1 for x in raw_data if x > reference_avg + 2)
    return int(raw_score - penalty)

# Execute main logic
temp_snapshot = temperature_readings[2:8]  # Slice used in no further computation - red herring

# Key statement
final_score = calculate_performance(temperature_readings)

print(f"Result: {final_score}")