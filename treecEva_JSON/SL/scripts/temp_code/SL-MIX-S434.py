import re
from itertools import combinations

def tokenize(expr):
    return re.findall(r'\w+|[^\w\s]', expr)

def hash_token(token):
    val = 0
    for char in token:
        val = (val * 31 + ord(char)) & 0xFF
    return val

class TokenProcessor:
    def __init__(self, modifiers=None):
        self.modifiers = modifiers or []
    
    def process(self, tokens):
        scores = []
        for t in tokens:
            base = hash_token(t)
            if any(c.isdigit() for c in t):
                base *= 2
            elif t.isupper():
                base += 100
            scores.append(base)
        
        # Apply modifier functions if any
        for mod in self.modifiers:
            scores = [mod(s) for s in scores]
        
        # Compute pairwise XOR of all combinations of 2
        xor_results = [a ^ b for a, b in combinations(scores, 2)]
        
        # Return sum modulo a prime
        return sum(xor_results) % 1291

def double_if_even(x):
    return x * 2 if x % 2 == 0 else x

token_processor = TokenProcessor([double_if_even])
input_sequence = "SECURITY2023 TOKEN_abc DEF456x"
tokens = tokenize(input_sequence)
final_score = token_processor.process(tokens)
print(f"Result: {final_score}")