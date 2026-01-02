def analyze_text_pattern(text):
    """Irrelevant helper that analyzes letter frequency (distractor)"""
    freq = {}
    for char in text.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return [item[0] for item in sorted_freq[:3]]


def validate_checksum(data_str):
    """Misleading checksum validator (dead path)"""
    total = 0
    for i, c in enumerate(data_str):
        if c.isdigit():
            total += int(c) * (i + 1)
    return total % 11 == 0

# Irrelevant data preprocessing chain (distractor)
raw_input = "X9L2M4N7P1"
decoded_parts = [c for c in raw_input if c.isdigit()]
segment_sums = [int(d) ** 2 for d in decoded_parts]
avg_segment = sum(segment_sums) / len(segment_sums) if segment_sums else 0

# Unused complex transformation (red herring)
encoded_stream = ''
for i, d in enumerate(decoded_parts):
    shift = (int(d) + i) % 26
    encoded_stream += chr(ord('A') + shift)

# Decoy function with early exit (misleading control flow)
def compute_legacy_metric(value):
    if value < 5:
        return value * 3.7
    elif value == 7:
        return 0  # Trap result
    else:
        return (value + 1) // 2

# Real logic buried in noise
base_metrics = {
    'accuracy': 87,
    'latency': 44,
    'throughput': 124,
    'consistency': 91
}

adjustment_map = {k: v % 10 for k, v in base_metrics.items()}

bonus_multiplier = 1.75
penalty_factor = 0.88  # Distractor, not used

# Complex conditional masking (mixed relevance)
mask_threshold = 85
flags = {
    'high_acc': base_metrics['accuracy'] >= mask_threshold,
    'low_lat': base_metrics['latency'] <= 50,
    'stable': base_metrics['consistency'] > 88
}

# Simulated system state (overhead)
current_mode = 'performance'
override_enabled = False

# Core processing with string manipulation and arithmetic
def extract_modifier(key, val):
    mod_str = f'{key}{val}'
    if 'u' in mod_str:  # throughput contains 'u'
        reversed_mod = mod_str[::-1]
        digit_sum = sum(int(c) for c in reversed_mod if c.isdigit())
        return digit_sum * 0.1
    return 0.05

# Heavily interwoven logic with distractors
def process_performance(metrics, multiplier):
    score = 0
    modifier_total = 0.0
    
    for k, v in metrics.items():
        # String case conversion as part of key processing
        normalized_key = k.upper().replace('_', '')
        
        # Real contribution
        if len(normalized_key) % 2 == 0:
            score += v // 2
        else:
            score += v // 3
        
        # Actual modifier application
        key_mod = extract_modifier(k, v)
        modifier_total += key_mod
    
    # Combine with multiplier
    score *= multiplier
    score += modifier_total * 100
    
    # Final clamping (relevant)
    if score > 200:
        score = 192.4  # Hard cap
    
    # Dead branch (distractor)
    if current_mode == 'debug' and override_enabled:
        fallback = sum(metrics.values()) / len(metrics)
        score = fallback
    
    return round(score, 3)

# Trigger computation
final_score = process_performance(base_metrics, bonus_multiplier)

# Print result as required
print(f"Result: {final_score}")