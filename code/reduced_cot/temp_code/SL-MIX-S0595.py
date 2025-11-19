from collections import defaultdict

def process_cryptographic_terms(token_list, depth=0):
    if depth > 3:
        return {}
    
    base_frequency = defaultdict(int)
    for token in token_list:
        if len(token) > 3 and token.isalnum():
            transformed_token = token[::-1].upper()
            base_frequency[transformed_token] += 1
    
    # Recursive processing for nested structures
    nested_tokens = [t for t in token_list if '(' in t]
    if nested_tokens and depth < 3:
        nested_frequency = process_cryptographic_terms(nested_tokens, depth + 1)
        # Merge frequencies with weighting
        for key, value in nested_frequency.items():
            base_frequency[key] += value * 2
    
    return dict(base_frequency)

def calculate_weighted_score(freq_map):
    score = 0
    for term, count in freq_map.items():
        # Apply cryptographic significance weighting
        weight_factor = sum(ord(c) for c in term) % 7
        score += count * weight_factor
    return score

document_tokens = [
    "AES", "rsa(2048)", "SHA256", "md5(hash)", 
    "ECC(curve)", "blake2b", "scrypt(key)", "pbkdf2",
    "hmac(sha256)", "argon2", "bcrypt(salt)"
]

# Process tokens through recursive analyzer
frequency_analysis = process_cryptographic_terms(document_tokens)

# Calculate final cryptographic score
final_cryptographic_score = calculate_weighted_score(frequency_analysis)

print(f"Result: {final_cryptographic_score}")