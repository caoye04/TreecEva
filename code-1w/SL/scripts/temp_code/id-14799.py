from collections import defaultdict

# Simulated sensor array data with noise and redundant channels
data_stream = [14, 17, 23, 14, 91, 22, 17, 14, 88, 23, 11, 91]
redundant_tags = ['A7', 'B2', 'C5', 'B2', 'D1', 'E9', 'C5', 'F3', 'A7', 'D1', 'E9', 'F3']

timestamp_marks = [1623450100, 1623450160, 1623450220, 1623450280, 1623450340, 1623450400,
                     1623450460, 1623450520, 1623450580, 1623450640, 1623450700, 1623450760]

# Irrelevant signal smoothing (distractor)
smoothed = [data_stream[i] for i in range(len(data_stream)) if i == 0 or data_stream[i] != data_stream[i-1]]

# Misleading frequency counter (red herring)
freq_map = defaultdict(int)
for val in data_stream:
    freq_map[val] += 1

# Decoy transformation using bitwise shifts (dead path)
shifted_vals = []
for x in data_stream:
    temp_val = (x << 2) ^ 7
    shifted_vals.append(temp_val)

# Unused recursive function (decoy logic)
def compute_entropy(seq, depth=0):
    if depth > 3 or len(seq) == 0:
        return 0
    mid = len(seq) // 2
    left = seq[:mid]
    right = seq[mid+1:]
    return (seq[mid] % 7) + compute_entropy(left, depth+1)

# Spurious list of thresholds (irrelevant)
thresh_levels = [10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100]
high_thresholds = [t for t in thresh_levels if t > 25 and t % 10 == 0]

# Real processing begins here — pattern detection via modular cycles
sequence_pairs = list(zip(data_stream, redundant_tags))
mod_cycle = []
for num, tag in sequence_pairs:
    if '7' in tag or '9' in tag:  # Filter by tag digit (subtle relevance)
        mod_cycle.append(num % 11)

# Secondary filter: only even-indexed timestamps
relevant_indices = []
for idx, ts in enumerate(timestamp_marks):
    if ts % 120 == 0:  # Every 2 minutes
        relevant_indices.append(idx)

# Combine filtered results (actual signal path)
filtered_mods = []
for i, (num, tag) in enumerate(sequence_pairs):
    if i in relevant_indices and tag in ['B2', 'E9', 'F3']:
        filtered_mods.append(num % 9)

# Base computation chain
running_total = 0
for x in filtered_mods:
    running_total = (running_total * 3 + x) % 1000

base_flux = running_total  # Critical intermediate value

# Mode configuration (simulated)
mode_flag = (len(filtered_mods) + sum(relevant_indices)) % 3

# Actual adjustment logic — depends on mode
def adjust_flux(flux, mode):
    if mode == 0:
        return flux * 2 + 10
    elif mode == 1:
        return (flux + 55) * 3
    else:  # mode == 2
        return (flux * 7) % 997

# Execution point of interest
final_flux = adjust_flux(base_flux, mode_flag)

# Print final result as required
print(f"Target result: {final_flux}")