from collections import namedtuple

def fibonacci_sequence(n):
    if n <= 0: return []
    elif n == 1: return [0]
    elif n == 2: return [0, 1]
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def transform_char_code(char, fib_index):
    base_code = ord(char)
    transformed = (base_code + fib_index) % 127
    return transformed

CipherConfig = namedtuple('CipherConfig', ['message', 'modulus'])
config = CipherConfig(message="SECRET", modulus=97)

fib_indices = fibonacci_sequence(len(config.message))
char_transformations = [transform_char_code(ch, fib_indices[i]) for i, ch in enumerate(config.message)]

security_key = 1
for i, code in enumerate(char_transformations):
    if i % 2 == 0:
        security_key = (security_key * code) % config.modulus
    else:
        security_key = (security_key + code) % config.modulus

print(f"Result: {security_key}")