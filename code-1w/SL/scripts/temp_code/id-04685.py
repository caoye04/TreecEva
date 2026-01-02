def analyze_purity_levels(samples, threshold):
    # Irrelevant transformation: normalize names (distractor)
    sample_labels = [s['id'].upper().strip() for s in samples]
    normalized_labels = set()
    for label in sample_labels:
        if 'X' in label:
            normalized_labels.add(label.replace('X', 'Z'))  # Red herring
        else:
            normalized_labels.add(label)

    # Decoy analysis: computes unused metric
    def compute_turbidity_index(s):
        return sum(ord(c) for c in s['id']) % 100  # Not used in final logic

    turbidity_map = {s['id']: compute_turbidity_index(s) for s in samples}

    # Actual relevant logic begins here
    valid_samples = []
    cumulative_impurity = 0
    for s in samples:
        if s['status'] != 'quarantined':
            reading = s['purity']
            adjusted_reading = reading * 0.95  # Calibration factor
            if adjusted_reading < threshold:
                cumulative_impurity += (threshold - adjusted_reading)
            else:
                valid_samples.append(adjusted_reading)
    
    # Secondary filter based on string pattern in id (uses string method)
    high_priority_ids = [s['id'] for s in samples if s['id'].endswith('HP')]
    priority_bonus = len(high_priority_ids) * 10

    # Complex conditional with short-circuit logic (Boolean Logic + Control Flow)
    base_score = len(valid_samples) * 100
    if cumulative_impurity > 0 and (threshold > 70 or True):  # Short-circuit trap
        adjustment_factor = 0.8
    elif len(valid_samples) == 0:
        adjustment_factor = 0.1
    else:
        adjustment_factor = 1.0

    # Final score calculation (target answer)
    filtration_score = int((base_score - cumulative_impurity * 2 + priority_bonus) * adjustment_factor)

    # Dead code path (unused function)
    def log_final_audit():
        return {"entries": [], "status": "simulated"}
    
    # Unused data structure manipulation (set operations as distractor)
    all_contaminants = set(['lead', 'mercury'])
    detected_in_run = set(['arsenic'])
    cross_detected = all_contaminants & detected_in_run  # Always empty

    return filtration_score

# Input data
water_samples = [
    {'id': 'A001HP', 'purity': 88, 'status': 'active'},
    {'id': 'B002', 'purity': 76, 'status': 'active'},
    {'id': 'C003X', 'purity': 65, 'status': 'quarantined'},  # Excluded due to status
    {'id': 'D004HP', 'purity': 92, 'status': 'active'},
    {'id': 'E005', 'purity': 54, 'status': 'active'},  # Below threshold after calibration
    {'id': 'F006HP', 'purity': 85, 'status': 'active'}
]
contamination_threshold = 70

# Execution point
filtration_score = analyze_purity_levels(water_samples, contamination_threshold)
print(f"Result: {filtration_score}")