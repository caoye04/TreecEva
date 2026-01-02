from itertools import combinations, chain

def analyze_text_segments(text_blocks):
    # Preprocess: clean and normalize text blocks
    cleaned = [block.strip().lower() for block in text_blocks]
    tokenized = [block.split() for block in cleaned]
    
    # Compute various metrics (some are distractions)
    word_count = sum(len(tokens) for tokens in tokenized)
    unique_words = len(set(chain.from_iterable(tokenized)))
    avg_word_length = sum(len(word) for word in chain.from_iterable(tokenized)) / word_count if word_count else 0
    
    # Segment analysis (relevant)
    segment_pairs = list(combinations(tokenized, 2))
    overlap_scores = []
    for a, b in segment_pairs:
        set_a, set_b = set(a), set(b)
        intersection = len(set_a & set_b)
        union = len(set_a | set_b)
        jaccard = intersection / union if union else 0
        overlap_scores.append(jaccard)
    
    # Distraction: character frequency analysis
    char_freq = {}
    for char in chain.from_iterable(cleaned):
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    top_chars = sorted(char_freq.items(), key=lambda x: -x[1])[:5]
    
    # Distraction: sentence complexity proxy (not used)
    complexity_score = 0
    for tokens in tokenized:
        if len(tokens) > 10:
            complexity_score += 1
        if any(len(word) > 8 for word in tokens):
            complexity_score += 0.5
    
    # Key logic: weighted score based on overlaps
    total_overlap = sum(overlap_scores)
    pair_count = len(overlap_scores)
    normalized_overlap = total_overlap / pair_count if pair_count else 0
    
    # Final aggregation with irrelevant adjustment
    adjustment_factor = 0.9 + (unique_words / 1000)  # minor influence
    final_score = int((normalized_overlap * 1000) * adjustment_factor)
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
input_texts = [
    "The quick brown fox jumps over the lazy dog repeatedly",
    "A fast auburn fox leaps above a sleepy canine multiple times",
    "The agile fox vaults over the inactive hound again and again"
]

# Execute
final_score = analyze_text_segments(input_texts)