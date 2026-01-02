def analyze_text_patterns(text_data):
    char_count = len(text_data)
    vowel_count = sum(1 for c in text_data.lower() if c in 'aeiou')
    consonant_count = char_count - vowel_count
    uppercase_ratio = sum(1 for c in text_data if c.isupper()) / char_count
    
    # Irrelevant intermediate analysis (distractor)
    entropy_approx = 0.0
    freq_map = {}
    for c in text_data:
        freq_map[c] = freq_map.get(c, 0) + 1
    for v in freq_map.values():
        if v > 0:
            entropy_approx -= (v / char_count) * ((v / char_count) ** 0.5)

    # Semi-relevant transformation
    normalized_vowels = vowel_count / (char_count or 1)
    complexity_score = (vowel_count * 0.3) + (consonant_count * 0.7) + (uppercase_ratio * 10)
    
    return {
        'length': char_count,
        'vowels': vowel_count,
        'consonants': consonant_count,
        'norm_vowels': normalized_vowels,
        'score': complexity_score,
        'entropy': entropy_approx  # Not used later
    }


def filter_noisy_data(raw_samples):
    filtered = []
    noise_threshold = 5
    for sample in raw_samples:
        if len(sample) > noise_threshold and 'http' not in sample:
            filtered.append(sample)
    return filtered

# Main execution
raw_input = ["HelloWorld", "API_KEY_123", "dataAnalysis", "CodeGen", "LLM_TASK"]

# Distractor: unused data transformation
encoded_stream = list(map(lambda s: s.encode('utf-8').hex(), raw_input))

cleaned_data = filter_noisy_data(raw_input)

# Real processing begins here
analysis_results = []
for item in cleaned_data:
    result = analyze_text_patterns(item)
    analysis_results.append(result)

# Extract features for scoring
feature_matrix = [list(r.values()) for r in analysis_results]

# Weight vector — only first three elements actually matter
weights = [0.5, 0.3, 0.2, 0.0, 0.0, -0.1]  # Last two weights are neutralized

# Scoring function with lambda and slicing
weighted_scorer = lambda feats, w: sum(f * w[i] for i, f in enumerate(feats[:5]))

metrics = [r['score'] for r in analysis_results]  # Only this metric is used

# Dead code path (distractor)
if any(m < 0 for m in metrics):
    correction_factor = 1.1
else:
    correction_factor = 1.0  # Never applied

baseline_shift = sum(r['norm_vowels'] for r in analysis_results) * 0.05

# Key statement
final_score = evaluate_performance(metrics, weights)

# Actual implementation (defined after use due to Python hoisting considerations)
def evaluate_performance(data, weight_vec):
    aggregate = 0.0
    for val in data:
        temp_val = val * weight_vec[0]  # Only first weight used effectively
        aggregate += temp_val
    aggregate += baseline_shift
    return int(aggregate)  # Deterministic integer output

print(f"Result: {final_score}")