def analyze_sentiment(texts):
    # Irrelevant sentiment analysis function (dead end)
    sentiment_values = []
    for t in texts:
        score = 0
        for c in t.lower():
            if c in 'aeiou':
                score += 1
            elif c in 'xyz':
                score -= 2
        sentiment_values.append(score)
    return sum(sentiment_values)


def transform_data(records):
    # Distractor: complex data transformation with no impact on result
    temp_output = []
    for r in records:
        transformed = r[::-1]  # reverse string
        if len(transformed) % 2 == 0:
            transformed = transformed[len(transformed)//2:] + transformed[:len(transformed)//2]
        temp_output.append(transformed)
    return temp_output


def compute_entropy(sequence):
    # Misleading scientific computation (not used in final answer)
    from math import log2
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    total = len(sequence)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 6)


def evaluate_performance(feedback_log):
    # Core logic embedded in noise
    
    # Irrelevant preprocessing
    clean_log = [entry.strip().lower() for entry in feedback_log if entry.strip()]
    filtered_log = [msg for msg in clean_log if 'error' not in msg]
    
    # Real work starts here — character frequency analysis
    char_count = {}
    for msg in filtered_log:
        for char in msg:
            if char.isalpha():
                char_count[char] = char_count.get(char, 0) + 1
    
    # Extract top characters by frequency (distractor: sorting)
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    top_five = [item[0] for item in sorted_chars[:5]]
    
    # Hidden calculation: sum of ASCII values of top five unique letters
    ascii_sum = sum(ord(c) for c in top_five)
    
    # Secondary path: length-based weighting
    lengths = [len(msg) for msg in filtered_log]
    avg_length = sum(lengths) / len(lengths) if lengths else 0
    
    # Decoy intermediate result
    phantom_metric = compute_entropy([len(msg) for msg in filtered_log])
    
    # Actual answer derivation (non-obvious)
    adjustment_factor = len(top_five) * 2
    base_score = ascii_sum // 3
    
    # Final score depends only on base_score and adjustment_factor
    final_score = base_score + adjustment_factor
    
    # Dead code branch (never executed)
    if False:
        backup_system = transform_data(filtered_log)
        fallback = analyze_sentiment(backup_system)
        final_score = fallback

    return int(final_score)

# Main execution block
if __name__ == '__main__':
    # Input data with red herrings
    raw_messages = [
        "System OK", "No errors detected", "All systems nominal",
        "Status green", "Operation within parameters",
        "WARNING: minor fluctuation", "Check completed", "Validation passed",
        "INFO: diagnostics running", "DEBUG: trace enabled"
    ]

    # Unused variables to distract
    metadata_tags = ['SYS_001', 'MONITOR_2', 'SECURE_LOG']
    timestamp_sequence = [1634567890 + i*60 for i in range(len(raw_messages))]
    priority_flags = [False, True, False, False, True]

    # Real input to function
    feedback_chain = raw_messages.copy()

    # Add decoy mutation
    feedback_chain.append("ERROR: false positive")  # Will be filtered out

    # Key statement
    final_score = evaluate_performance(feedback_chain)
    
    # Output result
    print(f"Result: {final_score}")