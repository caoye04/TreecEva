from collections import Counter

def validate_data_pattern(data):
    irrelevant_counter = sum([x for x in range(100) if x % 7 == 0])
    misleading_total = len(data) * 3.14
    
    if len(data) > 10:
        temp = data[:5] + data[-5:]
        pattern_check = sum(temp) * 2
    else:
        pattern_check = sum(data) // 2
    
    char_map = {chr(i): i-96 for i in range(97, 123)}
    char_sum = sum(char_map.values())  # This is unused distraction
    
    return pattern_check

class ChecksumProcessor:
    def __init__(self):
        self.redundant_cache = {}
        self.distraction_factor = 42
        
    def process_data(self, values):
        # Irrelevant preprocessing
        doubled = [x * 2 for x in values]
        filtered = list(filter(lambda x: x % 3 != 0, doubled))
        
        # Misleading intermediate calculation
        fake_checksum = sum(filtered) // len(values) if values else 0
        
        # Actual logic path
        counter = Counter(values)
        most_common = counter.most_common(2)
        
        if len(most_common) >= 2:
            primary, secondary = most_common[0][0], most_common[1][0]
            validation_result = validate_data_pattern(values)
            
            # Core calculation
            bit_ops = (primary ^ secondary) & 0xFF
            adjustment = (validation_result % 256) >> 3
            result = bit_ops + adjustment
            
            # More distractions
            unused_branch = result * self.distraction_factor
            dead_code_check = sum(range(50))  # Never used
            
            self.redundant_cache['temp'] = fake_checksum
            return result
        else:
            return fake_checksum  # This path is never taken

# Main execution
input_data = [15, 22, 15, 8, 22, 15, 30, 8, 15, 22, 45, 22]
encoded_values = [x + 10 for x in input_data]

checksum_processor = ChecksumProcessor()
final_checksum = checksum_processor.process_data(encoded_values)

print(f"Target result: {final_checksum}")