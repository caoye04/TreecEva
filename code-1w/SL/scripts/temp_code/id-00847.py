from collections import defaultdict

# Simulate a ranked voting system with weighted adjustments and noise filtering
def process_votes(raw_data, thresholds):
    vote_counts = defaultdict(int)
    noise_filter = defaultdict(list)
    magnitude_shift = 0

    for entry in raw_data:
        category = entry['cat']
        votes = entry['votes']
        quality = entry['qual']

        if quality < thresholds['min_quality']:
            noise_filter[category].append(votes)
            continue

        vote_counts[category] += votes

        # Irrelevant side computation (distractor)
        magnitude_shift += votes >> 2
        magnitude_shift -= len(noise_filter[category])

    # Normalize counts using a lambda (semi-relevant)
    total_votes = sum(vote_counts.values())
    normalized = {k: round(v / total_votes, 5) for k, v in vote_counts.items()}

    # Additional distraction: unused transformation
    decay_factor = 0.95
    decayed = list(map(lambda x: x * decay_factor, vote_counts.values()))

    return vote_counts, normalized


def calculate_total(rankings, bonus_weights):
    base_score = 0
    penalty_adjustment = 0

    # Real logic: score based on rankings and bonuses
    sorted_categories = sorted(rankings.keys(), key=lambda x: rankings[x], reverse=True)

    for i, cat in enumerate(sorted_categories):
        base_score += rankings[cat] * bonus_weights.get(cat, 1.0)
        penalty_adjustment += i ^ int(rankings[cat] % 7)  # Bitwise XOR distractor

    # Final score influenced only by base_score; penalty is calculated but not used
    final = int(base_score + 0.5)  # Round to nearest integer

    # Dead code path (never executed due to prior logic)
    if len(bonus_weights) > 100:
        fallback = sum(bonus_weights.values())
        final = fallback

    return final

# Input data
raw_input = [
    {'cat': 'A', 'votes': 450, 'qual': 0.78},
    {'cat': 'B', 'votes': 320, 'qual': 0.62},
    {'cat': 'A', 'votes': 180, 'qual': 0.85},
    {'cat': 'C', 'votes': 510, 'qual': 0.55},
    {'cat': 'B', 'votes': 290, 'qual': 0.91},
    {'cat': 'D', 'votes': 120, 'qual': 0.49},  # Below threshold
]

config = {
    'min_quality': 0.50,
    'max_entries': 100
}

# Process the votes
counted, norms = process_votes(raw_input, config)

# Assign weights arbitrarily
weights = {'A': 1.2, 'B': 1.5, 'C': 1.1}

# Key statement
final_score = calculate_total(counted, weights)

# Print result
print(f"Result: {final_score}")