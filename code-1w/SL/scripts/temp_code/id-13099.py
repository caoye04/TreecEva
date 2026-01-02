from itertools import combinations

# Simulate agricultural land plots with varying soil quality, moisture, and size
land_plots = [
    {'size': 12, 'soil_quality': 0.8, 'moisture': 0.6, 'slope': 0.03},
    {'size': 8,  'soil_quality': 0.9, 'moisture': 0.7, 'slope': 0.08},
    {'size': 15, 'soil_quality': 0.6, 'moisture': 0.5, 'slope': 0.02},
    {'size': 10, 'soil_quality': 0.7, 'moisture': 0.8, 'slope': 0.12},
    {'size': 5,  'soil_quality': 0.5, 'moisture': 0.4, 'slope': 0.05}
]

# Irrelevant helper: calculates perimeter (not used in yield)
def calculate_perimeter(size):
    return 4 * (size ** 0.5)

# Distraction: unused productivity table based on slope categories
slope_productivity = {
    'low': 1.0,
    'medium': 0.7,
    'high': 0.3
}

# Heuristic weight function for filtering non-ideal plots
is_suitable = lambda plot: plot['slope'] < 0.1 and plot['moisture'] > 0.45

# Filter suitable plots (used in final calculation)
suitable_plots = [p for p in land_plots if is_suitable(p)]

# Compute base yields per plot (will be adjusted later)
base_yields = []
for plot in suitable_plots:
    raw_yield = plot['size'] * plot['soil_quality'] * (plot['moisture'] + 0.2)
    # Artificial dampening factor for no clear reason (distractor)
    if plot['size'] > 9:
        raw_yield *= 0.95
    base_yields.append(raw_yield)

# Additional distraction: unused combo analysis of all possible pairs
all_combinations = list(combinations(land_plots, 2))
pair_analysis = []
for pair in all_combinations:
    total_area = pair[0]['size'] + pair[1]['size']
    avg_moisture = (pair[0]['moisture'] + pair[1]['moisture']) / 2
    # This computation has no downstream use
    score = total_area * (avg_moisture ** 1.1)
    pair_analysis.append(score)  # Dead storage

# Real logic begins: find optimal subset of up to 3 plots maximizing adjusted yield
def calculate_adjusted_yield(subset):
    total_size = sum(p['size'] for p in subset)
    weighted_soil = sum(p['size'] * p['soil_quality'] for p in subset) / total_size
    avg_moisture = sum(p['moisture'] for p in subset) / len(subset)
    # Apply diminishing returns beyond certain size
    efficiency_factor = min(1.0, 1.1 - (total_size * 0.005))
    return total_size * weighted_soil * avg_moisture * efficiency_factor

# Generate all valid subsets of 1 to 3 plots
candidate_subsets = []
for k in range(1, 4):
    candidate_subsets.extend(combinations(suitable_plots, k))

# Evaluate each candidate
subset_scores = [(subset, calculate_adjusted_yield(subset)) for subset in candidate_subsets]

# Find best configuration
best_subset, max_score = max(subset_scores, key=lambda x: x[1])

# Final aggregation step with red herring variables
average_plot_size = sum(p['size'] for p in best_subset) / len(best_subset)
penalty_factor = 1.0
if any(p['slope'] > 0.07 for p in best_subset):
    penalty_factor = 0.92  # Not triggered due to prior filtering

# Critical assignment point
final_yield = round(max_score * penalty_factor, 4)

# Print result as required
print(f"Result: {final_yield}")