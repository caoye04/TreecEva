from collections import namedtuple
import hashlib

def tokenize_events(event_string):
    Token = namedtuple('Token', ['type', 'value'])
    tokens = []
    i = 0
    while i < len(event_string):
        char = event_string[i]
        if char == 'N':
            # Note followed by duration digit
            if i+1 < len(event_string) and event_string[i+1].isdigit():
                tokens.append(Token(type='NOTE', value=int(event_string[i+1])))
                i += 2
            else:
                tokens.append(Token(type='NOTE', value=1))
                i += 1
        elif char == 'R':
            # Rest followed by duration digit
            if i+1 < len(event_string) and event_string[i+1].isdigit():
                tokens.append(Token(type='REST', value=int(event_string[i+1])))
                i += 2
            else:
                tokens.append(Token(type='REST', value=1))
                i += 1
        elif char == 'C':
            # Chord followed by bracketed notes
            if i+1 < len(event_string) and event_string[i+1] == '[':
                j = event_string.find(']', i+2)
                if j != -1:
                    notes = list(map(int, event_string[i+2:j]))
                    tokens.append(Token(type='CHORD', value=sum(notes)))
                    i = j + 1
                else:
                    tokens.append(Token(type='CHORD', value=0))
                    i += 1
            else:
                tokens.append(Token(type='CHORD', value=3))
                i += 1
        else:
            i += 1
    return tokens

def calculate_checksum(tokens):
    # Map token types to numeric codes
    type_codes = {'NOTE': 1, 'REST': 2, 'CHORD': 3}
    
    # Initialize checksum
    checksum = 0
    
    # Process each token
    for token in tokens:
        code = type_codes[token.type]
        value = token.value
        
        # Apply transformation based on token type
        transformed = (lambda x, y: x * 2 + y if x % 2 == 0 else x * 3 - y)(code, value)
        
        # Update checksum with bitwise operations
        checksum = (checksum << 1) ^ transformed
        
        # Conditional adjustment
        if checksum > 100:
            checksum = checksum & 0xFF
    
    return checksum

def main():
    # Musical sequence: Note(4), Rest(2), Chord[5,7,2], Note(1), Rest(1), Chord[3,9]
    sequence = "N4R2C[572]N1R1C[39]"
    
    # Tokenize the sequence
    parsed_tokens = tokenize_events(sequence)
    
    # Calculate checksum
    checksum = calculate_checksum(parsed_tokens)
    
    print(f"Result: {checksum}")

if __name__ == "__main__":
    main()