import math

# Simulated sensor fusion system for environmental monitoring
# Real data processing with extensive irrelevant auxiliary computations

def collect_readings():
    return [23.4, 19.5, 27.3, 21.0, 30.2, 18.7, 25.6]

def filter_outliers(data, threshold=2.0):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean) <= threshold * std_dev]

def compute_entropy(values):
    total = sum(values)
    probs = [(v + 0.1) / (total + 0.1 * len(values)) for v in values]  # Smoothing
    return -sum(p * math.log(p) for p in probs)

def transform_signal(signal):
    # Irrelevant frequency analysis
    N = len(signal)
    transformed = []
    for k in range(N):
        real = sum(signal[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
        imag = sum(-signal[n] * math.sin(2 * math.pi * k * n / N) for n in range(N))
        transformed.append(complex(real, imag))
    magnitude_spectrum = [abs(t) for t in transformed]
    return magnitude_spectrum  # Dead end, never used

def calculate_robustness_index(arr):
    # Misleading function - looks important but unused
    sorted_vals = sorted(arr)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    return (q3 + q1) / (iqr + 1) if iqr != 0 else 0

def evaluate_stability(readings):
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    return sum(diffs) / len(diffs)

def normalize_vector(v):
    norm = sum(x**2 for x in v) ** 0.5
    return [x / norm for x in v] if norm != 0 else v

def simulate_failure_modes(temps):
    # Complex but irrelevant simulation
    critical_count = 0
    for t in temps:
        if t > 28:
            for _ in range(3):
                t *= 0.95
            if t > 26:
                critical_count += 1
    return critical_count * 0.1  # Unused result

def assess_trend_pattern(seq):
    increasing = sum(1 for i in range(1, len(seq)) if seq[i] > seq[i-1])
    decreasing = sum(1 for i in range(1, len(seq)) if seq[i] < seq[i-1])
    return 'increasing' if increasing > decreasing else 'decreasing'

def generate_synthetic_metrics(temp_data):
    base_metric = sum(temp_data) / len(temp_data)
    fluctuation = evaluate_stability(temp_data)
    trend = assess_trend_pattern(temp_data)
    entropy = compute_entropy(temp_data)
    
    # Generate multiple metrics including red herrings
    raw_metrics = {
        'thermal_baseline': base_metric,
        'variance_penalty': fluctuation * 2.5,
        'entropy_factor': entropy,
        'trend_bias': 1.5 if trend == 'increasing' else 0.8,
        'peak_ratio': max(temp_data) / min(temp_data),
        'sample_count': len(temp_data),
        'dummy_placeholder': 999,  # Obvious decoy
        'unused_diagnostic': calculate_robustness_index(temp_data)
    }
    
    # Remove dummy and unused fields
    del raw_metrics['dummy_placeholder']
    del raw_metrics['unused_diagnostic']
    
    return raw_metrics

def apply_calibration_curve(x):
    # Unused calibration logic
    return 1 / (1 + math.exp(-0.1 * (x - 20)))

def dynamic_weight_adjustment(metrics):
    # Complex weight adjustment with distractions
    base_weights = {
        'thermal_baseline': 0.3,
        'variance_penalty': 0.25,
        'entropy_factor': 0.15,
        'trend_bias': 0.2,
        'peak_ratio': 0.1
    }
    
    # Irrelevant dynamic adjustments
    if metrics['thermal_baseline'] > 22:
        base_weights['variance_penalty'] += 0.05
        base_weights['trend_bias'] -= 0.05
    if metrics['peak_ratio'] > 1.5:
        base_weights['entropy_factor'] += 0.03
        
    # Normalize weights
    total = sum(base_weights.values())
    return {k: v / total for k, v in base_weights.items()}

# Key lambda functions - required language feature
geometric_mean = lambda vals: math.exp(sum(math.log(v) for v in vals) / len(vals))
harmonic_mean = lambda vals: len(vals) / sum(1/v for v in vals)

# Data pipeline with distractors
raw_temperatures = collect_readings()
cleaned_temps = filter_outliers(raw_temperatures)

# Irrelevant signal processing chain
spectrum = transform_signal(cleaned_temps)
spectral_centroid = sum(i * mag for i, mag in enumerate(spectrum)) / sum(spectrum) if spectrum else 0

# Simulate failure modes - dead end
failure_risk = simulate_failure_modes(cleaned_temps)

# Core computation path begins here
metrics = generate_synthetic_metrics(cleaned_temps)
weights = dynamic_weight_adjustment(metrics)

# Secondary irrelevant calculations
historical_avg = 22.5
variance_from_history = (metrics['thermal_baseline'] - historical_avg) ** 2
adjustment_factor = apply_calibration_curve(variance_from_history)

# Main aggregation using normalized values and weights
normalized_metrics = {}
for key in weights.keys():
    val = metrics[key]
    # Normalize each metric to 0-1 scale (approximately)
    if key == 'variance_penalty':
        normalized_metrics[key] = 1 - (val / 10)  # Inverted: lower penalty = better
    elif key == 'peak_ratio':
        normalized_metrics[key] = max(0, min(1, 2 - val))  # Cap at reasonable
    else:
        normalized_metrics[key] = min(1, val / 50)  # Rough scaling

# Final weighted aggregation
aggregate_performance = lambda mets, wts: sum(mets[k] * wts[k] for k in wts)

# Critical execution point
final_score = aggregate_performance(normalized_metrics, weights)

# Print result as required
print(f"Result: {final_score}")