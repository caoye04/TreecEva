import re
from functools import reduce
from collections import defaultdict

def decode_segment(encoded):
    return bytes.fromhex(encoded).decode('utf-8')

def calculate_weight(segment):
    vowels = len(re.findall(r'[aeiouAEIOU]', segment))
    consonants = len(re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', segment))
    return (vowels << 2) + (consonants & 0xF)

def process_segments(segments):
    decoded_segments = list(map(decode_segment, segments))
    weights = list(map(calculate_weight, decoded_segments))
    pattern_matches = [
        any(re.match(r'^[A-Z]', seg) for seg in decoded_segments),
        all(len(seg) > 3 for seg in decoded_segments),
        sum(1 for seg in decoded_segments if re.search(r'\d', seg)) > 0
    ]
    match_score = reduce(lambda x, y: x | (y << 1), [int(match) for match in pattern_matches], 0)
    total_weight = reduce(lambda x, y: x ^ y, weights, 0)
    return (total_weight << 3) | match_score

# Encoded linguistic segments
segments_registry = ['48656c6c6f', '576f726c64', '507974686f6e', '436f6465']
segment_weights = defaultdict(int)

for idx, seg in enumerate(segments_registry):
    segment_weights[idx] = calculate_weight(decode_segment(seg))

initial_score = process_segments(segments_registry)
adjusted_score = initial_score & 0xFF
linguistic_score = adjusted_score ^ 0xAA

print(f"Result: {linguistic_score}")