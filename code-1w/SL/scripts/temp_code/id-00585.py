def analyze_system_load(workloads, efficiency_ratio):
    base_load = sum(workloads)
    adjusted_load = base_load * efficiency_ratio
    peak_load = max(workloads)
    normalized_peak = peak_load / adjusted_load if adjusted_load != 0 else 0
    
    # Irrelevant computation - distractor
    theoretical_capacity = len(workloads) * 100
    unused_buffer = theoretical_capacity - adjusted_load
    
    return adjusted_load

# Simulate stress distribution across components
def generate_stress_profile(n_components, age_factor):
    stress = []
    for i in range(n_components):
        raw_stress = (i + 1) ** 1.5
        decayed_stress = raw_stress * (0.9 ** age_factor)
        stress.append(int(decayed_stress))
    
    # Dead code path - misleading
    if len(stress) > 100:
        stress = stress[:50]
    
    return stress

# Calculate system equilibrium using combinatorics and decay factors
def calculate_equilibrium(stress_levels, resilience_factor):
    n = len(stress_levels)
    
    # Combinatorics: number of interacting component pairs
    interaction_count = n * (n - 1) // 2 if n > 1 else 0
    
    # Weighted stress using lambda transformation
    stress_transform = lambda s: s ** 0.5 if s > 0 else 0
    transformed_stress = [stress_transform(s) for s in stress_levels]
    total_transformed = sum(transformed_stress)
    
    # Intermediate irrelevant metric
    average_stress = total_transformed / n if n > 0 else 0
    volatility_index = max(transformed_stress) - min(transformed_stress) if n > 1 else 0
    
    # Core equilibrium formula
    raw_equilibrium = total_transformed * resilience_factor
    damping_factor = 0.85
    
    # Final score with damping
    equilibrium_score = raw_equilibrium * damping_factor
    
    # Unused derived metrics - distraction
    potential_overload = raw_equilibrium > 200
    safety_margin = 1.0 - (raw_equilibrium / 300) if raw_equilibrium < 300 else 0.1
    
    return equilibrium_score

# Main execution
workloads = [12, 15, 18, 22, 27, 33, 40]
efficiency_ratio = 0.93
resilience_factor = 1.2

# Distractor function call
current_load = analyze_system_load(workloads, efficiency_ratio)

# Generate stress levels
stress_levels = generate_stress_profile(len(workloads), age_factor=3)

# Key statement
equilibrium_score = calculate_equilibrium(stress_levels, resilience_factor)

print(f"Result: {equilibrium_score}")