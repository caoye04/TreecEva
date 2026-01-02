def analyze_efficiency(metrics):
    adjusted = []
    multiplier = 1.5
    offset = 0.8
    temp_sum = 0

    for val in metrics:
        temp_sum += val ** 0.5 * multiplier + offset
    avg_temp = temp_sum / len(metrics)

    for val in metrics:
        if val > avg_temp:
            adjusted.append(val * 1.1)
        else:
            adjusted.append(val * 0.95)

    return sum(adjusted)


def calculate_stress_level(workload, thresholds):
    stress = 0
    baseline = 50
    distraction_counter = 0  # unused variable (distractor)

    for task in workload:
        if task > thresholds['high']:
            stress += 3
        elif task > thresholds['medium']:
            stress += 2
        else:
            stress += 1

    normalized_stress = (stress * 10) / len(workload)
    return normalized_stress


def extract_keywords(log_entries):
    keywords = set()
    for entry in log_entries:
        words = entry.lower().split()
        for word in words:
            cleaned = word.strip('.,!?"')
            if len(cleaned) > 4 and 'error' not in cleaned:
                keywords.add(cleaned)
    size_hint = len(keywords) % 7  # irrelevant computation
    return keywords


def evaluate_performance(output_levels, risk):
    base_score = sum(output_levels) / len(output_levels)
    penalty = 0

    if risk > 60:
        penalty = base_score * 0.3
    elif risk > 40:
        penalty = base_score * 0.15

    bonus = 0
    if base_score > 85:
        bonus = 10

    # Complex adjustment using string-based logic as a red herring
    status_msg = "Performance: Optimal" if base_score >= 80 else "Review Needed"
    flag_length = len(status_msg.replace(":", "").replace(" ", ""))
    adjustment_factor = flag_length * 0.05  # misleading but non-impacting

    final_score = base_score - penalty + bonus + adjustment_factor
    return round(final_score, 2)

# Main execution block
productivity_data = [88, 76, 92, 81, 95]
work_patterns = [67, 71, 58, 83, 74]
risk_assessment = {
    'low': 30,
    'medium': 50,
    'high': 70
}

# Irrelevant data processing (distractor)
log_messages = [
    "System initialized successfully",
    "User login detected from remote IP",
    "Background task completed without errors",
    "Cache refreshed at interval"
]
keyword_set = extract_keywords(log_messages)

# Semi-relevant preprocessing
efficiency_score = analyze_efficiency(productivity_data)
productivity = [efficiency_score / 5] * 5  # transformed metric

risk_level = calculate_stress_level(work_patterns, risk_assessment)
dummy_tracker = {'peak': max(work_patterns), 'trend': 'stable'}  # dead storage

# Key statement
final_score = evaluate_performance(productivity, risk_level)

print(f"Result: {final_score}")