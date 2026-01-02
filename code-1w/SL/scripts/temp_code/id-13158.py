def analyze_text_patterns(input_str):
    char_frequency = {}
    for char in input_str:
        if char.isalpha():
            lower_char = char.lower()
            char_frequency[lower_char] = char_frequency.get(lower_char, 0) + 1
    
    # Distractor: vowel counting (not directly used)
    vowels = 'aeiou'
    total_vowels = sum(char_frequency.get(v, 0) for v in vowels)
    total_consonants = sum(char_frequency.values()) - total_vowels

    # Semi-relevant transformation
    normalized_freq = {k: round(v / sum(char_frequency.values()), 3) for k, v in char_frequency.items()}
    
    # Red herring computation
    entropy_proxy = 0
    for freq in normalized_freq.values():
        if freq > 0:
            entropy_proxy -= freq * __import__('math').log(freq)
    
    return normalized_freq, total_vowels  # Only normalized_freq is used later


def calculate_efficiency_metric(data, threshold=0.05):
    above_threshold = [k for k, v in data.items() if v > threshold]
    below_threshold = [k for k, v in data.items() if v <= threshold]
    
    # Dummy sorting with no impact
    above_threshold.sort(reverse=True)
    below_threshold.sort()
    
    # Efficiency score based on distribution
    high_impact = len(above_threshold)
    low_impact = len(below_threshold)
    efficiency = (high_impact * 2 + low_impact) / (len(data) or 1)
    
    # Irrelevant string manipulation
    label = ''.join(above_threshold)[:5].upper() if above_threshold else 'NONE'
    label_checksum = sum(ord(c) for c in label)
    
    return efficiency  # Only efficiency matters


def validate_consistency(log_entries):
    # Simulate state tracking
    state_log = []
    errors = 0
    for entry in log_entries:
        words = entry.split()
        if 'ERROR' in words:
            errors += 1
            state_log.append('error')
        elif 'WARNING' in words:
            state_log.append('warn')
        else:
            state_log.append('ok')
    
    # Dead code path
    if len(state_log) > 100:
        compression_ratio = len(state_log) / 100
    else:
        compression_ratio = 1.0
    
    # Return only what's needed
    return errors

# Main execution flow
text_sample = "The quick brown fox jumps over the lazy dog multiple times efficiently."

# Step 1: Extract character patterns
freq_map, vowel_total = analyze_text_patterns(text_sample)

# Step 2: Compute efficiency from frequency distribution
raw_efficiency = calculate_efficiency_metric(freq_map)
efficiency = round(raw_efficiency * 100, 2)  # Scale to percentage

# Step 3: Log simulation for error tracking
system_logs = [
    "STATUS OK",
    "DATA RECEIVED",
    "ERROR INVALID FORMAT",
    "PROCESSING COMPLETE",
    "ERROR TIMEOUT",
    "RETRY SUCCESS"
]
error_count = validate_consistency(system_logs)

# Step 4: Metadata processing with dictionary operations
document_metadata = {
    'title': 'Performance Analysis Report',
    'author': 'AutoGen System',
    'version': '2.1.0',
    'tags': ['analysis', 'text', 'metrics']
}

# Irrelevant transformation chain
caps_title = document_metadata['title'].upper()
word_count = len(caps_title.split())
tag_summary = ','.join(document_metadata['tags']).replace(' ', '')
summary_length = len(tag_summary)

# Final scoring logic
base_score = efficiency * 0.8
penalty = error_count * 5.5
final_score = int(base_score - penalty)

# Additional distraction: unused backup calculation
backup_score = round((efficiency - (error_count * 4)) * 0.9, 1)

# Output target result
Result: final_score