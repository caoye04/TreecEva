import hashlib
from itertools import combinations
def transform_substring(s):
    transformed = ''
    for i, char in enumerate(s):
        if i % 2 == 0:
            transformed += chr((ord(char) + 3) % 256)
        else:
            transformed += chr((ord(char) * 2) % 256)
    return transformed

def compute_hash(s):
    return int(hashlib.md5(s.encode()).hexdigest()[:8], 16)

def generate_substrings(s):
    substrings = []
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.append(s[i:j])
    return substrings

def verify_hash_sequence(input_string):
    substrings = generate_substrings(input_string)
    total_hash = 0
    for sub in substrings:
        transformed = transform_substring(sub)
        hash_val = compute_hash(transformed)
        total_hash ^= hash_val
    return total_hash

class VerificationSession:
    def __init__(self, session_id, data_block):
        self.session_id = session_id
        self.data_block = data_block
        self.processed_hashes = []
    
    def run_verification(self):
        hash_result = verify_hash_sequence(self.data_block)
        self.processed_hashes.append(hash_result)
        return hash_result

def aggregate_sessions(session_list):
    agg_value = 0
    for session in session_list:
        result = session.run_verification()
        agg_value = (agg_value * 31 + result) % 100000007
    return agg_value

# Main execution
if __name__ == "__main__":
    sessions = [
        VerificationSession("SES_001", "alpha"),
        VerificationSession("SES_002", "beta"),
        VerificationSession("SES_003", "gamma")
    ]
    final_verification_code = aggregate_sessions(sessions)
    print(f"Result: {final_verification_code}")