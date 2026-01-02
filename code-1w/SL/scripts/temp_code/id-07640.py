from collections import defaultdict

# Simulate system performance logs with event counting
event_log = ['start', 'compute', 'io_wait', 'compute', 'compute', 'error', 'io_wait', 'success']
event_counter = defaultdict(int)
for event in event_log:
    event_counter[event] += 1

# Extract key metrics
compute_count = event_counter['compute']
io_wait_count = event_counter['io_wait']
error_count = event_counter['error']

# Bonus conditions based on operational efficiency
bonus_flags = []
if compute_count > 2:
    bonus_flags.append('high_compute')
if io_wait_count < 3 and error_count == 1:
    bonus_flags.append('stable_io')

efficiency_ratings = [0.85, 0.91, 0.76, 0.94]
base_efficiency = sum(efficiency_ratings) / len(efficiency_ratings)

# Scoring logic
def calculate_performance(flags, ratings):
    score = base_efficiency * 100
    if 'high_compute' in flags:
        score += 15
    if 'stable_io' in flags:
        score += 10
    # Penalty for low consistency
    if max(ratings) - min(ratings) > 0.15:
        score -= 5
    return int(score)

final_score = calculate_performance(bonus_flags, efficiency_ratings)
Result: {final_score}