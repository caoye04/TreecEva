import math

def tokenize_expression(expr):
    return [tok for tok in expr.split() if tok]

def transform_token(tok):
    if tok.isdigit():
        val = int(tok)
        return math.log(val + 1) if val > 0 else 0
    elif tok in ['+', '-', '*', '/', '**']:
        return ord(tok[0]) * 0.1
    else:
        return sum(ord(c) for c in tok) * 0.01

def apply_weighted_exponent(vals):
    weighted = []
    for i, v in enumerate(vals):
        weight = 1 + (i % 3) * 0.5
        weighted.append(math.pow(v, weight))
    return weighted

mathematical_expression = "3 x ** 2 + 5 y - 7"
token_sequence = tokenize_expression(mathematical_expression)
transformed_values = list(map(transform_token, token_sequence))
weighted_exponential_results = apply_weighted_exponent(transformed_values)
final_hash_accumulator = round(sum(weighted_exponential_results) * 1000)
print(f"Result: {final_hash_accumulator}")