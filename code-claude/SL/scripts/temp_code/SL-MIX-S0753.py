from collections import Counter, defaultdict

def analyze_text(text):
    # Create frequency counter for characters
    char_counts = Counter(text.lower())
    
    # Initialize dictionaries for analysis
    letter_scores = defaultdict(int)
    word_stats = defaultdict(int)
    
    # Assign scores to each letter (a=1, b=2, etc.)
    for char in 'abcdefghijklmnopqrstuvwxyz':
        letter_scores[char] = ord(char) - ord('a') + 1
    
    # Split text into words and analyze
    words = text.lower().split()
    unique_words = set(words)
    
    # Calculate various metrics
    total_chars = len(text)
    filtered_chars = sum(char_counts[c] for c in char_counts if c.isalpha())
    
    # Track word lengths
    word_lengths = [len(word) for word in words]
    avg_length = sum(word_lengths) / len(words) if words else 0
    
    # Calculate word importance based on frequency and length
    word_importance = {}
    for word in unique_words:
        frequency = words.count(word)
        word_importance[word] = frequency * len(word)
    
    # Find most important word
    most_important = max(word_importance.items(), key=lambda x: x[1])[0] if word_importance else ""
    
    # Calculate letter value of most important word
    important_value = sum(letter_scores[c] for c in most_important if c in letter_scores)
    
    # Apply weighting based on text statistics
    base_score = important_value * 5
    length_factor = int(avg_length * 2)
    uniqueness_factor = len(unique_words) - len(words) // 2
    
    # Calculate final score
    total_score = base_score + length_factor + uniqueness_factor
    word_weight = total_score // 10
    
    # Apply modifier based on character distribution
    vowel_count = sum(char_counts.get(c, 0) for c in 'aeiou')
    consonant_count = filtered_chars - vowel_count
    
    if vowel_count > consonant_count:
        modifier = 15
    else:
        modifier = 7
    
    # This adjustment doesn't affect the final answer
    adjusted_weight = word_weight + modifier
    
    print(f"Result: {word_weight}")
    return word_weight

# Sample text to analyze
sample_text = "Python is a versatile programming language"
result = analyze_text(sample_text)