from collections import defaultdict

class CurrencyNode:
    def __init__(self, name, score=0.0):
        self.name = name
        self.score = score
        self.children = {}

def build_preference_tree():
    root = CurrencyNode('USD')
    root.children['GBP'] = CurrencyNode('GBP', 1.25)
    root.children['JPY'] = CurrencyNode('JPY', 0.95)
    
    root.children['GBP'].children['CHF'] = CurrencyNode('CHF', 1.1)
    root.children['GBP'].children['EUR'] = CurrencyNode('EUR', 1.15)
    
    root.children['JPY'].children['CAD'] = CurrencyNode('CAD', 0.85)
    root.children['JPY'].children['AUD'] = CurrencyNode('AUD', 0.9)
    
    root.children['GBP'].children['CHF'].children['EUR'] = CurrencyNode('EUR', 1.05)
    
    return root

def traverse_greedy_path(root):
    current = root
    path_score = 0.0
    visited_currencies = frozenset([root.name])
    
    while current.name != 'EUR':
        if not current.children:
            break
        
        # Greedily select child with highest score not in visited_currencies
        candidates = {name: node for name, node in current.children.items() 
                     if name not in visited_currencies}
        
        if not candidates:
            break
            
        next_currency = max(candidates.keys(), key=lambda x: candidates[x].score)
        path_score += candidates[next_currency].score
        current = candidates[next_currency]
        visited_currencies |= {current.name}
    
    return path_score

tree_root = build_preference_tree()
final_score = traverse_greedy_path(tree_root)
print(f'Result: {final_score}')