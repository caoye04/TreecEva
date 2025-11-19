def token_handler(token_type):
    def decorator(func):
        func.token_type = token_type
        return func
    return decorator

class Lexer:
    def __init__(self):
        self.handlers = {}
        self.state = 'START'
        self.buffer = ''
        self.tokens = []
    
    def register(self, func):
        self.handlers[func.token_type] = func
        return func
    
    def tokenize(self, input_str):
        i = 0
        while i < len(input_str):
            char = input_str[i]
            if self.state == 'START':
                if char.isdigit():
                    self.state = 'INTEGER'
                    self.buffer = char
                elif char.isalpha():
                    self.state = 'IDENTIFIER'
                    self.buffer = char
                elif char.isspace():
                    pass
                else:
                    # Handle single character tokens if needed
                    pass
            elif self.state == 'INTEGER':
                if char.isdigit():
                    self.buffer += char
                else:
                    self.tokens.append(int(self.buffer))
                    self.buffer = ''
                    self.state = 'START'
                    continue  # Re-evaluate current char in START state
            elif self.state == 'IDENTIFIER':
                if char.isalnum():
                    self.buffer += char
                else:
                    keyword = self.buffer
                    if keyword in ['SET', 'APPLY']:
                        self.tokens.append(keyword)
                    else:
                        self.tokens.append(('ID', keyword))
                    self.buffer = ''
                    self.state = 'START'
                    continue
            i += 1
        # Handle last token if buffer is not empty
        if self.state == 'INTEGER' and self.buffer:
            self.tokens.append(int(self.buffer))
        elif self.state == 'IDENTIFIER' and self.buffer:
            keyword = self.buffer
            if keyword in ['SET', 'APPLY']:
                self.tokens.append(keyword)
            else:
                self.tokens.append(('ID', keyword))
        return self.tokens

lexer = Lexer()
input_config = 'SET threshold APPLY 42 SET mode APPLY debug'
tokens = lexer.tokenize(input_config)
token_count = len(tokens)
print(f'Result: {token_count}')