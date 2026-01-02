import itertools

# Simulated sensor data processing pipeline for environmental monitoring

def collect_readings():
    return [0.88, 0.76, 0.91, 0.67, 0.82, 0.95, 0.73]

def normalize(data):
    max_val, min_val = max(data), min(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def filter_outliers(data, threshold=0.1):
    mean = sum(data) / len(data)
    return [x for x in data if abs(x - mean) > threshold]

def compute_rolling_avg(data, window=3):
    if len(data) < window:
        return [0.0]
    rolling = [(sum(data[i:i+window]) / window) for i in range(len(data)-window+1)]
    return rolling

def apply_calibration(readings, factor=1.05):
    # Irrelevant calibration function (not used in final path)
    return [r * factor for r in readings]

def detect_anomalies(patterns):
    # Dead code path — never called
    triggers = []
    for i, p in enumerate(patterns):
        if p > 0.9:
            triggers.append(i)
    return triggers

def generate_combinations(values):
    # Distractor: creates irrelevant combinations
    combos = []
    for r in range(2, 4):
        combos.extend(list(itertools.combinations(values, r)))
    return combos[:10]  # Truncate to avoid explosion

def assess_stability(profile):
    variance = sum((x - sum(profile)/len(profile))**2 for x in profile) / len(profile)
    adjustment = 0.0
    if variance < 0.01:
        adjustment = 0.1
    elif variance > 0.03:
        adjustment = -0.15
    else:
        adjustment = 0.05
    return adjustment

def score_consistency(ratios):
    # Another distractor scoring method (not used)
    total = 0.0
    for r in ratios:
        if r > 0.85:
            total += 0.2
    return total

def evaluate_reliability(indices):
    # Unused reliability check
    return sum(1 for x in indices if x < 0.75)

def evaluate_performance(metrics, base):
    # Core logic begins here
    normalized = normalize(metrics)
    filtered = filter_outliers(normalized, threshold=0.12)
    roll_avg = compute_rolling_avg(filtered)
    
    # Misleading intermediate calculation
    phantom_score = sum([x ** 2 for x in metrics]) * 0.01
    
    # Real contribution: stability assessment
    stability = assess_stability(filtered)
    
    # Red herring: complex combo generation with no impact
    dummy_combos = generate_combinations([0.1, 0.3, 0.6, 0.8])
    combo_value = len(dummy_combos) * 0.001  # Looks important, isn't
    
    # Key decision point: compare against baseline average
    base_avg = sum(base) / len(base)
    met_criteria = sum(1 for m in normalized if m >= base_avg) >= 4
    
    # Final score computation (this is what matters)
    raw_score = sum(roll_avg) + stability
    if met_criteria:
        raw_score += 0.25
    
    # Normalize to integer scale (0-1000)
    final_score = int(raw_score * 1000)
    
    # Decoy print that looks like it's logging the answer
    debug_value = phantom_score * 100
    
    return final_score

# Main execution
if __name__ == '__main__':
    raw_metrics = collect_readings()
    baseline = [0.78, 0.81, 0.75, 0.83]
    
    # Spurious transformations
    calibrated = apply_calibration(raw_metrics)
    anomalies = []  # Never populated
    consistency = score_consistency(calibrated)
    
    # Critical statement
    final_score = evaluate_performance(raw_metrics, baseline)
    
    # Only this line matters
    print(f"Result: {final_score}")