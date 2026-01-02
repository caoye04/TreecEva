from collections import defaultdict

def process_entries(entries):
    counts = defaultdict(int)
    totals = 0
    temp_sum = 0  # Irrelevant accumulator
    
    for entry in entries:
        category = entry['type'].lower().strip()
        value = entry['value']
        
        if 'test' in category:
            counts['test'] += 1
            totals += value
        elif 'trial' in category:
            counts['trial'] += 1
            temp_sum += value * 0.5  # Semi-relevant but not used later
        else:
            counts['other'] += 1

    return counts, totals

def analyze_pattern(sequence):
    pattern_count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i + 1]:
            pattern_count += 1
    return pattern_count

def calculate_performance(data):
    raw_entries = data.get('entries', [])
    seq = data.get('sequence', [])
    
    # Primary computation branch
    metadata_counts, base_total = process_entries(raw_entries)
    growth_trend = analyze_pattern(seq)
    
    adjustment_factor = 1.0
    if metadata_counts['test'] > metadata_counts['trial']:
        adjustment_factor = 1.2
    elif metadata_counts['test'] == metadata_counts['trial']:
        adjustment_factor = 1.1

    # Distractor block: complex but unused calculation
    outlier_check = [x['value'] for x in raw_entries if x['value'] > 100]
    suspicious_flag = False
    for val in outlier_check:
        if val % 7 == 0:
            suspicious_flag = True
            break

    # Another red herring: string processing with no effect
    labels = [entry['label'] for entry in raw_entries]
    combined_label = ''.join(labels).upper()
    label_stats = {}
    for char in combined_label:
        if char.isalpha():
            label_stats[char] = label_stats.get(char, 0) + 1

    entropy_sim = 0.0
    for k, v in label_stats.items():
        entropy_sim += v * 0.01

    # Core logic with dependency on prior steps
    base_metric = base_total * adjustment_factor
    trend_modifier = growth_trend * 0.75
    
    intermediate_result = base_metric + trend_modifier
    
    # Final adjustment based on presence of 'other' category
    extra_penalty = 0
    if metadata_counts['other'] > 0:
        extra_penalty = metadata_counts['other'] * 2
    
    final_score = int(intermediate_result - extra_penalty)
    
    # DO NOT REMOVE: required output format
    print(f"Result: {final_score}")
    return final_score

# Input data
benchmark_data = {
    'entries': [
        {'type': 'TEST ', 'value': 40, 'label': 'A'},
        {'type': 'test', 'value': 35, 'label': 'B'},
        {'type': 'TRIAL', 'value': 20, 'label': 'C'},
        {'type': 'trial', 'value': 50, 'label': 'D'},
        {'type': 'control', 'value': 30, 'label': 'E'}
    ],
    'sequence': [10, 15, 12, 18, 22]
}

final_score = calculate_performance(benchmark_data)