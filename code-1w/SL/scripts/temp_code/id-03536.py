import math

# Simulated sensor array diagnostics with noise filtering and pattern analysis
def collect_readings():
    raw_readings = [2.1, 1.9, 3.5, 4.8, 4.9, 5.1, 6.3, 7.2, 7.0, 6.8, 5.3, 4.7, 3.6, 2.5, 1.8]
    noise_floor = 1.5
    processed = [x for x in raw_readings if x > noise_floor]
    return processed

# Irrelevant auxiliary function - decoy
def compute_entropy(data):
    total = 0.0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return round(total, 3)

# Signal baseline correction - partially relevant but not used in final path
def adjust_baseline(signal, base=2.0):
    return [x - base for x in signal]

# Frequency bucketing - red herring
def categorize_frequencies(readings):
    low = [x for x in readings if x < 3.0]
    mid = [x for x in readings if 3.0 <= x < 6.0]
    high = [x for x in readings if x >= 6.0]
    return {'low': len(low), 'mid': len(mid), 'high': len(high)}

# Real processing: detect symmetry in central window
def extract_window(signal, size=7):
    mid = len(signal) // 2
    start = max(0, mid - size // 2)
    end = start + size
    return signal[start:end]

# Check reflective symmetry - core logic
def is_symmetric(segment):
    n = len(segment)
    for i in range(n // 2):
        if abs(segment[i] - segment[n-1-i]) > 0.1:
            return False
    return True

# Misleading transformation chain - dead path
def transform_signal(signal):
    doubled = [2*x for x in signal]
    shifted = [x - 1 for x in doubled]
    inverted = [10 - x for x in shifted]
    return inverted  # Never actually used

# Main analysis with distractors
def analyze_pattern(data, threshold):
    # Step 1: Extract working window
    window = extract_window(data, size=7)
    
    # Step 2: Apply arbitrary scaling (distraction)
    scaled = [round(x * 1.05, 2) for x in window]
    
    # Step 3: Create fake anomaly score (unused)
    anomalies = 0
    for val in scaled:
        if val > threshold + 1.5 or val < threshold - 1.5:
            anomalies += 1
    
    # Step 4: Generate dummy summary (irrelevant)
    avg_val = sum(scaled) / len(scaled)
    peak = max(scaled)
    stability = round(peak - avg_val, 2)
    
    # Step 5: Determine symmetry status - this affects outcome
    symmetrical = is_symmetric(window)  # Uses original, unscaled window
    
    # Step 6: Compute dispersion metric
    deviations = [abs(x - avg_val) for x in scaled]
    rms_dev = math.sqrt(sum(d**2 for d in deviations) / len(deviations))
    
    # Step 7: Apply conditional logic based on symmetry
    if symmetrical:
        base_score = 420
    else:
        base_score = 280
    
    # Step 8: Final adjustment using RMS deviation
    final_score = base_score + int(rms_dev * 10)
    
    # Step 9: Red herring calculation (never used)
    smoothed = [scaled[0]]
    for i in range(1, len(scaled)):
        smoothed.append(round(0.7 * scaled[i] + 0.3 * smoothed[i-1], 2))
    
    # Step 10: One more distraction
    cumulative = []
    total = 0
    for x in scaled:
        total += x
        cumulative.append(total)
    
    # Step 11: Real final computation
    adjustment_factor = 1 if len(cumulative) % 2 == 0 else -1
    final_diagnostic = final_score + adjustment_factor * 12
    
    # Step 12: Print irrelevant transformed version to distract
    transformed = transform_signal(data)
    
    return final_diagnostic

# Execution flow
sensor_data = collect_readings()
filtered_data = adjust_baseline(sensor_data, base=1.0)  # Note: adjustment doesn't affect logic
threshold = 4.5

# Dead code block - never called
'''
def legacy_analysis():
    return sum(transformed) // 2
'''

# Key statement
final_diagnostic = analyze_pattern(filtered_data, threshold)

# Additional distractions
entropy = compute_entropy(sensor_data)
freq_dist = categorize_frequencies(sensor_data)

# Output the target result
print(f"Result: {final_diagnostic}")