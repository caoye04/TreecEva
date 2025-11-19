from collections import deque

# Initialize today's bread inventory as a FIFO queue
bakery_inventory = deque()

# Morning batch additions
bakery_inventory.append(25)  # First batch: 25 loaves
bakery_inventory.append(30)  # Second batch: 30 loaves

# Customer orders fulfilled (FIFO)
fulfilled_orders = 0
fulfilled_orders += bakery_inventory.popleft()  # First order takes all from first batch
fulfilled_orders += bakery_inventory.popleft()  # Second order takes remaining from second batch

# Afternoon batch addition
bakery_inventory.append(20)  # Third batch: 20 loaves

# Late customer order
if bakery_inventory:
    fulfilled_orders += bakery_inventory.popleft()  # Takes from third batch

# Calculate remaining inventory
remaining_loaves = sum(bakery_inventory)
print(f'Result: {remaining_loaves}')