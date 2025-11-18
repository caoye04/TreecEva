import itertools

def transform_char(c):
    return (ord(c) ^ 0x5C) & 0xFF

def generate_tokens(phrase):
    tokens = []
    for char in phrase:
        if char.isalpha():
            tokens.append(transform_char(char))
    return tokens

def compute_verification(tokens):
    pairs = list(itertools.combinations(tokens, 2))
    total = 0
    for a, b in pairs:
        xor_result = a ^ b
        if xor_result % 3 == 0:
            total += xor_result
    return total

secret_phrase = "CRYPTO"
token_list = generate_tokens(secret_phrase)
verification_code = compute_verification(token_list)
print(f"Result: {verification_code}")