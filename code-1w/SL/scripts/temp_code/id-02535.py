def analyze_text_patterns(text):
    # Irrelevant text analysis (distractor)
    vowels = sum(1 for c in text if c.lower() in 'aeiou')
    consonants = sum(1 for c in text if c.isalpha() and c.lower() not in 'aeiou')
    word_count = len(text.split())
    avg_word_length = sum(len(word.strip('.,!?')) for word in text.split()) / word_count if word_count else 0
    
    # Misleading intermediate result
    pseudo_entropy = (vowels + 0.5 * consonants) / len(text) if text else 0
    return pseudo_entropy

# Dead function - never called (red herring)
def legacy_compatibility_mode(data):
    shifted = [((val << 2) ^ 0xA3) % 256 for val in data]
    return [x for x in shifted if x % 3 == 0]

# Decoy data structure
user_preferences = {
    'theme': 'dark',
    'notifications': False,
    'auto_save': True,
    'sensitivity_level': 7
}

# Real computation begins here
raw_metrics = [12, 18, 24, 30, 36]
scaling_factor = 1.5
adjusted_metrics = [x * scaling_factor for x in raw_metrics]

# Bit manipulation distraction
bitwise_mask = 0xF0
masked_values = [(int(x) & bitwise_mask) for x in adjusted_metrics]
checksum = sum(masked_values) % 256

# Conditional expression chain with red herring
status_flag = 'A' if checksum > 100 else 'B'
bonus_applied = True if status_flag == 'A' and len(raw_metrics) > 4 else False

# Core logic buried among noise
def compute_baseline(items):
    total = 0
    for item in items:
        if item % 6 == 0:  # Key filtering condition
            total += item
    return total

baseline = compute_baseline(raw_metrics)

# Logical operations with short-circuit distraction
is_optimal = baseline > 50 and bonus_applied or checksum < 200  # Always true due to second clause

# String method used as decoy
system_log = "ERROR: Failed to load module X"
system_flags = system_log.split(':')
error_count = system_flags[0].count('E')

# Another irrelevant transformation
shifted_logs = [flag.strip().lower().replace(' ', '_') for flag in system_flags]

# Main scoring logic (non-obvious path)
def evaluate_performance(data):
    raw_sum = sum(data)
    count_valid = sum(1 for x in data if x >= 20)
    adjustment = 0.75 if count_valid >= 3 else 1.0
    
    # Real answer computed here, obscured by prior noise
    score = (raw_sum * adjustment) + (checksum // 10)
    
    # Distracting string formatting
    debug_msg = f"Performance score: {score:.2f} (based on {count_valid} valid entries)"
    debug_msg.upper().replace('.', 'p').split('p')  # Useless operation
    
    return int(score)

# Critical execution point
metric_data = adjusted_metrics  # Note: adjusted_metrics are floats
final_score = evaluate_performance(metric_data)

print(f"Result: {final_score}")