def analyze_workflow():
    # Simulate employee performance metrics
    base_hours = 40
    overtime_bonus = 1.5
    productivity = [85, 90, 78, 92, 88]
    error_log = ['critical', 'minor', 'none', 'minor', 'critical']
    efficiency_ratio = sum(productivity) / len(productivity)

    # Irrelevant distraction: unused computation on string data
    department_names = ['Dev', 'QA', 'Ops', 'Support', 'Security']
    coded_labels = list(map(lambda x: x[:2].lower(), department_names))
    checksum = sum([hash(label) % 100 for label in coded_labels])  # Dead-end computation

    # Mapping errors to severity scores (used later)
    severity_map = {'none': 0, 'minor': 1, 'critical': 5}
    errors = [severity_map[err] for err in error_log if err in severity_map]

    # Distraction: set operations that don't affect final result
    unique_severities = set(severity_map.values())
    hypothetical_cases = {0, 1, 2, 5}
    missing_cases = hypothetical_cases - unique_severities  # Computed but unused

    # Conditional adjustments based on performance
    if efficiency_ratio > 80:
        base_multiplier = 1.2
    else:
        base_multiplier = 1.0

    # Secondary distraction: string analysis with no impact
    feedback_strings = ["Good job", "Improve focus", "Excellent work"]
    word_count = sum(len(s.split()) for s in feedback_strings)

    def evaluate_performance(perf_list, err_list):
        total_perf = sum(perf_list)
        total_penalty = sum(err_list) * 10
        raw_score = total_perf - total_penalty
        adjustment = 5 if len(perf_list) >= 5 else 0
        return int((raw_score * base_multiplier) + adjustment)

    final_score = evaluate_performance(productivity, errors)
    
    # Final red herring: bitwise operation chain
    debug_flag = (base_hours ^ 42) & 0xFF
    
    print(f"Result: {final_score}")

analyze_workflow()