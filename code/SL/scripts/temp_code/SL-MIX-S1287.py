from collections import defaultdict

class TagNode:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

# Build tag hierarchy
document_tags = {}
document_tags['root'] = TagNode('root')
document_tags['historical'] = TagNode('historical')
document_tags['scientific'] = TagNode('scientific')
document_tags['manuscript'] = TagNode('manuscript', 15)
document_tags['letter'] = TagNode('letter', 8)
document_tags['diary'] = TagNode('diary', 12)
document_tags['research'] = TagNode('research', 20)
document_tags['observation'] = TagNode('observation', 5)

document_tags['root'].add_child(document_tags['historical'])
document_tags['root'].add_child(document_tags['scientific'])
document_tags['historical'].add_child(document_tags['manuscript'])
document_tags['historical'].add_child(document_tags['letter'])
document_tags['historical'].add_child(document_tags['diary'])
document_tags['scientific'].add_child(document_tags['research'])
document_tags['scientific'].add_child(document_tags['observation'])

# Propagation function with ternary and set operations
visited = set()
propagation_order = []

# Determine processing order using DFS
stack = [document_tags['root']]
while stack:
    node = stack.pop()
    if node.name not in visited:
        visited.add(node.name)
        propagation_order.append(node)
        stack.extend(reversed(node.children))

# Process in reverse order (leaves first)
for node in reversed(propagation_order):
    if node.children:
        # Use lambda to calculate weighted sum
        weight_func = lambda x: x.value * (1.5 if x.name in {'manuscript', 'research'} else 1.0)
        node.value = sum(weight_func(child) for child in node.children)
    # Apply bonus if node has more than 2 children
    node.value = node.value + (10 if len(node.children) > 2 else 0)

# Calculate final score with additional constraints
bonus_tags = frozenset(['manuscript', 'research'])
top_level_values = {name: node.value for name, node in document_tags.items() if name in ['historical', 'scientific']}

final_score = int(sum(top_level_values.values()) * (1.2 if len(bonus_tags & set(document_tags.keys())) >= 2 else 1.0))

print(f"Result: {final_score}")