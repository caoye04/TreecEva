def analyze_text_patterns(text_data):
    char_count = {}
    for c in text_data:
        char_count[c] = char_count.get(c, 0) + 1
    
    # Irrelevant vowel tracking (distractor)
    vowels = 'aeiou'
    vowel_count = sum(1 for c in text_data if c.lower() in vowels)
    consonant_ratio = (len(text_data) - vowel_count) / len(text_data) if text_data else 0

    # Misleading entropy calculation (unused later)
    import math
    entropy = -sum((count / len(text_data)) * math.log2(count / len(text_data)) 
                   for count in char_count.values() if count > 0)

    # Real processing: count alphanumeric and special chars
    alpha_count = sum(1 for c in text_data if c.isalpha())
    digit_count = sum(1 for c in text_data if c.isdigit())
    special_count = len(text_data) - alpha_count - digit_count

    return {
        'length': len(text_data),
        'alpha': alpha_count,
        'digits': digit_count,
        'special': special_count,
        'unique_chars': len(char_count)
    }


def transform_metrics(raw):
    # Distractor transformation chain
    scaled = {k: v * 1.5 for k, v in raw.items()}
    normalized = {k: v / (raw['length'] + 1e-8) for k, v in scaled.items()}

    # Fake smoothing operation (dead path)
    smoothed = {}
    for k, v in normalized.items():
        if len(k) > 5:
            smoothed[k] = v * 0.9
        else:
            smoothed[k] = v * 1.1

    # Actual feature engineering
    features = []
    weights = {'alpha': 1.2, 'digits': 2.0, 'special': 3.5, 'unique_chars': 0.8}
    for key, val in raw.items():
        if key in weights:
            features.append(val * weights[key])
    
    return sum(features)


def filter_outliers(scores):
    if len(scores) < 3:
        return scores
    sorted_vals = sorted(scores)
    q1, q3 = sorted_vals[len(sorted_vals)//4], sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower, upper = q1 - 1.5*iqr, q3 + 1.5*iqr
    filtered = [s for s in scores if lower <= s <= upper]
    return filtered if len(filtered) >= 3 else scores  # fallback


def calculate_baseline_adjustment(data_list):
    # Complex but irrelevant statistical adjustment
    means = [sum(d.values()) / len(d) for d in data_list]
    grand_mean = sum(means) / len(means) if means else 0
    variance = sum((m - grand_mean)**2 for m in means) / len(means) if means else 0
    adjustment = math.sqrt(variance) if variance > 0.1 else 0.1
    
    # Dead code: z-score normalization not used
    z_scores = [(m - grand_mean) / adjustment for m in means]
    
    return grand_mean * 0.75  # actual baseline contribution


def evaluate_performance(metrics_list, base):
    # Multi-step scoring with red herrings
    total_raw = transform_metrics(metrics_list)
    
    # Fake clustering attempt (distractor)
    clusters = {}
    for i, m in enumerate([total_raw]):
        label = 'high' if m > base else 'low'
        clusters[label] = clusters.get(label, []) + [i]
    
    # Decoy conditional logic
    bonus = 0
    if len(clusters.get('high', [])) > 5:
        bonus += 10
    elif base > 50 and metrics_list['special'] > 10:
        bonus += 5
    else:
        bonus -= 2  # misleading penalty
    
    # Critical computation path
    adjustment_factor = 1.0
    if metrics_list['digits'] > 0:
        adjustment_factor *= (1 + metrics_list['special'] / metrics_list['digits'])
    else:
        adjustment_factor *= 0.5
    
    intermediate = total_raw * adjustment_factor
    final_score = intermediate - base + bonus  # final formula

    # Unused diagnostic print (distractor)
    diagnostics = f"Score breakdown: raw={total_raw:.2f}, adj={intermediate:.2f}, base={base}, bonus={bonus}"
    
    return final_score

# Main execution with layered distractions
input_text = "SecureLog!2023#AlphaTest$987"
data_metrics = analyze_text_patterns(input_text)

# Generate fake auxiliary datasets (red herring)
aux_texts = [
    "Error404:PageNotFound!",
    "DEBUG_MODE_ACTIVE$$$",
    "AuthSuccess!@#2025"
]
aux_metrics = [analyze_text_patterns(txt) for txt in aux_texts]
outlier_filtered = filter_outliers([len(txt) for txt in aux_texts])

# Compute phantom correlations (dead path)
correlations = []
for aux in aux_metrics:
    corr_val = (aux['alpha'] * aux['digits']) / (aux['length'] + 1) if aux['length'] else 0
    if corr_val > 2.0:
        correlations.append(corr_val)

baseline_ref = calculate_baseline_adjustment([data_metrics] + aux_metrics)

# Key statement
final_score = evaluate_performance(data_metrics, baseline_ref)

print(f"Result: {final_score}")