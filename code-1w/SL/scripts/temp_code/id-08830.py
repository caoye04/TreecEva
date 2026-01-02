from itertools import combinations

def evaluate_hand(cards):
    # Count occurrences of each rank
    ranks = [card[:-1] for card in cards]
    rank_count = {r: ranks.count(r) for r in set(ranks)}
    
    # Calculate base score from pairs (each pair adds 2)
    pairs = sum(1 for count in rank_count.values() if count == 2)
    base_score = pairs * 2
    
    # Bonus for flush (all same suit)
    suits = [card[-1] for card in cards]
    is_flush = len(set(suits)) == 1
    flush_bonus = 5 if is_flush else 0
    
    # Extra points for specific high cards in flush
    high_cards_in_flush = sum(1 for r in ranks if r in ['A', 'K', 'Q']) if is_flush else 0
    
    # Use combinations to check for sequential ranks (straight-like pattern)
    rank_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    sorted_ranks = sorted([rank_values[r] for r in ranks])
    is_consecutive = all(sorted_ranks[i+1] - sorted_ranks[i] == 1 for i in range(len(sorted_ranks)-1))
    straight_bonus = 8 if is_consecutive else 0
    
    # Compute total hand score
    total_hand_score = base_score + flush_bonus + straight_bonus + high_cards_in_flush
    return total_hand_score

# Irrelevant utility function (minor distraction)
def format_card(card):
    return card.upper().strip()

# Main evaluation
player_hands = {
    'Alice': ['10H', 'JH', 'QH', 'KH', 'AH'],  # Royal flush in hearts
    'Bob': ['2C', '3D', '4S', '5H', '6C']       # Straight (not flush)
}

hand_a = player_hands['Alice']
score_a = evaluate_hand(hand_a)

hand_b = player_hands['Bob']
score_b = evaluate_hand(hand_b)

# Aggregation logic
total_combined_score = score_a + score_b
adjustment_factor = 0.5
normalized_score = total_combined_score * adjustment_factor

# Final scoring with conditional bonus
def calculate_final_score():
    if score_a > score_b:
        return int(normalized_score + 10)
    else:
        return int(normalized_score)

final_score = calculate_final_score()
print(f"Result: {final_score}")