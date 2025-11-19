import re
from functools import reduce

class TokenProcessor:
    def __init__(self):
        self.transformations = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def process_tokens(self, token_list):
        valid_tokens = [t for t in token_list if re.match(r'^[A-Z]{2,}[0-9]+$', t)]
        transformed = []
        for token in valid_tokens:
            parts = re.split(r'(\d+)', token)
            if len(parts) >= 3 and parts[1]:
                numeric_part = int(parts[1])
                match numeric_part % 4:
                    case 0:
                        transformed.append(numeric_part ** 2)
                    case 1:
                        transformed.append(numeric_part * 3)
                    case 2:
                        transformed.append(numeric_part + 10)
                    case 3:
                        transformed.append(numeric_part << 2)
        self.transformations = len(transformed)
        return transformed

tokens = ['AB12', 'XYC37', 'PQ92', 'MNOP104', 'GHJ5', 'RSTU16']

with TokenProcessor() as processor:
    results = processor.process_tokens(tokens)
    semantic_score = reduce(lambda x, y: x ^ y, results, 0) if results else 0
    semantic_score += processor.transformations

print(f"Result: {semantic_score}")