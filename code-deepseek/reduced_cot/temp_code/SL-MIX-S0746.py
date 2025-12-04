def encrypt_transform(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def analyze_frequency(data):
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    return freq_map

def process_security_data(messages, key_factor):
    temp_sum = 0
    irrelevant_computation = 42 * 3.14159
    
    for idx, msg in enumerate(messages):
        transformed = encrypt_transform(msg, key_factor)
        char_count = len([c for c in transformed if c.isalpha()])
        
        if idx % 2 == 0:
            temp_sum += char_count * (idx + 1)
        else:
            temp_sum -= char_count // 2
    
    # Misleading intermediate calculation
    decoy_value = temp_sum * 2 - irrelevant_computation
    
    frequency_data = analyze_frequency([''.join(sorted(msg)) for msg in messages])
    pattern_weight = sum(frequency_data.values()) // len(messages)
    
    # Dead code path that doesn't affect result
    if pattern_weight > 10:
        unused_value = pattern_weight * 3
    else:
        unused_value = pattern_weight // 2
    
    # Final computation with bit operations
    crypto_key = (temp_sum ^ pattern_weight) & 0xFF
    
    # Additional misleading operations
    distraction = crypto_key << 2
    another_distraction = crypto_key | 0xAA
    
    return crypto_key

encoded_messages = ['hello', 'world', 'python', 'secure', 'data']
result = process_security_data(encoded_messages, 5)
crypto_key = result + 0

print(f"Target result: {crypto_key}")