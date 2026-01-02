def analyze_trends(data):
    trends = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trends.append(1)
        elif data[i] < data[i-1]:
            trends.append(-1)
        else:
            trends.append(0)
    return trends

# Simulate sensor readings over time
temperature_readings = [20, 22, 21, 23, 25, 24, 26, 26, 27, 25]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1013, 1012, 1011, 1010, 1009]
humidity_readings = [45, 47, 46, 48, 50, 55, 60, 62, 63, 61]

# Extract trend patterns
temp_trend = analyze_trends(temperature_readings)
pressure_trend = analyze_trends(pressure_readings)
humidity_trend = analyze_trends(humidity_readings)

# Misleading distraction: unused derived metric
combined_volatility = [abs(temp_trend[i]) + abs(pressure_trend[i]) + abs(humidity_trend[i]) for i in range(len(temp_trend))]

# Slice only the middle segment for detailed analysis (days 2-8)
effective_trends = [temp_trend[1:8], pressure_trend[1:8], humidity_trend[1:8]]

# Weighted scoring system
weights = [0.5, 0.3, 0.2]  # temp, pressure, humidity importance
metrics = []

for i in range(len(effective_trends[0])):
    score = 0
    # Positive trend in temperature contributes positively
    if effective_trends[0][i] == 1:
        score += 10 * weights[0]
    elif effective_trends[0][i] == -1:
        score -= 5 * weights[0]
    
    # Pressure stability preferred; deviations penalized
    if abs(effective_trends[1][i]) == 1:
        score -= 3 * weights[1]
    
    # Rising humidity moderately penalized due to comfort index
    if effective_trends[2][i] == 1:
        score -= 2 * weights[2]
    elif effective_trends[2][i] == -1:
        score += 1 * weights[2]
    
    metrics.append(round(score, 4))

# Auxiliary function with red herring logic
def calculate_efficiency_index(values):
    peak = max(values) if values else 0
    avg = sum(values) / len(values) if values else 0
    efficiency = (avg / (peak + 1)) * 100 if peak > 0 else 0
    return round(efficiency, 2)

# Unused but plausible calculation — distractor
eff_index = calculate_efficiency_index([len(temp_trend), len(pressure_trend)])

# Core evaluation logic
def evaluate_performance(metric_scores, w):
    adjusted_total = 0.0
    decay_factor = 0.9
    
    for idx, s in enumerate(metric_scores):
        # Apply exponential decay to emphasize recent performance
        adjusted_total += s * (decay_factor ** idx)
    
    # Normalize by number of observations
    normalized = adjusted_total / len(metric_scores) if metric_scores else 0
    
    # Secondary adjustment based on trend consistency
    consecutive_improvements = 0
    max_consecutive = 0
    for sc in metric_scores:
        if sc > 0:
            consecutive_improvements += 1
            max_consecutive = max(max_consecutive, consecutive_improvements)
        else:
            consecutive_improvements = 0
    
    if max_consecutive >= 3:
        normalized += 2.5  # bonus for sustained positive trend
    
    return round(normalized, 4)

# Final computation
dummy_padding = [0]*5  # irrelevant buffer
trimmed_metrics = metrics[:]  # full copy, no actual trimming
final_score = evaluate_performance(trimmed_metrics, weights)

# Irrelevant slicing operation on dummy data
shadow_slice = dummy_padding[2:4]

# Print result as required
print(f"Result: {final_score}")