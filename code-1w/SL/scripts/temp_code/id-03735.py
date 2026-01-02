def calculate_equilibrium(forces, constraints):
    # Simulate mechanical equilibrium calculation under constraints
    total_force = sum(f * 1.0 for f in forces)
    adjustment_factor = 1.0
    
    # Irrelevant tracking variables (distractors)
    max_force_seen = max(forces) if forces else 0
    force_distribution_score = (max_force_seen / (total_force + 1e-5)) * 100
    temp_diagnostic_log = f'Score: {force_distribution_score:.2f}'

    # Constraint-based conditional logic
    constraint_met = all(c <= total_force for c in constraints)
    override_flag = False

    # Simulated sensor tolerance check (semi-relevant)
    sensor_readings = [0.98, 1.02, 0.99, 1.01]
    calibration_offset = sum(abs(1.0 - r) for r in sensor_readings) / len(sensor_readings)
    
    if calibration_offset > 0.05:
        adjustment_factor *= 0.95
    else:
        adjustment_factor *= 1.05

    # Complex nested condition with conditional expression
    safety_margin = 1.1 if not override_flag else 0.9
    adjusted_total = total_force * adjustment_factor
    
    # Equilibrium depends on constraint satisfaction
    base_equilibrium = adjusted_total if constraint_met else adjusted_total * 0.5
    
    # Secondary correction using combinatorics-inspired weighting
    n_constraints = len(constraints)
    combination_weight = 1.0
    if n_constraints >= 2:
        # Simple combinatorics: C(n,2) influence factor
        combination_weight = (n_constraints * (n_constraints - 1)) / 2.0
        combination_weight = 1.0 + (combination_weight / 10.0)  # Normalize impact

    # Final equilibrium state
    equilibrium = base_equilibrium * combination_weight * safety_margin
    
    # Dead code path (irrelevant to final result)
    if False:
        equilibrium = -999
        debug_trace = "Emergency override triggered"
    
    return equilibrium

# Main execution context
forces = [15, 25, 35, 45]
constraints = [60, 70]

# Spurious variable assignments and computations (distraction)
diagnostic_mode = True
system_status = "ACTIVE"
sync_timestamp = 1234567890
redundant_forces_copy = forces[:]
scaling_ratio = (forces[3] / forces[0])  # Not used in core logic

# Key computation
equilibrium = calculate_equilibrium(forces, constraints)

# Output result as required
print(f"Result: {equilibrium}")