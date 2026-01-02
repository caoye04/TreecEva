def analyze_segments(text_blocks):
    word_frequencies = {}
    total_chars = 0
    segment_count = len(text_blocks)
    
    for block in text_blocks:
        words = block.lower().split()
        block_char_count = sum(len(word) for word in words)
        total_chars += block_char_count
        
        for word in words:
            cleaned_word = ''.join(filter(str.isalpha, word))
            if cleaned_word:
                word_frequencies[cleaned_word] = word_frequencies.get(cleaned_word, 0) + 1

    avg_length = total_chars / len(words) if words else 0
    unique_words = len(word_frequencies)
    
    # Distractor: irrelevant statistical computation
    variance_proxy = sum((len(w) - avg_length) ** 2 for w in words if w.isalpha()) / (len(words) + 1)
    
    return word_frequencies, unique_words, variance_proxy


def calculate_diversity_score(freq_dict, threshold=2):
    # Uses dictionary and filtering with list comprehension
    common_words = [word for word, count in freq_dict.items() if count >= threshold]
    rare_words = [word for word, count in freq_dict.items() if count == 1]
    diversity_index = len(rare_words) - len(common_words)
    
    # Misleading normalization (not used later)
    normalized_diversity = diversity_index / (len(common_words) + 1)
    
    return diversity_index


def calculate_final_score(blocks):
    frequencies, unique_count, var_proxy = analyze_segments(blocks)
    
    # Real computation path
    base_score = sum(frequencies.values())
    diversity_bonus = calculate_diversity_score(frequencies)
    
    # Irrelevant intermediate calculations (distractors)
    temp_weights = [len(k) * v for k, v in frequencies.items() if v > 1]
    adjustment_factor = sum(temp_weights) / (len(temp_weights) + 1e-5)
    decay_correction = adjustment_factor * 0.03  # Never actually applied
    
    # Core logic
    raw_score = base_score + diversity_bonus * 5
    scaling_factor = len(blocks) / 2
    final_score = int(raw_score / scaling_factor) if scaling_factor != 0 else 0
    
    # Print to ensure visibility
    print(f"Target result: {final_score}")
    return final_score

# Input data
document_segments = [
    "The signal integrity improves with proper shielding.",
    "Noise reduction is critical in high-frequency circuits.",
    "Signal reflections can distort transmission waveforms.",
    "Impedance matching minimizes energy loss."
]

# Execute
final_score = calculate_final_score(document_segments)