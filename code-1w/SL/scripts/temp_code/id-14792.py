import itertools

# System health monitoring simulation with noise filtering and diagnostic logic
def analyze_sensor_stream(raw_readings, baseline):
    filtered = [x for x in raw_readings if abs(x - baseline) > 3]
    anomalies = set()
    trend_magnitude = 0
    
    for i in range(1, len(filtered)):
        if filtered[i] > filtered[i-1]:
            trend_magnitude += 1
        else:
            trend_magnitude -= 1
        anomalies.add(abs(filtered[i] - filtered[i-1]))

    # Irrelevant transformation - red herring
    squared_pairs = [(x**2, y**2) for x, y in zip(filtered, filtered[1:])]
    sum_squares = sum(a * b for a, b in squared_pairs)  # Dead computation

    # Actual signal extraction
    valid_anomalies = {x for x in anomalies if x % 2 == 1}
    peak_response = max(valid_anomalies) if valid_anomalies else 0

    # Decoy recursive function (never called)
    def recursive_dampen(value, depth):
        if depth <= 0 or value < 5:
            return value
        return recursive_dampen(value // 1.5, depth - 1)

    # Unused statistical measures
    mean_deviation = sum(abs(x - baseline) for x in raw_readings) / len(raw_readings)
    variance_proxy = sum((x - baseline)**2 for x in raw_readings) / len(raw_readings)

    return peak_response, trend_magnitude

# Simulated data ingestion
readings = [12, 15, 10, 23, 25, 29, 18, 14, 33, 37, 41, 20, 16]
base = 20

# Spurious list processing - distraction
shifted_blocks = list(itertools.chain.from_iterable([[x-1, x+1] for x in readings]))
duplicate_filter = [x for x in shifted_blocks if x in readings]  # Unused

# Phantom conditional logic with no impact
mode_flag = 'aggressive'
sensitivity_curve = [i**0.5 for i in range(1, len(readings)+1)]
scaling_factor = 1.75 if mode_flag == 'aggressive' else 0.9  # Not used

# Core diagnostic pipeline
primary_peak, direction_bias = analyze_sensor_stream(readings, base)

# Secondary fake analysis path
fake_aggregates = []
for window in itertools.combinations(readings, 4):
    fake_aggregates.append(sum(window) / len(window))
median_fake = sorted(fake_aggregates)[len(fake_aggregates)//2]  # Distractor

# Real but obscured logic
aggregate_score = primary_peak * abs(direction_bias)
threshold_adjustment = 0
if aggregate_score > 50:
    threshold_adjustment = 25
elif aggregate_score > 30:
    threshold_adjustment = 15
else:
    threshold_adjustment = 5

# Final computation buried in irrelevant context
final_diagnostic = aggregate_score + threshold_adjustment

# Noise variable to mislead
post_analysis_audit = [final_diagnostic * 1.1, final_diagnostic * 0.9, median_fake]

# Output the target result
Target result: {final_diagnostic}