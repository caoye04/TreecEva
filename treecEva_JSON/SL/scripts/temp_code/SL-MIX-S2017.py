import math
from functools import reduce

def encode_transform(text):
    return ''.join(chr(ord(c) + 3) for c in text)

def calculate_base(sequence):
    return reduce(lambda x, y: x * y, [i for i in sequence if i > 0], 1)

# Initial parameters
messages = ['alpha', 'beta', 'gamma']
weights = [2, 3, 5]
scaling_factor = 1.5

# Transformation pipeline
encoded_messages = list(map(encode_transform, messages))
char_products = [calculate_base([ord(c) for c in msg]) for msg in encoded_messages]
weighted_sum = sum(p * w for p, w in zip(char_products, weights))
log_scaled = math.log(weighted_sum) * scaling_factor
exp_amplified = math.exp(log_scaled / 10)

# Final scoring mechanism
final_score = int(exp_amplified) ^ (len(messages) << 2)
print(f"Result: {final_score}")