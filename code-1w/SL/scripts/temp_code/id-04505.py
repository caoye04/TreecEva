import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples():
    raw_readings = [i * 0.7 for i in range(1, 26)]
    noise_floor = sum([math.sin(x) for x in raw_readings]) / len(raw_readings)
    calibrated = [r + noise_floor for r in raw_readings]
    return calibrated

# Irrelevant auxiliary function - red herring
def compute_efficiency_rating(data):
    total = 0
    for x in data:
        if x > 10:
            total += x * 0.3
    return total // 2  # Dead computation path

# Data transformation pipeline
def filter_outliers(sequence, limit=15.0):
    filtered = []
    for val in sequence:
        if abs(val) < limit:
            filtered.append(val)
    return filtered

# Misleading intermediate analysis (not used in final result)
def estimate_entropy(data):
    entropy = 0.0
    for x in data:
        if x != 0:
            entropy += x * math.log(abs(x))
    return round(entropy, 4)

# Core pattern analyzer with complex logic chain
def analyze_pattern(signal, cutoff):
    magnitude_sum = 0
    oscillation_count = 0
    prev_sign = 1
    
    for idx, sample in enumerate(signal):
        # Accumulate energy above threshold
        if sample > cutoff:
            magnitude_sum += sample * (idx % 3 + 1)
        
        # Detect zero-crossing-like behavior
        current_sign = 1 if sample >= 0 else -1
        if current_sign != prev_sign:
            oscillation_count += 1
        prev_sign = current_sign
        
        # Early termination decoy (never triggers due to data range)
        if idx > 100:
            return -999
    
    # Complex weight application
    adjustment_factor = (oscillation_count ** 2) / (cutoff + 1)
    score = magnitude_sum * adjustment_factor
    
    # Distractor: unused conditional branch
    if score < 0:
        final_normalization = math.tanh(score)
    else:
        final_normalization = math.sqrt(score) if score > 1 else score
    
    # Final computation
    return int(score + 0.5)  # Round to nearest integer

# Unused helper - adds interference
def generate_synthetic_baseline(n):
    return [math.cos(i * 0.5) for i in range(n)]

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect real sensor samples
    sensor_data = collect_samples()
    
    # Step 2: Apply filtering (some values truncated)
    cleaned_data = filter_outliers(sensor_data, limit=15.0)
    
    # Step 3: Transform via non-linear scaling
    transformed_data = [math.asinh(x) for x in cleaned_data]  # Hyperbolic transform
    
    # Step 4: Compute irrelevant metrics (distractors)
    efficiency = compute_efficiency_rating(sensor_data)
    entropy_estimate = estimate_entropy(transformed_data)
    baseline = generate_synthetic_baseline(10)
    
    # Step 5: Set threshold based on statistical property (median approx)
    sorted_data = sorted(transformed_data)
    threshold = sorted_data[len(sorted_data) // 2]  # Median as threshold
    
    # Step 6: Critical statement - analyze transformed signal
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Print final answer
    print(f"Result: {final_diagnostic}")