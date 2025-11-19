import hashlib

def tokenize_document(doc):
    return [token.strip('.,!?;') for token in doc.split()]

def hash_token(token):
    return int(hashlib.md5(token.encode()).hexdigest(), 16) % 1000

class PatternValidator:
    def __init__(self):
        self.state = 'START'
        self.pattern_match = False
    
    def process_token(self, token):
        if self.state == 'START' and token.isalpha():
            self.state = 'WORD'
        elif self.state == 'WORD' and token.isdigit():
            self.state = 'NUMBER'
        elif self.state == 'NUMBER' and token in ['.', ',']:
            self.state = 'DELIMITER'
        elif self.state == 'DELIMITER' and token.isalpha():
            self.pattern_match = True
            self.state = 'START'
        else:
            self.state = 'START'
            self.pattern_match = False
        return self.pattern_match

document = "apple 123 . banana 456 , cherry 789 . date"
tokens = tokenize_document(document)
validator = PatternValidator()
validated_count = 0
hash_accumulator = 0

for i in range(len(tokens)):
    token = tokens[i]
    hash_val = hash_token(token)
    hash_accumulator += hash_val
    
    if validator.process_token(token):
        validated_count += 1
        # Nested loop to simulate cross-validation
        for j in range(min(validated_count, 3)):
            if (hash_accumulator + j) % (validated_count + 1) == 0:
                validated_count += 1
    
    # Reset accumulator periodically
    if i % 5 == 4:
        hash_accumulator = 0

# Apply final transformation using functional programming
final_validations = list(map(lambda x: x * 2 if x % 2 == 1 else x // 2, 
                           filter(lambda x: x > 0, 
                                  [validated_count - i for i in range(3)])))
validated_count = sum(final_validations)

print(f"Result: {validated_count}")