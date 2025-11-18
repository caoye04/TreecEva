class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def count_accesses(head):
    access_count = {}
    current = head
    while current:
        ip = current.val
        access_count[ip] = access_count.get(ip, 0) + 1
        current = current.next
    return access_count

def create_linked_list(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for elem in elements[1:]:
        current.next = ListNode(elem)
        current = current.next
    return head

# Simulated access log as a linked list
access_logs = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.1", "192.168.1.1", "10.0.0.1", "10.0.0.1"]
ip_list_head = create_linked_list(access_logs)

# Count accesses using functional approach
access_counts = count_accesses(ip_list_head)

# Use ternary to determine whitelisting
whitelist = frozenset(ip for ip, count in access_counts.items() if count >= 3)

final_whitelist_size = len(whitelist)
print(f"Result: {final_whitelist_size}")