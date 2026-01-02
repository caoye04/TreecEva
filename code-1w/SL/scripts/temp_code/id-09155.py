import itertools

# Simulate agricultural yield optimization with noise filtering and red herrings
def generate_growth_pattern(base, cycles):
    pattern = []
    for i in range(cycles):
        if i % 4 == 0:
            pattern.append(base * (1.1 ** i))
        elif i % 3 == 0:
            pattern.append(base * 0.95)  # Distractor: stress condition
        else:
            pattern.append(base + i * 0.05)
    return [round(p, 3) for p in pattern]


def filter_anomalies(data_stream):
    # Heavy distraction: complex filtering that isn't fully used
    filtered = []
    moving_avg = 0
    threshold = 2.0
    for val in data_stream:
        if abs(val - moving_avg) < threshold or val > 15:  # Loosely applied
            filtered.append(val * 1.05)
        else:
            filtered.append(moving_avg)
        moving_avg = sum(filtered) / len(filtered) if filtered else val
    return filtered


def compute_root_mean_square(seq):
    # Unused but plausible function (dead code path)
    return (sum(x**2 for x in seq) / len(seq)) ** 0.5 if seq else 0


def evaluate_stress_resilience(matrix):
    # Misleading intermediate metric
    resilience_score = 0
    for row in matrix:
        for val in row:
            if val < 8:
                resilience_score -= 0.5
            else:
                resilience_score += 0.3
    return round(resilience_score, 2)


def calculate_harvest_efficiency(grid, iterations):
    # Core logic buried in distractions
    time_series = generate_growth_pattern(7.2, iterations)
    processed = filter_anomalies(time_series)
    
    # Real computation begins here — well-hidden
    cumulative_gain = 0
    adjustment_factor = 0.88
    
    # Key transformation using itertools
    paired_shifts = list(itertools.pairwise(processed))  # Important: captures trend deltas
    
    for a, b in paired_shifts:
        delta = b - a
        if delta > 0:
            cumulative_gain += delta * adjustment_factor
    
    # Secondary correction based on grid shape
    rows, cols = len(grid), len(grid[0]) if grid else (0, 0)
    shape_bonus = (rows * cols) * 0.15 if rows > 0 else 0
    
    efficiency = cumulative_gain + shape_bonus
    
    # Red herring: irrelevant conditional with no effect
    if efficiency > 50:
        temp_debug_log = [efficiency / 2 for _ in range(5)]
        temp_debug_log.reverse()
    
    return round(efficiency, 4)

# Irrelevant setup variables (distractors)
crop_type = 'Triticum aestivum'
growth_rate_table = {f'cycle_{i}': 7.2 * (1.03 ** i) for i in range(12)}
baseline_readings = [6.8, 7.1, 7.0, 7.3, 7.5, 7.4, 7.2, 7.0]  # Unused sensor baseline

# Decoy data structure
stress_markers = {
    'heat': [0.1, 0.3, 0.4],
    'drought': [0.2, 0.2],
    'nutrient_deficit': []
}

# Main data — only shape matters, not content
cluster_matrix = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]

growth_cycles = 12

# Spurious intermediate call (no side effects)
stress_test_result = evaluate_stress_resilience(cluster_matrix)

# Actual target computation
final_yield = calculate_harvest_efficiency(cluster_matrix, growth_cycles)

print(f"Result: {final_yield}")