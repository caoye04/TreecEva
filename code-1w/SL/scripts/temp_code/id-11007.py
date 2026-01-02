from collections import defaultdict, Counter
import itertools

# Simulated sensor data processing for environmental monitoring system
def collect_readings():
    readings = [23.4, 24.1, 22.7, 25.3, 26.0, 24.8, 23.9, 22.1, 25.0]
    return readings

def apply_calibration(readings, factor=1.02):
    # Apply sensor calibration (benign transformation)
    return [r * factor for r in readings]

def compute_derivatives(signal):
    # First-order differences (used in distraction path)
    return [signal[i+1] - signal[i] for i in range(len(signal)-1)]

def analyze_trend(derivatives):
    # Determine trend direction (red herring function - not used in final result)
    pos = sum(1 for d in derivatives if d > 0)
    neg = sum(1 for d in derivatives if d < 0)
    return 'upward' if pos > neg else 'downward'

def generate_combinations(values):
    # Create all 2-element combinations (distractor computation)
    combs = list(itertools.combinations(values, 2))
    avg_product = sum(a * b for a, b in combs) / len(combs) if combs else 0
    return avg_product

def filter_outliers(data, threshold=2.0):
    mean = sum(data) / len(data)
    std = (sum((x - mean)**2 for x in data) / len(data))**0.5
    return [x for x in data if abs(x - mean) <= threshold * std], std

def aggregate_metrics(clean_data, std_dev):
    metrics = defaultdict(float)
    metrics['mean'] = sum(clean_data) / len(clean_data)
    metrics['range'] = max(clean_data) - min(clean_data)
    metrics['stability'] = metrics['mean'] / (metrics['range'] + 1e-6)
    metrics['entropy'] = 0.0
    for val in clean_data:
        p = val / (sum(clean_data) + 1e-6)
        metrics['entropy'] -= p * __import__('math').log(p + 1e-6)
    return dict(metrics)

def evaluate_performance(metrics, base_threshold):
    # Core evaluation logic
    score = 0
    score += int(metrics['mean'] * 10)
    score -= int(metrics['range'])
    if metrics['stability'] > 0.8:
        score += 25
    elif metrics['stability'] > 0.5:
        score += 10
    else:
        score -= 5
    
    # Hidden key calculation: contribution from entropy discretization
    entropy_contribution = int(metrics['entropy'] * 5)
    score += entropy_contribution
    
    # Decoy conditional based on unused variables
    if 'phantom_metric' in metrics:
        score *= 2  # Dead code path - never reached
    
    return score

# Irrelevant global constants (distractors)
MAX_ITERATIONS = 1000
CONVERGENCE_TOLERANCE = 1e-5
TEMPORAL_WINDOW = 30

# Main execution flow
raw_readings = collect_readings()
calibrated = apply_calibration(raw_readings)

# Distraction branch 1: derivative analysis (not used later)
derivatives = compute_derivatives(calibrated)
trend = analyze_trend(derivatives)

# Distraction branch 2: combination statistics
combination_avg = generate_combinations(calibrated)

# Critical data path
filtered_data, std_deviation = filter_outliers(calibrated, threshold=1.8)
metric_data = aggregate_metrics(filtered_data, std_deviation)
base_threshold = 0.75

# Key statement
final_score = evaluate_performance(metric_data, base_threshold)

# Print result as required
print(f"Result: {final_score}")