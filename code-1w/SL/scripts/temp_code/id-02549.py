def analyze_signal(samples):
    filtered = [x for x in samples if abs(x) > 0.1]
    squared = [x * x for x in filtered]
    energy = sum(squared)
    avg = energy / len(squared) if squared else 0
    return avg

samples = [0.12, -0.05, 0.33, -0.21, 0.0, 0.55, -0.61, 0.08, 0.44]

# Irrelevant transformation chain (distractor)
signal_copy = [s * 1.5 for s in samples]
denoised = list(filter(lambda x: x != 0, signal_copy))
transformed = [abs(d) ** 0.5 for d in denoised]
entropy_approx = len(transformed) - sum(transformed)  # unused

# Real processing path begins
baseline = sum(samples) / len(samples)
deviations = [abs(s - baseline) for s in samples]
high_deviation_indices = {i for i, d in enumerate(deviations) if d > 0.2}

# Simulated sensor flags (red herring)
sensor_flags = {}
for idx in range(len(samples)):
    if idx % 3 == 0:
        sensor_flags[idx] = 'STABLE'
    elif idx % 3 == 1:
        sensor_flags[idx] = 'NOISY'
    else:
        sensor_flags[idx] = 'CALIBRATING'

# Unused flag analysis (dead code path)
flag_counts = {k: 0 for k in set(sensor_flags.values())}
for flag in sensor_flags.values():
    flag_counts[flag] += 1

# Data aggregation with tuples and sets
data_points = [(i, round(s, 2), deviations[i]) for i, s in enumerate(samples)]
valid_points = {(i, s) for i, s, d in data_points if d > 0.15}
outlier_set = {i for i, s, d in data_points if s > 0.5 or s < -0.5}

# Mock classification (irrelevant)
class_map = {}
for i, s, d in data_points:
    if d < 0.1:
        class_map[i] = 'LOW_VARIANCE'
    elif d < 0.3:
        class_map[i] = 'MODERATE'
    else:
        class_map[i] = 'HIGH_DRIFT'

# Threshold logic with conditional expressions
global_shift = baseline > 0.05
amplitude_flag = 'HIGH' if max(samples) - min(samples) > 0.7 else 'NORMAL'
size_category = 'LARGE' if len(valid_points) >= 5 else 'SMALL'

# Define threshold rules (used later)
thresholds = {
    'energy': 0.1,
    'complexity': 3,
    'stability': 'STABLE',
    'shift': global_shift
}

# Create composite diagnostic features
feature_vector = []
for i, s, d in data_points:
    contribution = s * d
    penalty = 0.1 if i in {1, 3, 7} else 0  # arbitrary index penalty
    adjusted = contribution - penalty
    feature_vector.append(adjusted)

# Compute complexity metric via bit manipulation (distraction)
raw_bits = int(sum(feature_vector) * 1000) & 0xFFFF
inverted = raw_bits ^ 0xAAAA
popcount = bin(inverted).count('1')
complexity_score = popcount + (inverted % 7)  # unused standalone

# Aggregate real metrics
total_energy = sum([s*s for s in samples])
effective_dimensions = len(high_deviation_indices)
consistency_metric = len(valid_points) / len(samples)

# Simulated multi-source data fusion
source_a = {'data': total_energy, 'weight': 0.6}
source_b = {'data': effective_dimensions * 0.8, 'weight': 0.4}
fused_estimate = source_a['data'] * source_a['weight'] + source_b['data'] * source_b['weight']

# Actual aggregation structure used
aggregate_data = (
    total_energy,
    consistency_metric,
    fused_estimate,
    complexity_score,  # included but not dominant
    len(outlier_set)
)

# Unused backup logic (dead function)
def fallback_analysis(data):
    return sum(data) % 5

# Core processing function
def process_metrics(data_tuple, config):
    energy, consistency, fused, comp, outliers = data_tuple
    
    # Conditional expression chain
    base_score = energy * 10 if energy > config['energy'] else energy * 5
    stability_bonus = 2 if config['stability'] == 'STABLE' else -1
    shift_penalty = -3 if config['shift'] else 0
    
    # Set-based filtering effect
    indirect_modifier = 1.0
    if outliers > 0:
        if consistency > 0.5:
            if comp > 5:
                indirect_modifier = 1.25
            else:
                indirect_modifier = 0.9
        else:
            indirect_modifier = 0.7
    
    # Final composition
    raw_diagnostic = base_score + fused * 0.3 + stability_bonus + shift_penalty
    final_normalized = raw_diagnostic * indirect_modifier
    
    # Secondary adjustment based on tuple unpacking result
    temp_vals = [energy, fused, comp]
    if all(v > 1 for v in temp_vals[:2]):
        final_normalized += 1.5
    
    return round(final_normalized, 4)

# Execute key statement
final_diagnostic = process_metrics(aggregate_data, thresholds)
print(f"Target result: {final_diagnostic}")