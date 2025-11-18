import re
from functools import reduce
from collections import namedtuple

def decode_token_segment(segment):
    if len(segment) <= 2:
        return sum(ord(c) for c in segment)
    mid = len(segment) // 2
    left_result = decode_token_segment(segment[:mid])
    right_result = decode_token_segment(segment[mid:])
    return left_result ^ right_result

class EncodingProcessor:
    def __init__(self):
        self.transform_rules = [
            lambda x: x >> 1,
            lambda x: x ^ 0xFF,
            lambda x: (x * 3) & 0xFF
        ]
    
    def process_sequence(self, tokens):
        processed = []
        for token in tokens:
            if re.match(r'^[A-Z]{2,}$', token):
                value = decode_token_segment(token)
                for rule in self.transform_rules:
                    value = rule(value)
                processed.append(value)
            else:
                processed.append(0)
        return processed

TokenSequence = namedtuple('TokenSequence', ['primary', 'secondary'])
token_data = TokenSequence(['ABCD', 'EFGH'], ['XYZ', 'ABC123'])

processor = EncodingProcessor()
primary_results = processor.process_sequence(token_data.primary)
secondary_results = processor.process_sequence(token_data.secondary)

combined_results = [a | b for a, b in zip(primary_results, secondary_results)]
decoded_value = reduce(lambda x, y: (x + y) & 0xFF, combined_results, 0)

print(f"Result: {decoded_value}")