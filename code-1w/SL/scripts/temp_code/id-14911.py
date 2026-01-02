from collections import defaultdict, Counter

# Simulate industrial thermal process stages with efficiency tracking
def simulate_process_efficiency(stages):
    efficiency_log = defaultdict(float)
    temp_accumulator = 0
    volatility_index = 0.0
    correction_factor = 1.0

    for i, stage in enumerate(stages):
        phase_weight = stage['input_mass'] * stage['duration']
        energy_input = stage['temperature'] * phase_weight
        if stage['catalyst_used']:
            energy_input *= 1.15  # Catalyst boosts efficiency

        # Record intermediate efficiency (distractor: not used in final result)
        efficiency_log[f'stage_{i}'] = energy_input / (phase_weight + 1)

        temp_accumulator += energy_input

        # Volatility calculation (dead-end computation)
        if energy_input > 5000:
            volatility_index += 0.3
            adjustment = energy_input * 0.02
            temp_accumulator -= adjustment  # Compensate

    return temp_accumulator

# Secondary function to mislead with similar logic
def analyze_stage_volatility(stages):
    volatile_count = 0
    for stage in stages:
        stress_metric = stage['temperature'] * stage['pressure']
        if stress_metric > 25000:
            volatile_count += 1
    return volatile_count  # Not used in main path

# Main calculation with relevant logic buried
process_stages = [
    {'input_mass': 12, 'temperature': 420, 'duration': 8, 'pressure': 3200, 'catalyst_used': True},
    {'input_mass': 15, 'temperature': 380, 'duration': 6, 'pressure': 2800, 'catalyst_used': False},
    {'input_mass': 10, 'temperature': 450, 'duration': 10, 'pressure': 3500, 'catalyst_used': True},
    {'input_mass': 8, 'temperature': 500, 'duration': 5, 'pressure': 4000, 'catalyst_used': True}
]

# Spurious data analysis (distractor)
stress_profile = Counter()
for stage in process_stages:
    key = 'high' if stage['pressure'] > 3000 else 'low'
    stress_profile[key] += 1

baseline_energy = 0
for stage in process_stages:
    baseline_energy += stage['input_mass'] * stage['temperature']
baseline_energy *= 0.85  # hypothetical loss factor (unused)

# Core algorithm hidden among distractions
def calculate_thermal_output(stages):
    total_output = 0.0
    stage_contributions = []

    for idx, stage in enumerate(stages):
        raw_contribution = stage['input_mass'] * stage['duration'] * stage['temperature']
        
        # Conditional boost (relevant)
        if stage['catalyst_used']:
            raw_contribution *= 1.2
        
        # Destructuring assignment (tuple unpacking)
        mass, temp = stage['input_mass'], stage['temperature']
        heat_factor = mass * temp
        
        # Early termination check (not triggered but adds complexity)
        if heat_factor > 5000 and idx == 5:  # Impossible index
            return -1
            
        stage_contributions.append(raw_contribution)
    
    total_output = sum(stage_contributions)
    
    # Final scaling based on process stability (fixed condition)
    if len(stages) >= 3:
        total_output *= 0.95
    
    return total_output

# Execute main logic
system_diagnostics = {'status': 'nominal', 'version': '2.1.5'}

# Critical execution point
thermal_capacity = calculate_thermal_output(process_stages)

# Print required result
print(f"Result: {thermal_capacity}")