from itertools import groupby

def analyze_performance(records):
    # Irrelevant preprocessing: convert all strings to uppercase (no effect on logic)
    processed = [r.upper() for r in records]
    
    # Semi-relevant transformation: extract numeric scores
    raw_scores = [int(r.split('_')[1]) for r in records]
    
    # Dead code path: unused function definition
    def unused_helper(x):
        return x * 2 + 1
    
    # Distractor computation: sorting but not assigning
    sorted(raw_scores)
    
    # Actual relevant state tracking
    score_counts = {}
    for s in raw_scores:
        score_counts[s] = score_counts.get(s, 0) + 1
    
    return score_counts

def create_rank_hierarchy(counts):
    # Apply lambda to filter high-frequency scores
    frequent = dict(filter(lambda item: item[1] > 1, counts.items()))
    
    # Misleading string manipulation
    keys_str = ''.join(map(str, frequent.keys()))
    shuffled = ''.join(sorted(keys_str, reverse=True))
    
    # Real logic: assign ranks based on score magnitude
    sorted_scores = sorted(frequent.keys(), reverse=True)
    rank_map = {score: idx + 1 for idx, score in enumerate(sorted_scores)}
    
    # Extra computation that doesn't affect result
    total_pairs = sum(1 for _ in groupby(sorted_scores))
    
    return rank_map

def process_rankings(ranks, multiplier):
    base_value = 10
    adjustment = 0
    
    # Nested loop with partial relevance
    for rank in ranks.values():
        for i in range(1, 4):
            if rank == i:
                adjustment += base_value // i
            else:
                # Unused branch with red herring calculation
                adjustment -= len('penalty')

    # Core formula: deterministic and critical
    final_score = adjustment * multiplier
    
    # Irrelevant string formatting
    log_entry = f"Final: {final_score:.2f}".strip()
    
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Input data with meaningful pattern
    performance_data = [
        'entry_85', 'entry_92', 'entry_85',
        'entry_96', 'entry_92', 'entry_96',
        'entry_77'
    ]
    
    # Unused variable - distraction
    max_entry = max(performance_data)
    
    # Trigger analysis chain
    frequency_map = analyze_performance(performance_data)
    
    # Intermediate mapping
    rank_system = create_rank_hierarchy(frequency_map)
    
    # Bonus depends on sum of digits in fixed seed (distractor logic)
    seed_text = '7341'
    bonus_sum = sum(int(d) for d in seed_text)
    bonus_multiplier = bonus_sum % 5 or 1
    
    # Key statement
    final_score = process_rankings(rank_system, bonus_multiplier)
    
    print(f"Result: {final_score}")