def calculate_similarity(s1, s2):
    # Irrelevant similarity calculation
    common_chars = set(s1.lower()) & set(s2.lower())
    unique_chars = set(s1.lower()) | set(s2.lower())
    return len(common_chars) / len(unique_chars) if unique_chars else 0

def process_keywords(text_data):
    # Misleading preprocessing
    words = text_data.split()
    processed = [w.strip('.,!?').lower() for w in words if len(w) > 2]
    frequencies = {}
    for word in processed:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

def analyze_sentiment(text):
    # Distractor function
    positive_words = {'good', 'great', 'excellent', 'best'}
    negative_words = {'bad', 'worst', 'terrible', 'poor'}
    
    words = text.lower().split()
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)
    
    if pos_count > neg_count:
        return 1
    elif neg_count > pos_count:
        return -1
    return 0

def calculate_final_priority(words, importance):
    # This is the key function that determines the answer
    if not words:
        return 0
    
    total = 0
    multiplier = 1
    
    for i, word in enumerate(words):
        # Check if word is uppercase and in importance map
        if word.isupper() and word.lower() in importance:
            value = importance[word.lower()] * 2
        elif word.lower() in importance:
            value = importance[word.lower()]
        else:
            value = len(word) % 5  # Fallback value based on length
        
        # Every third word gets special treatment
        if (i + 1) % 3 == 0:
            multiplier += value // 10
        else:
            total += value * multiplier
    
    # Apply a bitwise operation to the total
    bitwise_factor = (total & 15) + 1  # 15 is binary 1111
    
    return (total // bitwise_factor) + (len(words) % 4)

# Main processing starts here
text_corpus = "The QUICK brown FOX jumps OVER the lazy DOG and runs AWAY from hunters"

# Distractor calculations
sentiment = analyze_sentiment(text_corpus)
word_frequencies = process_keywords(text_corpus)
similarity_score = calculate_similarity("fox", "box")

# These are irrelevant calculations
total_chars = len(text_corpus)
unique_chars = len(set(text_corpus.lower()))
char_ratio = unique_chars / total_chars if total_chars else 0

# Extract words with capital letters (misleading approach)
all_words = text_corpus.split()
capitalized = [word for word in all_words if word[0].isupper()]

# This is the actual relevant processing
importance_map = {
    'quick': 15,
    'brown': 7,
    'fox': 20,
    'jumps': 12,
    'over': 8,
    'lazy': 5,
    'dog': 18,
    'away': 10
}

# Another distractor calculation
if sentiment > 0 and char_ratio > 0.5:
    importance_map['good'] = 25
    importance_map['great'] = 30

# Filter words that matter (key step)
filtered_words = [word for word in all_words if word.lower() in importance_map or word.isupper()]

# More distractor code
if len(capitalized) > len(filtered_words):
    filtered_words = capitalized
    importance_map = {k: v*2 for k, v in importance_map.items()}

# Calculate the priority score (this is the key statement)
priority_score = calculate_final_priority(filtered_words, importance_map)

# Misleading final adjustments
if sentiment < 0:
    priority_score -= 10
elif similarity_score > 0.5:
    priority_score += 5

# Print the result
print(f"Result: {priority_score}")
