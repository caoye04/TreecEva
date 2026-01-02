from itertools import cycle

def preprocess_readings(sensor_data):
    filtered = []
    offset_correction = 0.05
    total_shift = 0
    
    for val in sensor_data:
        if val < 0:
            continue
        adjusted = val + offset_correction
        total_shift += offset_correction
        if adjusted > 100:
            break
        filtered.append(adjusted)
    
    # Irrelevant aggregation
    avg_filtered = sum(filtered) / len(filtered) if filtered else 0
    return filtered

def calculate_efficiency(phases):
    efficiency = 1.0
    decay_rate = 0.98
    for _ in phases:
        efficiency *= decay_rate
    return efficiency

def calculate_thermal_output(phases):
    base_output = 0
    thermal_losses = []
    phase_contributions = []
    
    for i, phase in enumerate(phases):
        if i % 2 == 0:
            base_output += phase['input_heat'] * 0.75
        else:
            base_output += phase['input_heat'] * 0.65
        
        loss = phase['input_heat'] * 0.25
        thermal_losses.append(loss)
        
    # Dummy tracking variables (distractors)
    cumulative_loss = sum(thermal_losses)
    average_loss = cumulative_loss / len(thermal_losses) if thermal_losses else 0
    
    # Real computation path
    scaling_factor = len(phases) / 4.0
    efficiency = calculate_efficiency(phases)
    final_output = base_output * efficiency * scaling_factor
    
    # Misleading intermediate that looks important but isn't used
    theoretical_max = sum(p['input_heat'] for p in phases) * 0.9
    safety_margin = theoretical_max * 0.1
    
    return final_output

def main():
    # Simulated industrial process phases
    process_phases = [
        {'input_heat': 40, 'duration': 120, 'mode': 'startup'},
        {'input_heat': 60, 'duration': 180, 'mode': 'steady'},
        {'input_heat': 55, 'duration': 150, 'mode': 'recovery'},
        {'input_heat': 70, 'duration': 200, 'mode': 'peak'}
    ]
    
    # Irrelevant preprocessing step (distractor)
    raw_sensor_input = [38.2, 41.1, -5, 60.3, 58.9, 105, 70.1]
    cleaned_readings = preprocess_readings(raw_sensor_input)
    
    # Core calculation with key intervention point
    thermal_capacity = 0
    temp_accumulator = 0
    for reading in cleaned_readings:
        temp_accumulator += reading * 0.1
    
    thermal_capacity = calculate_thermal_output(process_phases)
    
    # Additional noise
    diagnostics = {}
    diagnostics['stability_index'] = 0.95
    diagnostics['calibration_offset'] = 0.002
    
    # Print required result
    print(f"Result: {thermal_capacity}")

if __name__ == "__main__":
    main()