from itertools import combinations

def evaluate_response_time(base_time, load_factor):
    return base_time * (1.1 ** load_factor)

# Simulate system benchmark under varying loads
load_levels = [1, 2, 3, 4]
base_timing = 100
response_times = list(map(lambda x: evaluate_response_time(base_timing, x), load_levels))

# Irrelevant metric (distractor)
peak_memory_usage = sum([t * 0.8 for t in response_times])

# Generate performance pairs for comparison
performance_pairs = list(combinations(response_times[:3], 2))
bonus_points = 0
for a, b in performance_pairs:
    if a < b * 0.95:  # 5% improvement threshold
        bonus_points += 5

stability_penalty = len(response_times) * 2
raw_score = int(sum(response_times))

# Final scoring logic
def calculate_performance(data):
    return raw_score + bonus_points - stability_penalty

final_score = calculate_performance(response_times)
print(f"Result: {final_score}")