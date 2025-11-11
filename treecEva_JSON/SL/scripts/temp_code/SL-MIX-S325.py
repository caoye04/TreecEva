import re
from collections import defaultdict

def hash_string(s, mod):
    hash_val = 0
    for char in s:
        hash_val = (hash_val * 31 + ord(char)) % mod
    return hash_val

def explore_combinations(prefix, remaining, target_hash, mod):
    if len(prefix) == 3:
        if hash_string(prefix, mod) == target_hash:
            return prefix
        return None
    
    for i, char in enumerate(remaining):
        result = explore_combinations(prefix + char, remaining[:i] + remaining[i+1:], target_hash, mod)
        if result:
            return result
    return None

class DocumentSegment:
    def __init__(self, content):
        self.content = content
        self.processed = False
        self.hash_map = defaultdict(list)
    
    def process(self, mod):
        self.processed = True
        segments = re.split(r'[.!?]', self.content)
        for seg in segments:
            clean_seg = re.sub(r'[^a-zA-Z]', '', seg).lower()
            if len(clean_seg) >= 3:
                key = hash_string(clean_seg[:3], mod)
                self.hash_map[key].append(clean_seg)
    
    def find_match(self, target_hash, mod):
        if not self.processed:
            self.process(mod)
        
        candidates = self.hash_map.get(target_hash, [])
        for candidate in candidates:
            if hash_string(candidate, mod) == target_hash:
                return candidate
        
        # If not found, try to construct a 3-char string with matching hash
        charset = ''.join(set(''.join(candidates)))
        result = explore_combinations('', charset, target_hash, mod)
        return result

doc_content = "Natural language processing involves statistical models. These models often use neural networks!"
segment = DocumentSegment(doc_content)
modulus = 1009
target_checksum = 523

match_result = segment.find_match(target_checksum, modulus)

# Execution Point Y
checksum = 0
if match_result:
    for c in match_result:
        checksum = (checksum * 26 + (ord(c) - ord('a') + 1)) % 1000000007
else:
    checksum = -1

print(f"Result: {checksum}")