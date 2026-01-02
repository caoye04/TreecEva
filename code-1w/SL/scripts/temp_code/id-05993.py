import itertools

# Simulated cryptographic transformation pipeline
# Target: compute final checksum after complex data flow with heavy distractions

def main():
    # Primary data sources
    payload = [127, 85, 193, 42, 156]
    salt = [23, 17, 91]

    # Irrelevant transformation branch 1: unused hashing attempt
    temp_hash = 0
    for x in payload:
        temp_hash ^= (x * 17) % 251
        temp_hash = (temp_hash << 1) | (temp_hash >> 7)
        temp_hash &= 0xFF

    # Dead code path: never called function
    def decoy_mix(data):
        result = []
        for i in range(len(data)):
            result.append((data[i] ^ 0x55) + (i * 3))
        return result

    # Unused but plausible-looking round constants
    rcon = [(1 << i) % 256 for i in range(10)]
    rcon_map = {i: val for i, val in enumerate(rcon)}

    # Real computation begins: state initialization
    state = [p ^ 0x3A for p in payload]

    # Key schedule generation (only this part matters)
    key_seed = sum(salt) ^ len(payload)
    key_schedule = []
    k = key_seed
    for i in range(8):
        k = (k * 7 + 13) % 199
        key_schedule.append(k % 256)

    # Decoy data structure: looks important but unused
    audit_log = []
    for idx, val in enumerate(state):
        entry = {
            'index': idx,
            'raw': payload[idx],
            'masked': val,
            'flagged': (val & 0x80 != 0),
            'score': (val ^ key_seed) % 100  # red herring
        }
        audit_log.append(entry)

    # Multi-step state mixing with distractor operations
    mixed_state = state[:]
    shift_offset = key_schedule[0] % 5
    
    # Rotate elements based on key
    mixed_state = mixed_state[shift_offset:] + mixed_state[:shift_offset]

    # Spurious statistical analysis (irrelevant)
    avg_val = sum(mixed_state) / len(mixed_state)
    variance_proxy = sum((x - avg_val) ** 2 for x in mixed_state) / len(mixed_state)
    entropy_approx = 0
    for x in mixed_state:
        if x > 0:
            entropy_approx += x * x
    entropy_approx = (entropy_approx // 1000) % 256

    # Real processing: apply XOR cascade with key schedule
    for round_idx in range(4):
        round_key = key_schedule[round_idx * 2]
        for i in range(len(mixed_state)):
            prev = mixed_state[i - 1] if i > 0 else mixed_state[-1]
            mixed_state[i] ^= (prev << 1) ^ round_key
            mixed_state[i] &= 0xFF

    # Aggregation via bitwise diffusion
    aggregated = 0
    for i, val in enumerate(mixed_state):
        contribution = val << (i % 4) * 2
        contribution ^= (contribution >> 8)
        aggregated ^= contribution & 0xFFFF

    # Finalize hash using second half of key schedule
    def finalize_hash(value, keys):
        acc = value & 0xFFFF
        for k in keys[4:]:
            acc ^= k
            acc = (acc * 17) % 65537
            if acc >= 32768:
                acc -= 65537
        return acc & 0xFFFF

    checksum = finalize_hash(aggregated, key_schedule)

    # DECOY finalization: looks valid but unused
    alt_checksum = 0
    for chunk in itertools.batched(payload + salt, 3):
        block = 0
        for i, v in enumerate(chunk):
            block |= v << (i * 8)
        alt_checksum = (alt_checksum + block) % 65536
    alt_checksum ^= entropy_approx

    # RED HERRING: misleading print suggestion (not used)
    # print(f"Diagnostic: {alt_checksum=}, {temp_hash=}")

    print(f"Result: {checksum}")

if __name__ == "__main__":
    main()