from collections import defaultdict, deque

class VendingMachine:
    def __init__(self):
        self.state = 'RESTOCKING'
        self.inventory = {'A': 100, 'B': 50, 'C': 75}
        self.event_queue = deque()
        
    def process_events(self):
        events = [
            ('customer_purchase', 15),
            ('maintenance_check', None),
            ('customer_purchase', 25),
            ('restock', 40),
            ('customer_purchase', 10),
            ('maintenance_check', None)
        ]
        
        for event_type, value in events:
            if self.state == 'RESTOCKING':
                if event_type == 'restock':
                    self.inventory['A'] += value
                    self.state = 'ACTIVE'
                elif event_type == 'customer_purchase':
                    # Cannot sell during restocking
                    self.state = 'MAINTENANCE'
                else:
                    self.state = 'ACTIVE'
                    
            elif self.state == 'ACTIVE':
                if event_type == 'customer_purchase':
                    if self.inventory['A'] >= value:
                        self.inventory['A'] -= value
                    else:
                        self.state = 'RESTOCKING'
                        continue
                elif event_type == 'maintenance_check':
                    self.state = 'MAINTENANCE'
                else:
                    self.state = 'RESTOCKING'
                    
            elif self.state == 'MAINTENANCE':
                if event_type == 'maintenance_check':
                    # Maintenance completed
                    inspection_result = sum(1 for v in self.inventory.values() if v > 0)
                    if inspection_result >= 2:
                        self.state = 'ACTIVE'
                    else:
                        self.state = 'RESTOCKING'
                elif event_type == 'restock':
                    self.inventory['A'] += value // 2
                    self.state = 'RESTOCKING'
                else:
                    self.state = 'RESTOCKING'
        
        return self.inventory['A']

# Linked list node for tracking transaction history
class TransactionNode:
    def __init__(self, transaction_id, amount, next_node=None):
        self.transaction_id = transaction_id
        self.amount = amount
        self.next = next_node

# Build transaction history
head = TransactionNode('T001', 15)
head = TransactionNode('T002', 25, head)
head = TransactionNode('T003', 10, head)

# Calculate total transactions processed
total_processed = 0
current = head
while current:
    total_processed += current.amount
    current = current.next

# State machine processing
vm = VendingMachine()
final_product_a_count = vm.process_events()

# Apply final adjustment based on transaction history
if total_processed > 40:
    final_product_a_count -= 5
else:
    final_product_a_count += 10

print(f"Result: {final_product_a_count}")