from collections import defaultdict

# Simulate developer contribution analysis with noise and distractors
def analyze_developer_activity(logs):
    activity_count = defaultdict(int)
    temp_memo = {}  # Irrelevant caching structure
    total_lines = 0
    distraction_sum = 0

    for entry in logs:
        dev = entry['developer']
        lines = entry['lines_added']
        total_lines += lines
        activity_count[dev] += lines

        # Distractor computation: tracks something irrelevant
        if lines > 100:
            distraction_sum += 5
            temp_memo[dev] = temp_memo.get(dev, 0) + 1

    # Another red herring: unused aggregate
    average_per_entry = total_lines / len(logs) if logs else 0

    return dict(activity_count), average_per_entry, distraction_sum

def apply_bonus(schedule, base_bonus=10):
    bonus_map = {}
    overtime_tracker = []  # Collected but not used

    for day, hours in schedule.items():
        extra = 0
        if hours > 8:
            extra = (hours - 8) * base_bonus
            overtime_tracker.append(extra)
        bonus_map[day] = extra + base_bonus  # Base always applied

    # Dummy filter operation with no effect
    filtered_bonuses = {k: v for k, v in bonus_map.items() if v > 10}

    return bonus_map  # Unused filtered_bonuses adds distraction

def calculate_rating(contributions, penalty_factor):
    raw_score = 0
    decay = 0.95
    adjustment_log = []  # Tracking for debugging, not used in result

    for i, (dev, score) in enumerate(contributions.items()):
        weighted = score * (decay ** i)  # Fades older devs in iteration order
        if weighted > 50:
            adjustment_log.append('high')
        elif weighted < 10:
            adjustment_log.append('low')
        raw_score += weighted

    # Apply penalty only if certain threshold met
    if sum(contributions.values()) > 200:
        raw_score -= penalty_factor * 15

    return int(raw_score)

# Main execution flow
if __name__ == '__main__':
    # Input data: realistic simulation of dev logs
    logs = [
        {'developer': 'alice', 'lines_added': 120},
        {'developer': 'bob', 'lines_added': 85},
        {'developer': 'alice', 'lines_added': 200},
        {'developer': 'carol', 'lines_added': 45},
        {'developer': 'bob', 'lines_added': 60},
        {'developer': 'alice', 'lines_added': 300}
    ]

    # Step 1: Analyze contributions
    contributions, avg_lines, dist_sum = analyze_developer_activity(logs)

    # Distractor variables
    size_factor = len(logs) * 2
    growth_projection = size_factor * 1.5  # Unused in final logic

    # Step 2: Bonus application (irrelevant to score but present)
    work_schedule = {'mon': 7, 'tue': 9, 'wed': 10, 'thu': 8, 'fri': 12}
    daily_bonuses = apply_bonus(work_schedule)

    bonus_total = sum(daily_bonuses.values())  # Computed but not used

    # Step 3: Calculate final rating
    penalty_factor = 2
    final_score = calculate_rating(contributions, penalty_factor)

    # Output target result
    print(f"Result: {final_score}")