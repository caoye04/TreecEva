from collections import defaultdict

# Simulate user engagement scores across different content categories
def calculate_category_averages(engagement_logs):
    category_totals = defaultdict(float)
    category_counts = defaultdict(int)
    
    for entry in engagement_logs:
        cat = entry['category']
        score = entry['score']
        category_totals[cat] += score
        category_counts[cat] += 1
    
    averages = {}
    for cat in category_totals:
        averages[cat] = category_totals[cat] / category_counts[cat]
    return averages

def calculate_final_score(ranks, multiplier):
    base = sum(ranks)
    adjustment = len(ranks) * 0.5
    return int((base + adjustment) * multiplier)

def main():
    # Log data from user interactions (irrelevant to final score but adds context)
    logs = [
        {'user': 'u1', 'category': 'tech', 'score': 4.5},
        {'user': 'u2', 'category': 'design', 'score': 3.8},
        {'user': 'u3', 'category': 'tech', 'score': 4.2},
        {'user': 'u4', 'category': 'lifestyle', 'score': 3.9},
        {'user': 'u5', 'category': 'design', 'score': 4.0}
    ]
    
    # Calculate averages (not used in final score - minor distraction)
    avg_scores = calculate_category_averages(logs)
    
    # Core data for final score calculation
    rank_data = [3, 1, 4, 1, 5]
    bonus_multiplier = 2.0
    initial_offset = 10
    
    # Key computation
    final_score = calculate_final_score(rank_data, bonus_multiplier)
    
    # Print result as required
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()