import itertools

# Simulated sensor data processing with performance evaluation
raw_readings = [142, 89, 203, 77, 191, 64, 227, 130]
base_threshold = 100
calibration_factor = 0.87
noise_floor = 15

# Irrelevant transformation - red herring
shifted_values = [(x << 2) ^ 42 for x in raw_readings if x % 3 != 0]

# Distractor: unused function
def analyze_signal_strength(signal):
    return sum((s ** 0.5 for s in signal if s > 50)) // len(signal)

# Real preprocessing path
filtered_data = list(filter(lambda x: x > noise_floor, raw_readings))
normalized_data = [x * calibration_factor for x in filtered_data]

# Misleading intermediate metric
apparent_magnitude = sum(itertools.starmap(lambda x, y: abs(x - y), zip(normalized_data[:-1], normalized_data[1:])))

# Dummy control flow with dead branch
if apparent_magnitude < 50:
    adjustment = -10
elif apparent_magnitude > 200:
    adjustment = 0  # This will actually be taken
else:
    adjustment = 5

# Core logic disguised among distractions
metric_data = {
    'peaks': len([x for x in normalized_data if x > base_threshold]),
    'stability': len(normalized_data) - apparent_magnitude // 50,
    'consistency': sum(1 for x, y in zip(raw_readings, normalized_data) if (x + y) % 2 == 0)
}

# Decoy computation using itertools
rolling_averages = list(itertools.accumulate(
    [sum(normalized_data[i:i+3]) / 3 for i in range(len(normalized_data)-2)]
))

# Unused complex lambda chain
validate_chain = lambda f: lambda x: f(f(x))
double_check = validate_chain(lambda n: n * 2)

# Real scoring logic buried in complexity
def evaluate_performance(metrics, threshold):
    peak_weight = 3 if metrics['peaks'] > threshold / 50 else 2
    stability_weight = 2
    consistency_weight = 1
    
    # Complex conditional expression
    bonus = 10 if (metrics['peaks'] > 4 and metrics['stability'] > 6) or (metrics['consistency'] % 7 == 0) else 0
    
    # Core calculation
    raw_score = (
        peak_weight * metrics['peaks'] + 
        stability_weight * metrics['stability'] + 
        consistency_weight * metrics['consistency']
    )
    
    # Final adjustment based on hidden rule
    final_modifier = -5 if raw_score % 13 == 0 else adjustment  # adjustment is 0 from earlier
    return raw_score + bonus + final_modifier

# Key execution point
final_score = evaluate_performance(metric_data, base_threshold)

# Irrelevant post-processing
optimized_results = [round(x * 1.05) for x in rolling_averages if x > 100]
metadata_summary = {"count": len(optimized_results), "max": max(optimized_results) if optimized_results else 0}

print(f"Result: {final_score}")