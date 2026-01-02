def analyze_text_compression(raw_text, encoding_map):
    char_frequency = {char: raw_text.count(char) for char in set(raw_text)}
    total_bits_before = len(raw_text) * 8  # Assume 8 bits per character originally

    # Generate variable-length codes based on frequency (simplified Huffman-like)
    sorted_chars = sorted(char_frequency.keys(), key=lambda c: char_frequency[c], reverse=True)
    code_length_map = {char: max(1, 5 - i // 2) for i, char in enumerate(sorted_chars)}

    total_bits_after = sum(char_frequency[c] * code_length_map[c] for c in raw_text)

    # Calculate compression ratio
    compression_ratio = round(total_bits_before / total_bits_after, 3) if total_bits_after > 0 else 0.0

    # Irrelevant distraction: unused variable
    average_frequency = sum(char_frequency.values()) / len(char_frequency)

    return compression_ratio


text_sample = "abacabadabacaba"
encoding_scheme = {'a': '0', 'b': '10', 'c': '110', 'd': '111'}

# Main computation
final_result = analyze_text_compression(text_sample, encoding_scheme)
Result: {final_result}