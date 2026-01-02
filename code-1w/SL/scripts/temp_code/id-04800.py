def analyze_text_properties(text):
    char_count = len(text)
    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    avg_word_length = sum(len(word) for word in text.split()) / word_count if word_count > 0 else 0
    
    # Distractor: irrelevant linguistic metrics
    vowel_ratio = sum(1 for c in text.lower() if c in 'aeiou') / char_count if char_count > 0 else 0
    uppercase_density = sum(1 for c in text if c.isupper()) / char_count
    punctuation_load = text.count(',') + text.count(';') + text.count(':')

    return {
        'char_count': char_count,
        'word_count': word_count,
        'sentence_count': sentence_count,
        'avg_word_length': avg_word_length
    }


def filter_noisy_entries(data_list):
    filtered = []
    noise_threshold = 3
    for entry in data_list:
        clean_entry = {k: v for k, v in entry.items() if k != 'raw_noise'}
        if entry.get('anomaly_flag', 0) < noise_threshold:
            filtered.append(clean_entry)
    
    # Distractor: dead code path (never used)
    temp_stats = {}
    if len(filtered) > 10:
        temp_stats['dummy'] = 'unused'
    
    return filtered


def normalize_metrics(entries):
    if not entries:
        return []
    
    # Extract values for normalization
    word_counts = [e['word_count'] for e in entries]
    max_words = max(word_counts)
    min_words = min(word_counts)
    
    normalized = []
    for e in entries:
        norm_entry = e.copy()
        if max_words != min_words:
            norm_entry['norm_word_count'] = (e['word_count'] - min_words) / (max_words - min_words)
        else:
            norm_entry['norm_word_count'] = 0.5
        normalized.append(norm_entry)
    
    # Distractor: unused transformation
    lambda_transform = lambda x: x ** 0.5 if x > 0 else 0
    transformed_scores = [lambda_transform(e['sentence_count']) for e in normalized]

    return normalized


def calculate_final_score(entries):
    base_score = 0
    for entry in entries:
        # Core logic contribution
        base_score += entry['avg_word_length'] * 2.5
        base_score += entry['norm_word_count'] * 1.8
        base_score += entry['sentence_count'] * 0.7
    
    final_modifier = 1.1 if len(entries) >= 3 else 0.95
    return int(base_score * final_modifier)


# Simulated dataset
texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Hello world! This is a test string.",
    "Python programming requires logical thinking and attention to detail.",
    "Short. Another one! And a third? Yes indeed, this counts.",
    "Irrelevant noisy entry with excessive,,, punctuation;;; and anomalies:::"  # High anomaly
]

# Annotate with metadata
annotated_data = []
for t in texts:
    is_noisy = t.count(',') + t.count(';') + t.count(':') > 5
    annotated_data.append({
        'text': t,
        'length': len(t),
        'raw_noise': t.count(',') + t.count(';'),
        'anomaly_flag': 5 if is_noisy else 1
    })

# Processing pipeline
extracted_features = [analyze_text_properties(item['text']) for item in annotated_data]
for i, feat in enumerate(extracted_features):
    feat['source_id'] = i

processed_data = filter_noisy_entries([
    {**feat, 'raw_noise': annotated_data[i]['raw_noise']} 
    for i, feat in enumerate(extracted_features)
])

# Normalize only relevant metrics
processed_data = normalize_metrics(processed_data)

# Critical execution point
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")