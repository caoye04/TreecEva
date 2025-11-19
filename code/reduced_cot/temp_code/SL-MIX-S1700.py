import re
from collections import defaultdict

def transform_segment(segment):
    transformed = ''
    for char in segment:
        if char.isalpha():
            transformed += str(ord(char) % 10)
        else:
            transformed += char
    return transformed

def compute_checksum(value):
    checksum = 0
    for i, char in enumerate(value):
        if char.isdigit():
            digit = int(char)
            if i % 2 == 0:
                checksum ^= digit << 1
            else:
                checksum |= digit >> 1 if digit > 1 else digit
    return checksum & 0xFF

class TransactionProcessor:
    def __init__(self):
        self.validation_map = defaultdict(lambda: False)
        self.validation_map.update({
            'X': True,
            'Y': True,
            'Z': True,
            '7': True,
            '8': True,
            '9': True,
            'A': True,
            'B': True,
            'C': True
        })
    
    def process(self, transaction_id):
        # Step 1: Pattern matching to split ID
        match = re.match(r'([A-Z]+)(\d+)([A-Z]+)', transaction_id)
        if not match:
            return None
        prefix, middle, suffix = match.groups()
        
        # Step 2: Validate segments using hash table
        valid = True
        for char in transaction_id:
            valid = valid and self.validation_map[char]
            if not valid:  # Short-circuit evaluation
                break
        
        if not valid:
            return None
        
        # Step 3: Transform segments
        transformed_prefix = transform_segment(prefix)
        transformed_middle = transform_segment(middle)
        transformed_suffix = transform_segment(suffix)
        
        # Step 4: Combine and compute checksum
        combined = transformed_prefix + transformed_middle + transformed_suffix
        checksum = compute_checksum(combined)
        
        # Step 5: Generate clearance code
        clearance_base = (len(transaction_id) * 0x13) & 0xFF
        final_clearance_code = (clearance_base ^ checksum) & 0xFF
        
        return final_clearance_code

# Main execution
processor = TransactionProcessor()
transaction_id = "XYZ789ABC"
final_clearance_code = processor.process(transaction_id)
print(f"Result: {final_clearance_code}")