import re
from functools import reduce
from collections import defaultdict

def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str)*4)

def mask_bits(binary_str, mask):
    return ''.join(b if m == '1' else '0' for b, m in zip(binary_str, mask.ljust(len(binary_str), '1')))

def count_pattern(bin_str, pattern):
    return len(re.findall(pattern, bin_str))

class GeneticSegment:
    def __init__(self, seq_id, hex_data):
        self.seq_id = seq_id
        self.hex_data = hex_data
        self.bin_data = ''
        self.masked_data = ''
        self.pattern_counts = defaultdict(int)

segments = [
    GeneticSegment('SEG001', 'A3F1'),
    GeneticSegment('SEG002', 'B2E4'),
    GeneticSegment('SEG003', 'C1D5')
]

bit_mask = '11001100'
search_pattern = r'101'

final_count = 0
for seg in segments:
    seg.bin_data = hex_to_bin(seg.hex_data)
    seg.masked_data = mask_bits(seg.bin_data, bit_mask)
    seg.pattern_counts[search_pattern] = count_pattern(seg.masked_data, search_pattern)
    final_count += seg.pattern_counts[search_pattern]

print(f"Result: {final_count}")