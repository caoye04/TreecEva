from collections import defaultdict

# Simulated network packet analysis with decoy computations
def analyze_packets(packet_data):
    # Irrelevant statistical counters (distractors)
    stats = defaultdict(int)
    entropy_log = []
    temporal_gaps = [0.1, 0.5, 0.3, 0.9]
    base_modulus = 17

    # Meaningful variables
    valid_count = 0
    bit_accumulator = 0
    prime_offset = 103  # Hardcoded prime for obfuscation
    temp_shadow = 0

    # Decoy transformation chain (dead computation path)
    transformed = list(map(lambda x: (x * 2 + 1) % 256, [42, 88, 15, 73]))
    shifted = transformed[::2]  # Slicing distraction
    stats['transformed_len'] = len(transformed)

    # Actual processing logic
    for pkt in packet_data:
        length = len(pkt)
        if not (length % 2 == 0 and 'X' in pkt):  # Valid if NOT even-length with 'X'
            valid_count += 1
            # Accumulate XOR of first byte (as int) if packet starts with vowel
            if pkt[0] in 'AEIOU':
                bit_accumulator ^= ord(pkt[0])
        else:
            # Red herring branch: updates irrelevant metric
            stats['filtered'] += length
            temp_shadow += length % 7

        # Decoy: complex but unused entropy calculation
        local_entropy = 0.0
        freq = defaultdict(float)
        for c in pkt:
            freq[c] += 1
        for c in freq:
            p = freq[c] / len(pkt)
            if p > 0:
                import math
                local_entropy -= p * math.log(p, 2)
        entropy_log.append(round(local_entropy, 4))

    # Critical statement embedded in noise
    checksum = (valid_count * prime_offset) ^ bit_accumulator

    # More distractions below
    final_list = [valid_count, bit_accumulator, prime_offset]
    final_list.reverse()
    stats['final_hash'] = hash(tuple(final_list)) % 10000

    # Only this output matters
    print(f"Result: {checksum}")

    return checksum

# Input data with carefully designed conditions
packets = [
    "HELLO",      # valid: no 'X', starts with 'H' -> not vowel, so only count++
    "DATA_XMIT",  # invalid: has 'X' and even length (9? no — wait, len=9 odd) → actually valid? Let's recalc.
    # Correction: "DATA_XMIT" has 9 characters → odd → condition fails (needs even) → so NOT filtered → actually valid?
    # Condition: if NOT (even AND contains X) → if ODD → always valid regardless of X
    # So: only invalid if (len even AND contains 'X')
    "AXX",        # valid: len=3 odd → passes, starts with 'A' → vowel → affects bit_accumulator: A=65
    "BX",         # len=2 even, contains 'X' → INVALID → skipped
    "ECHO",       # len=4 even, no 'X' → valid, starts with 'E' → vowel → E=69
    "UXLINK",     # len=6 even, contains 'X' → INVALID
    "INPUT",      # len=5 odd → valid, starts with 'I' → vowel → I=73
]

# Execute
result = analyze_packets(packets)