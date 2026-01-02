def analyze_combinations(elements):
    """ Calculate all unique pairs and return count (distractor function) """
    pair_count = 0
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            pair_count += 1
    return pair_count

# Simulated dataset of user engagement scores
engagement_data = [12, 15, 22, 34, 18, 27]

# Step 1: Filter high-engagement users using threshold logic
threshold = 20
high_engagement = set()
for score in engagement_data:
    if score >= threshold:
        high_engagement.add(score)

# Step 2: Generate auxiliary statistics (semi-relevant)
discount_factor = 0.9
adjusted_scores = [int(s * discount_factor) for s in engagement_data]

# Step 3: Compute rare events via set difference (distractor)
baseline_set = {10, 15, 20, 25, 30, 35}
rare_scores = high_engagement - baseline_set  # {22, 27, 34}

# Step 4: Use combinatorics to assess interaction potential (irrelevant)
interaction_potential = analyze_combinations(list(high_engagement))  # C(n,2)

# Step 5: Define rank set based on sorted order and apply integer division
sorted_high = sorted(high_engagement)
rank_set = set()
for idx, val in enumerate(sorted_high):
    rank_equivalent = (val // (idx + 1))  # Integer division with position
    rank_set.add(rank_equivalent)

# Step 6: Apply conditional bonus logic with rounding
base_multiplier = len(high_engagement) * 1.5
bonus_multiplier = round(base_multiplier) if sum(rank_set) > 50 else 5

# Step 7: Final scoring logic depends only on rank_set and bonus_multiplier
def calculate_final_score(ranks, bonus):
    raw_total = 0
    for r in ranks:
        if r % 2 == 0:  # Only even-ranked contributions
            raw_total += r * bonus
    return raw_total + len(ranks)

final_score = calculate_final_score(rank_set, bonus_multiplier)
print(f"Target result: {final_score}")