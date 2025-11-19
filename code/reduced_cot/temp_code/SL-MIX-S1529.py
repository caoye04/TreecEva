import math

def generate_secure_key():
    fib_sequence = [1, 1]
    for i in range(2, 12):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    xor_accumulator = 0
    for idx, val in enumerate(fib_sequence):
        if idx % 3 == 0:
            scaled_val = int(math.log(val + 1) * 10) & 0xFF
            xor_accumulator ^= scaled_val << (idx % 8)
        elif idx % 3 == 1:
            if val > 50:
                break
            xor_accumulator |= val >> 1
        else:
            xor_accumulator &= ~(val ^ (val << 1))
    
    secure_key = xor_accumulator % 1000
    return secure_key

secure_key = generate_secure_key()
print(f'Result: {secure_key}')