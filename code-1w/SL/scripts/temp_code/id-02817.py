def compute_integrity_value():
    raw_input = "DataPacket_2024"
    offset_key = 3
    
    # Preprocess: shift each character by offset_key and reverse the string
    shifted_chars = []
    for c in raw_input:
        shifted_char = chr((ord(c) - ord('A') + offset_key) % 26 + ord('A')) if c.isalpha() else c
        shifted_chars.append(shifted_char)
    
    processed_data = ''.join(shifted_chars)[::-1]  # Reverse the shifted string
    
    # Compute checksum using modular arithmetic
    checksum = 0
    for c in processed_data:
        if c.isdigit():
            checksum = (checksum + int(c)) % 17
        else:
            checksum = (checksum + ord(c)) % 17
    
    # Irrelevant utility (minimal interference)
    def log_metadata():
        return len(raw_input), offset_key
    
    print(f"Result: {checksum}")

compute_integrity_value()