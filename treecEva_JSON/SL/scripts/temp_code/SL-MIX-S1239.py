import heapq
import re
from itertools import combinations
from collections import namedtuple

# Define a phrase structure
terminal_phrase = namedtuple('Phrase', ['priority', 'content'])

# Initialize processing components
linguistic_heap = []
transformation_rules = [
    (r'\b(\w+)ly\b', r'\1'),
    (r'\b(un|re|pre)(\w+)\b', r'\2'),
    (r'[^a-zA-Z\s]', '')
]

# Populate heap with phrases
input_phrases = [
    terminal_phrase(3, 'The researcher carefully examined the data'),
    terminal_phrase(1, 'Unexpected discoveries were made'),
    terminal_phrase(2, 'Preprocessing involves cleaning textual data')
]

for phrase in input_phrases:
    heapq.heappush(linguistic_heap, phrase)

# Process phrases with transformations
processed_count = 0
semantic_score = 0

while linguistic_heap:
    current_phrase = heapq.heappop(linguistic_heap)
    text_content = current_phrase.content.lower()
    
    # Apply transformations
    for pattern, replacement in transformation_rules:
        text_content = re.sub(pattern, replacement, text_content)
    
    # Clean whitespace
    text_content = ' '.join(text_content.split())
    
    # Extract words for combinatorial analysis
    word_list = text_content.split()
    
    # Calculate semantic weight through pairwise combinations
    if len(word_list) >= 2:
        pair_combinations = list(combinations(word_list, 2))
        semantic_weight = sum(
            len(pair[0]) * len(pair[1]) 
            for pair in pair_combinations
        )
        semantic_score += semantic_weight // len(pair_combinations)
    
    processed_count += 1

# Final adjustment based on processing order
semantic_score = semantic_score ^ (processed_count * 7)

print(f'Result: {semantic_score}')