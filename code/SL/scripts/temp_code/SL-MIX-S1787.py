import hashlib
from functools import reduce

def tokenize_packet(packet_str):
    return [token.strip() for token in packet_str.split(';') if token.strip()]

def compute_hash(token):
    return int(hashlib.md5(token.encode()).hexdigest(), 16) % 1000

def is_suspicious_token(token_hash):
    # Suspicious if hash ends in binary pattern 101 or 110
    return (token_hash & 0b111) == 0b101 or (token_hash & 0b111) == 0b110

def evaluate_packet_security(tokens):
    hashes = list(map(compute_hash, tokens))
    suspicious_flags = list(map(is_suspicious_token, hashes))
    
    # Short-circuit: if any token is suspicious and its hash > 500
    high_risk = any(flag and hash_val > 500 for flag, hash_val in zip(suspicious_flags, hashes))
    
    # Compute base score as sum of hashes where token is not suspicious
    base_score = sum(hash_val for flag, hash_val in zip(suspicious_flags, hashes) if not flag)
    
    # Adjust score based on high risk
    adjusted_score = base_score >> 2 if high_risk else base_score << 1
    
    return adjusted_score

# Packet data
packet_stream = "auth;login;admin;;reset;execute;;config;update"
tokens = tokenize_packet(packet_stream)

# Evaluate security
final_security_score = evaluate_packet_security(tokens)
print(f"Result: {final_security_score}")