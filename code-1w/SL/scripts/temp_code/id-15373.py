import itertools

# Simulate crop yield optimization under varying environmental constraints
def generate_environmental_factors():
    base_temp = [22, 25, 27, 30]
    rainfall = [80, 100, 120]
    soil_quality = [0.8, 0.9, 1.0]
    
    # Generate combinations but only use a subset for actual calculation
    all_conditions = list(itertools.product(base_temp, rainfall, soil_quality))
    filtered_conditions = [cond for cond in all_conditions if cond[0] >= 25 and cond[2] > 0.85]
    
    # Distractor: unused transformation
    transformed = [(t, r * 0.1, s ** 2) for t, r, s in all_conditions[:10]]
    
    return filtered_conditions

# Helper to compute growth index (not all paths are used)
def compute_growth_index(temp, rain, soil):
    base_index = temp * 0.3 + rain * 0.05
    if soil > 0.9:
        base_index *= 1.25
    elif soil < 0.85:
        base_index *= 0.75
    return round(base_index, 2)

# Unused recursive variant (dead code path - distractor)
def recursive_growth_factor(n):
    if n <= 1:
        return 1
    return recursive_growth_factor(n - 1) * 1.05

# Main strategy evaluator
def evaluate_strategy(level, duration, risk_factor):
    if level == 'high':
        return (duration * 1.5) / (risk_factor + 1)
    elif level == 'medium':
        return duration * 1.1
    else:
        return duration / 1.5

# Core function that determines final result
def calculate_optimal_harvest(strategies):
    accumulated_yields = []
    
    for strategy in strategies:
        temp, rain, soil = strategy
        growth = compute_growth_index(temp, rain, soil)
        
        # Simulated strategy weights (some are irrelevant)
        mock_weight = (temp % 5) * 0.1
        adjusted_growth = growth * (1 + mock_weight)
        
        # Actual contributing logic
        if rain > 90:
            adjusted_growth += 3.5
        if temp in [27, 30]:
            adjusted_growth *= 1.1
        
        accumulated_yields.append(adjusted_growth)
    
    # Real computation path
    raw_total = sum(accumulated_yields)
    penalty = len([y for y in accumulated_yields if y < 10]) * 1.2
    bonus = len([y for y in accumulated_yields if y > 15]) * 2.3
    
    # Distractor variables
    avg_yield = raw_total / len(accumulated_yields) if accumulated_yields else 0
    hypothetical_max = max(accumulated_yields) * len(accumulated_yields)
    efficiency_ratio = hypothetical_max / (raw_total + 1)  # Avoid zero div
    
    return int(raw_total - penalty + bonus)  # Final deterministic integer result

# Setup and execution
if __name__ == '__main__':
    # Generate environmental data
    env_data = generate_environmental_factors()
    
    # Define strategy matrix using permutations (some redundant)
    risk_levels = ['high', 'medium', 'low']
    durations = [60, 90]
    strategy_keys = list(itertools.product(risk_levels, durations))
    
    # Unused mapping (distractor)
    key_mapping = {k: idx for idx, k in enumerate(strategy_keys)}

    # Construct actual input matrix based on environment only
    strategy_matrix = []
    for temp, rain, soil in env_data:
        # Some derived values, only temp, rain, soil matter
        complexity_distractor = (temp + rain) % 7
        normalized_value = soil * 100
        strategy_matrix.append((temp, rain, soil))  # Only this tuple is used

    # Execute main logic
    intermediate_flag = len(env_data) > 5
    baseline_shift = 0.5 if intermediate_flag else 0.2

    # Critical execution point
    final_yield = calculate_optimal_harvest(strategy_matrix)
    
    # Print result as required
    print(f"Result: {final_yield}")