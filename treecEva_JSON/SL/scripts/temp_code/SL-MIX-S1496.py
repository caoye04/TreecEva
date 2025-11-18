from collections import defaultdict
import math

def tokenize_price_movements(movements_str):
    tokens = []
    current_token = ''
    for char in movements_str:
        if char in '+-':
            if current_token:
                tokens.append(current_token)
            current_token = char
        else:
            current_token += char
    if current_token:
        tokens.append(current_token)
    return tokens

def calculate_volatility(tokens):
    dp_weights = defaultdict(float)
    dp_weights[0] = 1.0
    max_score = float('-inf')
    
    for i in range(1, len(tokens) + 1):
        token = tokens[i-1]
        magnitude = float(token[1:]) if len(token) > 1 else 1.0
        sign = 1 if token[0] == '+' else -1
        
        # Nested loop for dynamic calculation
        for j in range(i):
            weight_contribution = dp_weights[j] * magnitude * sign
            dp_weights[i] += weight_contribution
        
        score = abs(dp_weights[i]) * math.log(i+1)
        if score > max_score:
            max_score = score
    
    return max_score

# Main execution
price_data = "+1.5-0.8+2.3-1.1+0.9-2.0+1.4"
tokenized_data = tokenize_price_movements(price_data)
max_volatility_score = calculate_volatility(tokenized_data)
print(f"Result: {round(max_volatility_score, 2)}")