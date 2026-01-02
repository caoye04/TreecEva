def compute_integrity_signature(data_sequence):
    checksum = 0
    temp_accumulator = 0
    offset = len(data_sequence) % 7
    
    for index, (char, pos) in enumerate(zip(data_sequence, range(len(data_sequence)))):
        if pos % 2 == 0:
            temp_accumulator += ord(char) % 5
            for inner in range(1, 4):
                shifted = (ord(char) >> (inner % 3)) + offset
                if shifted % 2 == 1:
                    checksum += inner
                else:
                    # This branch modifies a variable not used later
                    dummy_tracker = shifted ** 2
        else:
            checksum -= (ord(char) + index) % 4
        
        # Core logic step
        checksum = (checksum * 3) ^ index
        
        # Irrelevant transformation
        mirror_val = sum(ord(c) for c in reversed(data_sequence[:index+1])) % 19
        
    # Post-processing that doesn't affect final result
    final_length = len(data_sequence)
    padding_factor = (final_length * 2) % 5
    return checksum

result = compute_integrity_signature('algorithm')
print(f"Result: {result}")