from collections import defaultdict

# Simulate daily user engagement metrics over a week
daily_logins = [120, 135, 140, 90, 160, 180, 175]
feature_usage = ['search', 'profile', 'search', 'settings', 'search', 'profile', 'search']
error_rates = [0.02, 0.01, 0.03, 0.05, 0.02, 0.01, 0.04]

# Track bonus eligibility based on performance thresholds
bonus_tracker = []
streak_count = 0
penalty_points = 0

# Auxiliary tracking structures (some used, some not)
temporal_weights = {i: round(1 + 0.1 * (6 - i), 2) for i in range(7)}  # Decay factor
engagement_ranks = []
score_snapshot = None

base_multiplier = 1.5

for day in range(7):
    # Core metric: adjust login count by error rate impact
    adjusted_logins = daily_logins[day] * (1 - error_rates[day])

    # Update streak if above threshold
    if daily_logins[day] > 125:
        streak_count += 1
    else:
        streak_count = 0  # Reset if below threshold

    # Apply temporary bonus for search-dominant days
    search_heavy = feature_usage[day] == 'search'
    bonus_flag = False

    if search_heavy and adjusted_logins > 130:
        bonus_flag = True

    # Accumulate bonus only on eligible days
    if bonus_flag or streak_count >= 3:
        bonus_tracker.append(adjusted_logins * 0.1)

    # Irrelevant penalty accumulation (dead logic path)
    if error_rates[day] > 0.04:
        penalty_points += 1  # Never actually used in final computation

    # Distractor: update ranks but don't use until end (unused)
    engagement_ranks.append((day, adjusted_logins))

# Snapshot at midpoint (not used)
score_snapshot = engagement_ranks[3] if len(engagement_ranks) > 3 else None

# Secondary counter with red herring data
action_counter = defaultdict(int)
for action in feature_usage:
    action_counter[action] += 1

# Fake normalization (no effect)
total_actions = sum(action_counter.values())
normalized_profile = action_counter['profile'] / total_actions if total_actions else 0

# Real computation begins here — independent of prior distractors
def compute_performance(bonus_list):
    base_score = 50
    bonus_sum = sum(bonus_list)
    adjustment_factor = 1.2 if len(bonus_list) >= 4 else 0.9

    # Final score calculation
    raw_score = base_score + bonus_sum * adjustment_factor
    return int(round(raw_score))

# Critical execution point
final_score = compute_performance(bonus_tracker)

# Output result
print(f"Result: {final_score}")