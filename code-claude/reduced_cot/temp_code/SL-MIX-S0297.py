# Text analysis for academic paper submissions
# Analyzing keyword frequency and relevance

text = "machine learning algorithms have become essential tools for data analysis and pattern recognition in various domains including healthcare finance and education"

stop_words = {"and", "for", "in", "the", "have", "become"}
excluded_domains = {"sports", "entertainment", "politics"}
min_word_length = 4

# Word scores based on academic relevance (higher = more relevant)
word_scores = {
    "machine": 8.5,
    "learning": 9.0,
    "algorithms": 7.5,
    "essential": 5.0,
    "tools": 4.5,
    "data": 8.0,
    "analysis": 7.0,
    "pattern": 6.5,
    "recognition": 6.0,
    "domains": 4.0,
    "healthcare": 7.5,
    "finance": 6.0,
    "education": 5.5
}

# Processing the text
words = text.lower().split()
temporary_words = [w for w in words if len(w) > 2]  # Not directly used

# Remove stop words and short words
filtered_words = [w for w in words if w not in stop_words and len(w) >= min_word_length]

# Count domain occurrences - not directly relevant to final answer
domain_count = sum(1 for w in filtered_words if w in excluded_domains)
domain_ratio = domain_count / len(filtered_words) if filtered_words else 0

# Apply conditional scoring
scores = {}
for word in filtered_words:
    if word in word_scores:
        base_score = word_scores[word]
        length_factor = 1 + (len(word) - min_word_length) * 0.1
        scores[word] = base_score * length_factor
    else:
        scores[word] = 0

# Calculate average score - distractor calculation
avg_score = sum(scores.values()) / len(scores) if scores else 0
max_score = max(scores.values()) if scores else 0
min_score = min(scores.values()) if scores else 0

# Count valid words that have scores
valid_word_count = len([w for w in filtered_words if w in word_scores])

# Calculate weighted score - another distractor
weighted_score = sum(scores.values()) / valid_word_count if valid_word_count > 0 else 0

# Determine text quality rating - not relevant to answer
quality_rating = "High" if avg_score > 7 else "Medium" if avg_score > 5 else "Low"

print(f"Result: {valid_word_count}")