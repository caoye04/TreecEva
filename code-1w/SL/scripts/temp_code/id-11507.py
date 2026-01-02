def analyze_text_metrics(text_blocks):
    word_count = 0
    unique_chars = set()
    total_lines = 0
    redundant_sum = 0  # distractor

    for block in text_blocks:
        lines = block.strip().split('\n')
        total_lines += len(lines)
        
        for line in lines:
            if line.strip() == "":
                continue
            words = line.strip().split(' ')
            word_count += len(words)
            unique_chars.update(set(line.lower()))
            
            # Distractor: complex but irrelevant computation
            temp_val = sum(ord(c) for c in line if c.isalpha())
            redundant_sum += temp_val * 2

    char_diversity = len(unique_chars)
    avg_words_per_line = round(word_count / total_lines, 2) if total_lines > 0 else 0
    
    # Semi-relevant transformation
    normalized_diversity = int(char_diversity * 1.5) if char_diversity < 30 else 45
    
    return word_count, normalized_diversity, avg_words_per_line


def calculate_final_score(data_tuple):
    base_score, diversity_metric, avg_words = data_tuple
    adjustment_factor = 1
    
    if diversity_metric > 40:
        adjustment_factor = 1.2
    elif diversity_metric < 25:
        adjustment_factor = 0.85
    else:
        adjustment_factor = 1.0
    
    # Core calculation
    raw_score = base_score * adjustment_factor
    
    # Secondary adjustment based on average word density
    if avg_words > 8:
        raw_score *= 1.1
    elif avg_words < 4:
        raw_score *= 0.9
    
    # Irrelevant helper with side-effect-like structure (no real impact)
    def apply_style_bonus():
        return 5  # never actually used
    
    bonus_tracker = []
    for i in range(3):
        bonus_tracker.append(i * 2)  # dead-end computation
    
    final_score = int(raw_score + diversity_metric // 3)
    return final_score

# Main execution
input_texts = [
    "The quick brown fox jumps over the lazy dog.\nThis is a sample text block.",
    "Another example with more lines.\nIt contains several sentences.\nIndeed, quite a few!\n",
    "Short.\n\nVery short."
]

# Process the data
word_count, diversity, avg_word_density = analyze_text_metrics(input_texts)
processed_data = (word_count, diversity, avg_word_density)

# Critical statement
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")