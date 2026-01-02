from collections import defaultdict, Counter

# Simulate a competitive coding contest ranking analysis with noise and distractions
def analyze_rankings(submissions, user_preferences):
    score_map = defaultdict(int)
    attempt_count = Counter()
    penalty_time = 0

    for user, data in submissions.items():
        solved_count = len(data['solved'])
        failed_count = len(data['failed'])
        attempt_count[user] += solved_count + failed_count

        # Real logic: base score from problems solved
        score_map[user] = solved_count * 100

        # Distraction: irrelevant time-based penalty accumulation
        for t in data['timestamps']:
            if t > 3600:
                penalty_time += 5
            elif t < 600:
                penalty_time -= 2  # Artificial adjustment with no effect

        # Semi-relevant: preference boost (only some preferences matter)
        if 'difficulty' in user_preferences.get(user, {}):
            if user_preferences[user]['difficulty'] == 'hard':
                score_map[user] += 20  # Only this affects result

    # Dead code path: unused function definition
    def unused_helper(x):
        return x ** 2 + 3 * x + 1

    # Irrelevant string processing distraction
    summary_log = ""
    for user in score_map:
        summary_log += f"User{user[-1]}:" + "A" * (score_map[user] % 10) + "|"

    # Another red herring: complex but unused calculation
    max_streak = 0
    current_streak = 0
    for i in range(1, len(submissions['user_1']['timestamps'])):
        if submissions['user_1']['timestamps'][i] - submissions['user_1']['timestamps'][i-1] < 300:
            current_streak += 1
        else:
            max_streak = max(max_streak, current_streak)
            current_streak = 0
    max_streak = max(max_streak, current_streak)

    return score_map


def calculate_final_score(rankings, multiplier):
    base_total = sum(rankings.values())
    adjustment = 0

    # Nested logic with meaningful and distracting elements
    for i, (user, score) in enumerate(sorted(rankings.items(), key=lambda x: -x[1])):
        if i % 2 == 0:
            adjustment += 5
        else:
            adjustment -= 2  # Net effect is small but real

        # Use of zip: relevant for position-based scoring
        positions = list(range(1, len(rankings) + 1))
        bonuses = [0.1, 0.05, 0.025, 0.01]
        for p, b in zip(positions, bonuses):
            if i + 1 == p and p <= 4:
                adjustment += int(b * score)

    # Final computation: only this output matters
    final_score = base_total + adjustment
    final_score *= multiplier  # Applied uniformly

    # More distraction: unused set operations
    unique_scores = set(rankings.values())
    duplicate_count = len(rankings.values()) - len(unique_scores)
    temp_result = [x for x in unique_scores if x > 200]
    temp_result.sort(reverse=True)

    return int(final_score)

# Main execution
if __name__ == "__main__":
    contest_submissions = {
        'user_1': {
            'solved': ['A', 'B', 'C', 'D'],
            'failed': ['E', 'F'],
            'timestamps': [120, 450, 780, 1200, 3700, 7200]
        },
        'user_2': {
            'solved': ['A', 'B', 'C'],
            'failed': ['D', 'G', 'H'],
            'timestamps': [300, 900, 1500, 2000, 4000, 7000]
        },
        'user_3': {
            'solved': ['A', 'B', 'C', 'D', 'E'],
            'failed': ['F'],
            'timestamps': [100, 200, 600, 1100, 1300, 5000]
        }
    }

    preferences = {
        'user_1': {'difficulty': 'hard'},
        'user_2': {'difficulty': 'medium'},
        'user_3': {'difficulty': 'hard'}
    }

    # Intermediate variables with mixed relevance
    raw_analysis = analyze_rankings(contest_submissions, preferences)
    bonus_multiplier = 1.1
    final_score = calculate_final_score(raw_analysis, bonus_multiplier)
    
    print(f"Target result: {final_score}")