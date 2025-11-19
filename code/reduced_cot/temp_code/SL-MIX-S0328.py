from functools import reduce

def decode_token_stream(encoded_stream):
    return [chr((ord(ch) - ord('A') + 13) % 26 + ord('A')) for ch in encoded_stream]

def tokenize(decoded_chars):
    tokens = []
    buffer = ''
    for ch in decoded_chars:
        if ch in '(){}[]':
            if buffer:
                tokens.append(buffer)
                buffer = ''
            tokens.append(ch)
        elif ch.isalnum():
            buffer += ch
        # Ignore spaces and other characters
    if buffer:
        tokens.append(buffer)
    return tokens

class ConfigNode:
    def __init__(self, token_type, value=None):
        self.type = token_type
        self.value = value
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)

def build_config_tree(token_list):
    stack = []
    root = ConfigNode('root')
    current = root
    
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}
    opening_brackets = set(bracket_pairs.keys())
    closing_brackets = set(bracket_pairs.values())
    
    i = 0
    while i < len(token_list):
        token = token_list[i]
        if token in opening_brackets:
            new_node = ConfigNode(f'block_{token}')
            current.add_child(new_node)
            stack.append(current)
            current = new_node
        elif token in closing_brackets:
            if stack:
                current = stack.pop()
        else:
            # It's a value token
            current.add_child(ConfigNode('value', token))
        i += 1
    
    return root

class StateMachine:
    def __init__(self):
        self.state = 0
        self.history = []
    
    def transition(self, input_symbol):
        self.history.append(self.state)
        if self.state == 0:
            if input_symbol.startswith('CFG'):
                self.state = 1
            elif input_symbol.startswith('VAL'):
                self.state = 2
        elif self.state == 1:
            if input_symbol == 'block_(':
                self.state = 3
            elif input_symbol == 'block_[':
                self.state = 4
        elif self.state == 2:
            self.state = 5 if input_symbol.isdigit() else 0
        elif self.state == 3:
            self.state = 6 if input_symbol == 'block_{' else 1
        elif self.state == 4:
            self.state = 7
        elif self.state == 5:
            self.state = 0
        elif self.state == 6:
            self.state = 8
        elif self.state == 7:
            self.state = 1
        elif self.state == 8:
            self.state = 0
    
    def get_checksum(self):
        return reduce(lambda x, y: (x ^ y) & 0xFF, self.history, 0)

def traverse_and_process(node, sm):
    sm.transition(node.type)
    if node.value:
        sm.transition(str(node.value))
    for child in node.children:
        traverse_and_process(child, sm)

# Main execution
encoded_input = "URYYB_JBEYQ_PBQR_PBASVT_EBGNGR"

# Step 1: Decode the token stream
rot13_decoded = decode_token_stream(encoded_input)

# Step 2: Tokenize the decoded characters
parsed_tokens = tokenize(rot13_decoded)

# Step 3: Build configuration tree
config_tree_root = build_config_tree(parsed_tokens)

# Step 4: Process tree with state machine
processor = StateMachine()
traverse_and_process(config_tree_root, processor)

# Step 5: Calculate final checksum
final_state_checksum = processor.get_checksum()
print(f"Result: {final_state_checksum}")