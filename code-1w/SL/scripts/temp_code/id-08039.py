def analyze_text(sample):
    if not sample:
        return 0
    words = sample.split()
    word_lengths = [len(w) for w in words]
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    upper_count = len([c for c in sample if c.isupper()])
    digit_ratio = len([c for c in sample if c.isdigit()]) / len(sample)
    return {'avg_word_len': avg_length, 'upper': upper_count, 'digit_ratio': digit_ratio}

# Irrelevant helper function (distractor)
def decrypt_sequence(seq):
    result = 0
    for i, val in enumerate(seq):
        result += val * (i + 1)
    return result % 17

# Unused but plausible data transformation
def transform_data(data_list):
    transformed = []
    for item in data_list:
        if isinstance(item, str):
            transformed.append(item[::-1].lower())
        elif isinstance(item, int):
            transformed.append(item ** 2)
    return transformed

# Simulated sensor readings (red herring)
sensor_log = [3, 7, 2, 8, 1, 9, 4]
baseline_offset = decrypt_sequence(sensor_log)

# Core logic: employee performance evaluation
metrics = {
    'accuracy': 87.5,
    'speed': 64,
    'consistency': 73,
    'attendance': 92
}

weights = {
    'accuracy': 0.35,
    'speed': 0.25,
    'consistency': 0.20,
    'attendance': 0.20
}

# Distracting normalization that isn't used
temp_normalized = {k: v / 100 for k, v in metrics.items() if k != 'speed'}

# Another decoy path
def calculate_risk_profile(scores):
    total = 0
    for s in scores.values():
        total += s ** 0.5
    return total / 10

# Real evaluation function
def evaluate_performance(mets, wts):
    raw_score = 0
    for key in mets:
        if key in wts:
            raw_score += mets[key] * wts[key]
    
    # Apply text analysis bonus if present
    sample_feedback = "Excellent Work On Project DELTA"
    text_analysis = analyze_text(sample_feedback)
    
    # Bonus logic: only use digit_ratio from text analysis
    bonus = 0
    if text_analysis['digit_ratio'] > 0:
        bonus = 5
    elif text_analysis['upper'] > 10:
        bonus = 3
    else:
        bonus = 1
    
    # Final adjustment using irrelevant baseline_offset (but it's not actually used)
    adjusted_baseline = baseline_offset * 0.1  # Dead computation
    final_value = raw_score + bonus + 0.0  # Neutral addition to obscure logic
    
    # Additional misdirection
    phantom_correction = calculate_risk_profile(metrics) * 0  # Always zero
    
    return final_value + phantom_correction

# Spurious list comprehension with unused result
dummy_flags = [x > 5 for x in sensor_log if x % 2 == 1]

# Actual execution
text_metrics = analyze_text("Code Reviewed: PR-7892")
final_score = evaluate_performance(metrics, weights)

# Output the target variable
print(f"Result: {final_score}")