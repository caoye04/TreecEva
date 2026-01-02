def calculate_final_score(ranks, flags):
    base_score = sum(ranks)
    bonus_multiplier = 1.0
    
    # Irrelevant computation: process duplicate check (not used in final logic)
    seen = set()
    duplicates = set()
    for r in ranks:
        if r in seen:
            duplicates.add(r)
        seen.add(r)
    
    # Misleading flag analysis with dead-end branches
    critical_flag = False
    for flag in flags:
        if flag == "urgent" and len(ranks) > 3:
            critical_flag = True
        elif flag == "debug" and 0 in ranks:
            base_score -= 10
    
    # Real logic begins: filter high performers
    high_performers = {x for x in ranks if x >= 7}
    if len(high_performers) >= 2:
        bonus_multiplier += 0.5
    
    # Secondary condition using bitwise logic on flag pattern
    flag_code = 0
    for f in flags:
        flag_code ^= len(f)  # XOR length of each flag string
    
    if flag_code & 1:  # odd hash?
        bonus_multiplier += 0.2
    
    # Distractor: unused sorting attempt
    sorted_ranks_desc = sorted(ranks, reverse=True)
    median_offset = 0
    if len(sorted_ranks_desc) % 2 == 1:
        mid_idx = len(sorted_ranks_desc) // 2
        median_offset = sorted_ranks_desc[mid_idx] - 5

    # Actual score calculation
    adjustment = len(flags) - len(duplicates)  # uses duplicates but not seen
    base_score += adjustment * 2
    
    final_score = int(base_score * bonus_multiplier)
    return final_score

# Input setup
rank_set = [8, 6, 9, 4, 7]
performance_flags = ["stable", "optimized", "urgent"]

# Execution point
final_score = calculate_final_score(rank_set, performance_flags)
print(f"Result: {final_score}")