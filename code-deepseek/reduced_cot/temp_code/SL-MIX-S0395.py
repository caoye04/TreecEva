def apply_crypto_logic(bits, modifier):
    # Irrelevant encryption simulation
    dummy_encrypt = [bit ^ 0b101010 for bit in bits]
    dead_code_path = sum(dummy_encrypt) * 2  # Unused calculation
    
    # Main logic - bit manipulation with modifier
    processed = [(bit << 1) & 0xFF for bit in bits]
    masked = [p | modifier for p in processed]
    
    # Misleading intermediate result
    fake_key = sum(masked) % 256
    
    # Actual key computation
    filtered = [m for m in masked if m % 3 == 0]
    crypto_key = sum(filtered) ^ modifier
    
    # Red herring operation
    confusing_shift = (fake_key << 2) | 0b11
    return crypto_key

# Distractor variables and operations
initial_data = [45, 128, 77, 201, 33, 92]
preliminary_sum = sum([x * 2 for x in initial_data])  # Irrelevant
bitwise_check = preliminary_sum & 0xAA  # Dead code

# Main execution
bit_stream = [x % 64 for x in initial_data]
key_offset = (bit_stream[2] ^ bit_stream[4]) & 0x1F

# Misleading parallel computation
alternative_key = max(bit_stream) - min(bit_stream)
shadow_calc = [bin(x).count('1') for x in bit_stream]

final_result = apply_crypto_logic(bit_stream, key_offset)
crypto_key = final_result

print(f"Target result: {crypto_key}")