def analyze_signal(stream, threshold=0.75):
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(stream) for x in stream]
    filtered = [x for x in normalized if x > 0.1]
    segments = [filtered[i:i+4] for i in range(0, len(filtered), 4)]

    # Decoy function that's never called
    def decrypt_payload(x):
        return (x * 127) ^ 0xABCD

    # Unused transformation chain
    transformed = []
    for seg in segments:
        temp = 0
        for val in seg:
            temp += int(val * 100)
        transformed.append(temp % 256)

    # Real processing begins here (buried among distractions)
    primary_chunk = stream[::2][:8]  # Every other sample, first 8
    mask = 0xF0 | (len(primary_chunk) & 0x0F)  # Mask depends on length

    # Misleading checksum from decoy logic
    dummy_checksum = sum(transformed) ^ 0xFFFF

    # Actual target computation
    def process_segment(data, key):
        # Bit manipulation + slicing
        a = sum(data[:4])
        b = sum(data[4:])
        c = (a ^ key) & 0xFF
        d = (b >> 2) + (b & 0x03)
        e = (c * d) & 0xFFFF
        f = (e >> 8) | ((e & 0xFF) << 8)  # Byte swap
        g = f ^ (f >> 4)
        h = g & 0x7FFF
        if h > 32767:
            h -= 65536
        return h

    # Dead code path - looks important but unused
    backup_mode = False
    if sum(stream) % 17 == 0:
        backup_mode = True
        alternate = [x for x in stream if x % 2 == 0]
        mask = len(alternate) ^ 0xAA

    # Critical assignment
    checksum = process_segment(primary_chunk, mask)

    # Red herring: additional unrelated operations
    stats = {
        'mean': sum(stream) / len(stream),
        'peaks': len([x for x in stream if x > threshold * max(stream)]),
        'entropy': 0.0
    }

    # Output the real answer despite noise
    print(f"Result: {checksum}")

# Input data with non-uniform pattern
input_stream = [13, 27, 45, 19, 88, 34, 72, 51, 11, 93, 67, 22, 84, 39]
analyze_signal(input_stream)