import re
from collections import deque

class TokenizerState:
    START = 0
    READING = 1
    DONE = 2

class ConfigTokenizer:
    def __init__(self):
        self.state = TokenizerState.START
        self.tokens = []
    
    def process(self, input_str):
        parts = input_str.split()
        i = 0
        while i < len(parts):
            part = parts[i]
            if self.state == TokenizerState.START:
                if part == "START":
                    self.tokens.append(part)
                    self.state = TokenizerState.READING
            elif self.state == TokenizerState.READING:
                if part in ["END", "MODE"]:
                    self.tokens.append(part)
                    if part == "END":
                        self.state = TokenizerState.DONE
                        break
                else:
                    # It's a value
                    self.tokens.append(part)
            i += 1
        return self.tokens

tokenizer = ConfigTokenizer()
token_list = tokenizer.process("START config1 MODE fast END")
result_length = len(token_list)
print(f"Result: {result_length}")