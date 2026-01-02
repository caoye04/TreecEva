from itertools import combinations, cycle

# System for ranking engineering candidates based on multi-round evaluations
def evaluate_round(score, round_num, penalty_rate=0.1):
    adjusted = score * (1 - penalty_rate * round_num)
    return int(adjusted) if adjusted > 50 else 50

# Irrelevant helper - simulates test duration analysis
def analyze_duration(times):
    total = sum(times)
    avg = total / len(times)
    peaks = [t for t in times if t > avg]
    return len(peaks)  # Unused in final logic

def generate_feedback(code_samples):
    feedback = {}
    for i, code in enumerate(code_samples):
        lines = len(code.split('\n'))
        complexity = sum(1 for c in code if c in ['{', '}', '[', ']'])
        feedback[i] = {'lines': lines, 'complexity': complexity}
    return feedback  # Dead return - not used

def calculate_entropy(sequence):
    from math import log
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    total = len(sequence)
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 3)  # Distractor computation

def filter_candidates_by_tier(candidates, tier_map, min_tier=2):
    filtered = []
    for cid in candidates:
        if tier_map.get(cid, 0) >= min_tier:
            filtered.append(cid)
    return filtered  # Used, but tier logic partially irrelevant

def compute_combinations_skill(skill_levels):
    # Count how many pairs can collaborate above threshold
    count = 0
    for a, b in combinations(skill_levels, 2):
        if (a + b) > 150:
            count += 1
    return count  # Minor role, distracts from main flow

def process_ranking(candidates, boost_factor):
    base_scores = {cid: (cid * 7) % 93 for cid in candidates}  # Deterministic score gen
    
    # Apply performance rounds with decay
    round_1 = {cid: evaluate_round(base_scores[cid], 1) for cid in candidates}
    round_2 = {cid: evaluate_round(round_1[cid], 2) for cid in candidates}
    round_3 = {cid: evaluate_round(round_2[cid], 3) for cid in candidates}
    
    # Boost high-tier candidates
    tier_map = {cid: (cid % 4) + 1 for cid in candidates}
    boosted_scores = {}
    for cid in candidates:
        raw = round_3[cid]
        tier = tier_map[cid]
        boost = boost_factor if tier >= 3 else 0
        boosted_scores[cid] = raw + boost
    
    # Aggregate and normalize
    total = sum(boosted_scores.values())
    normalized = {cid: round(val / total * 1000) for cid, val in boosted_scores.items()}
    
    # Final adjustment: apply combinatorial synergy bonus
    synergy_pool = [normalized[cid] for cid in candidates if tier_map[cid] >= 3]
    combo_count = compute_combinations_skill(synergy_pool)
    bonus_per_combo = 2
    total_bonus = combo_count * bonus_per_combo
    
    # Critical line: final score derived here
    final_score = total_bonus + len(normalized) * 5
    
    # Decoy operations below
    _ = calculate_entropy(list(normalized.keys()))
    _ = list(combinations(synergy_pool, 2))
    _ = analyze_duration([120, 150, 180, 200])
    
    return final_score

# Setup data
candidate_ids = list(range(10, 20))  # 10 candidates
skill_data = ['def sort(arr):\n  return sorted(arr)', 'class Node:\n  def __init__(self):\n    pass']
times_spent = [125, 140, 160, 130, 155, 170, 120, 135, 145, 165]

# Irrelevant pre-processing
feedback_report = generate_feedback(skill_data)
duration_outliers = analyze_duration(times_spent)

# Active filtering
tier_assignments = {cid: (cid * 3) % 4 + 1 for cid in candidate_ids}
shortlist = filter_candidates_by_tier(candidate_ids, tier_assignments, min_tier=1)

# Key execution point
boost_factor = 12
final_score = process_ranking(shortlist, boost_factor)

print(f"Result: {final_score}")