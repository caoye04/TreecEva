from collections import defaultdict, Counter

# Simulate student responses across multiple test sections
def analyze_responses(responses):
    counts = defaultdict(int)
    section_letters = ['A', 'B', 'C', 'D', 'E']
    temp_sum = 0

    for section in section_letters:
        if section in responses:
            counts[section] = len([r for r in responses[section] if r == 'correct'])
            temp_sum += sum([i for i in range(len(responses[section]))])  # irrelevant accumulation

    return dict(counts)

# Assess consistency across attempts
def compute_consistency(records):
    streak = 0
    max_streak = 0
    prev = None
    for record in records:
        if record == prev and record == 'correct':
            streak += 1
        else:
            streak = 1 if record == 'correct' else 0
        max_streak = max(max_streak, streak)
        prev = record

    # Fake normalization (not used later)
    normalized_peak = max_streak / (len(records) + 1e-5) if records else 0
    return max_streak  # only this matters

# Main evaluation logic
def evaluate_performance(dist, weights):
    raw_scores = {}
    penalty_adjustment = 0.0

    # Score each section with weighted contribution
    for key, values in dist.items():
        correct_count = values['correct']
        total_count = values['total']
        base_score = correct_count / total_count if total_count > 0 else 0
        weight = weights.get(key, 1.0)
        raw_scores[key] = base_score * weight

        # Irrelevant penalty tracking
        if correct_count < 5:
            penalty_adjustment -= 0.05 * (5 - correct_count)

    # Aggregate score
    aggregate = sum(raw_scores.values())

    # Apply fake difficulty modifier (unused)
    difficulty_factor = len([k for k, v in dist.items() if v['total'] > 10])
    adjusted_aggregate = aggregate * (1 + 0.1 * min(difficulty_factor, 3))

    # Final transformation using consistency
    global_consistency = compute_consistency(flatten_responses(dist))
    final_value = adjusted_aggregate * (1 + 0.05 * global_consistency)

    return int(round(final_value * 100))


def flatten_responses(dist):
    flat = []
    order = ['A', 'B', 'C', 'D', 'E']
    for sect in order:
        if sect in dist:
            flat.extend(['correct'] * dist[sect]['correct'])
            flat.extend(['incorrect'] * (dist[sect]['total'] - dist[sect]['correct']))
    return flat

# --- Input Data ---
response_data = {
    'A': ['correct', 'correct', 'incorrect', 'correct'],
    'B': ['correct', 'incorrect', 'correct', 'correct', 'correct'],
    'C': ['incorrect', 'correct', 'correct'],
    'D': ['correct', 'correct', 'correct', 'incorrect', 'correct', 'correct'],
    'E': ['correct', 'incorrect']
}

# Build distribution using Counter and defaultdict
raw_distribution = defaultdict(lambda: {'correct': 0, 'total': 0})
summary_counter = Counter()

for section, results in response_data.items():
    raw_distribution[section]['correct'] = len([r for r in results if r == 'correct'])
    raw_distribution[section]['total'] = len(results)
    summary_counter[section] += len(results)  # tracked but not critical

# Weighting scheme per section
section_weights = {
    'A': 1.0,
    'B': 1.2,
    'C': 1.1,
    'D': 1.3,
    'E': 1.0
}

# Analyze responses (uses defaultdict)
analysis_results = analyze_responses(response_data)

# Compute consistency metric
consistency_score = compute_consistency(flatten_responses(raw_distribution))

# Evaluate final performance
final_score = evaluate_performance(raw_distribution, section_weights)

# Print result
print(f"Result: {final_score}")