def analyze_growth_pattern(heights):
    if not heights:
        return 0
    avg = sum(heights) / len(heights)
    variance = sum((h - avg) ** 2 for h in heights) / len(heights)
    return variance < 5

# Irrelevant growth simulation (distraction)
growth_cycles = [3, 7, 2, 8, 1]
processed_data = []
for cycle in growth_cycles:
    temp_result = (cycle ** 2 + 4) // 3
    processed_data.append(temp_result % 5)

# Unused function - red herring
def predict_rainfall(month):
    base = (month * 3.14) % 7
    adjustment = (base ** 3) / 10
    return int(adjustment) if adjustment > 2 else 0

# Core logic disguised among distractions
soil_nutrients = [12, 15, 14, 10, 13]
pest_load = [1, 0, 2, 1, 0]

# Distractor: unused nutrient transformation
transformed = [max(0, n - p * 3) for n, p in zip(soil_nutrients, pest_load)]
calibrated = list(map(lambda x: x + 2 if x < 12 else x - 1, transformed))

# Key data structure with meaningful and irrelevant fields
plant_data = {
    'readings': [
        {'height': 24, 'leaves': 6, 'age': 4},
        {'height': 28, 'leaves': 7, 'age': 5},
        {'height': 26, 'leaves': 6, 'age': 5},
        {'height': 30, 'leaves': 8, 'age': 6}
    ],
    'metadata': {
        'plot_id': 'X7G',
        'season': 'summer',
        'baseline_yield': 42
    }
}

# Simulate sensor noise filtering (partial distraction)
filtered_heights = []
for reading in plant_data['readings']:
    h = reading['height']
    if h >= 25 or reading['age'] >= 6:
        filtered_heights.append(h)

# Conditional expression used meaningfully
base_score = sum(r['leaves'] for r in plant_data['readings'])
bonus_applied = True if base_score >= 25 else False
adjusted_score = base_score * 1.2 if bonus_applied else base_score * 0.9

# Complex multi-step calculation chain
normalization_factor = 100 / (sum(soil_nutrients) / len(soil_nutrients))
effective_health = adjusted_score * normalization_factor

# Recursive helper function for yield prediction (core concept)
def calculate_harvest_efficiency(levels, depth=0):
    if depth >= 3 or not levels:
        return 1.0
    
    mid = len(levels) // 2
    left = levels[:mid] if mid > 0 else []
    right = levels[mid+1:]
    
    current_val = levels[mid] if mid < len(levels) else 0
    
    # Conditional recursion with arithmetic
    left_contrib = calculate_harvest_efficiency(left, depth + 1) * 0.7
    right_contrib = calculate_harvest_efficiency(right, depth + 1) * 0.7
    
    return current_val + left_contrib + right_contrib

# Derive input for recursive function from earlier computations
input_levels = [int(effective_health / 10), 5, int(avg_score * 0.5) if 'avg_score' in locals() else 3]
avg_score = sum(r['leaves'] for r in plant_data['readings']) / len(plant_data['readings'])
input_levels[-1] = int(avg_score * 0.5)  # Fix missing dependency

# Final computation - target intervention point
final_yield = calculate_harvest_efficiency(input_levels)

# Additional distractor: unused advanced analysis
def compute_fractal_index(data):
    if len(data) < 2:
        return 0
    diffs = [abs(data[i] - data[i-1]) for i in range(1, len(data))]
    return sum(d * (i+1) for i, d in enumerate(diffs))

fractal_debug = compute_fractal_index(processed_data)  # Dead end

# Print final result as required
Result: {final_yield}