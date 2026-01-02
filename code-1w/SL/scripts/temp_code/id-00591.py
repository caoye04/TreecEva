def analyze_trend(data, threshold):
    trend_vector = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_vector.append(1)
        elif data[i] < data[i-1]:
            trend_vector.append(-1)
        else:
            trend_vector.append(0)
    
    # Irrelevant computation: counts transitions but not used
    flat_to_up = 0
    for j in range(1, len(trend_vector)):
        if trend_vector[j-1] == 0 and trend_vector[j] == 1:
            flat_to_up += 1
    
    return [x * threshold for x in trend_vector]


def normalize_series(series):
    total = sum(abs(x) for x in series)
    if total == 0:
        return series
    return [round(x / total, 4) for x in series]

# Simulated sensor metrics over time
temperature_readings = [23.5, 24.1, 23.9, 24.3, 25.0, 24.8, 25.2]
humidity_readings = [45, 46, 48, 47, 50, 52, 51]
pressure_readings = [1013, 1012, 1014, 1015, 1013, 1012, 1011]

# Extract key trends
temp_trend = analyze_trend(temperature_readings, 0.8)
humid_trend = analyze_trend(humidity_readings, 0.5)
press_trend = analyze_trend(pressure_readings, 0.3)

# Combine trends
combined_trend = []
for i in range(len(temp_trend)):
    combined_trend.append(temp_trend[i] + humid_trend[i] + press_trend[i])

# Normalize combined trend
normalized_trend = normalize_series(combined_trend)

# Slice middle portion for stability analysis
stability_window = normalized_trend[1:-1]

# Filler variables - misleading but not used
baseline_offset = sum(normalized_trend) * 0.1
adjustment_factor = max(stability_window, default=0) - min(stability_window, default=0)
dummy_weights = [0.1, 0.2, 0.4, 0.2, 0.1][:len(stability_window)]

# Real processing begins here
metrics = [abs(x) for x in stability_window]
weights = [0.25, 0.25, 0.25, 0.25][:len(metrics)]  # Uniform weighting

# Dead code path - looks important but unused
if len(metrics) > 5:
    scaled_metrics = [m * 1.5 for m in metrics]
else:
    temp_buffer = [0] * 5  # Unused allocation
    scaled_metrics = metrics  # Redundant assignment

# Core evaluation logic
def evaluate_performance(mets, wts):
    score = 0.0
    for i in range(len(mets)):
        contribution = mets[i] * wts[i]
        score += contribution
    
    # Extra distraction: entropy-like calc (not used)
    import math
    entropy = 0
    for m in mets:
        if m > 0:
            entropy -= m * math.log(m)
    
    # Final adjustment based on pattern symmetry
    reversed_mets = mets[::-1]
    symmetry_match = sum(1 for i in range(len(mets)) if abs(mets[i] - reversed_mets[i]) < 0.01)
    if symmetry_match >= len(mets) // 2:
        score *= 1.1
    
    return round(score, 4)

# Critical execution point
final_score = evaluate_performance(metrics, weights)

# Output result
print(f"Result: {final_score}")