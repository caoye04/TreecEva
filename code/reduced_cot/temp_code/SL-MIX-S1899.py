import re
from collections import defaultdict

def tokenize_config(config_str):
    tokens = []
    i = 0
    while i < len(config_str):
        if config_str[i].isspace():
            i += 1
            continue
        elif config_str[i] == '"':
            j = i + 1
            while j < len(config_str) and config_str[j] != '"':
                j += 1
            tokens.append(config_str[i+1:j])
            i = j + 1
        else:
            j = i
            while j < len(config_str) and not config_str[j].isspace():
                j += 1
            tokens.append(config_str[i:j])
            i = j
    return tokens

class ConfigValidator:
    def __init__(self):
        self.valid_directives = frozenset(['port', 'host', 'timeout', 'retry'])
        self.valid_param_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-')
    
    def validate_token(self, token):
        if '=' in token:
            parts = token.split('=', 1)
            if len(parts) != 2:
                return False
            directive, value = parts
            return (directive in self.valid_directives and 
                   all(c in self.valid_param_chars for c in value))
        else:
            return token in self.valid_directives

def process_network_config(config_string):
    validator = ConfigValidator()
    raw_tokens = tokenize_config(config_string)
    valid_tokens = []
    
    for token in raw_tokens:
        if validator.validate_token(token):
            valid_tokens.append(token)
    
    # Count occurrences of each directive type
    directive_counts = defaultdict(int)
    for token in valid_tokens:
        if '=' in token:
            directive = token.split('=', 1)[0]
            directive_counts[directive] += 1
        else:
            directive_counts[token] += 1
    
    # Apply filtering logic
    final_token_count = 0
    for directive, count in directive_counts.items():
        if directive == 'port' and count > 1:
            final_token_count += count - 1
        elif directive == 'host' and count >= 1:
            final_token_count += count * 2
        elif directive == 'timeout' and count == 1:
            final_token_count += count + 1
        elif directive == 'retry' and count <= 3:
            final_token_count += count
    
    return final_token_count

# Main execution
config_data = 'host=server1 port=8080 port=9000 timeout=30 retry=1 retry=2 host=backup retry=3'
final_token_count = process_network_config(config_data)
print(f"Result: {final_token_count}")