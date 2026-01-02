from collections import defaultdict, Counter

# Simulate student assessment scores across multiple subjects and attempts
def generate_assessment_data():
    data = [
        ('math', 'quiz1', 85), ('math', 'quiz2', 90), ('math', 'retake', 87),
        ('physics', 'midterm', 78), ('physics', 'final', 85),
        ('chemistry', 'lab', 92), ('chemistry', 'exam', 88), ('chemistry', 'bonus', 100),
        ('math', 'challenge', 95), ('physics', 'project', 82)
    ]
    return data

# Process raw data into structured format
def parse_assessments(raw_data):
    parsed = defaultdict(list)
    frequency = Counter()  # Track how often a subject appears

    for subject, category, score in raw_data:
        parsed[subject].append(score)
        frequency[subject] += 1

    # Distractor computation: unused transformation
    normalized_freq = {k: v / len(raw_data) for k, v in frequency.items()}
    total_normalization = sum(normalized_freq.values())  # Unused

    return parsed

# Apply grading logic with adjustment rules
def calculate_subject_average(scores, pass_threshold=85):
    best_score = max(scores)
    average_score = sum(scores) / len(scores)
    adjusted_avg = average_score * 1.05 if best_score >= pass_threshold else average_score * 0.95
n    # Artificial intermediate to add noise
    stability_metric = (max(scores) - min(scores)) / average_score if len(scores) > 1 else 0.0

    return min(adjusted_avg, 100)  # Cap at 100

# Aggregate performance with weighting heuristic
def aggregate_performance(assessments):
    weights = {'math': 1.2, 'physics': 1.1, 'chemistry': 1.15}
    total_weighted = 0.0
    total_influence = 0.0

    # Secondary tracking structure (partially irrelevant)
    performance_trend = {}

    for subject, scores in assessments.items():
        base_avg = calculate_subject_average(scores)
        weight = weights.get(subject, 1.0)
        contribution = base_avg * weight
        total_weighted += contribution
        total_influence += weight

        # Tracking trend (not used in final calculation)
        performance_trend[subject] = round(base_avg, 2)

    # Distractor block: analyze trend volatility (unused)
    if performance_trend:
        trends = list(performance_trend.values())
        trend_variance = sum((x - sum(trends)/len(trends))**2 for x in trends) / len(trends) if trends else 0

    final_raw = total_weighted / total_influence if total_influence else 0

    # Final adjustment based on holistic rule
    ceiling_adjusted = min(final_raw, 98.5)  # Conservative cap

    # Key assignment point
    final_score = int(round(ceiling_adjusted))  # Convert to integer

    return final_score

# Execution flow
if __name__ == "__main__":
    raw = generate_assessment_data()
    parsed_assessments = parse_assessments(raw)
    
    # Extraneous pre-check (dead-end analysis)
    subject_count = len(parsed_assessments)
    total_entries = sum(len(scores) for scores in parsed_assessments.values())
    density_ratio = total_entries / subject_count if subject_count else 0  # Not used
    
    # Core computation
    final_score = aggregate_performance(parsed_assessments)
    print(f"Result: {final_score}")