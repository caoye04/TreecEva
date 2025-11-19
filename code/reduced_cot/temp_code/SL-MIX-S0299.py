from collections import defaultdict

def process_textile_inspections():
    batch_rolls = ['F201', 'G405', 'H709', 'J113']
    weight_scores = {'F201': 85, 'G405': 92, 'H709': 78, 'J113': 88}
    dimension_scores = {'F201': 90, 'G405': 87, 'H709': 95, 'J113': 82}
    defect_counts = {'F201': 3, 'G405': 1, 'H709': 5, 'J113': 2}
    
    # Initialize state machine for tracking inspection phases
    inspection_phases = defaultdict(str)
    cumulative_ratings = defaultdict(int)
    verified_score_count = 0
    
    # Phase 1: Weight validation
    for roll_id in batch_rolls:
        if weight_scores[roll_id] >= 80:
            inspection_phases[roll_id] = 'WEIGHT_PASS'
            cumulative_ratings[roll_id] += weight_scores[roll_id] % 17
        else:
            inspection_phases[roll_id] = 'WEIGHT_FAIL'
    
    # Phase 2: Dimension assessment
    for roll_id in batch_rolls:
        if inspection_phases[roll_id].endswith('PASS'):
            adjusted_dimension = (dimension_scores[roll_id] * 2) % 19
            cumulative_ratings[roll_id] += adjusted_dimension
            inspection_phases[roll_id] += '_DIM_PASS'
        else:
            inspection_phases[roll_id] += '_DIM_SKIP'
    
    # Phase 3: Defect analysis
    for roll_id in batch_rolls:
        if 'DIM_PASS' in inspection_phases[roll_id]:
            defect_penalty = defect_counts[roll_id] * 3
            cumulative_ratings[roll_id] = (cumulative_ratings[roll_id] - defect_penalty) % 13
            inspection_phases[roll_id] += '_DEFECT_ANALYZED'
        
        # Verification hash check
        verification_hash = hash(roll_id) % 7
        if cumulative_ratings[roll_id] > verification_hash:
            verified_score_count += 1
    
    return verified_score_count

verified_score_count = process_textile_inspections()
print(f"Result: {verified_score_count}")