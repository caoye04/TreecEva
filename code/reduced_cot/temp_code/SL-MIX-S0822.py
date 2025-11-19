def decode_log(encoded_logs, passphrase):
    decoded = []
    key_length = len(passphrase)
    for i, char in enumerate(encoded_logs):
        key_char = passphrase[i % key_length]
        decoded_char = chr(ord(char) ^ ord(key_char))
        decoded.append(decoded_char)
    return ''.join(decoded)

# Encoded logs from the breach
encoded_entries = ["\x1f\x01\x1c\x0e\x1d", "\x1a\x06\x1b\x0b\x16", "\x19\x07\x18\x0c\x17"]
security_key = "SEC"

# Decoding process
access_logs = [decode_log(entry, security_key) for entry in encoded_entries]

# User activity mapping with dictionary comprehension
user_ids = ['U1001', 'U2002', 'U3003']
activity_map = {uid: log for uid, log in zip(user_ids, access_logs)}

# Risk assessment lambda
risk_evaluator = lambda log: sum(1 for c in log if c.isupper()) > 2 and 'ADMIN' in log

# Suspicious activity filter
suspicious_users = {uid: log for uid, log in activity_map.items() if risk_evaluator(log)}

# Threat level calculation
base_threat = 10
threat_modifier = 5 if any('DELETE' in log for log in suspicious_users.values()) else 2
threat_level = base_threat + threat_modifier if suspicious_users else 0

print(f"Result: {threat_level}")