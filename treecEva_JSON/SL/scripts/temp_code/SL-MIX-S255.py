from collections import Counter

def modular_power(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def process_cipher_text(text):
    tokens = list(text)
    freq_map = Counter(tokens)
    position_weights = {}
    for i, char in enumerate(tokens):
        if char not in position_weights:
            position_weights[char] = 0
        position_weights[char] += (i + 1) * freq_map[char]
    
    accumulator = 0
    for char, weight in position_weights.items():
        mod_weight = weight % 13
        accumulator = (accumulator + mod_weight * ord(char)) % 1000
    
    return accumulator

cipher_message = "HELLO WORLD TEST MESSAGE"
normalized_message = ''.join(filter(str.isalpha, cipher_message.upper()))
intermediate_value = process_cipher_text(normalized_message)
checksum = modular_power(intermediate_value, 17, 1000000007)
print(f"Result: {checksum}")