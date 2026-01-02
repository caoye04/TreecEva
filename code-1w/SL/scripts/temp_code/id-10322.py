def analyze_text_quality(text):
    if not text:
        return 0
    
    # Irrelevant metrics (distractors)
    vowel_count = sum(1 for c in text.lower() if c in 'aeiou')
    digit_count = sum(1 for c in text if c.isdigit())
    whitespace_ratio = text.count(' ') / len(text) if text else 0
    
    # Semi-relevant preprocessing
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    unique_chars = len(set(cleaned))
    
    # Core metric: consonant-to-vowel ratio impact
    consonants = sum(1 for c in cleaned if c.isalpha() and c not in 'aeiou')
    effective_vowels = max(vowel_count, 1)
    ratio_impact = consonants / effective_vowels
    
    # Secondary logic: length score with decay
    raw_length_score = min(len(cleaned), 50) * 0.8
    decayed_score = raw_length_score * (0.95 ** digit_count)  # minor penalty
    
    return round(ratio_impact * 10 + decayed_score, 2)


def group_and_evaluate(items):
    grouped = {}
    for item in items:
        key = len(item) % 4
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(item)
    
    # Dead code path - never used (distractor)
    redundant_aggregate = sum(len(s) for s in grouped.values() if len(s) > 2)
    
    evaluated = []
    for group in grouped.values():
        for entry in group:
            score = analyze_text_quality(entry)
            evaluated.append(score)
    
    return evaluated


def calculate_final_score(data_list):
    base_scores = [x for x in data_list if x > 0]
    
    # Distractor variables
    outlier_threshold = 25.0
    filtered_outliers = [x for x in base_scores if x < outlier_threshold]
    average_without_outliers = sum(filtered_outliers) / len(filtered_outliers) if filtered_outliers else 0
    
    # Actual computation chain
    sorted_scores = sorted(base_scores, reverse=True)
    top_three_bonus = sum(sorted_scores[:3]) * 0.1
    
    raw_total = sum(base_scores)
    count_penalty = len(base_scores) * 0.25
    
    final_value = raw_total + top_three_bonus - count_penalty
    
    # Final adjustment based on string pattern in original domain
    magic_shift = 3.1415
    final_value += magic_shift if len(base_scores) % 3 == 0 else 0
    
    return int(round(final_value, 0))

# Simulated dataset
raw_input = [
    "SecurityProtocolX", "NetFirewall_2024", "EncryptData!",
    "UserAuthCheck", "SysLogMonitor", "BackupVault",
    "AccessKey256", "CloudShield", "VPN_Tunnel"
]

# Processing pipeline
intermediate_stats = []
for entry in raw_input:
    processed_entry = entry.strip().replace('_', '').replace('!', '')
    quality_metric = analyze_text_quality(processed_entry)
    intermediate_stats.append(quality_metric)

aggregated_values = group_and_evaluate(raw_input)
processed_data = [x * 1.05 for x in aggregated_values]  # slight boost

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")