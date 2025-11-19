import functools

class ParserCheckpoint:
    def __init__(self):
        self.memo_hits = 0
        self.call_count = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def memoized_parser(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(parser_ctx, tokens, pos):
        parser_ctx.call_count += 1
        if pos in cache:
            parser_ctx.memo_hits += 1
            return cache[pos]
        result = func(parser_ctx, tokens, pos)
        cache[pos] = result
        return result
    return wrapper

@memoized_parser
def parse_expression(ctx, tokens, position):
    if position >= len(tokens):
        return 0
    
    current_token = tokens[position]
    if current_token == 'ADD':
        # Simulate processing two operands
        left = parse_expression(ctx, tokens, position + 1)
        right = parse_expression(ctx, tokens, position + 2)
        return left + right
    elif current_token.isdigit():
        return int(current_token)
    else:
        return 0

# Token stream to process
input_tokens = ['ADD', '5', 'ADD', '3', '2', 'ADD', '5', 'ADD', '3', '2']

with ParserCheckpoint() as parser_context:
    # First pass to populate cache
    parse_expression(parser_context, input_tokens, 0)
    # Second pass to trigger memo hits
    parse_expression(parser_context, input_tokens, 0)
    parse_expression(parser_context, input_tokens, 3)
    parse_expression(parser_context, input_tokens, 6)
    
    target_result = parser_context.memo_hits

print(f"Result: {target_result}")