from collections import defaultdict
import re

def modular_transform(value, modulus=257):
    return (value * 17 + 23) % modulus

def tokenize_message(message):
    tokens = re.findall(r'[a-zA-Z]+|\d+', message)
    transformed_tokens = []
    for token in tokens:
        if token.isalpha():
            char_sum = sum(ord(c) - ord('a') + 1 for c in token.lower())
            transformed_tokens.append(modular_transform(char_sum))
        else:
            transformed_tokens.append(modular_transform(int(token)))
    return transformed_tokens

def calculate_token_weights(tokens):
    weight_map = defaultdict(int)
    for i, token in enumerate(tokens):
        weight = (token ^ (i + 1)) & 0xFF
        weight_map[token] += weight
    return dict(weight_map)

def process_communication_pipeline(raw_message):
    # Stage 1: Tokenization and transformation
    token_sequence = tokenize_message(raw_message)
    
    # Stage 2: Weight calculation
    token_weights = calculate_token_weights(token_sequence)
    
    # Stage 3: Aggregate scoring with conditional logic
    aggregate_score = 0
    for token_val, weight in token_weights.items():
        if token_val % 3 == 0:
            adjusted_weight = weight << 1
        elif token_val % 3 == 1:
            adjusted_weight = weight >> 1
        else:
            adjusted_weight = weight ^ 0xAA
        
        # Apply modular correction
        corrected = (adjusted_weight * 7 + 11) % 251
        aggregate_score = (aggregate_score + corrected) % 1009
    
    return aggregate_score

# Main execution
communication_data = "Alpha7Beta13Gamma5Delta11"
intermediate_scores = [process_communication_pipeline(communication_data[:i]) for i in range(5, len(communication_data), 3)]

# Calculate final token score
final_token_score = sum((score ^ 0x55) % 97 for score in intermediate_scores if score > 100)
print(f"Result: {final_token_score}")