def calculate_final_score(raw_data):
    # Preprocessing: clean and transform data
    cleaned = list(filter(lambda x: isinstance(x, str), raw_data))
    upper_case = [s.upper() for s in cleaned]
    lengths = [len(s) for s in upper_case]

    # Irrelevant distraction: character frequency analysis (not used)
    char_freq = {}
    for s in upper_case:
        for c in s:
            char_freq[c] = char_freq.get(c, 0) + 1
    avg_freq = sum(char_freq.values()) / len(char_freq) if char_freq else 0

    # Core logic: count strings with even length and vowels
    has_vowel = lambda s: any(v in s for v in 'AEIOU')
    even_with_vowel = 0
    for s in upper_case:
        if len(s) % 2 == 0 and has_vowel(s):
            even_with_vowel += 1

    # Secondary path: sum of lengths at prime indices (semi-relevant)
    primes = [2, 3, 5, 7, 11]
    prime_index_sum = sum(lengths[i] for i in primes if i < len(lengths))

    # Tertiary distraction: set operations on unique characters
    unique_chars = set()
    for s in upper_case:
        unique_chars.update(s)
    vowel_set = {'A', 'E', 'I', 'O', 'U'}
    consonant_count = len(unique_chars - vowel_set)

    # Final computation: mix of relevant metrics
    base_score = even_with_vowel * 7
    bonus = prime_index_sum // 10 if prime_index_sum > 50 else 5
    final_score = base_score + bonus

    return final_score

# Input data with mixed types (strings, numbers, etc.)
data = ['hello', 42, 'world', 'AI', 'Python', None, 'Open', 'GPT', 3.14, 'xyz']

# Execution point
final_score = calculate_final_score(data)
print(f"Result: {final_score}")