from itertools import compress

data_stream = 'a1b2c3d4e5f6'
error_mask = [True, False, True, False, True, False, True, False, True, False, True, False]

# Filter characters based on error mask
filtered_data = ''.join(compress(data_stream, error_mask))

MOD_BASE = 1009
checksum = 0

for c in filtered_data:
    if c.isalpha():
        checksum = (checksum + ord(c) - ord('a') + 1) % MOD_BASE
    else:
        checksum = (checksum + int(c)) % MOD_BASE

Result: {checksum}