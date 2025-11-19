import re
from collections import namedtuple

token_pattern = r'([A-Z]+):(\w+)'
ConfigToken = namedtuple('ConfigToken', ['type', 'value'])

class TokenProcessor:
    def __init__(self):
        self.rules = {
            'ENABLE': lambda x: x.upper() == 'TRUE',
            'PRIORITY': lambda x: x.isdigit() and 1 <= int(x) <= 10,
            'MODE': lambda x: x in ['AUTO', 'MANUAL', 'HYBRID']
        }
    
    def process(self, token_stream):
        tokens = [ConfigToken(*re.match(token_pattern, t).groups()) for t in token_stream if re.match(token_pattern, t)]
        priority_values = []
        enable_flag = False
        
        for token in tokens:
            if token.type == 'ENABLE' and self.rules['ENABLE'](token.value):
                enable_flag = True
            elif token.type == 'PRIORITY' and self.rules['PRIORITY'](token.value):
                priority_values.append(int(token.value))
            elif token.type == 'MODE' and self.rules['MODE'](token.value):
                hashed = hash(token.value) % 100
                if hashed > 50:
                    priority_values = [p + 2 for p in priority_values]
        
        matched_priority = (max(priority_values) if priority_values else 0) + (10 if enable_flag else 0)
        return matched_priority

tokens = ['ENABLE:true', 'PRIORITY:3', 'MODE:AUTO', 'PRIORITY:7', 'MODE:HYBRID']
processor = TokenProcessor()
matched_priority = processor.process(tokens)
print(f'Result: {matched_priority}')