# Text analysis for document classification

raw_text = "AI machine learning data science algorithms neural networks models training datasets validation"
stop_words = ["and", "the", "in", "of", "for", "with", "on"]
min_length = 3
word_importance = {"AI": 8.5, "machine": 7.2, "learning": 9.0, "data": 6.8, "science": 8.2, 
                  "algorithms": 7.5, "neural": 8.7, "networks": 8.0, "models": 6.5, 
                  "training": 7.0, "datasets": 6.0, "validation": 5.5}

# Process the raw text
all_words = raw_text.lower().split()
processed_text = "-".join([w for w in all_words if len(w) > 2])
document_length = len(raw_text)

# Calculate word frequencies
word_freq = {}
for word in all_words:
    word_freq[word] = word_freq.get(word, 0) + 1

# Apply filters to words
filtered_words = []
ignored_words = []
for i, word in enumerate(all_words):
    if len(word) >= min_length and word not in stop_words:
        filtered_words.append(word)
    else:
        ignored_words.append((i, word))

# Calculate relevance scores
max_freq = max(word_freq.values()) if word_freq else 0
word_scores = {}
for word in filtered_words:
    # Normalized frequency score
    freq_score = word_freq[word] / max_freq if max_freq > 0 else 0
    # Word length score
    length_score = min(1.0, len(word) / 10)
    # Combined score with importance factor
    importance = word_importance.get(word, 5.0) / 10
    word_scores[word] = (freq_score * 0.3) + (length_score * 0.2) + (importance * 0.5)

# Set threshold for word relevance
base_threshold = 0.6
threshold_modifier = 0.1 if document_length > 100 else 0
threshold = base_threshold - threshold_modifier

# Count valid words above threshold
valid_words = len([word for word in filtered_words if word_scores[word] > threshold])

# Calculate additional metrics (not used in final result)
avg_word_length = sum(len(word) for word in filtered_words) / len(filtered_words) if filtered_words else 0
unique_ratio = len(set(filtered_words)) / len(filtered_words) if filtered_words else 0

print(f"Result: {valid_words}")