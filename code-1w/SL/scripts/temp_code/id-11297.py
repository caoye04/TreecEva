from collections import defaultdict

def analyze_pattern(sequence):
    freq = defaultdict(int)
    for char in sequence:
        freq[char] += 1
    return freq

def validate_sequence(seq):
    if not seq.isalpha():
        return False
    return len(seq) % 2 == 0

def compute_base_value(text):
    count = 0
    for c in text:
        if c.lower() in 'aeiou':
            count += 1
    adjustment = len(text) // 3
    temp_result = count * 7 - adjustment
    return temp_result

def extract_segments(data_string):
    parts = data_string.split('-')
    segment_length = [len(p) for p in parts]
    avg_len = sum(segment_length) / len(segment_length)
    return parts, round(avg_len)

def calculate_performance(flags, readings):
    base = readings['input_level'] * 2
    modifier = 1
    if flags['optimized'] and readings['consistency'] > 5:
        modifier += 0.5
    if flags['debug_mode']:
        modifier -= 0.3
    
    # Irrelevant distraction: analyzing a fixed pattern
    fake_seq = "abccba"
    pattern_analysis = analyze_pattern(fake_seq)
    valid = validate_sequence(fake_seq)
    
    # Dummy computation with no effect on result
    dummy_score = 0
    for k, v in pattern_analysis.items():
        if valid:
            dummy_score += ord(k) % v
    
    final_value = base * modifier
    scaling_factor = readings['efficiency'] / 10.0
    final_value *= scaling_factor
    
    return int(final_value)

# Main execution block
raw_input = "hello-world-test-case"
segments, average_size = extract_segments(raw_input)

# Misleading variable - looks important but only used in dummy context
bonus_metrics = {
    'sequence': 'xyzabc',
    'threshold': 42,
    'mode': 'legacy'
}

# Actual input data
metrics = {
    'input_level': 12,
    'consistency': 8,
    'efficiency': 15
}

bonus_flags = {
    'optimized': True,
    'debug_mode': False,
    'tracing': True
}

base_evaluation = compute_base_value(raw_input)
temp_flag = validate_sequence(bonus_metrics['sequence'])

# Key statement
final_score = calculate_performance(bonus_flags, metrics)

print(f"Result: {final_score}")