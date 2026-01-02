def analyze_signal(stream, threshold=0.75):
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(stream) for x in stream]
    filtered = [x for x in normalized if x > threshold]
    segments = [stream[i:i+4] for i in range(0, len(stream), 4)]

    # Misleading statistical computation (red herring)
    avg_energy = sum(x**2 for x in stream) / len(stream)
    peak_magnitude = max(abs(x) for x in stream)

    # Unused transformation function (dead code path)
    def transform(x):
        return (x + 1) ** 0.5 if x >= 0 else 0

    # Real processing starts here
    config = {'mode': 'fast', 'level': 3, 'active': True}
    mode_flag = config['mode'] == 'debug'

    # Key data structures with cross-references
    indices = list(enumerate([x % 4 for x in stream[::2]]))
    pairs = list(zip(stream[1::2], [x[1] for x in indices]))

    # Bit manipulation matrix (complex distraction)
    bit_grid = []
    for a, b in pairs[:6]:
        row = []
        for shift in [1, 2]:
            val = ((int(a) & 0xF) << shift) ^ int(b)
            row.append(val % 9)
        bit_grid.append(row)

    # Decoy accumulation (looks important but unused)
    aggregate = 0
    for i in range(len(bit_grid)):
        for j in range(len(bit_grid[i])):
            if i % 2 == 0:
                aggregate += bit_grid[i][j] * (j + 1)

    # Actual relevant logic buried within
    base_sequence = [3, 1, 4, 1, 5, 9, 2, 6]
    mask = [x & 1 for x in base_sequence]  # Generates [1,1,0,1,1,1,0,0]

    def process_segment(data, msk):
        temp = 0
        for idx, (val, bit) in enumerate(zip(data, msk)):
            if bit:
                temp ^= val  # XOR accumulation
            else:
                temp += val % 3
        return temp % 1000

    # Critical execution point
    data = [12, 8, 7, 3, 21, 15, 4, 2]
    checksum = process_segment(data, mask)

    # Output requirement
    print(f"Result: {checksum}")

# Simulated signal input (deterministic)
signal_input = [12, 5, 8, 3, 7, 9, 3, 1, 21, 4, 15, 8, 4, 6, 2, 1]
analyze_signal(signal_input)