from collections import defaultdict
import string

def preprocess_logs(raw_logs):
    # Irrelevant preprocessing step (distractor)
    cleaned = []
    for log in raw_logs:
        entry = log.strip().lower()
        if 'error' not in entry and 'fail' not in entry:
            cleaned.append(entry)
    return cleaned

def generate_metrics(logs):
    # Semi-relevant function: counts word frequencies (some used later)
    freq = defaultdict(int)
    for log in logs:
        for char in log:
            if char in string.ascii_lowercase:
                freq[char] += 1
    return dict(freq)

def filter_redundant_chars(charset, exclusions):
    # Distractor function with dead logic
    result = set()
    priority_group = {'a', 'e', 'i', 'o', 'u'}
    for c in charset:
        if c not in exclusions and c.isalpha():
            if len(result) < 10:  # Artificial limit (misleading)
                result.add(c)
    return result

def calculate_entropy(values):
    # Unused helper (dead code path)
    total = sum(values)
    entropy = 0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * __import__('math').log2(p)
    return round(entropy, 4)

def evaluate_performance(metrics, logs):
    # Core logic begins
    key_chars = {k for k in metrics.keys() if k in 'abcdef'}
    base_score = 0
    adjustment = len(logs) % 7  # Minor influence

    # Nested logic with interdependencies
    temp_buffer = []
    for log in logs:
        if 'warning' in log:
            temp_buffer.append(len(log))

    buffer_sum = sum(temp_buffer) if temp_buffer else 15  # Default fallback

    # Real computation chain (5-8 steps)
    step1 = sum(metrics[c] for c in key_chars if c in metrics)  # Sum relevant frequencies
    step2 = step1 * 3
    step3 = step2 + adjustment
    
    # Conditional modification based on structural property
    if len(key_chars) >= 4:
        step4 = step3 * 2
    else:
        step4 = step3 + 50

    # Secondary adjustment using string method side effect
    all_text = ''.join(logs)
    uppercase_count = sum(1 for c in all_text if c.isupper())
    step5 = step4 - (uppercase_count * 2)

    # Final threshold adjustment
    if step5 > 200:
        final_score = step5 - 77
    else:
        final_score = step5 + 23

    return final_score

# Main execution flow
if __name__ == '__main__':
    # Input data
    system_logs = [
        'INFO: System initialized...',
        'WARNING: Low memory (85%)',
        'INFO: User abcdef logged in',
        'DEBUG: Processing request from XYZ',
        'WARNING: Disk usage high',
        'INFO: Backup completed successfully'
    ]

    # Irrelevant variables (distractors)
    max_threshold = 95
    retry_limit = 3
    timeout_ms = 5000
    temp_var = [1, 2, 3]
    unused_dict = {'x': 10, 'y': 20}

    # Preprocess (has side effect of filtering)
    filtered_logs = preprocess_logs(system_logs)
    
    # Generate full metrics (only part used later)
    metric_set = generate_metrics(filtered_logs)
    
    # Useless set operation (distractor)
    alphabet_set = set(string.ascii_letters)
    excluded = set(string.digits + string.punctuation)
    filtered_alphabet = filter_redundant_chars(alphabet_set, excluded)

    # Actual target computation
    final_score = evaluate_performance(metric_set, filtered_logs)
    
    # Print result as required
    print(f"Target result: {final_score}")