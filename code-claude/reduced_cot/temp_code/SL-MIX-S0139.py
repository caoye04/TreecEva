from collections import Counter, defaultdict
import itertools

def analyze_text(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = ''.join(c.lower() if c.isalpha() or c.isspace() else ' ' for c in text)
    
    # Split into words
    words = [word for word in cleaned_text.split() if word]
    
    # Count word occurrences (not directly used for final answer)
    word_counts = Counter(words)
    most_common_word = word_counts.most_common(1)[0][0] if words else ''
    
    # Group words by their first letter
    words_by_first_letter = defaultdict(list)
    for word in words:
        if word:
            words_by_first_letter[word[0]].append(word)
    
    # Calculate word lengths
    word_lengths = [len(word) for word in words]
    avg_length = sum(word_lengths) / len(words) if words else 0
    
    # Find the most frequent word length
    frequency_lengths = Counter(word_lengths)
    most_frequent_word_length = frequency_lengths.most_common(1)[0][0]
    
    # Calculate some statistics (distractors)
    unique_letters = set(''.join(words))
    letter_frequency = Counter(''.join(words))
    most_common_letter = letter_frequency.most_common(1)[0][0] if letter_frequency else ''
    
    # Create pairs of adjacent words (distractor)
    word_pairs = list(itertools.pairwise(words)) if hasattr(itertools, 'pairwise') else list(zip(words, words[1:]))
    pair_count = len(word_pairs)
    
    # Calculate a meaningless score (distractor)
    arbitrary_score = sum(ord(c) % 10 for c in most_common_word) if most_common_word else 0
    
    return most_frequent_word_length

# Sample text for analysis
sample_text = "The quick brown fox jumps over the lazy dog. The dog was not very impressed by this stunt."

result = analyze_text(sample_text)
print(f"Result: {result}")
