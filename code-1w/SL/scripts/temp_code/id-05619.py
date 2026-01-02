import itertools

# System health monitoring simulation with diagnostic scoring
base_metrics = [0.85, 0.91, 0.76, 0.94, 0.88]
thresholds = {'critical': 0.7, 'warning': 0.85, 'optimal': 0.9}

# Irrelevant historical data (distractor)
historical_load = [0.67, 0.71, 0.78, 0.82, 0.79, 0.83, 0.81]
cached_results = {i: val ** 2 for i, val in enumerate(historical_load)}

# Simulated sensor drift compensation (unused path)
def apply_drift_correction(values, factor=1.02):
    return [v * factor for v in values]

corrected_metrics = apply_drift_correction(base_metrics, 0.99)  # Computed but not used

# Real-time anomaly detection
anomalies = []
for i, metric in enumerate(base_metrics):
    if metric < thresholds['warning']:
        anomalies.append(i)

# Diagnostic engine with multiple phases
phase_weights = {'initial': 0.3, 'deep': 0.5, 'final': 0.2}

# Phase 1: Initial assessment
initial_score = sum(1 for m in base_metrics if m >= thresholds['optimal'])

# Phase 2: Deep analysis with bit manipulation red herring
shift_register = 0b1010
mask = 0b1100
masked_value = shift_register & mask  # Distractor: bitwise op with no impact

# Actual deep analysis
outlier_count = len([m for m in base_metrics if m < thresholds['critical']])
deep_analysis_bonus = 0
if outlier_count == 0:
    deep_analysis_bonus = 15
else:
    temp_adjust = outlier_count << 2  # Bit shift distractor
    deep_analysis_bonus = 10

deep_score = len(base_metrics) - len(anomalies) + deep_analysis_bonus

# Phase 3: Final integration using itertools
sequence_pairs = list(itertools.combinations(base_metrics, 2))
stability_index = sum(1 for a, b in sequence_pairs if abs(a - b) < 0.1)

# Unused combinatorics (distractor)
permutation_count = len(list(itertools.permutations([len(anomalies), stability_index])))

final_weighted_score = (
    initial_score * phase_weights['initial'] + 
    deep_score * phase_weights['deep'] + 
    stability_index * phase_weights['final']
)

# Normalization and adjustment
baseline_reference = sum(base_metrics) / len(base_metrics)
adjustment_factor = 0.0
if baseline_reference > 0.85:
    adjustment_factor = 0.15
elif baseline_reference > 0.8:
    adjustment_factor = 0.1
else:
    adjustment_factor = 0.05

# Critical execution point
aggregate_score = final_weighted_score * 10
final_diagnostic = aggregate_score * (1 + adjustment_factor)

# Dead code path (distractor)
if False:
    debug_log = []
    for idx in range(100):
        debug_log.append(f"Debug step {idx}: value={idx**2 % 17}")

# Unused dictionary operations
summary_stats = {
    'count': len(base_metrics),
    'anomaly_rate': len(anomalies) / len(base_metrics),
    'max_metric': max(base_metrics),
    'min_metric': min(base_metrics),
    'temp_flag': masked_value > 0  # Red herring
}

# Print required result
print(f"Target result: {final_diagnostic}")