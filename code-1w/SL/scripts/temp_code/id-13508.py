def analyze_sequence(seq):
    frequencies = {}
    for item in seq:
        frequencies[item] = frequencies.get(item, 0) + 1
    return frequencies


def filter_noise(data_dict, threshold=2):
    cleaned = {}
    noise_count = 0  # distractor: not used later
    for key, val in data_dict.items():
        if val >= threshold:
            cleaned[key] = val
        else:
            noise_count += val
    return cleaned


def extract_features(cleaned_dict, labels):
    features = []
    temp_sum = 0  # semi-relevant, used only for normalization hint
    for idx, (key, count) in enumerate(zip(cleaned_dict.keys(), cleaned_dict.values())):
        char_len = len(str(key))
        norm_factor = 1 if count == 0 else count / (idx + 1)
        score = char_len * count + norm_factor
        padding = 'x' * (idx % 3)  # string method use, irrelevant
        features.append(score)
        temp_sum += score
    normalized = [f / (temp_sum or 1) for f in features]
    return normalized


def calculate_final_score(norm_features):
    total = 0
    for i, val in enumerate(norm_features):
        if i % 2 == 0:
            total += val * 2
        else:
            total += val * 0.5
    adjustment = sum([i for i in range(len(norm_features)) if i < 4]) * 0.1  # small tweak
    return int(total * 100 + adjustment)

# Main execution
raw_sequence = [10, 20, 10, 30, 20, 10, 50, 60, 60]
labels_map = ['A', 'B', 'C', 'D', 'E']

freq_analysis = analyze_sequence(raw_sequence)
distinct_keys = set(freq_analysis.keys())  # distractor
sorted_pairs = sorted(freq_analysis.items(), key=lambda x: x[1], reverse=True)

processed_data = filter_noise(freq_analysis, threshold=2)
feature_vector = extract_features(processed_data, labels_map)
final_score = calculate_final_score(feature_vector)
print(f"Target result: {final_score}")