def analyze_trend(values):
    trend = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend += 1
        elif values[i] < values[i-1]:
            trend -= 1
    return trend

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return x ** 2 + 3 * x - 7

# Simulate sensor data drift (distractor computation)
def simulate_drift(data, factor=0.98):
    drifted = [data[0]]
    for i in range(1, len(data)):
        drifted.append(data[i] * factor)
        factor *= 0.999  # Gradual change
    return drifted

# Core logic
thresholds = {'low': 22.5, 'high': 45.0}
data = [12, 25, 30, 48, 41, 39, 52, 28]

# Distractor: irrelevant transformation
shifted_data = [x + 5 for x in data]
sliced_window = shifted_data[2:6]  # Not used later

# Misleading intermediate calculation
baseline = sum(data) / len(data)
adjusted_baseline = baseline * 1.05

# Another red herring: complex but unused structure
trend_analysis = {
    'up': 0,
    'down': 0,
    'stable': 0
}
for i in range(1, len(data)):
    if data[i] > data[i-1]:
        trend_analysis['up'] += 1
    elif data[i] < data[i-1]:
        trend_analysis['down'] += 1
    else:
        trend_analysis['stable'] += 1
}

# Actual relevant slicing and processing
effective_slice = data[1:-1]  # Exclude first and last
smoothed = [sum(effective_slice[i:i+3]) / 3 for i in range(len(effective_slice) - 2)]

# Logical operations and comparisons
valid_readings = 0
for val in smoothed:
    if val >= thresholds['low'] and val <= thresholds['high']:
        valid_readings += 1

# Boolean flags with short-circuiting
is_stable = len(smoothed) > 0 and abs(smoothed[-1] - smoothed[0]) < 10
is_significant = valid_readings > 0 or analyze_trend(smoothed) >= 1

# Final score calculation (key statement)
def calculate_final_score(data, thresholds):
    temp = data[2:5]  # Slice of interest
    total = 0
    multiplier = 1
    for x in temp:
        if x > thresholds['high']:
            multiplier = 2
        total += x
    result = total * multiplier
    
    # Extra distraction inside function
    dummy = [x**0.5 for x in temp if x > 0]
    adjustment = len(dummy) > 2 and multiplier == 2
    if adjustment:
        result -= 5  # This won't trigger
        
    return int(result)

final_score = calculate_final_score(data, thresholds)
print(f"Target result: {final_score}")