import math
from itertools import combinations
from functools import reduce

class CipherEngine:
    def __init__(self, base_key):
        self.base_key = base_key
        self.encoded_sequence = []
    
    def encode_step(self, value):
        return math.log(value, self.base_key)
    
    def transform_sequence(self, data_list):
        self.encoded_sequence = [self.encode_step(x) for x in data_list]
        return self.encoded_sequence

def binary_search_closest(arr, target):
    low, high = 0, len(arr) - 1
    closest = float('inf')
    while low <= high:
        mid = (low + high) // 2
        if abs(arr[mid] - target) < abs(closest - target):
            closest = arr[mid]
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return closest

def process_cipher(base_key, input_values):
    engine = CipherEngine(base_key)
    encoded = engine.transform_sequence(input_values)
    target = math.exp(1)  # e
    
    # Find closest encoded value to e
    closest_val = binary_search_closest(encoded, target)
    
    # Apply lambda transformation
    transform_func = lambda x: math.pow(x, 1.5) if x > 1 else math.pow(x, 2.5)
    transformed = transform_func(closest_val)
    
    # Combine with combinatorial operation
    combo_sum = sum(len(list(combinations(input_values, 2))) for _ in range(int(transformed)))
    
    # Final cipher value
    final_cipher_value = int(transformed * combo_sum % 1000)
    return final_cipher_value

# Execution
base_key = 7
input_values = [49, 343, 2401, 16807]
final_cipher_value = process_cipher(base_key, input_values)
print(f"Result: {final_cipher_value}")