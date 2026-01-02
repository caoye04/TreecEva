def compute_integrity_value(data_sequence):
    base_offset = 23
    checksum = 1
    scaling_factor = 4

    for char in data_sequence:
        if char.isalpha():
            checksum = (checksum + ord(char)) % 97
            checksum = (checksum * scaling_factor) % 97

    temp_result = checksum + base_offset  # Irrelevant computation
    return f"Result: {checksum}"

print(compute_integrity_value("BeaconX9"))