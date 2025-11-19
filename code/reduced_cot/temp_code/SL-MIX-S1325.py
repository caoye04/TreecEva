from collections import defaultdict

def fibonacci_generator():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

class VendingMachine:
    def __init__(self):
        self.inventory = defaultdict(int)
        self.popularity = defaultdict(int)
        self.fib_gen = fibonacci_generator()
        self.current_threshold = next(self.fib_gen)
        self.restock_events = 0
        self.state = 'IDLE'
    
    def purchase(self, item):
        if self.inventory[item] > 0:
            self.inventory[item] -= 1
            self.popularity[item] += 1
            self.state = 'PROCESSING'
            if self.popularity[item] >= self.current_threshold:
                self.restock(item)
            self.state = 'IDLE'
    
    def restock(self, item):
        self.restock_events += 1
        self.inventory[item] += 10
        self.popularity[item] = 0
        self.current_threshold = next(self.fib_gen)

# Initialize vending machine
vm = VendingMachine()
vm.inventory.update({'cola': 5, 'chips': 3, 'candy': 7})

# Customer interaction sequence
purchases = ['cola', 'chips', 'cola', 'candy', 'cola', 'chips', 'cola', 'candy', 'candy']
for item in purchases:
    vm.purchase(item)

restock_events = vm.restock_events
print(f"Result: {restock_events}")