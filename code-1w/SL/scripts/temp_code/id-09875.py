from itertools import combinations

def evaluate_performance(record):
    base_score = 0
    penalty_adjustment = 0
    for entry in record:
        if entry['errors'] == 0:
            base_score += 10
        elif entry['errors'] < 5:
            base_score += 5
        else:
            penalty_adjustment -= 2  
    return base_score + penalty_adjustment

def generate_metrics(data):
    # Irrelevant metric computation (distractor)
    avg_time = sum(d['time'] for d in data) / len(data)
    max_concurrent = max(len(list(combinations(data, r))) for r in [2]) if len(data) >= 2 else 0
    return avg_time

def calculate_ranking(participants):
    raw_scores = []
    temp_offsets = []
    
    for p in participants:
        score = evaluate_performance(p['log'])
        multiplier = 1.5 if p['tier'] == 'advanced' else 1.0
        adjusted = score * multiplier
        raw_scores.append(adjusted)
        
        # Distractor: complex but unused calculation
        buffer_zone = (adjusted ** 2) // (len(p['log']) + 1)
        temp_offsets.append(buffer_zone)

    # Real logic: find highest adjusted score under constraint
    filtered_candidates = [s for s in raw_scores if s > 15]
    
    # Secondary filter based on auxiliary condition (semi-relevant)
    qualified = []
    for i, p in enumerate(participants):
        if raw_scores[i] in filtered_candidates and p['active']:
            qualified.append(raw_scores[i])
    
    # Final decision logic
    if not qualified:
        final_rank_score = 0
    else:
        peak = max(qualified)
        count_bonus = len([q for q in qualified if q >= peak * 0.9])
        final_rank_score = peak + (count_bonus * 0.5)
    
    # Normalization step (part of actual logic)
    normalization_factor = 1.2 if len(qualified) > 2 else 1.0
    final_rank_score /= normalization_factor
    
    # Unused debugging trace (distractor)
    debug_snapshot = [round(x, 2) for x in temp_offsets if x > 5]
    
    return round(final_rank_score, 3)

# Main execution
competitors = [
    {
        'name': 'Alice',
        'tier': 'advanced',
        'active': True,
        'log': [
            {'errors': 0, 'time': 120},
            {'errors': 0, 'time': 110},
            {'errors': 3, 'time': 130}
        ]
    },
    {
        'name': 'Bob',
        'tier': 'intermediate',
        'active': True,
        'log': [
            {'errors': 0, 'time': 140},
            {'errors': 6, 'time': 150},
            {'errors': 2, 'time': 135}
        ]
    },
    {
        'name': 'Charlie',
        'tier': 'advanced',
        'active': False,  # Will be filtered out due to inactive
        'log': [
            {'errors': 0, 'time': 100},
            {'errors': 0, 'time': 95}
        ]
    }
]

# Trigger key computation
final_score = calculate_ranking(competitors)
print(f"Target result: {final_score}")