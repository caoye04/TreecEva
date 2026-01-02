def calculate_phase_score(level, duration, stress_factor):
    base = level * duration
    adjusted = base // (stress_factor + 1)
    return adjusted * 2

phases = [(3, 8, 2), (5, 6, 1), (4, 10, 3)]
phase_scores = []

for idx, (level, duration, stress) in enumerate(phases):
    score = calculate_phase_score(level, duration, stress)
    phase_scores.append(score)

normalization_factor = 1.5
total_raw = sum(phase_scores)

scaled_scores = [round(s / normalization_factor) for s in phase_scores]
total_scaled = sum(scaled_scores)

final_bonus = 10 if total_scaled > 50 else 0
total_efficiency = total_scaled + final_bonus

Result: {total_efficiency}