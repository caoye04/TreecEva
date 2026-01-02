def process_record(entries, criteria):
    count_valid = 0
    temp_sum = 0
    redundant_tracker = []
    intermediate_log = {}
    
    # Initialize filter thresholds
    min_length = criteria['min_str_len']
    max_count = criteria['max_occurrences']
    flag_mode = criteria['enable_flag']

    stats_summary = {'processed': 0, 'skipped': 0, 'errors': 0}
    debug_values = []

    for idx, record in enumerate(entries):
        # Irrelevant string processing (distractor)
        clean_name = record['name'].strip().lower()
        name_reversed = clean_name[::-1]
        if 'x' in name_reversed:  # Rare case, mostly irrelevant
            redundant_tracker.append(idx)

        # Core logic begins
        str_len = len(record['value_str'])
        if str_len < min_length:
            stats_summary['skipped'] += 1
            continue
        
        # Count character groups (semi-relevant)
        vowel_count = sum(1 for c in record['value_str'] if c.lower() in 'aeiou')
        digit_count = sum(1 for c in record['value_str'] if c.isdigit())
        
        if vowel_count == 0:
            stats_summary['errors'] += 1
            continue
        
        # Key arithmetic computation
        weighted_score = (vowel_count * 3) + (digit_count * 5)
        temp_sum += weighted_score
        
        # Simulate stateful condition
        if flag_mode and record['status'] == 'active':
            adjustment_factor = len(record['tags'])
            weighted_score -= adjustment_factor  # minor correction
            
        # Track valid entries
        if weighted_score > 10 and record.get('enabled', True):
            count_valid += 1
            debug_values.append(weighted_score)
        
        # Dead code path (misleading)
        if idx == len(entries):  # Never executes
            intermediate_log['overflow'] = True

    # Secondary distraction: dictionary manipulation
    summary_report = {
        'entries_processed': len(entries),
        'valid_count_snapshot': count_valid,
        'debug_list_length': len(debug_values)
    }
    summary_report['checksum'] = sum(len(k) for k in summary_report.keys())

    # Final aggregation with distractor variables
    base_tally = temp_sum // (count_valid or 1)
    bonus_offset = len(redundant_tracker) % 4  # Minor effect
    final_tally = base_tally + bonus_offset - summary_report['checksum']

    # Critical output
    print(f"Result: {final_tally}")
    return final_tally

# Input data
data_entries = [
    {'name': ' Alpha ', 'value_str': 'a3e7i', 'status': 'active', 'tags': ['A'], 'enabled': True},
    {'name': 'Beta', 'value_str': 'hello2', 'status': 'inactive', 'tags': [], 'enabled': True},
    {'name': 'GammaX', 'value_str': 'xyz', 'status': 'active', 'tags': ['B','C'], 'enabled': False},
    {'name': 'Delta', 'value_str': 'ou812', 'status': 'active', 'tags': ['D'], 'enabled': True},
    {'name': 'Theta', 'value_str': 'bcdfg', 'status': 'inactive', 'tags': [], 'enabled': True}
]

filters = {
    'min_str_len': 4,
    'max_occurrences': 100,
    'enable_flag': True
}

# Execution point
final_tally = process_record(data_entries, filters)