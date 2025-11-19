from collections import deque

def process_parentheses(token_sequence):
    stack = deque()
    cumulative_score = 0
    max_cumulative = 0
    
    for token in token_sequence:
        if token == '(':
            stack.append('(')
            current_depth = len(stack)
            cumulative_score += current_depth
            max_cumulative = max(max_cumulative, cumulative_score)
        elif token == ')' and stack:
            current_depth = len(stack)
            cumulative_score -= current_depth
            stack.pop()
    
    return max_cumulative

token_input = "((())(()))"
max_score = process_parentheses(token_input)
print(f"Result: {max_score}")