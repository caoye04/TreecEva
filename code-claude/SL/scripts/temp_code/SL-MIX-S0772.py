from collections import defaultdict, Counter

# Text analysis function to calculate word frequencies
def analyze_text(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = ''.join(c.lower() if c.isalnum() or c.isspace() else ' ' for c in text)
    
    # Split into words
    words = cleaned_text.split()
    
    # Count word frequencies
    word_counts = Counter(words)
    return word_counts

# Sample text for analysis
sample_text = "Python programming is both fun and challenging. Programming requires logical thinking."
backup_text = "Data analysis with Python is becoming increasingly popular among researchers."

# Analyze both texts
main_counts = analyze_text(sample_text)
backup_counts = analyze_text(backup_text)

# Calculate word importance based on frequency
word_importance = defaultdict(int)
for word, count in main_counts.items():
    if len(word) > 3:  # Only consider words longer than 3 characters
        word_importance[word] = count * len(word)

# Add some noise words that won't be used
noise_words = ["code", "syntax", "debug"]
for word in noise_words:
    word_importance[word] = len(word) * 2

# Extract words containing 'ing'
ing_words = [word for word in main_counts if 'ing' in word]

# Extract words from backup text for comparison
comparison_words = [word for word in backup_counts if len(word) > 5]

# Initialize scoring parameters
base_score = 10
multiplier = 2
decay_factor = 0.8

# Calculate a weighted score (not used in final answer)
weighted_score = base_score
for word in ing_words:
    weighted_score += main_counts.get(word, 0) * multiplier
    multiplier *= decay_factor

# Determine final words to analyze
final_words = []
for word in main_counts:
    if len(word) > 4 or word in ['fun', 'is']:
        final_words.append(word)

# Calculate total frequency importance
total_frequency = sum(word_importance[word] for word in final_words if word in word_importance)

# Apply an adjustment factor (distractor)
adjustment = sum(1 for word in final_words if word.startswith('p'))

print(f"Result: {total_frequency}")
