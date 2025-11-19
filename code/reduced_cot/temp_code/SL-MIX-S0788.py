from collections import deque

# Batch IDs produced today (stack behavior - last in, first out)
production_batches = [3, 1, 4, 2]  # Batch IDs
cookie_stack = []  # Stack of cookies

# Push batches onto stack in reverse order to simulate LIFO
for batch_id in reversed(production_batches):
    cookie_count = batch_id ** 2
    cookie_stack.extend([batch_id] * cookie_count)

# Order quantities (queue behavior - first in, first out)
orders_queue = deque([10, 25, 5, 16])
cookies_sold = 0

# Fulfill orders
while orders_queue and cookie_stack:
    order_size = orders_queue.popleft()
    for _ in range(min(order_size, len(cookie_stack))):
        cookie_stack.pop()
        cookies_sold += 1

# Remaining cookies is the length of the stack
remaining_cookies = len(cookie_stack)
print(f'Result: {remaining_cookies}')