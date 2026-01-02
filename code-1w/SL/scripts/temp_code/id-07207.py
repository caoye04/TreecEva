from collections import defaultdict
import math

# Simulated sensor data processing with red herrings
def preprocess_sensor_readings(raw):    
    offset = 0.003
    adjusted = [x + offset for x in raw if x > -50]
    baseline = sum(adjusted) / len(adjusted)
    normalized = [(x - baseline) * 1.05 for x in adjusted]
    return normalized

# Irrelevant transformation - decoy function
def spectral_decompose(signal):
    result = []
    for i in range(len(signal)):
        component = 0
        for j in range(5):
            component += math.sin(signal[i] * j) * math.cos(j * 0.1)
        result.append(component)
    return result  # Never used

# Data cleaning with distractor logic
def filter_anomalies(seq, limit=100):
    counts = defaultdict(int)
    for val in seq:
        rounded = round(val, 1)
        counts[rounded] += 1
    
    # Misleading filtering criteria
    noise_floor = 0.1
    filtered = []
    for val in seq:
        if abs(val) < noise_floor:
            continue  # Skip near-zero (but this doesn't actually help)
        filtered.append(val)
    
    # Dead code path - condition never met due to prior preprocessing
    if len(filtered) == 0 and False:  
        fallback = [0.0] * 10
        return fallback
        
    return filtered

# Core pattern analyzer - actually used
def detect_cycle(sequence):
    if len(sequence) < 4:
        return False
    for i in range(len(sequence) - 3):
        if sequence[i] == sequence[i+2] and sequence[i+1] == sequence[i+3]:
            return True
    return False

# Threshold engine with multiple irrelevant parameters
def compute_thresholds(data, sensitivity='high', mode='adaptive'):
    meta_stats = {}
    meta_stats['max'] = max(data)
    meta_stats['min'] = min(data)
    meta_stats['range'] = meta_stats['max'] - meta_stats['min']
    
    # Complex but unused calculation
    integral = 0.0
    for i in range(1, len(data)):
        integral += (data[i] + data[i-1]) * 0.5
    
    # Actual thresholds computed simply
    base_thresh = sum(x ** 2 for x in data) ** 0.5 / len(data)
    adaptive_factor = 1.4 if sensitivity == 'high' else 1.0
    
    thresholds = {
        'critical': base_thresh * 2.1,
        'warning': base_thresh * 1.3,
        'stable': base_thresh * 0.7
    }
    
    # Dead assignment - overwritten later
    thresholds = {k: v * 0.95 for k, v in thresholds.items()}
    
    return thresholds

# Main transformation pipeline
def transform_sequence(values):
    # Apply non-linear scaling
    scaled = [math.log(abs(x) + 1) * 2.1 for x in values]
    
    # Introduce artificial oscillation (distractor)
    modulated = []
    for i, val in enumerate(scaled):
        modulation = math.sin(i * 0.3) * 0.1
        modulated.append(val + modulation)
    
    # Real operation: reverse if pattern detected
    if detect_cycle(modulated):
        modulated = modulated[::-1]
    
    return modulated

# Final analysis - uses the real result
def analyze_pattern(dataset, thresholds):
    magnitude = sum(x ** 2 for x in dataset) ** 0.5
    category_score = 0
    
    # Determine classification
    if magnitude > thresholds['critical']:
        category_score = 7342
    elif magnitude > thresholds['warning']:
        category_score = 3671
    else:
        category_score = 1835
    
    # Spurious complexity
    adjustment = 0
    for x in dataset:
        if x > thresholds['stable']:
            adjustment += int(abs(math.tan(x % 0.5)) * 10) % 3
    
    # Final diagnostic is only based on category_score
    final_value = category_score + adjustment  # adjustment mostly noise
    return final_value

# --- Execution Flow ---
raw_sensor_data = [12.5, -8.3, 12.5, -8.3, 45.0, -15.7, 45.0, -15.7]

# Step 1: Preprocess
processed_data = preprocess_sensor_readings(raw_sensor_data)

# Step 2: Filter anomalies (has no effect here, but looks important)
cleaned_data = filter_anomalies(processed_data)

# Step 3: Transform sequence
dummy_spectral = spectral_decompose(cleaned_data)  # Unused
transformed_data = transform_sequence(cleaned_data)

# Step 4: Compute thresholds
threshold_map = compute_thresholds(transformed_data, sensitivity='high')

# Step 5: Analyze pattern - KEY STATEMENT
final_diagnostic = analyze_pattern(transformed_data, threshold_map)

print(f"Target result: {final_diagnostic}")