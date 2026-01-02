import itertools

def analyze_trend(data, threshold=5):
    # Irrelevant trend analysis with misleading logic
    increasing = sum(1 for a, b in zip(data, data[1:]) if b > a)
    decreasing = sum(1 for a, b in zip(data, data[1:]) if b < a)
    steady = sum(1 for a, b in zip(data, data[1:]) if b == a)
    total_changes = increasing + decreasing + steady
    
    # Distractor computation: not used later
    volatility = (decreasing * 1.5 + increasing * 0.8) / (total_changes + 1e-5)
    
    return increasing > decreasing


def filter_outliers(values, factor=1.5):
    # Semi-relevant filtering using IQR concept (but simplified)
    sorted_vals = sorted(values)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    
    # Return filtered list
    return [v for v in values if lower_bound <= v <= upper_bound]


def calculate_performance(base, samples):
    # Core function that determines the answer
    adjusted_samples = [abs(s - base) for s in samples]
    
    # Use of itertools to create pairs for difference analysis
    diffs = [abs(a - b) for a, b in itertools.combinations(adjusted_samples, 2)]
    
    # Compute average deviation after filtering
    filtered_diffs = filter_outliers(diffs, factor=2.0)
    
    # Misleading intermediate variables
    peak_deviation = max(filtered_diffs) if filtered_diffs else 0
    avg_deviation = sum(filtered_diffs) / len(filtered_diffs) if filtered_diffs else 0
    
    # Secondary distractor: unused complexity
    normalized_scores = [(d / (peak_deviation + 1)) ** 0.5 for d in filtered_diffs]
    
    # Key decision logic
    trend_stable = analyze_trend(samples)
    
    # Final score depends only on avg_deviation and base adjustment
    adjustment_factor = 0.9 if trend_stable else 1.1
    raw_score = abs(base - avg_deviation) * adjustment_factor
    
    # Introduce another red herring variable
    efficiency_ratio = (len(samples) / (len(diffs) + 1)) * 100  # Unused
    
    final_score = int(raw_score + 0.5)  # Rounded to nearest integer
    
    # This print is required to expose the answer
    return final_score

# Simulated sensor readings and baseline
baseline = 42
readings = [45, 39, 43, 40, 46, 38, 41, 44]

# Dead code path - misleading conditional
if len(readings) > 100:
    extended_analysis = True
    buffer_cache = [0] * 200
else:
    extended_analysis = False  # Not used anywhere

# Intermediate variables that feed into final calculation
preliminary_check = sum(readings) / len(readings)
drift_detected = abs(preliminary_check - baseline) > 3

# Another irrelevant list comprehension
signal_peaks = [x for x in readings if x > preliminary_check]
signal_troughs = [x for x in readings if x < preliminary_check]

# Key execution point
final_score = calculate_performance(baseline, readings)

# Output result as required
print(f"Result: {final_score}")