import math

def preprocess_input(raw_values):
    # Normalize values and filter outliers
    normalized = [x / max(raw_values) for x in raw_values]
    filtered = [x for x in normalized if x >= 0.1]
    return filtered

# Simulate sensor readings with noise
temperature_readings = [23.5, 24.1, 22.8, 25.6, 19.3, 20.0, 26.5, 18.2]

# Misleading secondary computation (distractor)
baseline_avg = sum(temperature_readings) / len(temperature_readings)
scaled_scores = [math.exp((x - baseline_avg) / 10) for x in temperature_readings]
decay_factor = 0.95
adjusted_scores = [score * (decay_factor ** i) for i, score in enumerate(scaled_scores)]

# Preprocess the data for scoring
processed_data = preprocess_input(temperature_readings)

# Auxiliary function with conditional logic and early returns
def evaluate_stability(metric):
    if metric > 1.0:
        return 3
    elif metric > 0.8:
        return 2
    elif metric > 0.5:
        return 1
    else:
        return 0

# Secondary distractor: unused helper function (dead code path)
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [abs(x - mean_val) for x in data]

# Main scoring logic with multiple concepts
def calculate_final_score(data):
    base_score = sum(data) * 100
    
    # Apply bonus based on data consistency
    consistency = all(abs(a - b) < 0.05 for a, b in zip(data, data[1:]))
    bonus = 10 if consistency else 0
    
    # Use of slicing and conditional expression
    recent_segment = data[-3:] if len(data) >= 3 else data
    trend_score = sum(recent_segment) * 10
    
    # Nested conditionals and logical operations
    high_performer = any(x > 0.9 for x in data)
    low_variance = (max(data) - min(data)) < 0.2
    
    stability_level = evaluate_stability(base_score / 100)
    
    # Final composition using boolean logic and arithmetic
    final_modifier = 1.2 if high_performer and low_variance else 1.0
    
    # Key assignment point
    final_score = int((base_score + bonus + trend_score) * final_modifier)
    
    return final_score

# Execute main calculation
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")