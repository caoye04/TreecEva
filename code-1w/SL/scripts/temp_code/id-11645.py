from collections import Counter

def calculate_final_score(ranks):
    base_score = 0
    multiplier = 1
    for rank, count in ranks.items():
        if rank in ['A', 'K', 'Q']:
            base_score += count * 10
        elif rank == 'J':
            base_score += count * 5
        elif rank.isdigit():
            base_score += count * int(rank)
    
    # Apply diminishing returns for high counts
    total_cards = sum(ranks.values())
    if total_cards > 10:
        multiplier = 0.9
    
    return int(base_score * multiplier)

# Simulate a card hand analysis scenario
hand = ['A', 'K', 'K', 'Q', 'J', 'J', '7', '7', '7', '3', '3']
risk_factor = 0.85  # Irrelevant distractor variable
rank_counts = Counter(hand)
bonus_award = 50     # Another irrelevant variable

final_score = calculate_final_score(rank_counts)
print(f"Result: {final_score}")