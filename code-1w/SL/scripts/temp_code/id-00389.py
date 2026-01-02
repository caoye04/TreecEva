def analyze_phase(signal_data, baseline):
    adjusted = [x - baseline for x in signal_data]
    filtered = list(filter(lambda y: y > 0.5, adjusted))
    return len(filtered) if filtered else 0

# Irrelevant diagnostic helper (dead function)
def validate_checksum(data):
    return sum(data) % 7 == 0

# Misleading preprocessing step
temp_cache = {}
for i in range(5):
    temp_cache[f'key_{i}'] = i ** 3 + 2 * i

# Real data inputs
diagnostics = [3.2, 4.1, 2.8, 5.6, 3.9, 4.4, 2.1]
thresholds = {'low': 2.5, 'high': 4.0}

# Simulate system state drift
state_vector = [0.1, -0.3, 0.2]
correction_factor = 1.1

# Distractor: unused normalization
normalized_diagnostics = [round((x - min(diagnostics)) / (max(diagnostics) - min(diagnostics)), 3) for x in diagnostics]

# Auxiliary computation with misleading intermediate result
aggregate_score = sum([int(x) for x in diagnostics if x > 3.0])
weight_map = {i: val ** 0.5 for i, val in enumerate(diagnostics)}

# Conditional expression with red herring branch
mode_flag = 'aggressive' if len(diagnostics) > 6 else 'conservative'
override = False
if mode_flag == 'aggressive':
    override = any([x < 2.0 for x in diagnostics])

# Actual processing chain
baseline_shift = thresholds['low'] - 0.3
primary_count = analyze_phase(diagnostics, baseline_shift)

# Secondary analysis with bit manipulation distraction
bit_flags = 0
for i, val in enumerate(diagnostics):
    if val > thresholds['high']:
        bit_flags |= (1 << i)  # Track high values via bit position

# Unused but plausible-looking validation
checksum_passed = (bit_flags & 0xFF) != 0  # Looks important, not used

# Core logic disguised among distractors
trigger_points = [i for i, x in enumerate(diagnostics) if thresholds['low'] < x < thresholds['high']]
effective_rate = len(trigger_points) * correction_factor

# Final decision logic with conditional expression
interim_result = effective_rate if not override else primary_count * 0.5

# Key statement
final_output = process_signals(diagnostics, thresholds)

# Supporting function defined after use (increases interference)
def process_signals(data, limits):
    low_bound = limits['low']
    high_bound = limits['high']
    above_high = sum(1 for x in data if x > high_bound)
    between = sum(1 for x in data if low_bound < x <= high_bound)
    score = above_high * 3 + between * 2
    adjustment = 1 if len(data) % 2 == 1 else -1
    return int(score + adjustment)

print(f"Result: {final_output}")