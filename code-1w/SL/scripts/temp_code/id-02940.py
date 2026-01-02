def analyze_component(x, threshold=5):
    if x < threshold:
        return x * 1.8 + 2
    else:
        return x * 0.9 - 1

# Simulate system benchmark data with multiple metrics
temperature_readings = [2, 8, 5, 12, 3]
load_factors = [4, 7, 6, 10, 1]
efficiency_modes = ['eco', 'high', 'normal', 'eco', 'high']

# Initialize tracking variables
aggregate = 0
interim_results = []
diagnostic_flags = {mode: 0 for mode in efficiency_modes}

# Misleading intermediate calculation (distractor)
temp_sum = sum(t ** 2 for t in temperature_readings if t % 2 == 1)
baseline_offset = temp_sum // 3 if temp_sum > 10 else 0

# Real processing begins
for i in range(len(load_factors)):
    raw_value = load_factors[i]
    adjusted = analyze_component(raw_value)

    # Dictionary-based mode multiplier (relevant logic)
    mode_multiplier = {'eco': 1.2, 'normal': 1.0, 'high': 0.85}
    if efficiency_modes[i] in mode_multiplier:
        adjusted *= mode_multiplier[efficiency_modes[i]]

    # Accumulate only even-indexed results (key dependency)
    if i % 2 == 0:
        aggregate += adjusted

    # Track mode occurrences (semi-relevant, distracts from core)
    diagnostic_flags[efficiency_modes[i]] += 1

    # Store intermediate (partially used)
    interim_results.append(round(adjusted, 2))

# Secondary processing on intermediates (red herring)
flag_sum = sum(diagnostic_flags.values())
normalized_flags = {k: v / flag_sum for k, v in diagnostic_flags.items()}

# Core accumulation using dictionary lookup and filtering
category_map = {0: 'A', 1: 'B', 2: 'A', 3: 'C', 4: 'B'}
category_totals = {'A': 0, 'B': 0, 'C': 0}

for idx, val in enumerate(interim_results):
    cat = category_map[idx]
    if cat == 'C':
        category_totals[cat] += val * 0.5
    else:
        category_totals[cat] += val * 0.7

# Final performance score computation (target)
def calculate_performance(data):
    base = aggregate  # Depends on filtered index logic
    penalty = category_totals['C'] * 1.1
    bonus = len([x for x in temperature_readings if x < 5]) * 0.5
    return int(base - penalty + bonus)

final_score = calculate_performance(benchmark_data=None)
print(f"Result: {final_score}")