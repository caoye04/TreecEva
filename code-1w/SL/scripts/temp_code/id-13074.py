import math

def analyze_phase_shift(frequencies, damping_ratio):
    # Irrelevant function - dead code path
    return [f * damping_ratio for f in frequencies]

def compute_heat_dissipation(thermal_inputs):
    # Another decoy function with misleading intermediate results
    base_loss = sum(thermal_inputs) * 0.07
    adjusted_loss = base_loss
    for i in range(len(thermal_inputs)):
        if thermal_inputs[i] > 50:
            adjusted_loss += thermal_inputs[i] * 0.02
    return round(adjusted_loss, 2)

def process_sensor_array(raw_readings):
    # Distractor: processes unrelated sensor data
    normalized = []
    for idx, val in enumerate(raw_readings):
        if idx % 2 == 0:
            normalized.append(val * 1.05)
        else:
            normalized.append(val * 0.98)
    return normalized

def calculate_strain_response(stress_sequence, material_params):
    modulus, poisson, yield_threshold, creep_factor = material_params
    cumulative_creep = 0.0
    transient_buffer = []
    
    # Real logic begins here
    for index, stress in enumerate(stress_sequence):
        elastic_strain = stress / modulus
        plastic_contribution = 0.0
        
        if stress > yield_threshold:
            excess_stress = stress - yield_threshold
            plastic_contribution = excess_stress * 0.003
            
            # Nested conditional red herring
            if index % 3 == 0:
                dummy_adj = excess_stress * 0.0001
                plastic_contribution -= dummy_adj  # Cancelled out later

        total_strain = elastic_strain + plastic_contribution
        
        # Creep accumulation over time (key computation)
        time_weight = (index + 1) * 0.5
        cumulative_creep += total_strain * creep_factor * time_weight
        
        transient_buffer.append(total_strain)
    
    # Final transformation using zip and enumerate (required python features)
    decay_correction = 0.0
    for i, (buf_val, orig_stress) in enumerate(zip(transient_buffer, stress_sequence)):
        if i > 0 and orig_stress < transient_buffer[i-1] * modulus:
            decay_correction += buf_val * 0.02 * math.sin(i)
    
    final_yield = cumulative_creep - decay_correction
    
    # Irrelevant post-processing
    smoothed_output = [x * 0.99 for x in transient_buffer]
    peak_value = max(smoothed_output) if smoothed_output else 0
    
    return final_yield

# Main execution block
if __name__ == "__main__":
    # Input setup
    stress_profile = [120, 180, 200, 220, 190, 160, 230, 250]
    material_consts = (150.0, 0.33, 175, 0.012)  # E, ν, σ_y, κ
    
    # Dead computations - red herrings
    thermal_loads = [35, 40, 45, 55, 65, 70]
    heat_loss = compute_heat_dissipation(thermal_loads)
    
    phase_frequencies = [50, 60, 75, 85]
    shift_analysis = analyze_phase_shift(phase_frequencies, 0.15)
    
    raw_sensors = [1024, 2048, 1536, 3072, 1792]
    calibrated = process_sensor_array(raw_sensors)
    
    # Critical statement
    final_yield = calculate_strain_response(stress_profile, material_consts)
    
    print(f"Result: {final_yield}")