def analyze_text_patterns(input_str):
    char_freq = {}
    for ch in input_str:
        char_freq[ch] = char_freq.get(ch, 0) + 1
    
    vowels = set('aeiou')
    vowel_count = sum(char_freq.get(v, 0) for v in vowels)
    consonant_count = len(input_str) - vowel_count - char_freq.get(' ', 0)
    
    return vowel_count, consonant_count, char_freq


def normalize_metrics(raw_data):
    total = sum(raw_data.values())
    if total == 0:
        return {}
    normalized = {k: v / total for k, v in raw_data.items()}
    temp_sum = sum(normalized.values())
    scale_factor = 1.0 / temp_sum if temp_sum != 0 else 1
    scaled = {k: v * scale_factor for k, v in normalized.items()}
    return scaled

def filter_noisy_signals(signal_list, threshold=0.05):
    filtered = [s for s in signal_list if abs(s) > threshold]
    magnitude_avg = sum(abs(x) for x in filtered) / len(filtered) if filtered else 0
    peak_value = max(filtered, default=0)
    return filtered, magnitude_avg, peak_value

def evaluate_performance(metrics, base_ref):
    score = 0
    adjustment = 0.1
    
    active_keys = set(metrics.keys()) & set(base_ref.keys())
    
    diff_set = set(metrics.keys()) ^ set(base_ref.keys())
    extra_penalty = len(diff_set) * 0.5
    
    for key in active_keys:
        if metrics[key] > base_ref[key]:
            score += 1
        elif metrics[key] < base_ref[key]:
            adjustment += 0.05
    
    stability_check = len(active_keys) >= 3
    complexity_bonus = 2 if stability_check and len(diff_set) < 4 else 0
    
    final_score = int(score - extra_penalty + complexity_bonus)
    
    # Distractor variables - not used in final logic
    temp_debug = [x for x in metrics.values() if x > 0.1]
    dummy_aggregate = sum(temp_debug) * adjustment if temp_debug else 0
    unused_intermediate = dummy_aggregate ** 2
    
    return final_score

# Main execution
raw_text = "dynamic programming solves complex problems efficiently"

vowels, consonants, frequency_map = analyze_text_patterns(raw_text)

normalized_features = normalize_metrics(frequency_map)

signal_values = list(normalized_features.values())
filtered_signals, avg_magnitude, peak = filter_noisy_signals(signal_values)

baseline = {'a': 0.05, 'e': 0.08, 'n': 0.07, 'o': 0.06, 'm': 0.04, 'p': 0.03}
metric_set = {k: v for k, v in normalized_features.items() if k in 'aeonmp'}

intermediate_weight = avg_magnitude * peak if peak else 0
placeholder_result = (vowels + consonants) // 2

final_score = evaluate_performance(metric_set, baseline)
print(f"Result: {final_score}")