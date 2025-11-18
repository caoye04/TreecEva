import heapq
from collections import defaultdict

class CategoryNode:
    def __init__(self, name, priority_modifier=0):
        self.name = name
        self.priority_modifier = priority_modifier
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)

def calculate_category_bonus(root, package_category):
    def dfs(node, path, target):
        if path == target:
            return node.priority_modifier
        for child in node.children:
            result = dfs(child, path + [child.name], target)
            if result is not None:
                return result + node.priority_modifier
        return None
    
    target_path = package_category.split('.')
    return dfs(root, [root.name], target_path) or 0

category_tree = CategoryNode('Logistics')
electronics = CategoryNode('Electronics', 5)
fashion = CategoryNode('Fashion', 3)
home_goods = CategoryNode('Home', 2)

category_tree.add_child(electronics)
category_tree.add_child(fashion)
category_tree.add_child(home_goods)

smartphones = CategoryNode('Smartphones', 8)
laptops = CategoryNode('Laptops', 6)
electronics.add_child(smartphones)
electronics.add_child(laptops)

clothing = CategoryNode('Clothing', 1)
footwear = CategoryNode('Footwear', 2)
fashion.add_child(clothing)
fashion.add_child(footwear)

# Package: (base_priority, category_path)
packages = [
    (42, 'Logistics.Electronics.Smartphones'),
    (35, 'Logistics.Fashion.Clothing'),
    (50, 'Logistics.Home'),
    (28, 'Logistics.Electronics.Laptops'),
    (33, 'Logistics.Fashion.Footwear')
]

heap = []
package_map = {}

for i, (base_priority, category) in enumerate(packages):
    bonus = calculate_category_bonus(category_tree, category)
    effective_priority = base_priority + bonus
    heapq.heappush(heap, (-effective_priority, i))  # Negative for max-heap
    package_map[i] = {
        'base': base_priority,
        'bonus': bonus,
        'effective': effective_priority,
        'category': category
    }

# Update operation - increase priority of package 2 (Home goods)
delta = 15
package_id = 2
old_priority = package_map[package_id]['effective']
new_priority = old_priority + delta
package_map[package_id]['effective'] = new_priority
package_map[package_id]['base'] += delta

# Rebuild heap with updated priorities
heap = [(-package_map[i]['effective'], i) for i in package_map]
heapq.heapify(heap)

# Process two deliveries (pop two highest priority items)
for _ in range(2):
    heapq.heappop(heap)

# Calculate statistics on remaining packages
remaining_priorities = [package_map[idx]['effective'] for _, idx in heap]
total_remaining = sum(remaining_priorities)
min_remaining = min(remaining_priorities)
max_remaining = max(remaining_priorities)

# Final adjustment using modular arithmetic
adjustment_factor = (total_remaining * 3) % 17
top_priority_score = max_remaining - min_remaining + adjustment_factor

print(f'Result: {top_priority_score}')