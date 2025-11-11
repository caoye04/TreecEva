import math

class SecureTransactionContext:
    def __init__(self, initial_state):
        self.state = initial_state
        self.log = []
    
    def __enter__(self):
        self.log.append(f"Entering secure context with state: {self.state}")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.log.append("Exiting secure context")
        return False
    
    def update_state(self, new_state):
        self.state = new_state
        self.log.append(f"State updated to: {self.state}")

def complex_validation_rule(value):
    return lambda x: (x & 0xF0) >> 4 == value

def process_transaction_data(raw_data):
    # Decode base64-like encoding
    decoded = bytes([b - 1 for b in raw_data]).decode('ascii')
    return sum(ord(c) for c in decoded)

# Transaction processing
transactions = [
    [66, 67, 68, 69, 70],  # ASCII chars: BCDEF
    [71, 72, 73, 74, 75],  # ASCII chars: GHIJK
    [76, 77, 78, 79, 80]   # ASCII chars: LMNOP
]

validation_score = 0.0
validation_rules = [
    complex_validation_rule(0xB),
    lambda x: x > 100,
    lambda x: not (x % 7 == 0)
]

with SecureTransactionContext(validation_score) as ctx:
    for i, tx_data in enumerate(transactions):
        processed_value = process_transaction_data(tx_data)
        
        # Apply bitwise transformation
        transformed_value = (processed_value ^ 0xAA) & 0xFF
        
        # Check validation rules
        rule_results = [rule(transformed_value) for rule in validation_rules]
        
        # Calculate floating-point weight based on position
        weight = math.sqrt(i + 1) / 2.0
        
        # Apply logical operations to determine score contribution
        if all(rule_results) and not (transformed_value < 0x50):
            score_delta = transformed_value * weight
        elif any(rule_results) or (transformed_value & 0x0F) == 0x05:
            score_delta = transformed_value / (i + 1)
        else:
            score_delta = -transformed_value * 0.1
        
        validation_score += score_delta
        ctx.update_state(validation_score)
    
    # Final adjustment
    if validation_score > 0:
        validation_score = math.floor(validation_score) & 0x7F
    else:
        validation_score = (int(validation_score) | 0x80) & 0xFF

print(f"Result: {validation_score}")