def encode_token(token):
    return sum(ord(c) << (i*3) for i, c in enumerate(token))

def decode_token(encoded):
    token = ''
    while encoded > 0:
        token += chr(encoded & 0xFF)
        encoded >>= 3
    return token

token_set_a = {'knowledge', 'wisdom', 'understanding'}
token_set_b = {'wisdom', 'insight', 'comprehension'}
encoded_tokens_a = {encode_token(t) for t in token_set_a}
encoded_tokens_b = {encode_token(t) for t in token_set_b}
common_encoded = encoded_tokens_a & encoded_tokens_b
transform_map = {k: decode_token(k).upper() for k in common_encoded}
base_score = len(transform_map) if transform_map else 0
semantic_overlap_score = base_score + (10 if any('WISDOM' in v for v in transform_map.values()) else 0) and base_score * 2
print(f'Result: {semantic_overlap_score}')