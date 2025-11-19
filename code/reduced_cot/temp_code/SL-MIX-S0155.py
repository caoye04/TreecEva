class PackageNode:
    def __init__(self, weight, value, next_node=None):
        self.weight = weight
        self.value = value
        self.next = next_node

def knapsack_dp(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]

def divide_conquer_knapsack(packages_head, capacity):
    if not packages_head:
        return 0
    if not packages_head.next:
        return packages_head.value if packages_head.weight <= capacity else 0
    
    # Split the list into two halves
    slow = fast = packages_head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    # Disconnect first half from second half
    prev.next = None
    
    left_weights, left_values = [], []
    right_weights, right_values = [], []
    
    current = packages_head
    while current:
        left_weights.append(current.weight)
        left_values.append(current.value)
        current = current.next
    
    current = slow
    while current:
        right_weights.append(current.weight)
        right_values.append(current.value)
        current = current.next
    
    left_capacity_map = {}
    right_capacity_map = {}
    
    for cap in range(capacity + 1):
        left_capacity_map[cap] = knapsack_dp(left_weights, left_values, cap)
        right_capacity_map[cap] = knapsack_dp(right_weights, right_values, cap)
    
    max_value = 0
    for cap in range(capacity + 1):
        remaining_cap = capacity - cap
        if remaining_cap >= 0:
            val = left_capacity_map[cap] + right_capacity_map.get(remaining_cap, 0)
            max_value = max(max_value, val)
    
    return max_value

# Build linked list of packages
packages_data = [
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 8),
    (9, 10)
]

head = None
for weight, value in reversed(packages_data):
    head = PackageNode(weight, value, head)

truck_capacity = 15
max_total_value = divide_conquer_knapsack(head, truck_capacity)
print(f"Result: {max_total_value}")