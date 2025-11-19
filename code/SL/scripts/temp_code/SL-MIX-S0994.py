class ScopeNode:
    def __init__(self, parent=None):
        self.variables = {}
        self.parent = parent

def tokenize(config_str):
    return config_str.split()

class ConfigProcessor:
    def __init__(self):
        self.current_scope = ScopeNode()
        self.global_registry = {}
        self.processed_count = 0
        
    def register_transform(self, name, func):
        self.global_registry[name] = func
        
    def enter_scope(self):
        self.current_scope = ScopeNode(self.current_scope)
        
    def exit_scope(self):
        if self.current_scope.parent:
            self.current_scope = self.current_scope.parent
            
    def set_var(self, name, value):
        self.current_scope.variables[name] = value
        
    def get_var(self, name):
        scope = self.current_scope
        while scope:
            if name in scope.variables:
                return scope.variables[name]
            scope = scope.parent
        return None
    
    def merge_scope_vars(self):
        if not self.current_scope.parent:
            return
        child_keys = set(self.current_scope.variables.keys())
        parent_keys = set(self.current_scope.parent.variables.keys())
        common_keys = child_keys & parent_keys
        unique_child_keys = child_keys - parent_keys
        for key in common_keys:
            self.current_scope.parent.variables[key] = self.current_scope.variables[key]
        for key in unique_child_keys:
            self.current_scope.parent.variables[key] = self.current_scope.variables[key]
        
    def apply_transforms(self, var_name):
        transforms = self.get_var('transforms')
        if not transforms:
            return
        value = self.get_var(var_name)
        if value is None:
            return
        for t in transforms:
            if t in self.global_registry:
                value = self.global_registry[t](value)
        self.set_var(var_name, value)
        
config_str = "scope BEGIN x 10 y 20 transforms [double increment] merge END scope BEGIN z 5 transforms [square] merge END"
tokens = tokenize(config_str)
processor = ConfigProcessor()
processor.register_transform('double', lambda v: v * 2)
processor.register_transform('increment', lambda v: v + 1)
processor.register_transform('square', lambda v: v * v)
i = 0
while i < len(tokens):
    token = tokens[i]
    if token == 'scope':
        processor.enter_scope()
    elif token == 'BEGIN':
        pass
    elif token.isdigit():
        processor.set_var(tokens[i-1], int(token))
        processor.processed_count += 1
    elif token == '[':
        j = i + 1
        transform_list = []
        while j < len(tokens) and tokens[j] != ']':
            if tokens[j] != '[':
                transform_list.append(tokens[j])
            j += 1
        processor.set_var('transforms', transform_list)
        i = j
    elif token == 'merge':
        vars_to_transform = list(processor.current_scope.variables.keys())
        for var in vars_to_transform:
            if var != 'transforms':
                processor.apply_transforms(var)
        processor.merge_scope_vars()
    elif token == 'END':
        processor.exit_scope()
    i += 1
# What is the value of processed_count at this point?
print(f"Result: {processor.processed_count}")