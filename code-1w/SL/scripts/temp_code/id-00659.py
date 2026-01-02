from itertools import compress

# Sensor data with timestamps (simulated)
raw_readings = [107, 214, 95, 188, 203, 77, 134, 221]
timestamps = [1623456000, 1623456060, 1623456120, 1623456180, 1623456240, 1623456300, 1623456360, 1623456420]

# Determine valid readings: odd timestamps and reading > 100
valid_flags = [(ts & 1 == 1) and (val > 100) for ts, val in zip(timestamps, raw_readings)]

# Extract valid entries using compress
decoy_variable_ignored = [x * 2 for x in raw_readings]  # irrelevant operation
valid_entries = list(compress(raw_readings, valid_flags))

# Apply bit mask based on number of valid entries
entry_count = len(valid_entries)
mask = entry_count << 2  # left shift by 2 bits

# Final checksum computation with XOR
filtered_checksum = sum(valid_entries) ^ mask

Result: filtered_checksum