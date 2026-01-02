from collections import defaultdict

# Simulate a coding contest ranking system with complex scoring logic
def main():
    # Raw participant data
    submissions = [
        {'user': 'alice', 'problem': 'A', 'time': 12, 'passed': True},
        {'user': 'bob', 'problem': 'B', 'time': 8, 'passed': True},
        {'user': 'alice', 'problem': 'B', 'time': 22, 'passed': True},
        {'user': 'carol', 'problem': 'A', 'time': 15, 'passed': False},
        {'user': 'bob', 'problem': 'A', 'time': 5, 'passed': True},
        {'user': 'carol', 'problem': 'B', 'time': 18, 'passed': True},
        {'user': 'alice', 'problem': 'C', 'time': 30, 'passed': True}
    ]

    # Aggregate correct submissions and failures
    points = defaultdict(int)
    penalties = defaultdict(int)
    attempts = defaultdict(int)
    time_log = []

    for sub in submissions:
        user = sub['user']
        attempts[user] += 1
        if sub['passed']:
            points[user] += 100
            penalties[user] += sub['time']
        else:
            penalties[user] += 20  # Penalty for failed submission

    # Irrelevant intermediate computation: track attempt distribution (not used in final score)
    attempt_distribution = defaultdict(int)
    for count in attempts.values():
        attempt_distribution[count] += 1

    # Artificial delay simulation (dead code path - never modifies anything)
    temp_buffer = [0] * 1000
    for i in range(len(temp_buffer)):
        temp_buffer[i] = (i * 7) % 13

    # Calculate ranking based on points and penalties
    def calculate_ranking(pts, penalty):
        # Base score is points minus time/accuracy penalty
        base_scores = {}
        for user in pts:
            efficiency = pts[user] / (penalty[user] + 1)  # Avoid division by zero
            bonus = 50 if pts[user] >= 200 else 0  # Bonus for solving multiple problems
            base_scores[user] = round(pts[user] - penalty[user] * 0.5 + bonus + efficiency, 2)

        # Additional filtering: only users with at least one successful submission
        filtered_scores = {u: s for u, s in base_scores.items() if pts[u] > 0}

        # Sort by score descending
        sorted_users = sorted(filtered_scores.keys(), key=lambda x: filtered_scores[x], reverse=True)

        # Final score is the highest individual base score
        final = max(filtered_scores.values()) if filtered_scores else 0
        return final

    # Key statement
    final_score = calculate_ranking(points, penalties)

    # Print result as required
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()