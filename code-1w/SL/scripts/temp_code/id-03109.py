def analyze_events(raw_data, threshold_config):
    # Irrelevant preprocessing block (dead path)
    temp_buffer = [x for x in raw_data if isinstance(x, str) and 'tmp' in x]
    debug_snapshot = list(enumerate(temp_buffer))

    # Real data extraction with distractor logic
    event_codes = []
    for item in raw_data:
        if isinstance(item, dict) and 'code' in item:
            if item.get('status') == 'active':
                event_codes.append(item['code'])

    # Distractor: unused transformation chain
    masked_values = [c ^ 255 for c in event_codes if c < 200]
    shifted_map = {i: v << 2 for i, v in enumerate(masked_values)}

    # Real logic begins: filter and transform
    valid_codes = [c for c in event_codes if c >= threshold_config['min_code']]
    weighted_scores = []
    for idx, code in enumerate(valid_codes):
        weight = threshold_config['base_weight']
        if idx % 2 == 0:
            weight += 0.5
        weighted_scores.append(code * weight)

    # Secondary distractor: complex but unused string analysis
    log_strings = [f"Event-{c}" for c in event_codes]
    char_analysis = {}
    for i, s in enumerate(log_strings):
        char_analysis[i] = sum([ord(ch) for ch in s if ch.isalpha()]) // len(s)
    sorted_chars = sorted(char_analysis.items(), key=lambda x: x[1], reverse=True)

    # Critical path: aggregate real result through indirect computation
    base_accum = sum(weighted_scores)
    adjustment_factor = len(valid_codes) ** 1.5 if valid_codes else 0
    interim_result = base_accum - adjustment_factor

    # Tertiary red herring: recursive decoy function
    def explore_tree(depth, value):
        if depth <= 0:
            return value
        return explore_tree(depth - 1, value + (value % 7))

    # Unused call — misleading complexity
    ghost_trace = explore_tree(5, 12)

    # Real final step hidden among noise
    scaling_constant = 3.141592
    final_value = interim_result * scaling_constant / (threshold_config['base_weight'] + 1)

    return int(final_value)


def process_metrics(entries, limit):
    # Mix of relevant and irrelevant operations
    parsed_logs = []
    for entry in entries:
        if isinstance(entry, str):
            parts = entry.split('|')
            if len(parts) > 2 and parts[1].isdigit():
                parsed_logs.append({'code': int(parts[1]), 'status': 'active'})
        elif isinstance(entry, dict):
            parsed_logs.append(entry)

    # Use of zip and enumerate — required Python features
    indices = list(range(len(parsed_logs)))
    paired_stream = list(zip(indices, parsed_logs))
    indexed_diagnostics = []
    for index, log in paired_stream:
        if log.get('code', 0) > 50:
            indexed_diagnostics.append((index, log['code'] * 2))

    # String method distraction
    metadata_tags = [str(log) for log in parsed_logs]
    clean_tags = [tag.strip('{}').replace("'", "") for tag in metadata_tags]
    hash_projection = sum([len(tag) for tag in clean_tags if 'active' in tag])

    # Actual signal buried in noise
    config = {
        'min_code': 40,
        'base_weight': 2
    }

    # Key computation
    result = analyze_events(parsed_logs, config)

    # Decoy arithmetic
    phantom_sum = sum([hash_projection, len(clean_tags), len(indexed_diagnostics)]) // 3

    # Final answer derived from core logic, not decoys
    final_diagnostic = result + 7  # small offset to invalidate direct copying

    return final_diagnostic

# Input data with mixed types and red herrings
log_entries = [
    'ERR|105|Z7',
    'WRN|88|X2',
    {'code': 35, 'status': 'inactive'},
    'INF|120|A9',
    {'code': 60, 'status': 'active'},
    'DBG|45|K4',
    'INF|150|M1'
]
system_threshold = 40

final_diagnostic = process_metrics(log_entries, system_threshold)
print(f"Result: {final_diagnostic}")