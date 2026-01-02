import itertools

# Domain: Employee performance review simulation with cognitive bias distractors

def simulate_review_cycle():
    # Core data
    base_ratings = [3.2, 4.1, 2.9, 3.8, 4.5]
    review_weights = [0.1, 0.2, 0.3, 0.25, 0.15]
    adjustment_factor = 1.07

    # Irrelevant distraction: Years of service correlation (unused)
    employee_tenure = [3, 7, 1, 5, 9]
    tenure_bonus = [min(0.5, years * 0.05) for years in employee_tenure]

    # Distractor: Simulated mood effects (never applied)
    mood_impact = list(itertools.accumulate([0.1, -0.05, 0.08, -0.12, 0.03], lambda x, y: (x + y) % 0.5))
    hypothetical_mood_adjusted = [r + m for r, m in zip(base_ratings, mood_impact)]

    # Red herring function: Unused peer comparison logic
    def calculate_peer_gap(ratings):
        sorted_ratings = sorted(ratings, reverse=True)
        return [sorted_ratings.index(r) for r in ratings]  # Rank positions

    peer_ranks = calculate_peer_gap(base_ratings)  # Computed but unused

    # Real processing begins here
    weighted_sum = sum(rating * weight for rating, weight in zip(base_ratings, review_weights))
    adjusted_average = weighted_sum * adjustment_factor

    # Distraction: Formatting for report (irrelevant to final score)
    formatted_report = f"Performance Index: {adjusted_average:.2f}"
    validation_checksum = sum(ord(c) for c in formatted_report[:10]) % 100

    # Complex decoy: Multi-stage normalization (unused path)
    normalized_ratings = []
    max_rating = max(base_ratings)
    for r in base_ratings:
        if r > 3.5:
            normalized_ratings.append(r / max_rating * 5.0)
        else:
            normalized_ratings.append(r / max_rating * 4.0)
    
    # Fake aggregation
    quadratic_penalty = sum((r - 3.0)**2 for r in base_ratings) / 10.0
    theoretical_index = adjusted_average - quadratic_penalty  # Looks important, unused

    # Critical data transformation
    feedback_sequence = [(i, round(r * 10)) for i, r in enumerate(base_ratings)]
    
    # Actual answer computation path
    def evaluate_performance(feedback):
        # Uses list comprehension and itertools
        digits = [digit for _, score in feedback for digit in str(score)]
        grouped = [list(g) for k, g in itertools.groupby(sorted(digits))]
        frequency_score = sum(len(g) * int(g[0]) for g in grouped if len(g) > 1)

        # Real adjustment
        base_component = adjusted_average * 100  # Scale up
        noise_offset = validation_checksum * 0.01  # Tiny irrelevant offset
        
        # Final computation - only this matters
        final_component = frequency_score + base_component - noise_offset
        return int(round(final_component))

    final_score = evaluate_performance(feedback_sequence)
    print(f"Result: {final_score}")

    # Dead code: Future phase placeholder
    def forecast_growth(scores):
        return [s * 1.1 for s in scores]

    return final_score

if __name__ == "__main__":
    simulate_review_cycle()