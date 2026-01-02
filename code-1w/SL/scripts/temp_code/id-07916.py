import math

def convert_to_fahrenheit(celsius_list):
    # Irrelevant conversion function (not used in final path)
    return [c * 9/5 + 32 for c in celsius_list]

def analyze_trend(temps):
    # Semi-relevant analysis that computes trend but isn't directly used
    avg = sum(temps) / len(temps)
    above_avg = [t for t in temps if t > avg]
    trend_score = len(above_avg) - (len(temps) - len(above_avg))
    return trend_score if trend_score != 0 else 1

def filter_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    std_dev = math.sqrt(sum((x - mean_val) ** 2 for x in data) / len(data))
    # Some filtered data
    filtered = [x for x in data if abs(x - mean_val) / std_dev < threshold]
    return filtered if len(filtered) > 0 else data

def compute_weighted_index(values, weights=None):
    # Dead code path — weights are always provided, default never used
    if weights is None:
        weights = [1] * len(values)
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    total_weight = sum(weights)
    return weighted_sum / total_weight if total_weight != 0 else 0

def process_temperatures(readings):
    # Step 1: Normalize readings by subtracting base offset
    base_offset = 273.15
    celsius_temps = [temp - base_offset for temp in readings]
    
    # Step 2: Filter extreme values using outlier detection
    cleaned_temps = filter_outliers(celsius_temps)
    
    # Step 3: Calculate moving average over 3-hour window (where possible)
    moving_averages = []
    for i in range(len(cleaned_temps) - 2):
        window_avg = (cleaned_temps[i] + cleaned_temps[i+1] + cleaned_temps[i+2]) / 3
        moving_averages.append(round(window_avg, 2))
    
    # Step 4: Apply decay factor to older readings (simulated weighting)
    decay_factors = [0.9**i for i in range(len(moving_averages))]
    adjusted_moving = [ma * df for ma, df in zip(moving_averages, decay_factors)]
    
    # Step 5: Compute stability metric based on variance of adjusted averages
    if len(adjusted_moving) < 2:
        stability = 0
    else:
        mean_adj = sum(adjusted_moving) / len(adjusted_moving)
        variance = sum((x - mean_adj) ** 2 for x in adjusted_moving) / (len(adjusted_moving) - 1)
        stability = math.sqrt(variance)
    
    # Step 6: Final output derived from inverse relation to instability
    final_output = int(100 / (1 + stability)) if stability > 0 else 100
    
    # Irrelevant debug prints and unused variables (distractors)
    debug_snapshot = {"count": len(readings), "base": base_offset, "stability_score": stability}
    trend_analysis = analyze_trend(celsius_temps)
    
    return final_output

# Simulated sensor input (Kelvin scale)
hourly_readings = [298.15, 301.2, 295.4, 303.0, 299.6, 302.8, 297.3, 300.1]

# Key execution point
final_output = process_temperatures(hourly_readings)
print(f"Result: {final_output}")