import math

# Simulated sensor data processing with diagnostic analysis
def collect_telemetry():
    raw_samples = [14.2, 17.5, 23.1, 9.8, 44.3, 12.7, 8.5, 55.9, 33.4, 19.2]
    baseline = 15.0
    adjusted = [x - baseline for x in raw_samples]
    return adjusted

# Irrelevant helper: calculates statistical dispersion (not used in final logic)
def compute_dispersion(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

# Signal filter that mimics noise reduction (partially relevant)
def apply_filter(signal):
    filtered = []
    for i, val in enumerate(signal):
        if i == 0:
            filtered.append(val)
        else:
            smoothed = 0.7 * val + 0.3 * filtered[-1]
            filtered.append(smoothed)
    return filtered

# Misleading anomaly detector (dead-end function, never called)
def detect_anomalies(stream):
    anomalies = []
    for idx, point in enumerate(stream):
        if abs(point) > 40:
            anomalies.append((idx, point))
    return anomalies  # This result is never used

# Core transformation: maps values to diagnostic categories
def categorize_magnitude(x):
    if x < 0:
        return 'LOW'
    elif 0 <= x < 10:
        return 'NORMAL'
    elif 10 <= x < 25:
        return 'ELEVATED'
    else:
        return 'CRITICAL'

# Data enrichment with decoy operations
def enrich_dataset(clean_signal):
    labeled = []
    temp_log = []  # Unused logging structure (distractor)
    
    for i, val in enumerate(clean_signal):
        category = categorize_magnitude(abs(val))
        entry = {
            'index': i,
            'value': round(val, 2),
            'class': category,
            'flagged': True if category == 'CRITICAL' else False
        }
        labeled.append(entry)
        
        # Dead code path: condition never met due to prior filtering
        if val > 100:
            temp_log.append(f"Extreme at {i}")
            break  # Unreachable break
            
    # Decoy operation: creates unused hash map
    lookup_index = {entry['index']: entry['class'] for entry in labeled}
    
    return labeled

# Threshold configuration map (actually used)
def generate_thresholds(levels=4):
    config = {}
    for level in range(levels):
        config[level] = {
            'min': 5 * level,
            'max': 5 * (level + 1),
            'weight': 0.1 * (level + 1)
        }
    return config

# Main diagnostic engine with complex control flow
def analyze_signal(dataset, thresholds):
    score = 0
    decay_factor = 0.95
    history = []
    
    # Linear search through enriched records
    for item in dataset:
        val = abs(item['value'])
        class_label = item['class']
        index = item['index']
        
        # Conditional expression with side-effect-like accumulation
        contribution = (val * 1.5) if class_label == 'ELEVATED' else (val * 2.0 if class_label == 'CRITICAL' else val)
        
        # Update score with weighted contribution
        level_key = min(3, int(val // 10))  # Map to 0-3
        weight = thresholds[level_key]['weight']
        score += contribution * weight
        
        # History tracking (only some entries matter)
        if item['flagged']:
            history.append(contribution)
        
        # Early termination if too many critical events
        if len(history) >= 2 and index > 5:
            score *= 1.2  # Penalty multiplier
            break
    
    # Final adjustment using enumerate and zip (core step)
    if len(history) > 0:
        indices = list(range(len(history)))
        for i, h_val in enumerate(history):
            adjustment = h_val * 0.1
            # Use of zip in a non-trivial context
            for idx, adj in zip(indices[i:], [adjustment] * (len(indices) - i)):
                score += adj * (0.9 ** idx)
    
    return int(round(score))

# --- Execution Flow ---
raw_data = collect_telemetry()
dispersion_metric = compute_dispersion(raw_data)  # Irrelevant assignment
filtered_signal = apply_filter(raw_data)
processed_data = enrich_dataset(filtered_signal)
threshold_map = generate_thresholds(4)

# Key execution point
final_diagnostic = analyze_signal(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")