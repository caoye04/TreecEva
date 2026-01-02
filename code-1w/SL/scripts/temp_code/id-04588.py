def analyze_material_efficiency(data):
    efficiency_score = 0
    temp_history = []
    for i, entry in enumerate(data):
        if entry['temperature'] > 300:
            adjusted_flow = entry['flow_rate'] * 0.85
            efficiency_score += (entry['purity'] / adjusted_flow) if adjusted_flow else 0
        else:
            baseline_flow = entry['flow_rate'] * 1.1
            efficiency_score -= (baseline_flow / 100) if entry['purity'] < 90 else 0
        
        temp_history.append(entry['temperature'])
    
    # Distractor: unused intermediate calculation
    avg_temp = sum(temp_history) / len(temp_history) if temp_history else 0
    peak_moment = max(enumerate(temp_history), key=lambda x: x[1])
    
    return efficiency_score


def calculate_thermal_properties(dataset):
    thermal_capacity = 0.0
    phase_shifts = []
    cumulative_energy = 0
    
    for idx, record in enumerate(dataset):
        energy = record['temperature'] * record['density']
        cumulative_energy += energy
        
        if energy > 25000:
            phase_shifts.append((idx, energy))
            
        # Irrelevant transformation
        normalized_density = record['density'] / max(d['density'] for d in dataset)
        offset_correction = (idx + 1) * 0.01
        
    # Key computation step
    if cumulative_energy > 0:
        scaling_factor = 1.75
        thermal_capacity = cumulative_energy * scaling_factor / len(dataset)
    
    # Dead code branch - never reached due to prior logic
    if len(phase_shifts) == 100:
        thermal_capacity *= 0.9
    
    # Slicing distractor
    recent_phases = phase_shifts[-5:] if len(phase_shifts) > 5 else phase_shifts
    
    return thermal_capacity

# Main execution
material_data = [
    {'temperature': 298, 'density': 850, 'flow_rate': 120, 'purity': 92},
    {'temperature': 315, 'density': 860, 'flow_rate': 110, 'purity': 88},
    {'temperature': 305, 'density': 855, 'flow_rate': 115, 'purity': 95},
    {'temperature': 330, 'density': 870, 'flow_rate': 105, 'purity': 87},
    {'temperature': 310, 'density': 865, 'flow_rate': 100, 'purity': 93}
]

# Unused helper data
auxiliary_metrics = [
    {'sensor': 'A1', 'reading': 42.5},
    {'sensor': 'A2', 'reading': 39.1}
]

# Red herring function call (no side effects)
analyze_material_efficiency(material_data)

# Critical statement
thermal_capacity = calculate_thermal_properties(material_data)

# Print result as required
print(f"Result: {thermal_capacity}")