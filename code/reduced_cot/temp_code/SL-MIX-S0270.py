import itertools

class ChecksumTracker:
    def __init__(self, base_value):
        self.base = base_value
        self.distractor_cache = []
        self.temp_calc = 0
        
    def process_data_chunk(self, data_range):
        # Distractor: complex-looking but unused operation
        self.distractor_cache = list(itertools.combinations(data_range, 2))
        relevant_values = [x for x in data_range if x % 3 == 0]
        
        # Misleading intermediate calculation
        self.temp_calc = sum(relevant_values) * 2
        
        actual_sum = sum(x for x in data_range if x % 4 == 0)
        return actual_sum
    
    def get_verification_value(self):
        # Main logic path
        data_range = range(1, 25)
        chunk_result = self.process_data_chunk(data_range)
        
        # Distractor: unused bit operations
        bit_check = chunk_result & 0xFF | 0x10
        
        # Final calculation
        verification = (chunk_result * 3 + self.base) % 47
        return verification

# Main execution with distractions
input_data = [5, 12, 8, 17, 23]
redundant_sum = sum(input_data) * 2  # Dead calculation

checksum_tracker = ChecksumTracker(15)

# Misleading operation that doesn't affect final result
mock_verification = checksum_tracker.process_data_chunk(range(10, 20))

final_checksum = checksum_tracker.get_verification_value()

# Distractor print statements
print(f"Debug temp: {checksum_tracker.temp_calc}")
print(f"Debug bit: {checksum_tracker.distractor_cache[:2]}")

print(f"Result: {final_checksum}")