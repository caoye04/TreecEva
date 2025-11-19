from collections import deque

class MigrationNode:
    def __init__(self, distance, next_node=None):
        self.distance = distance
        self.next = next_node

# Create linked list: 12 -> 18 -> 9 -> 15 -> 7
node5 = MigrationNode(7)
node4 = MigrationNode(15, node5)
node3 = MigrationNode(9, node4)
node2 = MigrationNode(18, node3)
node1 = MigrationNode(12, node2)

# Process using deque
migration_queue = deque()
current = node1
while current:
    migration_queue.append(current.distance)
    current = current.next

migration_total = sum(migration_queue)
print(f"Result: {migration_total}")