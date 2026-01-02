from collections import Counter

def calculate_char_frequency(text):
    return Counter(text.lower())

def filter_alpha_chars(char_dict):
    return {char: count for char, count in char_dict.items() if char.isalpha()}

def compute_weighted_score(freq_dict):
    score = 0
    for char, count in freq_dict.items():
        score += count * (ord(char) - ord('a') + 1)
    return score

def calculate_final_score(words):
    combined_text = ''.join(words)
    raw_freq = calculate_char_frequency(combined_text)
    filtered_freq = filter_alpha_chars(raw_freq)
    weighted_score = compute_weighted_score(filtered_freq)
    bonus = len(set(c for c in combined_text if c.isalpha()))
    return weighted_score + bonus

def main():
    word_list = ['challenge', 'reasoning', 'compute', 'logic']
    temp_var = [len(word) for word in word_list]
    total_score = calculate_final_score(word_list)
    print(f"Result: {total_score}")

if __name__ == "__main__":
    main()