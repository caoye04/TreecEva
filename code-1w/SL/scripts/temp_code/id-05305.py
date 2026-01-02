def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count += 1
    return count

# Simulate sensor data smoothing
def smooth_data(data):
    smoothed = [data[0]]
    for i in range(1, len(data)-1):
        smoothed.append((data[i-1] + data[i] + data[i+1]) / 3)
    smoothed.append(data[-1])
    return smoothed

# Irrelevant transformation - distractor
def transform_signal(signal):
    return [x * 0.95 + 2 for x in signal]

# Data calibration function - partially relevant
lambda_calibrate = lambda readings: [max(0, r - 1.5) for r in readings]

# Main evaluation logic
def evaluate_performance(weights, results):
    calibrated = lambda_calibrate(results)
    
    # Apply weight scaling - only some weights matter
    scaled = []
    for i, val in enumerate(calibrated):
        if i < len(weights):
            scaled.append(val * weights[i])
        else:
            scaled.append(val * 0.5)
    
    # Compute moving average of 3 points - distractor computation
    if len(scaled) >= 3:
        ma_values = []
        for j in range(1, len(scaled) - 1):
            ma_values.append((scaled[j-1] + scaled[j] + scaled[j+1]) / 3)
    
    # Identify performance peaks (actual key step)
    peak_count = analyze_pattern(scaled)
    
    # Secondary metric - unused distraction
    transformed = transform_signal(scaled)
    avg_transformed = sum(transformed) / len(transformed) if transformed else 0
    
    # Final scoring logic - depends only on peak_count and sum of scaled
    base_score = sum(scaled)
    bonus = peak_count * 10
    final = base_score + bonus
    
    # Red herring variable
    normalized_score = final / (max(scaled) if scaled else 1)
    
    return int(final)  # deterministic integer result

# Generate synthetic data
raw_results = [4.2, 6.8, 3.1, 7.9, 2.5, 5.3, 6.7, 1.8]
metric_weights = [1.2, 0.8, 1.5, 0.9, 1.1]

# Preprocessing chain with irrelevant steps
smoothed_raw = smooth_data(raw_results)
processed_results = [round(x, 1) for x in smoothed_raw]  # minor adjustment

# Unused alternate path - dead code branch
if False:
    processed_results = [x * 2 for x in raw_results]

# Key execution point
final_score = evaluate_performance(metric_weights, raw_results)

print(f"Result: {final_score}")