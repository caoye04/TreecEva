from collections import Counter, defaultdict
import itertools

def analyze_document(text):
    # Normalize the text for processing
    text = text.lower()
    
    # Remove some common punctuation
    for char in ',.!?;:()':
        text = text.replace(char, ' ')
    
    # Split into words
    words = text.split()
    
    # Count word frequencies
    word_counts = Counter(words)
    
    # Track statistics
    total_words = len(words)
    unique_words = len(word_counts)
    
    # Find words with specific patterns
    starts_with_a = [word for word in word_counts.keys() if word.startswith('a')]
    ends_with_s = [word for word in word_counts.keys() if word.endswith('s')]
    
    # Create a lookup for words by length
    words_by_length = defaultdict(list)
    for word in word_counts.keys():
        words_by_length[len(word)].append(word)
    
    # Find duplicates (words appearing more than once)
    duplicates = {word for word, count in word_counts.items() if count > 1}
    
    # Calculate average word length (not used in final result)
    avg_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
    
    # Count words that are at least 4 characters
    valid_length_words = sum(1 for word in word_counts if len(word) >= 4)
    
    # Count words that don't contain the letter 'e'
    no_e_words = sum(1 for word in word_counts if 'e' not in word)
    
    # This is the key calculation
    count_valid_words = valid_length_words + no_e_words
    
    # Identify potential keywords (not used in final result)
    keywords = [word for word, count in word_counts.items() 
               if len(word) >= 5 and count >= 2]
    
    # Calculate final count - this is the target statement
    final_count = count_valid_words - len(duplicates)
    
    return {
        'total_words': total_words,
        'unique_words': unique_words,
        'starts_with_a': len(starts_with_a),
        'ends_with_s': len(ends_with_s),
        'average_length': avg_length,
        'valid_words': count_valid_words,
        'no_e_words': no_e_words,
        'duplicates': len(duplicates),
        'final_count': final_count
    }

# Sample document text
document = "A python program analyzes text documents. The program counts words and tracks statistics. Python makes text analysis simple and efficient. Programs need careful testing."

# Analyze the document
results = analyze_document(document)

# Print the target result
print(f"Result: {results['final_count']}")