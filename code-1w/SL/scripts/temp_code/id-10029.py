from collections import defaultdict
from itertools import combinations

# Simulate structural load analysis for a truss bridge design

def analyze_member_stress(loads, connections):
    stress_map = defaultdict(float)
    temp_buffer = []
    total_joints = len(connections)
    
    # Compute base axial forces in members due to static loads
    for joint_id, connected_members in connections.items():
        joint_load = loads.get(joint_id, 0)
        if joint_load > 0:
            force_per_member = joint_load / len(connected_members) if connected_members else 0
            for member in connected_members:
                stress_map[member] += force_per_member

    # Distractor: Calculate unused geometric ratios
    geometric_ratio_sum = 0.0
    for i in range(total_joints):
        for j in range(i + 1, total_joints):
            distance = ((i - j) ** 2 + 1) ** 0.5  # Fake spatial model
            geometric_ratio_sum += 1 / distance if distance != 0 else 0
    
    # Secondary effect: thermal expansion interference (semi-relevant)
    thermal_factors = [0.05, 0.08, -0.03, 0.1]
    effective_thermal_drift = sum([abs(f) for f in thermal_factors]) * 0.15
    
    # Apply dynamic redistribution based on neighboring stress levels
    redistribution_delta = 0.0
    for member, stress in stress_map.items():
        neighbor_stress_sum = 0.0
        member_prefix = member[:-1]  # e.g., 'M1' from 'M1A'
        for other_member, s in stress_map.items():
            if other_member.startswith(member_prefix) and other_member != member:
                neighbor_stress_sum += s
        if neighbor_stress_sum > 1.0:
            redistribution_delta += stress * (0.1 * min(neighbor_stress_sum / 4.0, 1.0))
    
    # Update stresses with redistribution feedback
    for member in stress_map:
        stress_map[member] += redistribution_delta * 0.25

    return stress_map, geometric_ratio_sum, effective_thermal_drift


def calculate_stress_distribution(base_loads, topology):
    # Initial processing
    raw_stress, geo_sum, thermal_drift = analyze_member_stress(base_loads, topology)
    
    # Extract key member group
    primary_members = [k for k in raw_stress.keys() if k.startswith('M7')]
    secondary_members = [k for k in raw_stress.keys() if k.startswith('M8')]
    
    # Focus on critical load path
    critical_load = 0.0
    for m in primary_members:
        critical_load += raw_stress[m]
    
    # Distractor: combinatorial safety check (not used in final result)
    safety_combinations = list(combinations(primary_members, min(2, len(primary_members))))
    fail_count_simulated = 0
    for combo in safety_combinations:
        test_load = sum(raw_stress[c] for c in combo)
        if test_load > 8.0:
            fail_count_simulated += 1
    
    # Normalize critical load using empirical factor
    empirical_factor = 1.0 + (thermal_drift * 0.5)
    adjusted_critical_load = critical_load * empirical_factor
    
    # Final adjustment based on system redundancy index
    redundancy_index = len(safety_combinations) / max(len(primary_members), 1)
    if redundancy_index > 1.0:
        adjusted_critical_load *= (1 + 0.05 * min(redundancy_index, 2.0))
    
    # Key result computation
    final_load = int(adjusted_critical_load * 100) / 100.0  # Round to 2 decimal places
    
    # Irrelevant summary statistics
    avg_stress = sum(raw_stress.values()) / len(raw_stress)
    peak_stress = max(raw_stress.values())
    
    return final_load, avg_stress, peak_stress, fail_count_simulated

# Define input data
base_loads = {
    0: 12.5,
    1: 0.0,
    2: 18.3,
    3: 9.7,
    4: 0.0,
    5: 14.2,
    6: 0.0,
    7: 22.1,
    8: 5.8
}

topology = {
    0: ['M1A', 'M2B'],
    1: ['M2B', 'M3C', 'M7A'],
    2: ['M3C', 'M4D', 'M7B'],
    3: ['M4D', 'M5E'],
    4: ['M5E', 'M6F', 'M8A'],
    5: ['M6F', 'M7C'],
    6: ['M7C', 'M7D', 'M8B'],
    7: ['M7D', 'M8B', 'M9X'],
    8: ['M9X']
}

# Execute main calculation
final_load, _, _, _ = calculate_stress_distribution(base_loads, topology)
print(f"Result: {final_load}")