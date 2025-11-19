from collections import namedtuple
import base64

def transform_layer(data, op_type):
    if op_type == 'reverse':
        return data[::-1]
    elif op_type == 'encode':
        return base64.b64encode(data.encode()).decode()
    elif op_type == 'decode':
        return base64.b64decode(data).decode()
    else:
        return data

def calculate_checksum(text):
    return sum(ord(c) for c in text) % 256

class MessageProcessor:
    def __init__(self):
        self.states = ['INIT', 'REVERSE', 'ENCODE', 'DECODE', 'FINAL']
        self.current_state = 0
        self.checksum_history = []
    
    def process(self, message):
        data = message
        operations = [None, 'reverse', 'encode', 'decode', None]
        
        for i in range(len(self.states)):
            op = operations[i] if i < len(operations) else None
            data = transform_layer(data, op) if op else data
            checksum = calculate_checksum(data)
            self.checksum_history.append(checksum)
            self.current_state = i
        
        return data

def validate_layer_integrity(history):
    valid = True
    for i in range(1, len(history)):
        if history[i] < history[i-1]:
            valid = False
    return valid

# Main execution
processor = MessageProcessor()
input_message = "SECRET_KEY_2023"
processed_data = processor.process(input_message)

# Additional validation logic
is_valid_sequence = validate_layer_integrity(processor.checksum_history)
final_checksum = processor.checksum_history[-1] if is_valid_sequence else -1

# Apply conditional correction
final_checksum = final_checksum + 10 if final_checksum > 100 else final_checksum - 5

print(f"Result: {final_checksum}")