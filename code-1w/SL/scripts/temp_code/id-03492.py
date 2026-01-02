def analyze_composition(elements, baseline):
    total_mass = sum(elements)
    normalized = [e / total_mass for e in elements]
    entropy = 0
    for n in normalized:
        if n > 0:
            entropy -= n * __import__('math').log(n)
    return entropy


def refine_materials(batch_data):
    refined_batches = []
    for batch in batch_data:
        avg = sum(batch) / len(batch)
        if avg > 0.5:
            refined_batches.append([x for x in batch if x > 0.3])
    return refined_batches


def calculate_stability_index(seq):
    if len(seq) < 2:
        return 0
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    return sum(diffs) / len(diffs)


def monitor_calibration(readings):
    calibrated = []
    offset = readings[0] - 1.0
    for r in readings:
        adjusted = r - offset
        if adjusted > 0.9:
            calibrated.append(adjusted)
    return calibrated

# Irrelevant helper (distractor)
def predict_yield(entropy, stability):
    return (entropy * 0.6) + (stability * 0.4)

# Decoy function with dead logic
def assess_risk_level(data):
    risk = 0
    for d in data:
        if d < 0.2:
            risk += 1
        elif d > 0.8:
            risk -= 1  # Misleading: high values reduce risk?
    return risk

# Core relevant function with slicing and logic chain
def validate_purity_levels(samples, threshold):
    recent_samples = samples[-10:]  # slicing: focus on last 10
    high_purity = [p for p in recent_samples if p >= threshold]
    low_purity = [p for p in recent_samples if p < threshold]
    
    if len(high_purity) == 0:
        return -1
    
    ratio = len(high_purity) / len(recent_samples)
    
    # Additional logic step: adjust based on trend
    if len(recent_samples) >= 5:
        trend_window = recent_samples[-5:]
        increasing_trend = all(trend_window[i] <= trend_window[i+1] for i in range(len(trend_window)-1))
        if increasing_trend:
            ratio *= 1.25
    
    adjustment_factor = 0.8
    if ratio > 0.9:
        adjustment_factor = 1.1
    elif ratio > 0.7:
        adjustment_factor = 0.95
    
    score = ratio * adjustment_factor * 100
    
    # Final clamping
    if score > 100:
        score = 100
    
    return int(score)

# Simulated sensor data stream (with decoy entries)
purity_samples = [
    0.62, 0.58, 0.71, 0.73, 0.74, 0.69, 0.72, 0.76, 0.78, 0.77,
    0.79, 0.81, 0.80, 0.83, 0.85, 0.82, 0.86, 0.88, 0.91, 0.89,
    0.93, 0.95, 0.94, 0.96, 0.97, 0.98, 0.99, 1.00, 0.99, 0.98
]

# Unused variables (red herrings)
baseline_entropy = 1.45
stability_metric = 0.12
raw_readings = [0.91, 0.88, 0.93, 0.95, 0.92]
material_batches = [[0.4, 0.6, 0.7], [0.3, 0.8, 0.9], [0.5, 0.5, 0.6]]

# Dead code path (never executed but looks important)
calibrated_sensors = []
if len(purity_samples) > 50:
    calibrated_sensors = monitor_calibration(raw_readings)

# Meaningful computation chain starts here
composition_data = [12.1, 8.7, 15.2, 22.3, 10.5, 9.8]
entropy_value = analyze_composition(composition_data, baseline=0.1)
refined = refine_materials(material_batches)
stability_score = calculate_stability_index(purity_samples[::3])  # slicing every 3rd

# Key statement
filtration_score = validate_purity_levels(purity_samples, threshold=0.75)

# Output result
print(f"Result: {filtration_score}")