def analyze_pattern(sequence):
    count_a = sequence.count('A')
    count_t = sequence.count('T')
    count_g = sequence.count('G')
    count_c = sequence.count('C')
    ratio = (count_a + count_t) / (count_g + count_c + 1)
    return ratio * len(sequence)


def validate_checksum(token):
    total = 0
    for i, char in enumerate(token):
        if char.isdigit():
            total += int(char) * (i + 1)
    checksum = total % 17
    return checksum == 5


def transform_data(raw_list):
    transformed = []
    for item in raw_list:
        if isinstance(item, str):
            item = item.strip().upper()
            if 'X' in item:
                item = item.replace('X', 'Z')
        elif isinstance(item, int):
            item = item ** 2
        transformed.append(item)
    return transformed

# Irrelevant utility function (dead code path)
def deprecated_util(val):
    return val << 2 | 1

# Misleading preprocessing
raw_sequence = "ATGCTAGCTAXXGTACG"
encoded_seq = ''.join([c if c != 'X' else 'T' for c in raw_sequence])
pattern_metric = analyze_pattern(encoded_seq)

# Decoy data structures
flags = {
    'active': True,
    'debug_mode': False,
    'threshold_met': False,
    'legacy': True,
    'mode_flag': 3
}

config_map = {
    'version': '2.1',
    'max_iter': 150,
    'tolerance': 0.001,
    'scale': 4.2
}

# Actual relevant data
data_entries = [
    "ATGCATGC",
    "ATGXATCG",
    "GTACGTAC",
    "CGXTCGAT"
]

processed_entries = []
for entry in data_entries:
    cleaned = entry.replace('X', 'A')
    score = analyze_pattern(cleaned)
    processed_entries.append(score)

summary_stats = {
    'mean': sum(processed_entries) / len(processed_entries),
    'peak': max(processed_entries),
    'base_count': len(data_entries),
    'adjusted_total': sum(processed_entries) * 0.85
}

# Key function with mixed logic and distractors
def process_metrics(stats, options):
    base_value = stats['mean']
    multiplier = 1
    
    # Conditional logic with red herring branches
    if options['debug_mode']:
        multiplier *= 0.5
    elif options['mode_flag'] == 3:
        multiplier *= 2.1
    
    if options['threshold_met']:
        base_value += 100
    
    # Distractor: unused calculation
    temp_offset = stats['peak'] // 4
    
    # Relevant branching
    if stats['base_count'] > 3:
        base_value += 15
    
    final_raw = base_value * multiplier
    
    # String-based flag check (uses string method)
    mode_str = 'advanced_debug'
    if 'debug' in mode_str and not options['legacy']:
        final_raw *= 0.1
    
    # Final adjustment based on conditional expression
    adjustment = 8.5 if validate_checksum('7392') else 0
    final_raw += adjustment
    
    return int(final_raw)

# Unused but plausible-looking computation
aggregate = 0
for key, value in config_map.items():
    if isinstance(value, float):
        aggregate += value * 10

# Critical execution point
data_summary = summary_stats
final_score = process_metrics(data_summary, flags)
print(f"Result: {final_score}")