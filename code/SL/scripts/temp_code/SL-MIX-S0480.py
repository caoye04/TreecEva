from collections import defaultdict
import hashlib

def process_genomic_segment(segment_data):
    decoded_bytes = bytes.fromhex(segment_data)
    masked_data = bytearray()
    for byte_val in decoded_bytes:
        if (byte_val & 0xF0) != 0:
            masked_data.append(byte_val ^ 0xAA)
        else:
            masked_data.append(byte_val)
    return bytes(masked_data)

class GenomicValidator:
    def __init__(self):
        self.checksum_map = defaultdict(int)
    
    def update_validation(self, processed_data):
        hash_val = hashlib.sha256(processed_data).hexdigest()
        char_sum = sum(ord(c) for c in hash_val[:8] if c.isdigit() or c.isalpha())
        return char_sum % 100

segment_registry = {
    'segA': '48656c6c6f20',
    'segB': '576f726c6421',
    'segC': '47656e6f6d696373'
}

validator = GenomicValidator()
intermediate_mask = 0x0F
validation_score = 0

with open('temp_seq.tmp', 'w') as f:
    f.write(segment_registry['segA'])

for seg_id, hex_data in segment_registry.items():
    processed = process_genomic_segment(hex_data)
    score_part = validator.update_validation(processed)
    validation_score += score_part if (score_part & intermediate_mask) != 0 else -1

print(f"Result: {validation_score}")