class HashProcessor:
    def __init__(self):
        self.seed = 137
        self.cache = {}
        self.debug_mode = False
        
    def _calculate_checksum(self, data):
        # Misleading intermediate calculation
        temp_sum = sum([ord(c) if isinstance(c, str) else c for c in data])
        redundant_check = temp_sum ^ 0xFF  # Unused distractor
        return temp_sum % 256
        
    def _apply_bit_operations(self, value):
        # Multiple bitwise operations with some irrelevant steps
        step1 = value & 0x0F
        step2 = step1 | 0x80
        step3 = step2 ^ 0x55
        unused_shift = step3 << 2  # Dead code path
        return step3
        
    def process(self, data_list):
        # Main processing with complex logic chain
        intermediate_results = []
        
        # Process each data block with mixed operations
        for i, block in enumerate(data_list):
            checksum = self._calculate_checksum(block)
            bit_result = self._apply_bit_operations(checksum)
            
            # Combine with previous result using XOR
            if i == 0:
                current_hash = bit_result
            else:
                current_hash ^= bit_result
                
            # Add some irrelevant state tracking
            intermediate_results.append(current_hash)
            self.cache[f'block_{i}'] = current_hash  # Unused caching
            
        # Final hash calculation with dictionary comprehension
        weight_factors = {idx: (val % 8) + 1 for idx, val in enumerate(intermediate_results)}
        
        # Core logic: combine weighted intermediate results
        weighted_sum = sum([val * weight_factors[i] for i, val in enumerate(intermediate_results)])
        
        # Apply final transformation
        final_value = (weighted_sum & 0x7F) | ((self.seed % 64) << 7)
        
        # Misleading alternative calculation (dead code)
        alternative_hash = (sum(intermediate_results) * 3) % 1024
        
        return final_value

# Data preparation with list comprehensions
data_blocks = [
    [1, 5, 9, 13],
    [2, 6, 10, 14],
    [3, 7, 11, 15],
    [4, 8, 12, 16]
]

# Create processor and execute
hash_processor = HashProcessor()
final_hash = hash_processor.process(data_blocks)

# Print result
print(f"Result: {final_hash}")