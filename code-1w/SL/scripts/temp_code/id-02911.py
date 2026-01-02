def compute_integrity_value():
    sequence = 'XK78-2023-QRZ'
    offset = 13
    data_sum = 0
    
    # Extract numeric parts and sum ASCII values of uppercase letters
    for char in sequence:
        if char.isalpha():
            data_sum += ord(char)
        elif char.isdigit():
            data_sum += int(char)

    # Irrelevant tracking variable (minimal distraction)
    total_chars = len(sequence)
    
    position = sequence.find('Q')
    checksum = (data_sum + position) % 97
    
    # Additional unrelated but harmless operation
    multiplier = 1 if checksum > 50 else 2
    
    return checksum

result = compute_integrity_value()
print(f"Result: {result}")