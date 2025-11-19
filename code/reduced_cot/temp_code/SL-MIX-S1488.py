import re
from math import gcd
from itertools import permutations

def compute_lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

class AnalysisContext:
    def __init__(self, data):
        self.data = data
        self.transformed = []
    
    def __enter__(self):
        # Preprocess data with regex pattern matching
        pattern = r'[a-z]+'
        matches = re.findall(pattern, self.data)
        self.transformed = [len(m) for m in matches if len(m) > 1]
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# Encrypted message for analysis
message = "alpha9beta4gamma2delta"
verification_score = 0

with AnalysisContext(message) as ctx:
    lengths = ctx.transformed
    if lengths and len(lengths) >= 2:
        # Short-circuit evaluation with logical operations
        p_exists = len(list(permutations(lengths, 2))) > 10
        gcd_check = gcd(lengths[0], lengths[-1]) > 1
        
        if p_exists and gcd_check:
            # Compute verification using lambda closure
            lcm_func = lambda x, y: compute_lcm(x, y)
            primary_lcm = lcm_func(lengths[0], lengths[1])
            
            # Additional transformation based on string operations
            transformed_value = sum(map(lambda n: n**2 if n % 2 == 0 else n*3, lengths))
            
            # Final verification score calculation
            verification_score = primary_lcm + transformed_value
        elif not p_exists or not gcd_check:
            verification_score = -1
    else:
        verification_score = 0

print(f"Result: {verification_score}")