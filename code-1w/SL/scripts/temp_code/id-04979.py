from collections import defaultdict
import itertools

# Simulated health monitoring system with complex preprocessing

def analyze_risk_levels(data_stream):
    risk_counts = defaultdict(int)
    temp_flags = [False] * len(data_stream)
    cumulative_shift = 0

    for i, entry in enumerate(data_stream):
        if i % 3 == 0:
            temp_flags[i] = True
        base_risk = entry['value'] // 10
        adjusted_risk = (base_risk ^ entry['id']) & 7
        risk_counts[adjusted_risk] += 1
        
        # Red herring: complex bit manipulation with no real impact
        if adjusted_risk > 4:
            cumulative_shift += (entry['id'] << 2) ^ (i | 5)
        else:
            cumulative_shift -= (entry['id'] >> 1) & (i & 3)

    # Dead code path - never used later
    redundant_analysis = list(itertools.accumulate([v for v in risk_counts.values()]))
    
    # Meaningless transformation chain
    transformed = [x * 1.5 for x in risk_counts.values() if x % 2 == 0]
    normalized = sum(transformed) / (len(transformed) + 1) if transformed else 0
    
    return risk_counts, normalized, cumulative_shift


def compute_baseline_stability(indices):
    stability = 0
    decoy_buffer = []
    for i in indices:
        if i < 10:
            stability += i ** 2
        elif i < 20:
            stability -= i * 1.5
        else:
            stability += i % 7
        decoy_buffer.append(stability * 0.1)  # Unused buffer
    return stability  # Irrelevant to final result


def extract_critical_peaks(values):
    peaks = []
    for i in range(1, len(values)-1):
        if values[i] > values[i-1] and values[i] > values[i+1]:
            peaks.append(values[i])
    return peaks if len(peaks) > 0 else [0]


def validate_threshold_compliance(entry, rules):
    # Complex rule evaluation with short-circuiting
    id_check = (entry['id'] in rules['allowed_ids'] or entry['id'] % 2 == 1)
    value_check = (entry['value'] >= rules['min_val']) and (entry['value'] <= rules['max_val'])
    flag_check = entry.get('flag', True) or entry['id'] not in rules['sensitive_ids']
    
    # Distractor computation
    compliance_entropy = 0
    for k in rules:
        if isinstance(rules[k], list):
            compliance_entropy += len(rules[k]) * 0.3
    
    return id_check and value_check and flag_check


def process_metrics(raw_data, thresholds):
    # Key processing pipeline
    filtered_data = []
    debug_log = []
    total_weight = 0.0
    
    for item in raw_data:
        # Conditional filtering based on multiple criteria
        if item['value'] < 0:
            continue
            
        compliance = validate_threshold_compliance(item, thresholds)
        
        if not compliance:
            debug_log.append(f"Rejected: {item['id']}")
            continue
            
        # Weighted contribution calculation
        weight = 1.0
        if item['id'] in thresholds['bonus_ids']:
            weight *= 1.75
        if item['value'] > thresholds['priority_threshold']:
            weight *= 2.0
            
        # Accumulate only compliant entries
        filtered_data.append({**item, 'weight': weight})
        total_weight += weight
    
    # Real computation: weighted average of squared values
    weighted_sum = sum((d['value'] ** 2) * d['weight'] for d in filtered_data)
    
    # Secondary metric: count of high-id entries
    high_id_count = sum(1 for d in filtered_data if d['id'] > 50)
    
    # Final score formula - this is the actual answer
    base_score = weighted_sum / total_weight if total_weight > 0 else 0
    penalty = high_id_count * 15
    final_score = base_score - penalty
    
    # Multiple irrelevant variables below
    auxiliary_metric = compute_baseline_stability([d['id'] for d in filtered_data])
    peak_values = extract_critical_peaks([d['value'] for d in raw_data])
    risk_profile, norm_val, shift_val = analyze_risk_levels(raw_data)
    
    # Decoy output variables
    summary_stats = {
        'aux': auxiliary_metric,
        'peaks': peak_values,
        'risk': dict(risk_profile),
        'norm': norm_val,
        'shift': shift_val
    }
    
    # ONLY final_score is printed and matters
    return final_score

# Main execution block
if __name__ == '__main__':
    # Input data setup
    health_data = [
        {'id': 23, 'value': 45, 'flag': True},
        {'id': 67, 'value': 88, 'flag': False},
        {'id': 12, 'value': 34, 'flag': True},
        {'id': 89, 'value': 92, 'flag': True},
        {'id': 45, 'value': 67, 'flag': False},
        {'id': 34, 'value': -5, 'flag': True},  # Will be filtered
        {'id': 78, 'value': 73, 'flag': True},
        {'id': 56, 'value': 41, 'flag': False}
    ]
    
    threshold_map = {
        'allowed_ids': [23, 45, 67],
        'min_val': 30,
        'max_val': 100,
        'sensitive_ids': [89, 56],
        'bonus_ids': [23, 78],
        'priority_threshold': 70
    }
    
    # Execute main logic
    final_score = process_metrics(health_data, threshold_map)
    print(f"Result: {final_score}")