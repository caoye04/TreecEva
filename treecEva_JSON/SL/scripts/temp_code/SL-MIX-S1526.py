from functools import reduce

def decode_message(cipher_words, xor_key):
    decoded_words = []
    key_index = 0
    
    for word in cipher_words:
        decoded_chars = []
        for char_code in word:
            # Apply reverse XOR transformation with rotating key
            original_ascii = char_code ^ xor_key[key_index % len(xor_key)]
            decoded_chars.append(chr(original_ascii))
            key_index += 1
        decoded_words.append(''.join(decoded_chars))
    
    return decoded_words

def is_vowel(char):
    return char.lower() in 'aeiou'

def analyze_pattern(word):
    # Pattern: starts with consonant, ends with vowel, length > 3
    if len(word) <= 3:
        return False
    return (not is_vowel(word[0])) and is_vowel(word[-1])

# Ciphered message as list of lists (ASCII codes)
ciphered_message = [
    [115, 101, 99, 114, 101, 116],      # 'secret'
    [109, 101, 115, 115, 97, 103, 101],  # 'message'
    [116, 104, 105, 115],                # 'this'
    [105, 115],                          # 'is'
    [99, 111, 100, 101, 100]             # 'coded'
]

xor_mask = [4, 8, 15, 16, 23, 42]  # Lost-like cipher key

# Process the message
plaintext_words = decode_message(ciphered_message, xor_mask)

# Apply functional programming to count matches
vowel_set = frozenset('aeiouAEIOU')
word_properties = map(lambda w: (w, len(w), w[0] not in vowel_set, w[-1] in vowel_set), plaintext_words)
valid_words = filter(lambda item: item[1] > 3 and item[2] and item[3], word_properties)
matching_word_count = reduce(lambda acc, _: acc + 1, valid_words, 0)

print(f"Result: {matching_word_count}")