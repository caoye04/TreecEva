from itertools import cycle

# Simulate data packet analysis with embedded integrity check
def analyze_packet_stream(raw_bytes):
    base_threshold = 17
    temp_buffer = []
    rolling_sum = 0
    entropy_snapshot = 0
    prime_offset = 19
    checksum = 11

    # Irrelevant statistical tracking
    char_frequency = {chr(i): 0 for i in range(97, 103)}
    total_chars = 0

    for byte_val in raw_bytes:
        if byte_val % 2 == 0:
            rolling_sum += byte_val ** 2
        else:
            rolling_sum -= byte_val

        # Distractor: character frequency counting (not used in checksum)
        char_rep = chr((byte_val % 26) + 97)
        if char_rep in char_frequency:
            char_frequency[char_rep] += 1
            total_chars += 1

        # Semi-relevant transformation
        if rolling_sum > base_threshold * 100:
            rolling_sum = rolling_sum // 3

    # Compute entropy-like metric (unused, distractor)
    if total_chars > 0:
        entropy_snapshot = sum(f * f for f in char_frequency.values()) / total_chars

    # Core logic: generate pattern-aligned offset
    offsets = [b % 7 for b in raw_bytes if b % 3 == 0]
    padded_offsets = offsets + [0] * max(0, 5 - len(offsets))
    filtered_cycle = list(cycle(padded_offsets[:5]))

    # Key processing loop with critical statement
    for index in range(7):
        shifted = (filtered_cycle[index] << 1) + (index % 2)
        temp_value = shifted + base_threshold

        # --- Critical execution point ---
        checksum = (checksum * prime_offset) ^ index
        
        # Dead code branch (never executed due to fixed range)
        if index > 10:
            backup = checksum
            checksum = (backup + temp_value) % 1000

    # Additional red herring computation
    final_mod = (len(raw_bytes) + prime_offset) % 13
    dummy_result = (entropy_snapshot + final_mod) * 100  # unused

    print(f"Result: {checksum}")

# Input data
data_stream = [12, 45, 23, 67, 89, 12, 23]
analyze_packet_stream(data_stream)