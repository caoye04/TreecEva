import math
from functools import reduce

def tokenize_and_encode(message):
    tokens = list(map(ord, message))
    float_values = [val * math.pi for val in tokens]
    return float_values

def mod_process(values):
    processed = []
    for v in values:
        scaled = int(v * 100) % 256
        if scaled % 2 == 0:
            processed.append(scaled ^ 0xAA)
        else:
            processed.append((scaled << 1) % 256)
    return processed

text_message = "CodeEval"
float_sequence = tokenize_and_encode(text_message)
modulated_data = mod_process(float_sequence)
encoded_signal = reduce(lambda x, y: (x + y) % 1000, modulated_data, 0)
print(f"Result: {encoded_signal}")