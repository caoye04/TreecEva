import itertools
from functools import reduce

def analyze_data_patterns(data_stream):
    # Analyze patterns in data (distractor function)
    pattern_counts = {}
    for i in range(len(data_stream) - 2):
        pattern = data_stream[i:i+3]
        if pattern in pattern_counts:
            pattern_counts[pattern] += 1
        else:
            pattern_counts[pattern] = 1
    
    # Calculate entropy score (unused)
    entropy = sum([-count/len(data_stream) * (count/len(data_stream)) 
                  for count in pattern_counts.values()])
    return pattern_counts, entropy

def decrypt_message(message, key):
    # Simple XOR decryption
    result = ""
    for i, char in enumerate(message):
        result += chr(ord(char) ^ (ord(key[i % len(key)])))
    return result

def optimize_key_sequence(key_data):
    # Distractor function that creates an optimized sequence
    optimized = []
    for k in key_data:
        if isinstance(k, int) and k % 2 == 0:
            optimized.append(k // 2)
        elif isinstance(k, str):
            optimized.append(sum(ord(c) for c in k))
        else:
            optimized.append(42)  # Default fallback
    return optimized

def calculate_security_metrics(data):
    # Calculate letter frequencies
    freq = {}
    for char in data:
        if char.isalpha():
            char = char.lower()
            freq[char] = freq.get(char, 0) + 1
    
    # Calculate security metrics
    unique_chars = len(freq)
    most_common = max(freq.values()) if freq else 0
    least_common = min(freq.values()) if freq else 0
    
    # Calculate a meaningless ratio (distractor)
    ratio = most_common / least_common if least_common > 0 else 0
    
    return unique_chars, most_common, ratio

def calculate_checksum(data):
    # Calculate a simple checksum
    return sum(ord(c) for c in data) % 256

def calculate_final_score(encrypted_data, decryption_key):
    # Decrypt the message first
    decrypted = decrypt_message(encrypted_data, decryption_key)
    
    # Calculate various metrics
    unique_chars, char_frequency, ratio = calculate_security_metrics(decrypted)
    
    # Analyze patterns (distractor)
    patterns, entropy = analyze_data_patterns(decrypted)
    
    # This is a distractor - not used in final calculation
    key_sequence = optimize_key_sequence([5, "abc", 7, "xyz", 12])
    
    # Calculate checksum
    checksum = calculate_checksum(decrypted)
    
    # Generate combinations for analysis (distractor)
    combinations = list(itertools.combinations(range(5), 3))
    permutations = list(itertools.permutations(decryption_key[:3]))
    
    # This is the actual security score calculation
    word_count = len([w for w in decrypted.split() if len(w) > 2])
    security_metric = (unique_chars * 5) + (word_count * 3) + checksum
    
    # Normalize between 0-100
    normalized_score = min(100, max(0, security_metric))
    
    # Apply bitwise operations to create final score
    bit_factor = (normalized_score & 0x3F) | 0x20
    security_score = bit_factor ^ (len(decrypted) % 16)
    
    return security_score

# Main execution
encrypted_data = "Vjkr$ku#c#vguv#oguucig$hqt%vjg$rtqitcookpi$vcum"
decryption_key = "CIPHER"

# Distractor operations
all_keys = []
for i in range(3, 8):
    all_keys.extend(list(itertools.combinations(decryption_key, i)))

# More distractor calculations
key_variants = {}
for i, c in enumerate(decryption_key):
    key_variants[c] = (i * ord(c)) % 256

# Calculate intermediate values (distractors)
intermediate_sum = sum(ord(c) for c in encrypted_data)
intermediate_product = reduce(lambda x, y: (x * ord(y)) % 1000, encrypted_data, 1)

# Calculate the final security score
security_score = calculate_final_score(encrypted_data, decryption_key)

# Print various results to confuse
print(f"Encrypted length: {len(encrypted_data)}")
print(f"Key variants: {sum(key_variants.values())}")
print(f"Intermediate calculations: {intermediate_sum}, {intermediate_product}")
print(f"Result: {security_score}")