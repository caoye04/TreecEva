from itertools import combinations

# Simulate biomechanical load distribution across joint angles
def analyze_posture_efficiency(joint_angles):
    base_stability = 78.4
    cumulative_torque = 0
    stress_peaks = []
    angular_moments = []

    for angle in joint_angles:
        if angle < 90:
            adjusted_load = (90 - angle) * 1.8
            cumulative_torque += adjusted_load
            stress_peaks.append(adjusted_load)
        elif angle > 120:
            compensation_factor = (angle - 120) * 1.3
            cumulative_torque += compensation_factor
            angular_moments.append(compensation_factor)

    # Distractor: unused but plausible calculation
    theoretical_efficiency = base_stability - (cumulative_torque * 0.75)

    # Real computation path: assess forward vs reverse chain stress
    prime_pairs = list(combinations([x for x in range(2, 10) if all(x % i != 0 for i in range(2, x))], 2))
    pair_stress_sum = sum(a * b for a, b in prime_pairs[:len(stress_peaks)])

    forward_stress = len(stress_peaks) * 12 + int(pair_stress_sum % 100)
    reverse_stress = len(angular_moments) * 17 + (sum(angular_moments) if angular_moments else 45)

    # Key statement
    equilibrium_score = min(forward_stress, reverse_stress)

    # Additional red herring variables
    normalized_ratio = forward_stress / reverse_stress if reverse_stress != 0 else 1.0
    stability_index = base_stability + equilibrium_score // 3

    return equilibrium_score

# Input data based on motion capture readings
angles_data = [85, 92, 115, 125, 88, 130]

result = analyze_posture_efficiency(angles_data)
print(f"Target result: {result}")