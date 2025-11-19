import hashlib

def hash_token(token):
    return int(hashlib.md5(token.encode()).hexdigest(), 16) % 1000

class LexerContext:
    def __init__(self, input_str):
        self.input = input_str
        self.position = 0
        self.tokens = []
        self.state = 'START'
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    
    def advance(self):
        if self.position < len(self.input):
            char = self.input[self.position]
            self.position += 1
            return char
        return None
    
    def peek(self):
        if self.position < len(self.input):
            return self.input[self.position]
        return None
    
    def tokenize(self):
        current_token = ''
        while True:
            char = self.advance()
            if char is None:
                if current_token:
                    self.tokens.append(current_token)
                break
            
            if self.state == 'START':
                if char.isalpha():
                    current_token = char
                    self.state = 'IDENTIFIER'
                elif char.isdigit():
                    current_token = char
                    self.state = 'NUMBER'
                elif char == '=':
                    self.tokens.append('=')
                elif char.isspace():
                    continue
            elif self.state == 'IDENTIFIER':
                if char.isalnum():
                    current_token += char
                else:
                    self.tokens.append(current_token)
                    # Backtrack one character
                    self.position -= 1
                    self.state = 'START'
                    current_token = ''
            elif self.state == 'NUMBER':
                if char.isdigit():
                    current_token += char
                else:
                    self.tokens.append(current_token)
                    # Backtrack one character
                    self.position -= 1
                    self.state = 'START'
                    current_token = ''
        
        # Hash tokens for lookup table
        token_hash_table = {}
        for token in self.tokens:
            token_hash = hash_token(token)
            if token_hash not in token_hash_table:
                token_hash_table[token_hash] = []
            token_hash_table[token_hash].append(token)
        
        return len(self.tokens)

def main():
    config_string = 'SET mode=DEBUG port=8080 timeout=30'
    
    with LexerContext(config_string) as lexer:
        parsed_token_count = lexer.tokenize()
    
    print(f"Result: {parsed_token_count}")

if __name__ == "__main__":
    main()