class DrinkNode:
    def __init__(self, count):
        self.count = count
        self.next = None

class BeverageDispenser:
    def __init__(self):
        self.head = None
        self.state = 'IDLE'
    
    def add_customer(self, count):
        new_node = DrinkNode(count)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def serve_drinks(self):
        total_served = 0
        current = self.head
        while current:
            if self.state == 'IDLE':
                self.state = 'SERVING'
            if self.state == 'SERVING':
                total_served += current.count
                self.state = 'IDLE'
            current = current.next
        return total_served

dispenser = BeverageDispenser()
dispenser.add_customer(3)
dispenser.add_customer(5)
dispenser.add_customer(2)
total_served = dispenser.serve_drinks()
print(f'Result: {total_served}')