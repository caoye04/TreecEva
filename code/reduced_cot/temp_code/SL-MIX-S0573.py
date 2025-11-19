from functools import reduce

def tokenize_hex_stream(hex_string):
    return [int(hex_string[i:i+2], 16) for i in range(0, len(hex_string), 2)]

def apply_transformations(tokens):
    stack = []
    ops = [
        lambda x: x << 1,
        lambda x: x ^ 0xFF,
        lambda x: (x + 17) % 256
    ]
    
    for token in tokens:
        transformed = reduce(lambda acc, op: op(acc), ops, token)
        stack.append(transformed)
    
    return stack

class ChecksumCalculator:
    def __init__(self):
        self.checksum = 0
    
    def update(self, value):
        self.checksum = (self.checksum + value) & 0xFFFF
    
    def get_checksum(self):
        return self.checksum

def process_data_stream(data_stream):
    tokens = tokenize_hex_stream(data_stream)
    transformed_stack = apply_transformations(tokens)
    
    calculator = ChecksumCalculator()
    
    while transformed_stack:
        value = transformed_stack.pop()
        calculator.update(value)
    
    return calculator.get_checksum()

# Main execution
hex_data = "4A6B2C8D"
final_checksum = process_data_stream(hex_data)
print(f"Result: {final_checksum}")