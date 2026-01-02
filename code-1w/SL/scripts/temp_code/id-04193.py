from collections import defaultdict
import itertools

def process_metrics(stream):
    # Initialize tracking variables
    counts = defaultdict(int)
    totals = []
    temp_buffer = []
    cumulative_xor = 0
    scaling_factor = 1.5

    # Irrelevant statistical trackers (distractor)
    mean_tracker = []
    variance_accumulator = 0

    for val in stream:
        if val % 2 == 0:
            counts['even'] += 1
            temp_buffer.append(val * 0.5)
        else:
            counts['odd'] += 1
            temp_buffer.append(val + 1)

        # Bitwise manipulation relevant to final result
        cumulative_xor ^= (val & 7)  # Use lower 3 bits

        # Red herring: collecting data not used in final score
        if val > 10:
            mean_tracker.append(val)
            variance_accumulator += val ** 2

    # Simulated data smoothing (partially relevant)
    smoothed = [round(x * scaling_factor) for x in temp_buffer]
    totals = [x for x in smoothed if x > 5]

    # Additional distraction: unused nested loop structure
    backup_sum = 0
    for i in range(2):
        for j in range(3):
            backup_sum += i * j  # Dead computation

    # Core logic: combine counts, totals, and XOR
    base_score = sum(totals)
    adjustment = counts['even'] - counts['odd']
    final_score = base_score + adjustment * 2 + cumulative_xor

    # Distractor: conditional that never triggers (misleading)
    if len(mean_tracker) > 100:
        final_score *= 0.9

    return final_score

# Generate input stream using itertools
sequence_seed = [3, 4, 7, 8, 12]
repeated_cycle = itertools.cycle(sequence_seed)
data_stream = list(itertools.islice(repeated_cycle, 9))

# Execute main logic
temp_result = process_metrics(data_stream)
final_score = temp_result
print(f"Result: {final_score}")