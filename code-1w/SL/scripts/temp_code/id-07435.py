from collections import defaultdict, Counter
from itertools import cycle, islice

# Simulated sensor data processing with red herrings
def process_sensor_stream(raw_data):
    readings = [x for x in raw_data if x > 0]
    adjusted = [r ^ 211 for r in readings]  # bit manipulation

    # Irrelevant transformation branch (dead path)
    temp_map = defaultdict(int)
    for val in adjusted:
        temp_map[val] += 1
    _ = dict(Counter(temp_map))  # unused result

    # Filtering logic (partially relevant)
    filtered = [v for v in adjusted if v % 17 == 0]
    sum_filtered = sum(filtered)

    # Decoy statistical analysis
    mean_val = sum(adjusted) / len(adjusted) if adjusted else 0
    outlier_flags = [1 for a in adjusted if abs(a - mean_val) > 3 * 15.2]
    _ = len(outlier_flags) > 5  # unused boolean

    # Bitmasking and rotation (core logic disguised)
    mask = 0
    for i, bit in enumerate([1, 0, 1, 1, 0, 1, 0, 1]):
        mask |= (bit << i)

    # Unused complex structure
    history_log = []
    for tick in range(3):
        frame = {f"t{tick}_v{i}": (sum_filtered ^ tick) + i for i in range(5)}
        history_log.append(frame)

    # Critical operation buried in noise
    def finalize(x):
        base = x | 1023
        rotated = ((base << 3) & 0xFF) | (base >> 5)
        return rotated ^ 456

    checksum = finalize(sum_filtered & mask)

    # Distractor: secondary checksum with no use
    dummy_checksum = sum(adjusted[i] ^ i for i in range(0, len(adjusted), 3)) % 997
    _ = [print(f'Debug {k}: {v}') for k, v in history_log[0].items()]  # side effect, no impact

    return checksum

# Main execution
sensor_input = list(islice(cycle([18, -5, 35, 102, 0, 221, -3]), 97))
result = process_sensor_stream(sensor_input)

# Output the target result
Target result: {result}