def analyze_trend(values):
    if len(values) < 2:
        return 0
    trend = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend += 1
        elif values[i] < values[i-1]:
            trend -= 1
    return trend

values_dataset = [15, 22, 18, 24, 24, 30, 28]

# Irrelevant computation: tracking peaks (not used later)
peak_count = 0
for i in range(1, len(values_dataset)-1):
    if values_dataset[i-1] < values_dataset[i] > values_dataset[i+1]:
        peak_count += 1

baseline = sum(values_dataset) / len(values_dataset)
scaled_values = [round(x - baseline + 10) for x in values_dataset]

# Misleading intermediate transformation
transformed = {i: scaled_values[i]**2 for i in range(len(scaled_values))}
adjusted = [abs(scaled_values[i]) if i % 2 == 0 else -scaled_values[i] for i in range(len(scaled_values))]

# Dummy statistical measure (unused)
mean_adjusted = sum(adjusted) / len(adjusted)
variance_proxy = sum((x - mean_adjusted)**2 for x in adjusted) / len(adjusted)

thresholds = {'high': 12, 'medium': 8, 'low': 5}
data = {
    'readings': scaled_values,
    'status': ['high' if x > thresholds['high'] else 'low' for x in scaled_values]
}

# Conditional expression with slicing distraction
snapshot = data['readings'][2:5] if len(data['readings']) > 4 else [0]
impact_factor = 1.5 if sum(snapshot) > 10 else 0.5

# Helper function that appears complex but is deterministic
def calculate_final_score(data, thresholds):
    readings = data['readings']
    status_flags = data.get('status', [])
    
    # Nested logic with early termination
    if not readings or max(readings) < thresholds['low']:
        return -1
    
    high_count = 0
    for s in status_flags:
        if s == 'high':
            high_count += 1
    
    base_score = sum(readings)
    adjustment = 0
    
    # Interdependent calculations
    if high_count > 2:
        adjustment += 10
    elif high_count == 2:
        adjustment += 5
    
    trend_strength = analyze_trend(readings)
    if trend_strength > 0:
        adjustment += 3
    
    # Final conditional logic
    multiplier = 1.2 if adjustment > 7 else 1.0
    
    # Key result computation
    final = (base_score + adjustment) * multiplier
    
    # Dead code branch (never reached due to logic above)
    if final < 0:
        return 0
        extra_bonus = 20  # unreachable
    
    return int(round(final))

# Execution point of interest
final_score = calculate_final_score(data, thresholds)
print(f"Result: {final_score}")