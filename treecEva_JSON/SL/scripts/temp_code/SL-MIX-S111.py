from functools import reduce

def modular_power(base, exp, mod):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        half = modular_power(base, exp // 2, mod)
        return (half * half) % mod
    else:
        return (base * modular_power(base, exp - 1, mod)) % mod

def calculate_checksum(values, mod):
    if not values:
        return 0
    return (values[0] + calculate_checksum(values[1:], mod)) % mod

class CipherState:
    INIT = 0
    PROCESS = 1
    FINAL = 2

message = 'XYZ'
key = 7
state = CipherState.INIT
transformed_values = []

for char in message:
    ascii_val = ord(char)
    if state == CipherState.INIT:
        key = (key ^ 0b10101) & 0xFF
        state = CipherState.PROCESS
    if state == CipherState.PROCESS:
        transformed = ascii_val ^ key
        transformed_values.append(transformed)
        key = (key << 1) & 0xFF
    if len(transformed_values) == 2:  # Transition to FINAL after processing two characters
        state = CipherState.FINAL

checksum_result = calculate_checksum(transformed_values, 256)
print(f"Result: {checksum_result}")