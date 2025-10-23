import hashlib

def encode_message(msg):
    return ''.join(chr(ord(c) ^ 0b10101010) for c in msg)

def calculate_hash_prefix(data, length=8):
    return hashlib.sha256(data.encode()).hexdigest()[:length]

message_log = ['ALPHA', 'BRAVO', 'CHARLIE']
encoded_messages = list(map(encode_message, message_log))
hashes = [calculate_hash_prefix(m) for m in encoded_messages]

combined_hashes = ''.join(hashes)
security_flags = [len(h) > 4 and h[0] in '0123456789' for h in hashes]
valid_transmissions = sum(security_flags)

admin_override = False
system_integrity = True

security_clearance_level = valid_transmissions * 2 if admin_override or system_integrity else 0
security_clearance_level += (sum(map(lambda x: int(x, 16), hashes[0][:4])) & 0xF) if any(security_flags) else 0

print(f'Result: {security_clearance_level}')