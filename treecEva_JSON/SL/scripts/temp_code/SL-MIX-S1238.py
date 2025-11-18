import re
from collections import Counter

def analyze_literature():
    excerpt_one = "To be or not to be, that is the question. Whether 'tis nobler in the mind to suffer."
    excerpt_two = "All the world's a stage, and all the men and women merely players."
    
    # Extract words using regex, converting to lowercase
    words_one = re.findall(r"\b[a-zA-Z]+\b", excerpt_one.lower())
    words_two = re.findall(r"\b[a-zA-Z]+\b", excerpt_two.lower())
    
    # Create sets of unique words
    unique_words_one = frozenset(words_one)
    unique_words_two = frozenset(words_two)
    
    # Find intersection and difference
    common_vocabulary = unique_words_one & unique_words_two
    distinct_vocabulary = unique_words_one - unique_words_two
    
    # Count word frequencies
    frequency_counter = Counter(words_one + words_two)
    
    # Calculate base score from distinct vocabulary
    base_score = len(distinct_vocabulary)
    
    # Apply frequency weighting: only words appearing once contribute
    weighted_terms = {word for word, count in frequency_counter.items() if count == 1}
    
    # Intersection of distinct vocabulary with single-occurrence words
    significant_lexicon = distinct_vocabulary & weighted_terms
    
    # Initialize score
    lexicon_score = 0
    
    # Iterate through significant lexicon to calculate score
    for term in significant_lexicon:
        if term.startswith('t'):
            lexicon_score += 3
        elif term.endswith('er'):
            lexicon_score += 2
        else:
            lexicon_score += 1
        
        # Early termination condition
        if lexicon_score > 15:
            lexicon_score -= 5
            break
    
    # Final adjustment using lambda
    adjust = lambda x: x * 2 if x % 2 == 0 else x + 1
    lexicon_score = adjust(lexicon_score)
    
    return lexicon_score

# Execute the analysis
lexicon_score = analyze_literature()
print(f"Target result: {lexicon_score}")