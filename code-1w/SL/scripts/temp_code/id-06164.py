from itertools import combinations
from functools import reduce

# Simulate crop yield optimization under varying growth conditions
def generate_growth_phases(base_rate, stress_factors):
    phase_modifiers = [1.0, 0.85, 1.15, 0.95]
    raw_phases = [base_rate * mod for mod in phase_modifiers]
    
    # Irrelevant transformation (distractor)
    inverted_phases = [round(1 / (p + 0.1), 3) for p in raw_phases]
    normalized = [p / sum(raw_phases) for p in raw_phases]
    
    return [p * (1 - stress_factors.get(i, 0)) for i, p in enumerate(raw_phases)]

# Misleading helper function (partially dead code)
def analyze_soil_composition(elements):
    element_pairs = list(combinations(elements, 2))
    reactivity_scores = {pair: abs(pair[0] - pair[1]) for pair in element_pairs}
    avg_reactivity = sum(reactivity_scores.values()) / len(reactivity_scores)
    
    # This is never used in final computation
    stability_index = 1 / (avg_reactivity + 1e-5)
    return stability_index

# Core calculation with distractors
def calculate_optimal_yield(pattern, rates):
    # Destructuring assignment (relevant)
    primary, secondary, tertiary = pattern
    
    # Initialize multiple variables, some irrelevant
    cumulative_factor = 1.0
    decay_accumulator = 0.0  # Unused in result
    temp_results = []
    
    # Lambda function to mask actual logic
    apply_boost = lambda x, b: x * (1 + b) if b > 0 else x * 0.95
    
    # Nested loop with partial relevance
    for i, rate in enumerate(rates):
        growth_cycle = generate_growth_phases(rate, {1: 0.15, 3: 0.1})
        
        # Only first and third phases are used
        effective_growth = sum([growth_cycle[0], growth_cycle[2]])
        
        # Complex but semi-irrelevant intermediate
        rolling_metrics = [
            effective_growth * primary,
            effective_growth * secondary * 0.7,
            apply_boost(effective_growth, tertiary if i % 2 == 0 else 0)
        ]
        
        # Only first element matters
        temp_results.append(rolling_metrics[0])
        
        # Dead-end computation (distractor)
        decay_accumulator += pow(effective_growth, 0.1) * 0.05
    
    # Actual answer derivation (obscured by noise)
    base_yield = reduce(lambda a, b: a + b, temp_results)
    adjustment = len(temp_results) * tertiary * 100
    final_yield = int(base_yield + adjustment)
    
    # Print required output
    print(f"Result: {final_yield}")
    return final_yield

# Setup inputs
field_pattern = (0.6, 0.3, 0.1)
growth_rates = [0.8, 1.2, 0.9, 1.1]
soil_elements = [12, 18, 7, 23]

# Call function
final_yield = calculate_optimal_yield(field_pattern, growth_rates)