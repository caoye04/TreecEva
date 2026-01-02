def compute_positional_entropy(text):
    total_entropy = 0.0
    char_frequency = {}
    for char in text:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    
    normalized_freq = {char: count / len(text) for char, count in char_frequency.items()}
    
    for index, (char, weight) in enumerate(zip(text, [normalized_freq[c] for c in text])):
        position = index + 1
        if position % 2 == 0:
            char_weight = weight * 1.5
        else:
            char_weight = weight * 0.8
        total_entropy += char_weight * position
    
    correction_factor = len(char_frequency)
    total_entropy /= correction_factor
    total_entropy = round(total_entropy, 4)
    print(f"Result: {total_entropy}")
    return total_entropy

compute_positional_entropy("abracadabra")