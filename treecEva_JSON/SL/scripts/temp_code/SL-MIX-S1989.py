import hashlib

def hash_transform(value):
    return int(hashlib.md5(str(value).encode()).hexdigest(), 16) % 1000000

def arithmetic_chain(seed, ops):
    current = seed
    for op in ops:
        if op.startswith('ADD'):
            _, num = op.split(':')
            current += int(num)
        elif op.startswith('MUL'):
            _, num = op.split(':')
            current *= int(num)
        elif op == 'HASH':
            current = hash_transform(current)
    return current

operations = ['ADD:23', 'MUL:17', 'HASH', 'ADD:42', 'MUL:3', 'HASH']
seed_value = 12345
intermediate_result = arithmetic_chain(seed_value, operations[:3])
final_hash_value = arithmetic_chain(intermediate_result, operations[3:])
print(f'Result: {final_hash_value}')