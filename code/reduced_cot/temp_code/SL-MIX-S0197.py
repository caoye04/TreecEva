class PackageNode:
    def __init__(self, weight, priority):
        self.weight = weight
        self.priority = priority
        self.next = None

def build_package_chain(weights, priorities):
    head = PackageNode(weights[0], priorities[0])
    current = head
    for i in range(1, len(weights)):
        current.next = PackageNode(weights[i], priorities[i])
        current = current.next
    return head

def calculate_adjusted_priority(node):
    adjustment_factor = 3
    return (node.weight * 2 + node.priority) // adjustment_factor

def update_chain_priorities(head):
    current = head
    while current:
        current.priority = calculate_adjusted_priority(current)
        current = current.next

# Initialize package data
package_weights = [15, 22, 18, 30]
package_priorities = [4, 7, 5, 9]

# Build the linked list
logistics_chain = build_package_chain(package_weights, package_priorities)

# Update priorities based on weight calculations
update_chain_priorities(logistics_chain)

# Dictionary comprehension to map weights to updated priorities
priority_mapping = {node.weight: node.priority for node in [
    logistics_chain, 
    logistics_chain.next, 
    logistics_chain.next.next, 
    logistics_chain.next.next.next
]}

# Merge with base operational factors
base_factors = {15: 2, 22: 3, 18: 1, 30: 4}
merged_data = {**base_factors, **priority_mapping}

# Lambda to compute final score
compute_final_score = lambda mapping: sum(
    (weight + priority) * 2 - 1 
    for weight, priority in mapping.items()
    if weight > 20
)

# Calculate the final priority score
final_priority_score = compute_final_score(merged_data)
print(f"Result: {final_priority_score}")