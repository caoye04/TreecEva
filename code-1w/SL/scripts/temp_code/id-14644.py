from itertools import groupby

def process_results(data):
    # Filter valid responses and compute scores
    valid_entries = [d for d in data if d['status'] == 'completed']
    
    # Group by module and calculate average correctness
    sorted_data = sorted(valid_entries, key=lambda x: x['module'])
    grouped = {k: list(g) for k, g in groupby(sorted_data, key=lambda x: x['module'])}
    
    # Compute bitwise-adjusted score per module
    module_scores = {}
    for mod, records in grouped.items():
        total_correct = sum(1 for r in records if r['correct'])
        base_score = total_correct / len(records)
        adjustment = len(records) & 7  # Bitwise AND to modulate score
        adjusted_score = base_score * (1 + adjustment / 10)
        module_scores[mod] = round(adjusted_score, 3)
    
    # Aggregate final score using string-based weighting scheme
    weights = {'A': 0.5, 'B': 1.0, 'C': 1.5}
    final = 0
    for m, s in module_scores.items():
        category = m.split('_')[0].upper()
        weight_key = category if category in weights else 'A'
        final += s * weights[weight_key]
    
    return int(final * 10)  # Scale and discretize

# Simulated assessment data
assessment_data = [
    {'module': 'A_intro', 'status': 'completed', 'correct': True},
    {'module': 'A_intro', 'status': 'completed', 'correct': False},
    {'module': 'A_intro', 'status': 'completed', 'correct': True},
    {'module': 'B_logic', 'status': 'completed', 'correct': True},
    {'module': 'B_logic', 'status': 'completed', 'correct': True},
    {'module': 'B_logic', 'status': 'skipped', 'correct': False},
    {'module': 'C_adv', 'status': 'completed', 'correct': False},
    {'module': 'C_adv', 'status': 'completed', 'correct': True},
    {'module': 'C_adv', 'status': 'completed', 'correct': True},
    {'module': 'C_adv', 'status': 'completed', 'correct': True}
]

final_score = process_results(assessment_data)
print(f"Result: {final_score}")