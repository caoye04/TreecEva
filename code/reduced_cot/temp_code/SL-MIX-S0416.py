def encode_char(c, shift):
    if c.isalpha():
        base = ord('a') if c.islower() else ord('A')
        return chr((ord(c) - base + shift) % 26 + base)
    return c

def decode_char(c, shift):
    return encode_char(c, -shift)

def process_data(messages, pattern):
    decoded_chars = []
    temp_sum = 0
    bit_mask = 0b10101010
    
    for i, msg in enumerate(messages):
        decoded = [decode_char(c, pattern[i % len(pattern)]) for c in msg]
        decoded_chars.extend(decoded)
        temp_sum += len(msg) * (i + 1)
    
    char_count = {}
    for char in decoded_chars:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    
    irrelevant_calc = sum(ord(c) for c in ''.join(decoded_chars)) % 1000
    bit_ops = (temp_sum & bit_mask) | (irrelevant_calc ^ 0xFF)
    
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for c in decoded_chars if c in vowels)
    consonant_count = sum(1 for c in decoded_chars if c.isalpha() and c not in vowels)
    
    final_count = vowel_count * 3 - consonant_count + (bit_ops % 10)
    return final_count

encoded_messages = ['Khoor', 'Zruog', 'Wkhuh']
key_pattern = [3, 3, 3]
backup_data = [5, 8, 2, 7]
unused_var = sum(backup_data) * 2
placeholder_result = len(encoded_messages[0]) ** 2

result = process_data(encoded_messages, key_pattern)
print(f"Target result: {result}")