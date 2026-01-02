def main():
    # Simulate employee review data with performance metrics
    employees = ['alice', 'bob', 'carol', 'david']
    base_scores = [78, 85, 90, 88]
    peer_ratings = [[80, 75, 82], [88, 86, 87], [91, 89, 93], [84, 85, 80]]
    attendance_records = [29, 30, 28, 27]  # days present out of 30

    # Irrelevant computation: normalize attendance to unused scale
    normalized_attendance = [days / 30 * 100 for days in attendance_records]
    avg_rating = sum(normalized_attendance) / len(normalized_attendance)  # unused

    # Create feedback map using dictionary and zip
    feedback_map = {}
    for emp, score in zip(employees, base_scores):
        feedback_map[emp] = {'base': score}

    # Augment with peer ratings using average
    for i, emp in enumerate(employees):
        avg_peer = sum(peer_ratings[i]) / len(peer_ratings[i])
        feedback_map[emp]['peer'] = avg_peer

    # Add attendance bonus eligibility (not directly used in final formula)
    for emp in employees:
        idx = employees.index(emp)
        if attendance_records[idx] >= 29:
            feedback_map[emp]['bonus_eligible'] = True
        else:
            feedback_map[emp]['bonus_eligible'] = False

    # Distractor: complex lambda that computes something irrelevant
    complexity_metric = list(map(lambda x: x ** 2 - x * 0.5, base_scores))
    total_complexity = sum(complexity_metric)  # unused

    # Key function: aggregates performance using specific weighted logic
    def aggregate_performance(feedback):
        result = 0
        weights = {'base': 0.6, 'peer': 0.4}
        for emp_data in feedback.values():
            # Only base and peer contribute
            emp_total = emp_data['base'] * weights['base'] + emp_data['peer'] * weights['peer']
            result += emp_total
        return int(result / len(feedback))  # average across employees

    # Execution point of interest
    final_score = aggregate_performance(feedback_map)

    # Additional red herring: sort employees by unused metric
    sorted_employees = sorted(employees, key=lambda e: feedback_map[e]['base'] + feedback_map[e].get('peer', 0))

    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()