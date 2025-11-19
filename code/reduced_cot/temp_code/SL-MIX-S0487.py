import heapq
import re

def tokenize_config(config_str):
    tokens = []
    depth = 0
    i = 0
    while i < len(config_str):
        if config_str[i] == '[':
            depth += 1
            tokens.append(('LBRACKET', depth))
            i += 1
        elif config_str[i] == ']':
            if depth > 0:
                tokens.append(('RBRACKET', depth))
                depth -= 1
            else:
                # Unmatched bracket - trigger backtracking
                return None, True
            i += 1
        elif config_str[i].isspace():
            i += 1
        else:
            match = re.match(r'[a-zA-Z_][a-zA-Z0-9_]*', config_str[i:])
            if match:
                word = match.group(0)
                tokens.append((word, depth))
                i += len(word)
            else:
                i += 1
    return tokens, False

def process_with_backtracking(config_str):
    heap = []
    attempt = 0
    max_attempts = 3
    
    while attempt < max_attempts:
        tokens, needs_backtrack = tokenize_config(config_str)
        if not needs_backtrack:
            # Push tokens to heap with priority based on depth
            for token_type, depth in tokens:
                heapq.heappush(heap, (-depth, token_type))  # Max-heap using negative depth
            break
        else:
            # Backtrack: remove last unmatched closing bracket
            last_bracket_pos = config_str.rfind(']')
            if last_bracket_pos != -1:
                config_str = config_str[:last_bracket_pos] + config_str[last_bracket_pos+1:]
                attempt += 1
            else:
                break
    
    return heap

# Main execution
config_language = "settingA [subSettingB [item1 item2] settingC] [unmatched]"

priority_heap = process_with_backtracking(config_language)

# Calculate final token weight
final_token_weight = 0
weight_multiplier = 1

while priority_heap:
    neg_depth, token = heapq.heappop(priority_heap)
    depth = -neg_depth
    if token in ['LBRACKET', 'RBRACKET']:
        final_token_weight += depth * weight_multiplier
        weight_multiplier += 1
    else:
        # For identifiers, add fixed value
        final_token_weight += 10
        
# Execution point Z
print(f"Result: {final_token_weight}")