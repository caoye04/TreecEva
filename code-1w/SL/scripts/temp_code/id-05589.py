from collections import defaultdict, Counter
import math

# Irrelevant utility function (dead code path)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v]

# Misleading data structure with decoy values
decoys = {
    'outlier_1': 999,
    'outlier_2': -888,
    'placeholder': 0,
    'temp_metric': 42
}

# Simulated sensor readings (irrelevant to final result)
sensor_data = [1.2, 1.5, 1.1, 1.4, 1.3]
smoothed = list(map(lambda x: round(x + 0.05, 1), sensor_data))  # Distractor computation

# Core problem: system performance evaluation
base_weights = [0.2, 0.3, 0.5]
raw_metrics = [85, 76, 94]  # accuracy, precision, recall

# Irrelevant transformation
shifted_metrics = [m * 1.01 for m in raw_metrics]
buffer_dict = defaultdict(int)
for i, m in enumerate(shifted_metrics):
    buffer_dict[f'metric_{i}'] = m

# Real computation begins here — nested and obscured by noise
adjustment_factor = math.cos(math.pi / 3)  # 0.5

# Composite score with bit manipulation red herring
bit_noise = (0b1010 << 3) ^ 0b1100  # evaluates to 80, irrelevant
useless_shift = (len(base_weights) << 2) - 1  # 11, unused

# Key data structure mixed with decoys
metric_set = {
    'accuracy': raw_metrics[0],
    'precision': raw_metrics[1],
    'recall': raw_metrics[2],
    'version': 'v2.1',  # dummy metadata
    'active': True
}

# Decoy function that looks important but isn't called correctly
def calculate_f1(metrix):
    p = metrix['precision']
    r = metrix['recall']
    return 2 * p * r / (p + r) if (p + r) > 0 else 0

cached_results = []
for _ in range(2):
    cached_results.append({'status': 'skipped'})  # Red herring loop

# Real logic hidden among distractions
def evaluate_performance(metrics):
    acc = metrics['accuracy']
    prec = metrics['precision']
    rec = metrics['recall']

    # Weighted harmonic blend (not F1!)
    numerator = 1
    denominator = (base_weights[0]/(acc + 1e-6) + 
                  base_weights[1]/(prec + 1e-6) + 
                  base_weights[2]/(rec + 1e-6))
    weighted_harmonic = numerator / denominator
    
    # Apply adjustment from trigonometric distraction
    adjusted = weighted_harmonic * adjustment_factor
    
    # Bitwise XOR with irrelevant constant (but included anyway)
    magic_offset = bit_noise ^ 85  # 80 ^ 85 = 5
    
    # Final nonlinear scaling
    score = adjusted ** 1.1 + magic_offset
    
    # Dead conditional (never triggers due to data)
    if metrics.get('version') == 'v9.9':
        score *= 0.1
    
    return int(round(score))

# Unused alternative logic path (distractor)
if len(raw_metrics) == 4:
    fallback = sum(raw_metrics) / 4
else:
    fallback = None

# Critical execution point
final_score = evaluate_performance(metric_set)

# Print required output
print(f"Result: {final_score}")