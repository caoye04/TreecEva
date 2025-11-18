from collections import deque

token_sequence = ['ID', 'NUM', 'OP', 'OP', 'NUM', 'ID', 'ID']
state_stack = deque()
analysis_score = 0
previous_type = None

def update_score(current_type):
    global analysis_score, previous_type
    if previous_type is None:
        pass
    elif previous_type == current_type:
        analysis_score += 2
    else:
        analysis_score += 1
    previous_type = current_type

for token in token_sequence:
    if token == 'ID':
        state_stack.append('TEXT')
        update_score('TEXT')
    elif token == 'NUM':
        state_stack.append('NUMBER')
        update_score('NUMBER')
    elif token == 'OP':
        state_stack.append('SYMBOL')
        update_score('SYMBOL')

print(f"Result: {analysis_score}")