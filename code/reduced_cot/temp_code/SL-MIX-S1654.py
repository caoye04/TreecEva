class SignalNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create a linked list: 3 -> -2 -> 5 -> -1 -> 4
head = SignalNode(3)
head.next = SignalNode(-2)
head.next.next = SignalNode(5)
head.next.next.next = SignalNode(-1)
head.next.next.next.next = SignalNode(4)

transformer = lambda x: x * 2 if x > 0 else abs(x) + 1
THRESHOLD = 9
processed_sum = 0
current = head

while current:
    transformed_val = transformer(current.val)
    if transformed_val > THRESHOLD:
        break
    processed_sum += transformed_val
    current = current.next

print(f"Result: {processed_sum}")