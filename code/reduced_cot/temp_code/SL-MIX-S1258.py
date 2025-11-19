from collections import defaultdict

class VendingMachine:
    def __init__(self):
        self.state = 'idle'
        self.inventory = defaultdict(int)
        self.revenue = 0.0
    
    def process_event(self, event, item_price=0, payment=0.0):
        if self.state == 'idle' and event == 'select_item':
            self.state = 'awaiting_payment'
            self.current_item_price = item_price
        elif self.state == 'awaiting_payment' and event == 'insert_payment':
            if payment >= self.current_item_price:
                self.state = 'dispensing'
                change = payment - self.current_item_price
                self.revenue += self.current_item_price
                return change
            else:
                self.state = 'insufficient_funds'
                return -1
        elif self.state == 'dispensing' and event == 'item_dispensed':
            self.state = 'idle'
        elif self.state == 'insufficient_funds' and event == 'reset':
            self.state = 'idle'
        return 0

machine = VendingMachine()
total_revenue = 0.0
items = [('soda', 1.5), ('chips', 1.0), ('candy', 0.75)]
payments = [2.0, 0.5, 1.0, 1.0, 2.0]

for i in range(3):
    item_name, price = items[i]
    machine.process_event('select_item', item_price=price)
    payment = payments[i*2]
    result = machine.process_event('insert_payment', payment=payment)
    if result != -1:
        machine.process_event('item_dispensed')
        total_revenue = (total_revenue * 100 + int(price * 100)) % 97
    else:
        payment = payments[i*2 + 1]
        result = machine.process_event('insert_payment', payment=payment)
        if result != -1:
            machine.process_event('item_dispensed')
            total_revenue = (total_revenue * 100 + int(price * 100)) % 97
        machine.process_event('reset')

print(f"Result: {total_revenue}")