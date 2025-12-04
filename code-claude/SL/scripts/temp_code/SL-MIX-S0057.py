def process_text(input_str):
    # Text processing variables
    word_count = len(input_str.split())
    char_count = len(input_str)
    unique_chars = len(set(input_str))
    
    # Calculate reversals based on character positions
    reversals = 0
    for i in range(min(10, len(input_str))):
        if i % 2 == 0 and input_str[i].isalpha():
            ascii_val = ord(input_str[i].lower())
            reversals = (reversals << 1) | (ascii_val & 1)
    
    # Generate security parameters
    security_level = word_count * 3
    complexity = unique_chars // 2
    if complexity < 5:
        complexity = 5
    
    # Generate base value from string properties
    base_value = 0
    for c in input_str[:5]:
        if c.isdigit():
            base_value += int(c) * 10
        elif c.isalpha():
            base_value += (ord(c.lower()) - ord('a') + 1)
    
    # Apply bitwise operations for encryption
    mask = 0b1111111
    temp_key = base_value ^ complexity
    alt_key = (security_level & mask) | (base_value & ~mask)
    
    # Calculate encryption key
    encryption_key = (base_value & mask) ^ reversals
    
    # Verification steps (not affecting the result)
    verification = (base_value + security_level) % 256
    if verification > 128:
        debug_value = verification - 64
    else:
        debug_value = verification + 32
    
    return encryption_key

input_string = "Hello42World"
result = process_text(input_string)
print(f"Result: {result}")