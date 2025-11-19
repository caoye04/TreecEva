import re
from collections import defaultdict

class DirectoryAccessAnalyzer:
    def __init__(self):
        self.current_state = 'ROOT'
        self.permission_score = 0b11110000
        self.directory_permissions = {
            'ROOT': frozenset([1, 2, 3, 4]),
            'CONFIG': frozenset([2, 4, 6, 8]),
            'LOGS': frozenset([1, 3, 5, 7]),
            'TEMP': frozenset([2, 3, 5, 8])
        }
        self.state_transitions = {
            'ROOT': {'read_config': 'CONFIG', 'write_logs': 'LOGS'},
            'CONFIG': {'flush_temp': 'TEMP', 'exit': 'ROOT'},
            'LOGS': {'rotate': 'TEMP', 'exit': 'ROOT'},
            'TEMP': {'cleanup': 'CONFIG', 'exit': 'ROOT'}
        }
    
    def process_access(self, event_log):
        for entry in event_log:
            # Pattern matching to extract action
            match = re.search(r'ACCESS\((\w+):(\w+)\)', entry)
            if match:
                dir_name, action = match.groups()
                # State machine transition
                if action in self.state_transitions.get(self.current_state, {}):
                    self.current_state = self.state_transitions[self.current_state][action]
                
                # Calculate permission modification
                if dir_name in self.directory_permissions:
                    common_perms = self.directory_permissions[self.current_state] & self.directory_permissions[dir_name]
                    perm_value = sum(common_perms) if common_perms else 0
                    
                    # Bitwise operations based on action type
                    if action.startswith('read'):
                        self.permission_score &= ~(perm_value << 1)
                    elif action.startswith('write'):
                        self.permission_score |= (perm_value << 2)
                    elif action.startswith('flush'):
                        self.permission_score ^= (perm_value >> 1)
                    else:
                        self.permission_score >>= 1
        return self.permission_score

# Execution
analyzer = DirectoryAccessAnalyzer()
events = [
    "ACCESS(ROOT:read_config)",
    "ACCESS(CONFIG:flush_temp)",
    "ACCESS(TEMP:cleanup)",
    "ACCESS(CONFIG:exit)",
    "ACCESS(ROOT:write_logs)",
    "ACCESS(LOGS:rotate)",
    "ACCESS(TEMP:exit)"
]
final_score = analyzer.process_access(events)
print(f"Result: {final_score}")