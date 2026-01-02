from collections import defaultdict

# Simulate employee performance evaluation with multiple metrics and noise filtering
def analyze_performance(raw_evaluations):
    scores = defaultdict(int)
    penalties = defaultdict(float)
    temp_buffer = []

    for record in raw_evaluations:
        emp_id = record['id']
        quality = record['quality']
        timeliness = record['timeliness']
        teamwork = record.get('teamwork', 5)

        # Core scoring logic
        base_score = (quality * 0.4) + (timeliness * 0.3) + (teamwork * 0.2)
        adjustment = abs(quality - timeliness) * 0.1
        
        if quality >= 8 and timeliness >= 7:
            base_score += 1.5  # bonus for high performers

        scores[emp_id] += base_score - adjustment

        # Distractor: penalty logic not actually used
        late_count = record.get('late_days', 0)
        if late_count > 5:
            penalties[emp_id] = late_count * 0.2

        # Red herring accumulation
        temp_buffer.append(late_count * 0.01)

    # Unused transformation
    adjusted_penalties = {k: v * 1.1 for k, v in penalties.items()}
    smoothed_buffer = sum([x * 0.9 for x in temp_buffer])  # never used

    return scores


def preprocess_records(employee_list):
    processed = []
    id_map = {}
    
    for idx, e in enumerate(employee_list):
        # Create new structured record
        clean_id = e['employee_id'].strip().upper()
        perf_data = {
            'id': clean_id,
            'quality': int(e['q_score']),
            'timeliness': e['t_score'],
        }
        
        # Conditional field injection (some misleading)
        if 'team' in e:
            perf_data['teamwork'] = min(len(e['team']) * 2, 10)
        
        if 'absences' in e:
            perf_data['late_days'] = max(e['absences'] - 2, 0)
        
        processed.append(perf_data)
        id_map[clean_id] = idx * 0.001  # unused tracking
    
    # Dummy analytics
    id_entropy = sum(id_map.values()) * 100  # irrelevant
    return processed


def compute_final_score(score_dict):
    values = list(score_dict.values())
    
    # Apply nonlinear transformation
    boosted = [v ** 1.1 for v in values if v > 6.0]
    suppressed = [v * 0.9 for v in values if v <= 6.0]
    
    combined = boosted + suppressed
    
    # Final aggregation
    raw_mean = sum(combined) / len(combined) if combined else 0
    
    # Normalize to 100-point scale
    final = int(round(raw_mean * 10))
    
    # Dead code branch (never executed due to data)
    if raw_mean < 0:
        final -= 5
        anomaly_flag = True
    else:
        anomaly_flag = False  # unused
    
    return final

# Input data
employees = [
    {'employee_id': ' E101 ', 'q_score': '8', 't_score': 7, 'team': 'dev'},
    {'employee_id': 'e102', 'q_score': '9', 't_score': 8},
    {'employee_id': 'e103', 'q_score': '6', 't_score': 7, 'absences': 4},
    {'employee_id': 'e104', 'q_score': '7', 't_score': 6, 'team': 'ops', 'absences': 6},
    {'employee_id': 'e105', 'q_score': '5', 't_score': 5}
]

# Execution pipeline
processed_data = preprocess_records(employees)
analyzed_scores = analyze_performance(processed_data)
final_score = compute_final_score(analyzed_scores)

print(f"Result: {final_score}")