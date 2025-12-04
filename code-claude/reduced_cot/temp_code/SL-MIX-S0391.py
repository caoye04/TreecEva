from collections import Counter, defaultdict
from itertools import chain

def analyze_text_data(text):
    # Split text into words and clean
    words = [word.strip('.,!?;:()[]{}"\'\'').lower() for word in text.split()]
    
    # Create dictionary to track word frequencies by length
    length_to_words = defaultdict(list)
    for word in words:
        if word:  # Skip empty strings after cleaning
            length_to_words[len(word)].append(word)
    
    # Calculate average word length (not used in final result)
    total_length = sum(len(word) for word in words if word)
    avg_length = total_length / len([w for w in words if w]) if words else 0
    
    # Count occurrences of each word length
    word_lengths = [len(word) for word in words if word]
    word_length_counts = Counter(word_lengths)
    
    # Find the most frequent word length
    most_frequent_word_length = word_length_counts.most_common(1)[0][0]
    
    # Calculate letter frequency (distraction)
    letter_counts = Counter(chain.from_iterable(words))
    most_common_letter = letter_counts.most_common(1)[0][0] if letter_counts else ''
    
    # Track words with the most frequent length (not used in final calculation)
    frequent_length_words = length_to_words[most_frequent_word_length]
    unique_frequent_words = set(frequent_length_words)
    
    # Calculate a complexity score (distraction)
    complexity_score = avg_length * len(unique_frequent_words) / 10
    
    return most_frequent_word_length, complexity_score, most_common_letter

# Sample text for analysis
sample_text = "Python is a programming language that lets you work quickly and integrate systems effectively. Its elegant syntax and dynamic typing make it an ideal language for scripting and rapid application development."

result, complexity, common_letter = analyze_text_data(sample_text)
print(f"Result: {result}")