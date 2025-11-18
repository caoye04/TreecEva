import re
from collections import Counter

def is_hex_token(token):
    return bool(re.fullmatch(r'[0-9a-f]+', token))

log_fragment = "error ff00 proxy abc123 ghi invalid 4d2e"
tokens = log_fragment.split()
hex_token_count = sum(1 for token in tokens if is_hex_token(token))

print(f"Result: {hex_token_count}")