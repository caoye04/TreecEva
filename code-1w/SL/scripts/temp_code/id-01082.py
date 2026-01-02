from collections import defaultdict
import itertools

# Simulate developer contribution analysis with noise and distractors
def analyze_developer_activity():
    # Core data
    commits = [5, 8, 12, 3, 7, 14, 9]
    review_effort = {'senior': 40, 'mid': 30, 'junior': 20}
    complexity_weights = (1.2, 0.8, 1.5, 1.0)

    # Distractor variables (not directly used in final result)
    temp_buffer = [0] * len(commits)
    for i in range(len(commits)):
        temp_buffer[i] = commits[i] * complexity_weights[i % 4] + 5

    # Actual relevant processing begins
    contributions = defaultdict(int)
    for idx, val in enumerate(commits):
        phase = 'early' if idx < 3 else 'late'
        contributions[phase] += val * complexity_weights[idx % 4]

    # Irrelevant transformation
    shifted = [(x >> 1) + (x << 1) for x in commits]
    avg_shift = sum(shifted) / len(shifted)

    # Another red herring: unused helper
    def compute_entropy(data):
        total = sum(data)
        return sum(-(x/total)*((x/total).__log__(2)) for x in data if x > 0)

    # Penalty system based on error rates (semi-relevant structure)
    error_rates = {"critical": 0.02, "major": 0.08, "minor": 0.15}
    penalty_map = {}
    base_penalty = 10
    for k, v in error_rates.items():
        penalty_map[k] = int(base_penalty * (v * 100))

    # Dead code path (never called)
    def legacy_calculate(*args):
        return sum(args) // len(args) if args else 0

    # Core logic hidden among distractions
    def calculate_rating(contribs, penalties):
        base = contribs['early'] * 0.6 + contribs['late'] * 1.4
        adjustment = penalties['minor'] - penalties['critical']
        if adjustment > 15:
            base *= 1.1
        else:
            base *= 0.9
        return int(base)

    # Key execution point
    final_score = calculate_rating(contributions, penalty_map)
    
    # Print required output
    print(f"Result: {final_score}")

    # Unused cleanup
    del temp_buffer, shifted
    return final_score

# Execute
analyze_developer_activity()