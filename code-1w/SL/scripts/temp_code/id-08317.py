from collections import defaultdict

def calculate_final_score(ranks, multiplier):
    rank_counts = defaultdict(int)
    for rank in ranks:
        rank_counts[rank] += 1
    
    # Compute weighted sum based on rank frequency and position
    raw_score = sum(rank * freq for rank, freq in rank_counts.items())
    bonus = len(rank_counts) * 2 if len(ranks) > 5 else 1
    adjustment = 0.5 if any(freq > 2 for freq in rank_counts.values()) else -1.0
    
    temp_result = raw_score * multiplier + bonus
    final_value = temp_result + adjustment
    return final_value

# Simulation data
base_multiplier = 3
player_ranks = [1, 2, 2, 3, 2, 4]
extra_buffer = [99, 88, 77]  # irrelevant list
unused_flag = True  # distraction variable

rank_data = player_ranks
final_score = calculate_final_score(rank_data, base_multiplier)
print(f"Target result: {final_score}")