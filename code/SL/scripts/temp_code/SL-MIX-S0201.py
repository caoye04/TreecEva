def process_text(input_string):
    states = {'NORMAL': 0, 'ESCAPE': 1, 'HEX': 2}
    current_state = states['NORMAL']
    processed_length = 0
    i = 0
    
    while i < len(input_string):
        char = input_string[i]
        
        if current_state == states['NORMAL']:
            if char == '\\':
                current_state = states['ESCAPE']
            else:
                processed_length += 1
        elif current_state == states['ESCAPE']:
            if char == 'x':
                current_state = states['HEX']
                i += 1  # Skip the 'x'
                # Read two hex digits
                hex_digits = input_string[i:i+2]
                i += 1  # Move past first hex digit
                # Convert hex to character (we just count it)
                processed_length += 1
            else:
                # Invalid escape, treat as normal characters
                processed_length += 2  # Backslash and the character
                current_state = states['NORMAL']
        elif current_state == states['HEX']:
            # We've already processed the hex in the ESCAPE state
            current_state = states['NORMAL']
            continue  # Skip incrementing i as we've already moved
        
        i += 1
    
    return processed_length

# Process the input string
input_text = 'Hello\\x41\\x42\\x43World'
processed_length = process_text(input_text)
print(f"Result: {processed_length}")