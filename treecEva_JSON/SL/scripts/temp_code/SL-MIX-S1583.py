from collections import defaultdict, Counter
import hashlib

class TokenStream:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
    
    def has_next(self):
        return self.index < len(self.tokens)
    
    def next_token(self):
        if self.has_next():
            token = self.tokens[self.index]
            self.index += 1
            return token
        return None

def hash_token(token):
    return int(hashlib.md5(token.encode()).hexdigest(), 16) % 1000

token_stream = TokenStream(['[', 'section', ']', 'Hello', '[', '/', 'section', ']', '[', 'note', 'attr=value', ']', 'Content', '[', '/', 'note', ']'])
state = 'initial'
stack = []
frequency_map = defaultdict(int)
hashed_values = []

while token_stream.has_next():
    token = token_stream.next_token()
    hashed_values.append(hash_token(token))
    
    if state == 'initial':
        if token == '[':
            state = 'opening_tag_start'
        else:
            state = 'content'
    elif state == 'opening_tag_start':
        if token.startswith('/'):
            state = 'closing_tag_name'
        else:
            state = 'opening_tag_name'
            stack.append(token)
    elif state == 'opening_tag_name':
        if '=' in token:
            state = 'attribute'
        elif token == ']':
            state = 'initial'
            frequency_map[stack[-1]] += 1
        else:
            stack.append(token)
    elif state == 'attribute':
        if token == ']':
            state = 'initial'
            frequency_map[stack[-1]] += 1
    elif state == 'closing_tag_name':
        if token == ']':
            if stack:
                closed_tag = stack.pop()
                frequency_map[closed_tag] += 1
            state = 'initial'
    elif state == 'content':
        frequency_map['content'] += 1
        state = 'initial'

# Greedy selection of top 3 most frequent tokens
sorted_freq = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)[:3]

# Calculate weighted score
final_score = 0
for i, (token, freq) in enumerate(sorted_freq):
    weight = 3 - i  # First gets weight 3, second 2, third 1
    token_hash = hash_token(token)
    final_score += (freq * weight) + (token_hash % 10)

print(f"Result: {final_score}")