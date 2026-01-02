from collections import defaultdict

# Simulate employee evaluation system with multiple scoring tiers
def main():
    # Core data
    employees = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    base_scores = [85, 92, 78, 96, 88]
    attendance_rate = [0.94, 0.87, 0.96, 0.91, 0.89]
    peer_reviews = [4.3, 4.7, 3.9, 4.8, 4.5]  # out of 5

    # Irrelevant distraction: unused metrics
    login_frequency = [23, 18, 31, 25, 20]  # logs per week (not used)
    coffee_consumption = [3, 1, 4, 2, 3]   # cups per day (completely irrelevant)

    # Step 1: Normalize scores to 0-100 scale
    normalized_reviews = [int(x * 20) for x in peer_reviews]  # convert 0-5 to 0-100

    # Step 2: Compute composite performance score
    composite_scores = []
    for i in range(len(base_scores)):
        comp = (base_scores[i] * 0.6) + (attendance_rate[i] * 100 * 0.2) + (normalized_reviews[i] * 0.2)
        composite_scores.append(round(comp, 2))

    # Step 3: Assign performance tier based on composite score
    performance_tiers = []
    for score in composite_scores:
        if score >= 90:
            performance_tiers.append('Outstanding')
        elif score >= 80:
            performance_tiers.append('Exceeds Expectations')
        elif score >= 70:
            performance_tiers.append('Meets Expectations')
        else:
            performance_tiers.append('Needs Improvement')

    # Step 4: Create rankings using defaultdict for counting
    tier_counts = defaultdict(int)
    for tier in performance_tiers:
        tier_counts[tier] += 1

    # Assign numerical ranking based on tier priority
    tier_rank_map = {
        'Outstanding': 1,
        'Exceeds Expectations': 2,
        'Meets Expectations': 3,
        'Needs Improvement': 4
    }
    rankings = [tier_rank_map[tier] for tier in performance_tiers]

    # Distraction: Unused sorting attempt
    sorted_employees = sorted(zip(employees, composite_scores), key=lambda x: x[1], reverse=True)
    mid_performer = sorted_employees[len(sorted_employees)//2]  # not used further

    # Step 5: Calculate final weighted score based on rank and base performance
    def calculate_final_score(ranks, tiers):
        base_weight = 0.7
        rank_weight = 0.3
        final_values = []
        for i in range(len(composite_scores)):
            rank_bonus = max(0, (5 - ranks[i]) * 5)  # higher rank -> more bonus
            adjustment = 0
            if tiers[i] == 'Outstanding':
                adjustment = 10
            elif tiers[i] == 'Needs Improvement':
                adjustment = -15
            final_val = (composite_scores[i] * base_weight) + rank_bonus + adjustment
            final_values.append(final_val)
        return int(sum(final_values) / len(final_values))  # average final score

    # Key execution point
    final_score = calculate_final_score(rankings, performance_tiers)

    # Output result as required
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()