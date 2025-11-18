from collections import defaultdict
import math

def modular_power(base, exp, mod):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        half = modular_power(base, exp // 2, mod)
        return (half * half) % mod
    else:
        return (base * modular_power(base, exp - 1, mod)) % mod

def verify_block_checksum(block_id, depth):
    if depth == 0:
        return block_id % 97
    inner_sum = 0
    for i in range(1, min(depth + 2, 6)):
        inner_sum += verify_block_checksum((block_id + i) % 100, depth - 1)
    return inner_sum % 97

class VerificationContext:
    def __init__(self):
        self.block_validations = defaultdict(int)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def process_layer(self, layer_data):
        layer_result = 0
        for block_index, block_value in enumerate(layer_data):
            checksum = modular_power(block_value, 17, 31)
            validated = verify_block_checksum(checksum, 3)
            self.block_validations[block_index] += validated
            layer_result += self.block_validations[block_index]
        return layer_result

# Main processing pipeline
input_blocks = [23, 45, 67, 89, 12, 34, 56, 78]
verified_blocks = 0

with VerificationContext() as ctx:
    for layer in range(3):
        layer_input = list(map(lambda x: x + layer * 10, input_blocks[layer*2:(layer+1)*2]))
        layer_output = ctx.process_layer(layer_input)
        verified_blocks += layer_output

print(f"Result: {verified_blocks}")