from collections import Counter, defaultdict

def calculate_sentiment(text):
    positive_words = {'good', 'great', 'excellent', 'best', 'amazing'}
    negative_words = {'bad', 'worst', 'terrible', 'awful', 'poor'}
    
    words = text.lower().split()
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)
    
    # Return sentiment score
    return pos_count - neg_count

def analyze_character_distribution(text):
    char_counts = Counter(text.lower())
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = {c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in vowels}
    
    vowel_count = sum(char_counts[v] for v in vowels)
    consonant_count = sum(char_counts[c] for c in consonants)
    
    # Misleading calculation - not used in final result
    ratio = vowel_count / max(consonant_count, 1)
    return vowel_count, consonant_count, ratio

def keyword_impact(text, keywords):
    # Count occurrences of each keyword
    word_freq = defaultdict(int)
    for word in text.lower().split():
        word_freq[word] += 1
    
    # Calculate impact score for relevant keywords
    impact = 0
    for keyword in keywords:
        if keyword in word_freq:
            # Position bonus - earlier keywords have more impact
            position = text.lower().find(keyword)
            position_factor = 1.0 if position < 0 else max(0.5, 1 - position / len(text))
            
            # Frequency factor
            freq_factor = min(3, word_freq[keyword])
            
            # Calculate impact contribution
            keyword_score = position_factor * freq_factor * len(keyword)
            impact += keyword_score
    
    return impact

def calculate_priority(text, keywords):
    # Extract document statistics - these are actually used
    sentiment = calculate_sentiment(text)
    vowels, consonants, _ = analyze_character_distribution(text)
    
    # Misleading calculations - not used in final result
    complexity_score = len(set(text.split())) / max(len(text.split()), 1)
    redundancy_factor = sum(1 for word in text.split() if len(word) > 5) / max(len(text.split()), 1)
    
    # Calculate keyword impact - this is used
    impact = keyword_impact(text, keywords)
    
    # More misleading variables
    potential_score = (sentiment * 2) + (impact / 3) - (complexity_score * 10)
    adjusted_score = potential_score * (1 + redundancy_factor)
    
    # Dead code path - never executed
    if complexity_score > 0.9 and redundancy_factor < 0.2:
        return adjusted_score * 1.5
    
    # Actual priority calculation
    base_priority = 10 + sentiment * 2
    keyword_modifier = min(15, impact / 2)
    character_factor = min(5, vowels / 10)
    
    # The actual formula that matters
    priority_score = base_priority + keyword_modifier + character_factor
    
    return round(priority_score, 2)

# Test document
document_text = "The excellent research paper presents important findings about climate patterns. The analysis methods are great but some data sources might need verification. Overall this work provides good insights."

# Irrelevant keywords - not used
false_keywords = ['research', 'analysis', 'climate', 'patterns']

# The keywords that matter
true_keywords = ['excellent', 'important', 'climate', 'good']

# Misleading calculations
doc_length = len(document_text)
word_count = len(document_text.split())
complexity = doc_length / word_count

# Distraction: Calculate an alternative priority using different approach
alt_priority = word_count * 0.5 + complexity * 10

# The actual calculation we're interested in
priority_score = calculate_priority(document_text, true_keywords)

# Misleading final adjustments
final_score = priority_score * 0.8 + alt_priority * 0.2
adjusted_priority = final_score + (doc_length / 100)

print(f"Result: {priority_score}")