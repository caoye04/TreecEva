import re
from functools import wraps

def hex_transformer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return hex(result)[2:] if isinstance(result, int) else result
    return wrapper

class MarkerProcessor:
    def __init__(self, markers):
        self.markers = markers
        self.processed_values = {}
    
    @hex_transformer
    def compute_value(self, marker):
        # Convert hex string to integer for processing
        numeric_val = int(marker, 16)
        # Apply bit manipulation: XOR with 0xF0 and shift right by 2
        transformed = (numeric_val ^ 0xF0) >> 2
        return transformed
    
    def process_all(self):
        for marker in self.markers:
            pattern_match = re.match(r'^([A-F0-9]{2})([A-F0-9]{2})$', marker)
            if pattern_match:
                first_byte, second_byte = pattern_match.groups()
                val1 = int(first_byte, 16)
                val2 = int(second_byte, 16)
                # Conditional logic chain
                if (val1 & 0x80) == 0 and (val2 | 0x0F) > 0x1F:
                    computed = self.compute_value(marker)
                    self.processed_values[marker] = computed
                elif (val1 | val2) >= 0xC0:
                    self.processed_values[marker] = 'SKIP'
                else:
                    self.processed_values[marker] = 'DEFAULT'
        return self.processed_values

genomic_markers = ['A1B2', 'C3D4', 'E5F6', '1234']
processor = MarkerProcessor(genomic_markers)
results_map = processor.process_all()

# Dictionary comprehension to filter and transform results
filtered_results = {k: int(v, 16) for k, v in results_map.items() if v != 'SKIP' and v != 'DEFAULT'}

# Merge with default scoring map
scoring_defaults = {'A1B2': 100, 'C3D4': 200, 'E5F6': 300, '1234': 400}
merged_scores = {**scoring_defaults, **filtered_results}

# Calculate final marker value using logical conditions
final_marker_value = 0
for key, score in merged_scores.items():
    byte1, byte2 = int(key[:2], 16), int(key[2:], 16)
    condition_a = (byte1 & 0x0F) == (byte2 >> 4)
    condition_b = not ((byte1 | 0xF0) == 0xFF)
    if condition_a and condition_b:
        final_marker_value += score
    elif not condition_a or (condition_b and score > 150):
        final_marker_value -= score // 2

print(f"Result: {final_marker_value}")