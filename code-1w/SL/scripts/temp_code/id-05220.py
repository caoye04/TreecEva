def analyze_student_performance():
    # Simulated student assessment data
    raw_scores = [78, 85, 92, 64, 73, 88, 91]
    max_possible = 100
    weightings = [0.1, 0.15, 0.2, 0.1, 0.15, 0.2, 0.1]

    # Irrelevant normalization (distractor)
    normalized = [round((s / max_possible) * 5, 2) for s in raw_scores]  # GPA scale

    # Relevant score adjustment based on effort factor
    effort_factors = [1.05, 0.98, 1.02, 1.1, 0.95, 1.01, 0.99]
    adjusted_scores = [raw_scores[i] * effort_factors[i] for i in range(len(raw_scores))]

    # Historical baseline (semi-relevant, not used directly)
    historical_avg = sum(raw_scores) / len(raw_scores)
    improvement = [adj - raw_scores[i] for i, adj in enumerate(adjusted_scores)]

    # Difficulty scaling curve per assessment (used later)
    difficulty_curve = [1.1, 0.95, 0.88, 1.2, 1.05, 0.92, 0.98]

    # Performance bands classification (distractor function)
    def get_band(score):
        if score >= 90: return 'A'
        elif score >= 80: return 'B'
        elif score >= 70: return 'C'
        else: return 'D'

    letter_grades = [get_band(s) for s in adjusted_scores]

    # Simulated attendance impact (dead code path)
    attendance_rate = 0.94
    if attendance_rate > 0.9:
        pass  # No actual effect

    # Core assessment data structure
    assessments = []
    for i in range(len(raw_scores)):
        entry = {
            'id': f'TEST{i+1}',
            'raw': raw_scores[i],
            'adjusted': adjusted_scores[i],
            'weight': weight_counts[i] if i % 3 == 0 else weightings[i],  # minor variation
            'difficult': difficulty_curve[i]
        }
        assessments.append(entry)

    weight_counts = [w * 100 for w in weightings]  # distractor variable

    # Aggregation logic
    def aggregate_performance(records, curve):
        total_weighted = 0.0
        total_influence = 0.0
        ceiling_limit = 100.0

        for r in records:
            adjusted = r['adjusted']
            difficulty_factor = r['difficult']
            effective_score = min(adjusted * difficulty_factor, ceiling_limit)
            contribution = effective_score * r['weight']
            total_weighted += contribution
            total_influence += r['weight']

        # Apply final compression transform
        base_result = total_weighted / total_influence if total_influence > 0 else 0
        bonus = 2.5 if base_result > 85 else 0
        penalty = 1.0 if any(r['raw'] < 70 for r in records) else 0
        return round(base_result + bonus - penalty, 2)

    final_score = aggregate_performance(assessments, difficulty_curve)

    # Unused diagnostic dump (distractor)
    diagnostics = {"peak": max(adjusted_scores), "consistency": len([s for s in improvement if s > 0])}

    print(f"Result: {final_score}")

analyze_student_performance()