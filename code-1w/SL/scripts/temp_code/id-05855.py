def analyze_performance(grades, thresholds):
    # Irrelevant transformation (distractor)
    adjusted_grades = [g + 5 for g in grades if g < 90]
    
    # Semi-relevant preprocessing
    passing = [g for g in grades if g >= thresholds['pass']]
    honors = [g for g in grades if g >= thresholds['honors']]

    # Misleading computation with unused result
    avg_adjusted = sum(adjusted_grades) / len(adjusted_grades) if adjusted_grades else 0
    temp_analysis = {"count": len(passing), "ratio": len(honors) / len(grades) if grades else 0}

    # Core logic: compute weighted score based on distribution
    counts = {"low": 0, "mid": 0, "high": 0}
    for grade in grades:
        if grade < 70:
            counts["low"] += 1
        elif grade < 85:
            counts["mid"] += 1
        else:
            counts["high"] += 1

    # Use enumerate to add irrelevant indexing
    for i, (k, v) in enumerate(counts.items()):
        counts[k] = v * (i + 1)  # Distortion for distraction

    # Actual scoring uses original counts, not distorted ones
    original_total = sum(counts.values()) // max(len(counts), 1)  # Recovers approximate original magnitude
    
    # Real calculation: high-weighted contribution
    base_score = len(passing) * 10
    bonus = len(honors) * 7
    penalty = counts["low"] * 3
    
    # Final score computed here — key statement
    final_score = base_score + bonus - penalty + original_total
    
    # Dead code path (never executed)
    if False:
        final_score = max(final_score, 50)
    
    return final_score

# Main execution
student_grades = [65, 88, 72, 91, 85, 67, 74, 93]
cut-offs = {"pass": 70, "honors": 85}

# Unused helper (distractor)
def normalize(values):
    total = sum(values)
    return [v / total for v in values] if total else values

result = analyze_performance(student_grades, cut-offs)
Result: {result}