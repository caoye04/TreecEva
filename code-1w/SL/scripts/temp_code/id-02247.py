from collections import defaultdict
from itertools import combinations

# Simulate a competitive coding tournament with complex scoring logic

def preprocess_ranks(raw_scores):
    rank_map = defaultdict(int)
    for idx, score in enumerate(sorted(raw_scores, reverse=True)):
        rank_map[score] = idx + 1
    return rank_map

# Irrelevant helper function – dead code path (distractor)
def calculate_entropy(data):
    from math import log
    freq = defaultdict(float)
    total = len(data)
    for d in data:
        freq[d] += 1
    entropy = 0.0
    for f in freq.values():
        p = f / total
        entropy -= p * log(p, 2)
    return entropy

# Misleading intermediate transformation (red herring)
def apply_noise(seq, factor=0.1):
    import random
    random.seed(42)
    return [x + random.uniform(-factor, factor) for x in seq]

# Core logic disguised among distractors
def validate_sequence(seq):
    if len(seq) < 3:
        return False
    for i in range(2, len(seq)):
        if seq[i] != seq[i-1] + seq[i-2]:
            return False
    return True

# Another decoy function that's never called
def generate_fibonacci(n):
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def compute_weighted_sum(entries, weights=None):
    # Heavily nested logic with partial relevance
    if weights is None:
        weights = [1 for _ in entries]
    temp_result = 0
    for i, entry in enumerate(entries):
        adjustment = 1
        if i % 2 == 0 and entry > 50:
            adjustment = 1.5
        elif entry < 10:
            adjustment = 0.5
        temp_result += entry * weights[i] * adjustment
    return int(temp_result)

# Key function buried in complexity
def evaluate_performance(ranks, extras):
    base_score = 0
    multiplier = 1
    
    # Real logic starts here — non-obvious accumulation
    sorted_ranks = sorted(ranks.items(), key=lambda x: x[1])
    for i, (player, rank) in enumerate(sorted_ranks):
        if rank <= 3:
            base_score += 100 - (rank * 10)
            if player.startswith('A'):
                multiplier += 0.2
        elif rank <= 6:
            base_score += 50 - (rank * 5)

    # Hidden conditional using bitwise check on sum
    total_rank_sum = sum(r[1] for r in sorted_ranks)
    if total_rank_sum & 1:  # if odd
        base_score -= 15

    # Use of list comprehension with filtering (Python idiom)
    bonus_list = [b for b in extras if b > 0]
    if len(bonus_list) >= 3:
        base_score += sum(bonus_list[:3])

    # Final twist: modular arithmetic condition
    if base_score % 7 == 0:
        base_score = base_score // 7 * 8  # slight boost if divisible by 7
    else:
        base_score += (base_score % 7)

    # Critical assignment
    final_score = int(base_score * multiplier)
    return final_score

# Main execution block — realistic setup
if __name__ == "__main__":
    # Actual input data
    raw_scores = [88, 95, 76, 92, 83, 71]
    bonuses = [12, -5, 23, 8, 15, -10, 30]

    # Distractor variables
    noise_scores = apply_noise(raw_scores, 0.5)
    entropy_value = calculate_entropy(raw_scores)
    validation_test = [1, 2, 3, 5, 8]
    is_valid = validate_sequence(validation_test)

    # Relevant computation chain
    rankings = preprocess_ranks(raw_scores)
    adjusted_bonuses = [b if b % 2 == 0 else b + 1 for b in bonuses]  # minor transformation

    # Key execution point
    final_score = evaluate_performance(rankings, adjusted_bonuses)

    # Output result as required
    print(f"Result: {final_score}")