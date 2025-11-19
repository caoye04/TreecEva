from itertools import permutations
from dataclasses import dataclass
from typing import List

def hash_token(token: str) -> int:
    return hash(token) % 10000

def xor_reduce(values: List[int]) -> int:
    result = 0
    for v in values:
        result ^= v
    return result

@dataclass
class TokenSet:
    items: List[str]
    
    def get_permutation_hashes(self) -> List[int]:
        hashes = [hash_token(t) for t in self.items]
        perm_hashes = []
        for p in permutations(hashes):
            perm_value = xor_reduce(list(p)[:3])
            perm_hashes.append(perm_value)
        return perm_hashes

tokens = TokenSet(['alpha', 'beta', 'gamma'])

with open('temp_log.txt', 'w') as f:
    f.write("Processing tokens\n")
    hashes_list = tokens.get_permutation_hashes()
    secure_key = sum(hashes_list) % 997
    f.write(f"Secure key: {secure_key}\n")

print(f"Result: {secure_key}")