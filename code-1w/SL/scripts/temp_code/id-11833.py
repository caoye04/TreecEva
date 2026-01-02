from itertools import cycle, islice

def simulate_growth(base_rate, inhibitors, promoters):
    # Simulate plant growth with environmental factors (relevant)
    adjusted_rate = base_rate
    for inhibitor in inhibitors:
        adjusted_rate *= (1 - inhibitor)
    for promoter in promoters:
        adjusted_rate *= (1 + promoter)
    return adjusted_rate

def calculate_respiration_loss(age, mass):
    # Irrelevant function - not used in final computation path
    return age * mass * 0.02

def assess_stress_factors(environmental_data):
    # Dead code path - never called
    stress_index = 0
    for reading in environmental_data:
        if reading > 70:
            stress_index += 1
    return stress_index

def filter_noisy_sensors(sensor_readings):
    # Distractor: processes data but ultimately unused
    filtered = [r for r in sensor_readings if 10 <= r <= 90]
    outlier_count = len(sensor_readings) - len(filtered)
    scaling_factor = 1.05 if outlier_count < 3 else 0.95  # Misleading intermediate
    return filtered

def compile_growth_phases(phases, efficiency_map):
    # Relevant transformation using zip and dictionary lookup
    total = 0
    for phase, (start, end) in enumerate(phases):
        duration = end - start
        key = f'phase_{phase+1}'
        if key in efficiency_map:
            total += duration * efficiency_map[key] * (1.1 if duration > 5 else 1.0)
    return total

def harvest_results(cycles):
    # Core logic - computes final yield based on processed cycles
    cumulative = 0
    growth_cycle_pattern = cycle([2, 3, 1])
    
    # Real data processing with distractors embedded
    for i, cycle_data in enumerate(cycles):
        phase_duration = cycle_data['duration']
        base_efficiency = cycle_data['efficiency']
        
        # Red herring variables
        theoretical_max = phase_duration * 2.5  # Unused
        decay_correction = 0.98 ** i  # Computed but irrelevant
        
        # Key calculation mixed with noise
        temp_modifier = 1.0
        if i % 2 == 0:
            temp_modifier += 0.05
            
        # Actual contribution to result
        raw_output = phase_duration * base_efficiency * temp_modifier
        
        # Only every third cycle gets bonus due to nutrient reset
        nutrient_boost = next(growth_cycle_pattern)
        if (i + 1) % 3 == 0:
            raw_output *= nutrient_boost
            
        cumulative += raw_output
    
    return int(cumulative)

# Main execution block
if __name__ == '__main__':
    # Experimental setup parameters (some irrelevant)
    baseline_temperature = 22.5
    humidity_levels = [45, 50, 60, 70, 80]  # Unused
    co2_readings = [380, 400, 420, 410]     # Unused
    
    # Sensor data with noise filtering (distractor chain)
    raw_sensors = [15, 95, 25, 88, 5, 70, 92]
    clean_data = filter_noisy_sensors(raw_sensors)
    
    # Efficiency map for growth phases (relevant)
    efficiency_lookup = {
        'phase_1': 0.85,
        'phase_2': 0.92,
        'phase_3': 0.78,
        'phase_4': 0.88
    }
    
    # Growth phases definition (relevant)
    stages = [(0, 4), (4, 9), (9, 12), (12, 16)]
    total_phase_score = compile_growth_phases(stages, efficiency_lookup)
    
    # Production cycles - actual input data
    production_cycles = [
        {'duration': 4, 'efficiency': 2.1},
        {'duration': 5, 'efficiency': 1.8},
        {'duration': 6, 'efficiency': 2.3},
        {'duration': 3, 'efficiency': 1.9},
        {'duration': 7, 'efficiency': 2.0}
    ]
    
    # Control variables with misleading names
    preliminary_estimate = total_phase_score * 10  # Looks important, unused
    adjustment_buffer = []  # Dead storage
    
    # Critical statement
    final_yield = harvest_results(production_cycles)
    
    # Simulated side calculation (red herring)
    respiration_total = 0
    for day in range(1, 11):
        respiration_total += calculate_respiration_loss(day, 1.5)
    
    # Output result
    print(f"Result: {final_yield}")