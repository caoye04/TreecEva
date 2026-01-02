import math

# Simulate water quality analysis with multi-phase purification
water_samples = [
    {'id': 'A1', 'ph': 6.2, 'turbidity': 8.1, 'chlorine': 0.3},
    {'id': 'B2', 'ph': 7.8, 'turbidity': 12.5, 'chlorine': 0.1},
    {'id': 'C3', 'ph': 6.9, 'turbidity': 3.2, 'chlorine': 0.5},
    {'id': 'D4', 'ph': 8.1, 'turbidity': 18.7, 'chlorine': 0.2},
    {'id': 'E5', 'ph': 7.0, 'turbidity': 2.1, 'chlorine': 0.6}
]

treatment_phases = [
    {'name': 'coagulation', 'optimal_ph_range': (6.5, 7.5), 'efficiency_factor': 0.8},
    {'name': 'filtration', 'optimal_ph_range': (6.8, 7.8), 'efficiency_factor': 0.9},
    {'name': 'disinfection', 'optimal_ph_range': (6.0, 7.2), 'efficiency_factor': 0.95}
]

# Irrelevant calibration data (distractor)
calibration_readings = [0.98, 0.99, 1.02, 1.01, 0.97]
baseline_drift = sum(calibration_readings) / len(calibration_readings) - 1.0

# Decoy function that looks important but isn't used in main logic
def adjust_for_temperature(measurement, temp):
    return measurement * (1 + (temp - 25) * 0.02)

# Misleading intermediate calculation (dead path)
total_adjustment = 0
for sample in water_samples:
    if sample['ph'] > 7.5:
        total_adjustment += sample['turbidity'] * 0.1

# Unused transformation matrix for sensor fusion (red herring)
sensor_fusion_matrix = [
    [0.3, 0.4, 0.3],
    [0.2, 0.6, 0.2],
    [0.1, 0.8, 0.1]
]

# Auxiliary function with conditional expression and slicing
def assess_phase_efficiency(sample_ph, phase_info):
    low, high = phase_info['optimal_ph_range']
    return phase_info['efficiency_factor'] if low <= sample_ph <= high else phase_info['efficiency_factor'] * 0.4

# Complex processing with multiple concepts
def process_contaminants(samples, phases):
    cumulative_score = 0
    
    # Track per-sample degradation index (partially relevant)
    degradation_index = []
    
    for s in samples:
        # Initial assessment
        base_risk = s['turbidity'] * 10 + (7.0 - s['ph'])**2 * 5
        
        # Apply phase-based mitigation using conditional expressions
        net_mitigation = 0
        phase_contributions = []
        
        for p in phases:
            raw_eff = assess_phase_efficiency(s['ph'], p)
            chlorine_weight = 1.0 if s['chlorine'] < 0.4 else 0.7
            adjusted_eff = raw_eff * chlorine_weight
            phase_contributions.append(adjusted_eff)
        
        # Use slicing to analyze only middle phase (critical relevance)
        mid_phase_eff = phase_contributions[1]  # filtration phase at index 1
        primary_mitigation = base_risk * mid_phase_eff
        
        # Secondary adjustment based on neighboring samples (distraction)
        neighbor_impact = 0
        idx = samples.index(s)
        if 0 < idx < len(samples) - 1:
            neighbor_avg_turb = (samples[idx-1]['turbidity'] + samples[idx+1]['turbidity']) / 2
            neighbor_impact = (neighbor_avg_turb - s['turbidity']) * 0.3
        
        final_reduction = primary_mitigation + max(0, neighbor_impact)  # Ignore negative impact
        residual_risk = base_risk - final_reduction
        
        # Update cumulative score using bit manipulation (obscure but valid)
        risk_int = int(residual_risk)
        # XOR with sample ID character code for "randomization" (actually deterministic)
        id_char = ord(s['id'][1])  # '1', '2', etc.
        masked_risk = risk_int ^ id_char
        cumulative_score += masked_risk & 0xFF  # Keep lower 8 bits
        
        degradation_index.append(residual_risk)
    
    # Final aggregation uses list comprehension and conditional logic
    filtered_indices = [idx for idx, val in enumerate(degradation_index) if val < 50]
    
    # The real answer depends only on cumulative_score, others are distractions
    normalization_factor = len(filtered_indices) if filtered_indices else 1
    
    # Key computation - this is what matters
    result = int(cumulative_score / normalization_factor)
    
    # Dead code: would modify result if conditions met (but they aren't)
    emergency_override = False
    for s in samples:
        if s['ph'] < 6.0 or s['ph'] > 8.5:
            emergency_override = True
    
    if emergency_override:
        result = -999  # never reached
    
    return result

# Execution point of interest
filtration_score = process_contaminants(water_samples, treatment_phases)

# Print target result
Result: {filtration_score}