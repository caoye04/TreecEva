def xor_shift_hash(s, depth=3):
    if depth == 0:
        return sum(ord(c) for c in s) & 0xFF
    transformed = ''.join(chr((ord(c) ^ depth) & 0xFF) for c in s)
    shifted = ''.join(chr(((ord(c) << 1) | (ord(c) >> 7)) & 0xFF) for c in transformed)
    return xor_shift_hash(shifted, depth - 1) ^ len(s)

def process_message(msg):
    parts = [msg[i:i+4] for i in range(0, len(msg), 4)]
    hashes = [xor_shift_hash(part) for part in parts]
    combined = ''.join(f'{h:02x}' for h in hashes)
    return xor_shift_hash(combined)

message = 'SECURITY2023'
segment_hashes = [xor_shift_hash(message[i:i+3]) for i in range(len(message)-2)]
checksum_components = {f'chk{i}': segment_hashes[i] ^ segment_hashes[i+1] for i in range(len(segment_hashes)-1)}
intermediate_result = sum(checksum_components.values())
final_checksum = intermediate_result & ((1 << 16) - 1)

print(f'Result: {final_checksum}')