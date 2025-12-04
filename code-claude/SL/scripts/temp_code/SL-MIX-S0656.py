from collections import Counter
import string

# Document analysis function
def analyze_text(document, keywords):
    # Clean and split the document
    document = document.lower()
    for symbol in string.punctuation:
        document = document.replace(symbol, ' ')
    words = document.split()
    
    # Calculate word frequencies
    word_frequencies = Counter(words)
    
    # Extract statistics
    total_words = len(words)
    unique_words = len(word_frequencies)
    avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
    
    # Keywords tracking
    keyword_appearances = sum(word_frequencies[keyword] for keyword in keywords if keyword in word_frequencies)
    keyword_density = keyword_appearances / total_words if total_words > 0 else 0
    
    # Advanced filtering parameters
    min_length = 5
    frequency_threshold = 2
    importance_factor = keyword_density * 10
    
    # Process rare and common words
    rare_words = [word for word, count in word_frequencies.items() if count == 1]
    common_words = {word: count for word, count in word_frequencies.items() if count > 3}
    
    # Calculate word diversity score
    diversity_score = (unique_words / total_words * 100) if total_words > 0 else 0
    adjusted_score = diversity_score - importance_factor
    
    # Filter words based on frequency and length criteria
    filtered_count = sum(1 for word, count in word_frequencies.items() if count > frequency_threshold and len(word) >= min_length)
    
    # Unnecessary but distracting calculation
    potential_keywords = [(word, count * len(word)) for word, count in word_frequencies.items() 
                          if word not in keywords and len(word) > 3]
    potential_keywords.sort(key=lambda x: x[1], reverse=True)
    
    print(f"Result: {filtered_count}")
    return {
        'total_words': total_words,
        'unique_words': unique_words,
        'filtered_words': filtered_count,
        'keyword_density': keyword_density
    }

# Sample document
document = "Python is a versatile programming language. Python supports multiple programming paradigms including object-oriented, imperative and functional programming styles. Python is often praised for its simple syntax that emphasizes readability."

# Analyze with specific keywords
keywords = ['python', 'programming', 'language']
results = analyze_text(document, keywords)