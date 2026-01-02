import itertools

# Simulate crop yield optimization under varying weather and soil conditions
def generate_baseline_scenarios():
    temperatures = [22, 25, 27, 30]
    rainfall = [80, 100, 120]
    return [(t, r) for t in temperatures for r in rainfall]

# Irrelevant helper: computes theoretical evaporation (not used in final logic)
def compute_evaporation(temperature, humidity=60):
    return round((temperature * 1.8 + 32) * (humidity / 100) * 0.6, 2)

# Distractor function: looks relevant but unused in critical path
def analyze_soil_composition(elements):
    ratios = {elem: val / sum(elements.values()) for elem, val in elements.items()}
    return {k: round(v, 3) for k, v in ratios.items()}

# Core logic: score a given strategy based on resilience and output
def evaluate_strategy_performance(strategies):
    scores = []
    for s in strategies:
        base_score = 0
        penalty = 0
        # Simulate response to environmental stressors
        for i, (temp, rain) in enumerate(generate_baseline_scenarios()):
            if temp > 26 and s['heat_tolerance'] < 3:
                penalty += s['sensitivity_factor'] * 1.5
            if rain < 90 and s['drought_resistance'] == 1:
                penalty += 2.0
            # Primary yield calculation
            yield_potential = (s['base_yield'] * (0.8 + (rain - 80) * 0.01) * 
                             (0.9 + (temp - 22) * 0.05))
            base_score += yield_potential
        adjusted_score = base_score - penalty
        scores.append((s['id'], adjusted_score))
    return scores

# Higher-order function using lambda for dynamic filtering
def create_resilience_filter(threshold):
    return lambda entry: entry[1] >= threshold

# Main optimization function with complex data flow
def calculate_optimal_harvest(config):
    # Unpack configuration matrix
    raw_strategies = []
    for row in config:
        for col in row:
            raw_strategies.append(col)
    
    # Evaluate all candidate strategies
    performance_log = evaluate_strategy_performance(raw_strategies)
    
    # Compute average performance for normalization (semi-relevant)
    total = sum(entry[1] for entry in performance_log)
    count = len(performance_log)
    avg_performance = total / count if count else 0
    
    # Use lambda filter to isolate high-performing strategies
    strong_performer_filter = create_resilience_filter(avg_performance)
    top_tier = list(filter(strong_performer_filter, performance_log))
    
    # Secondary ranking by ID (tie-breaker)
    top_tier.sort(key=lambda x: (-x[1], x[0]))
    
    # Extract best performer
    best_id, best_score = top_tier[0] if top_tier else (None, 0)
    
    # Auxiliary computation: geometric mean of all scores (distraction)
    non_zero_scores = [entry[1] for entry in performance_log if entry[1] > 0]
    geo_mean = 1
    for score in non_zero_scores:
        geo_mean *= score
    geo_mean = geo_mean ** (1 / len(non_zero_scores)) if non_zero_scores else 0
    
    # Final yield derived from best score adjusted by fixed efficiency factor
    efficiency_ratio = 0.87
    final_yield = round(best_score * efficiency_ratio, 4)
    
    # Dead code branch: never executed due to prior validation
    if False and not performance_log:
        fallback = sum(geo_mean for _ in range(2))
        final_yield = fallback
    
    return final_yield

# Simulated strategy matrix (3x3 grid of farming strategies)
strategy_matrix = [
    [
        {'id': 1, 'base_yield': 45, 'heat_tolerance': 2, 'drought_resistance': 2, 'sensitivity_factor': 1.2},
        {'id': 2, 'base_yield': 48, 'heat_tolerance': 3, 'drought_resistance': 3, 'sensitivity_factor': 0.9},
        {'id': 3, 'base_yield': 43, 'heat_tolerance': 1, 'drought_resistance': 2, 'sensitivity_factor': 1.4}
    ],
    [
        {'id': 4, 'base_yield': 50, 'heat_tolerance': 4, 'drought_resistance': 4, 'sensitivity_factor': 0.7},
        {'id': 5, 'base_yield': 47, 'heat_tolerance': 3, 'drought_resistance': 2, 'sensitivity_factor': 1.1},
        {'id': 6, 'base_yield': 49, 'heat_tolerance': 2, 'drought_resistance': 1, 'sensitivity_factor': 1.3}
    ],
    [
        {'id': 7, 'base_yield': 52, 'heat_tolerance': 5, 'drought_resistance': 5, 'sensitivity_factor': 0.6},
        {'id': 8, 'base_yield': 46, 'heat_tolerance': 3, 'drought_resistance': 4, 'sensitivity_factor': 0.8},
        {'id': 9, 'base_yield': 44, 'heat_tolerance': 2, 'drought_resistance': 3, 'sensitivity_factor': 1.0}
    ]
]

# Execute main computation
final_yield = calculate_optimal_harvest(strategy_matrix)
print(f"Target result: {final_yield}")