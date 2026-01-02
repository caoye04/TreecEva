import itertools

# Simulate sensor array processing with noise filtering and phase transformations
sensors = [17, 23, 19, 41, 37, 31, 29]
noise_floor = 15
calibration_map = {i: val % 7 for i, val in enumerate(sensors)}

# Irrelevant preprocessing: normalize (unused later)
normalized = [round((x - min(sensors)) / (max(sensors) - min(sensors)) * 100) for x in sensors]

# Phase 1: filter active sensors above noise
active_sensors = [s for s in sensors if s > noise_floor]

# Phase 2: apply calibration shift using map
shifted = [s + calibration_map[i] for i, s in enumerate(active_sensors)]

# Phase 3: pair with dummy indices and reverse order (some used, some not)
paired = list(zip(shifted, range(len(shifted))))
reversed_pairs = sorted(paired, key=lambda x: x[1], reverse=True)
extracted = [p[0] for p in reversed_pairs]

# Phase 4: chunk into groups of 3 using itertools (distractor: not used directly)
groups = [list(g) for k, g in itertools.groupby(extracted, key=lambda x: extracted.index(x) // 3)]
flat_groups = [item for group in groups for item in group]  # Redundant flattening

# Phase 5: compute rolling XOR (3-element window) - only last result matters
rolling_xor = []
for i in range(len(flat_groups) - 2):
    rolling_xor.append(flat_groups[i] ^ flat_groups[i+1] ^ flat_groups[i+2])

intermediate_checksum = sum(rolling_xor) % 1000

# Phase 6: mirror array and combine (partial use)
mirrored = flat_groups[::-1]
combined = [flat_groups[i] + mirrored[i] for i in range(len(flat_groups))]

# Phase 7: extract every second element, then square and reduce
phase_seven = [x**2 for i, x in enumerate(combined) if i % 2 == 0]

# Decoy function that looks important but is never called
def decoy_aggregate(data):
    temp = 0
    for x in data:
        temp = (temp * 31 + x) % 997
    return temp

# Finalization logic (critical path)
def finalize(value):
    if value < 500:
        return value * 3 + 7
    else:
        return value - 42

# Misleading intermediate step (looks like checksum but unused)
temp_diagnostic = sum([calibration_map[k] for k in calibration_map]) * intermediate_checksum

# Critical assignment — answer depends on this
checksum = finalize(sum(phase_seven))

# Dead code path: unreachable due to structure
if len(sensors) < 5:
    alternate = [x for x in combined if x % 2 == 0]
    checksum = sum(alternate)

# Print final target result
print(f"Target result: {checksum}")