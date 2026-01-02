from itertools import groupby

# Simulate compression algorithm efficiency test
data_stream = 'AAABBBCCDAA'

# Count consecutive character groups (runs)
run_lengths = [len(list(group)) for char, group in groupby(data_stream)]

cycle_lengths = []
for length in run_lengths:
    if length % 2 == 0:
        cycle_lengths.append(length // 2)
    else:
        cycle_lengths.append(length + 1)

# Apply transformation based on parity
adjusted_cycles = [c+1 for c in cycle_lengths if c > 1]

# Final aggregation
baseline = len(run_lengths)
offset = 2
padding = 7  # unused variable - minor distraction

total_cycles = sum(cycle_lengths)
print(f"Result: {total_cycles}")