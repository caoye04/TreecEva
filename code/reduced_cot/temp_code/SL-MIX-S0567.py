from collections import defaultdict

class VendingMachine:
    def __init__(self):
        self.inventory = defaultdict(int)
        self.coin_denominations = [25, 10, 5, 1]  # quarters, dimes, nickels, pennies
        self.state = 'READY'
        self.total_coins_dispensed = 0
    
    def process_purchase(self, item_price, payment):
        if self.state != 'READY':
            return False
        
        self.state = 'PROCESSING'
        change_due = payment - item_price
        
        if change_due < 0:
            self.state = 'ERROR'
            return False
        
        # Dynamic programming approach to minimize coins for change
        dp = [float('inf')] * (change_due + 1)
        dp[0] = 0
        coin_used = [0] * (change_due + 1)
        
        for i in range(1, change_due + 1):
            for coin in self.coin_denominations:
                if coin <= i and dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    coin_used[i] = coin
        
        # Count coins dispensed
        amount = change_due
        while amount > 0:
            coin = coin_used[amount]
            self.total_coins_dispensed += 1
            amount -= coin
        
        self.state = 'READY'
        return True

# Initialize vending machine
vm = VendingMachine()

# Process transactions
transactions = [
    (125, 150),  # item price: $1.25, paid: $1.50
    (90, 100),   # item price: $0.90, paid: $1.00
    (75, 100),   # item price: $0.75, paid: $1.00
    (45, 50),    # item price: $0.45, paid: $0.50
    (190, 200)   # item price: $1.90, paid: $2.00
]

for price, paid in transactions:
    vm.process_purchase(price, paid)

print(f"Result: {vm.total_coins_dispensed}")