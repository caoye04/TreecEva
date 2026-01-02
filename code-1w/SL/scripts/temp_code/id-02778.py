from collections import defaultdict, Counter
import itertools

# Simulated sensor array data from environmental monitoring system
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.0, 23.7]
humidity_readings = [45, 47, 50, 44, 60, 55, 48, 52]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1014, 1016, 1011]

# Irrelevant auxiliary data (distractor)
sound_levels = [32, 34, 33, 36, 38, 35, 30, 31]
lux_readings = [400, 420, 380, 500, 600, 550, 480, 410]

# Data aggregation with red herring transformations
raw_stats = defaultdict(float)
for i, temp in enumerate(temperature_readings):
    raw_stats[f'temp_bin_{i//2}'] += temp / len(temperature_readings)

# Misleading normalization path (dead code path)
normalized_humidity = []
scaling_factor = 1.0
if len(humidity_readings) > 10:
    scaling_factor = 0.9
else:
    for val in humidity_readings:
        normalized_humidity.append(val * 1.05 if val < 50 else val * 0.98)  # Unused result

# Real processing begins: detect thermal anomalies
anomalies = []
for i in range(1, len(temperature_readings)):
    if abs(temperature_readings[i] - temperature_readings[i-1]) > 1.0:
        anomalies.append(i)

# Construct state transitions (relevant)
state_transitions = []
prev_high = False
for h in humidity_readings:
    current_high = h > 50
    if current_high and not prev_high:
        state_transitions.append('dry_to_wet')
    elif not current_high and prev_high:
        state_transitions.append('wet_to_dry')
    prev_high = current_high

# Decoy statistical analysis using irrelevant combinations
combinatorial_noise = []
for t, h, p in itertools.product([23, 24], [45, 46], [1010]):
    combinatorial_noise.append((t + h) * p % 7)  # No impact on final result

# Core logic: optimize detection path based on anomaly positions
optimized_path = []
cumulative_offset = 0
for idx in anomalies:
    adjusted = (idx + cumulative_offset) % 8
    optimized_path.append(adjusted)
    cumulative_offset += idx % 3

# Diagnostic flags from pressure instability
pressure_changes = [abs(pressure_readings[i] - pressure_readings[i-1]) for i in range(1, len(pressure_readings))]
diagnostic_flags = [1 if delta >= 3 else 0 for delta in pressure_changes]
flag_summary = Counter(diagnostic_flags)

# Secondary decoy structure (unused tree-like accumulator)
accumulator_tree = [[0]*3 for _ in range(3)]
for x in range(3):
    for y in range(3):
        if x == y:
            accumulator_tree[x][y] = x * y + 2
        else:
            accumulator_tree[x][y] = (x + y) * 3  # Dead computation

# Conditional expression mix (relevant)
base_score = sum(1 for x in pressure_changes if x > 2)
penalty = 5 if len(anomalies) > 3 else 2 if len(anomalies) == 0 else 3
effective_score = base_score - penalty if base_score > penalty else 0

# Final diagnostic computation (key statement)
diagnostics = {
    'transitions': len(state_transitions),
    'instability_periods': sum(diagnostic_flags),
    'effective_score': effective_score,
    'path_weight': sum(optimized_path)
}

final_diagnostic = process_metrics(optimized_path, diagnostics)

# Mock function to resolve final value
def process_metrics(path, metrics):
    base = metrics['instability_periods'] * 100
    adjustment = metrics['path_weight'] * 10
    if metrics['transitions'] > 1:
        adjustment += 50
    if metrics['effective_score'] >= 2:
        base += 200
    return base + adjustment - (path[0] * 5 if len(path) > 0 else 0)

# Print result
Result: {final_diagnostic}