def analyze_sentiment(text_blocks):
    """ Irrelevant function: analyzes sentiment but not used in final computation """
    scores = []
    for block in text_blocks:
        score = 0
        words = block.lower().split()
        for word in words:
            if word in ['excellent', 'great', 'good']:
                score += 1
            elif word in ['poor', 'bad', 'terrible']:
                score -= 1
        scores.append(score)
    return scores


def compute_entropy(data):
    """ Misleading function: computes entropy but unused """
    import math
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy

# Irrelevant data structures
text_corpus = [
    "The model performed poorly on edge cases",
    "Great improvement in reasoning tasks",
    "Good overall structure but bad formatting"
]

sentiment_analysis = analyze_sentiment(text_corpus)
entropy_value = compute_entropy([3, 1, 4, 1, 5, 9, 2, 6])

# Core logic begins here — disguised among distractors
feedback_levels = [5, 3, 4, 2, 5]
weights = [0.1, 0.2, 0.3, 0.15, 0.25]

# Distractor variables
scaling_factor = 1.5
offset_adjustment = -0.7
intermediate_results = []

# Simulated normalization (unused path)
normalized_levels = [level / max(feedback_levels) for level in feedback_levels]

# Real computation hidden in complex-looking context
def apply_weighting(levels, coeffs):
    """ Correctly applies weighted sum """
    result = 0
    for i, (lvl, w) in enumerate(zip(levels, coeffs)):
        temp_val = lvl * w
        intermediate_results.append(temp_val)
        result += temp_val
    return result

# Decoy transformation
transformed = [x**2 for x in feedback_levels if x >= 4]

# Another red herring: string-based encoding of weights
weight_labels = ['low', 'medium', 'high', 'mid_high', 'very_high']
encoded_map = {w: label for w, label in zip(weights, weight_labels)}

# Key function that actually determines the answer
def aggregate_performance(ratings, importance_weights):
    # Nested conditional with irrelevant branch
    if sum(ratings) > 10:
        adjusted = [r * 1.1 for r in ratings]
    else:
        adjusted = ratings  # Not triggered

    total = 0.0
    for idx, (rating, weight) in enumerate(zip(adjusted, importance_weights)):
        # Additional distraction: unused intermediate calculation
        squared_contribution = rating ** 2 * weight
        total += rating * weight

    # Extra operations to obscure logic
    total = round(total, 6)
    
    # Final adjustment based on parity check (always even in this case)
    if len(ratings) % 2 == 0:
        total += 0.0  # No-op
    else:
        total -= 0.1  # Not taken

    return total

# Unused recursive helper — dead code path
def recursive_sum(lst, n):
    if n <= 0:
        return 0
    return lst[n-1] + recursive_sum(lst, n-1)

# Actual execution
raw_aggregate = apply_weighting(feedback_levels, weights)
final_score = aggregate_performance(feedback_levels, weights)

# Output must be printed exactly like this
print(f"Target result: {final_score}")