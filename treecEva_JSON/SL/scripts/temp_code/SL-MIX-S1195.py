from collections import defaultdict

class VendingMachineAnalyzer:
    def __init__(self):
        self.customer_states = defaultdict(lambda: 'NEW')
        self.customer_scores = defaultdict(int)
        self.transaction_counts = defaultdict(int)
        
    def process_transaction(self, customer_id, item_price, payment_method):
        current_state = self.customer_states[customer_id]
        
        # State transition logic
        if current_state == 'NEW':
            if item_price > 5.0:
                self.customer_states[customer_id] = 'PREMIUM_INTEREST'
            else:
                self.customer_states[customer_id] = 'BASIC_USER'
        elif current_state == 'BASIC_USER':
            if item_price > 10.0 and payment_method == 'CARD':
                self.customer_states[customer_id] = 'UPGRADE_CANDIDATE'
        elif current_state == 'PREMIUM_INTEREST':
            if item_price > 15.0:
                self.customer_states[customer_id] = 'LOYAL_CUSTOMER'
        elif current_state == 'UPGRADE_CANDIDATE':
            if item_price > 8.0:
                self.customer_states[customer_id] = 'LOYAL_CUSTOMER'
        
        # Update transaction count
        self.transaction_counts[customer_id] += 1
        
        # Calculate transaction score based on state and price
        state_scores = {
            'NEW': 1,
            'BASIC_USER': 2,
            'PREMIUM_INTEREST': 3,
            'UPGRADE_CANDIDATE': 4,
            'LOYAL_CUSTOMER': 5
        }
        
        self.customer_scores[customer_id] += state_scores[self.customer_states[customer_id]] * int(item_price)
    
    def finalize_scores(self):
        # Apply bonus logic for frequent customers
        for customer_id in self.customer_scores:
            if self.transaction_counts[customer_id] >= 3:
                # Fibonacci bonus calculation
                fib_sequence = [1, 1]
                for i in range(2, self.transaction_counts[customer_id]):
                    fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
                bonus = fib_sequence[-1] if fib_sequence else 0
                self.customer_scores[customer_id] += bonus
        
        # Calculate statistical adjustment
        scores_list = list(self.customer_scores.values())
        if scores_list:
            mean_score = sum(scores_list) / len(scores_list)
            variance = sum((x - mean_score) ** 2 for x in scores_list) / len(scores_list)
            adjustment_factor = int(variance ** 0.5) if variance > 0 else 1
            
            # Apply adjustment to highest scoring customer
            max_customer = max(self.customer_scores.keys(), key=lambda k: self.customer_scores[k])
            self.customer_scores[max_customer] += adjustment_factor

# Transaction data: (customer_id, item_price, payment_method)
transactions = [
    ('CUST_001', 3.50, 'COIN'),
    ('CUST_002', 12.75, 'CARD'),
    ('CUST_001', 8.25, 'CARD'),
    ('CUST_003', 6.00, 'COIN'),
    ('CUST_002', 15.50, 'CARD'),
    ('CUST_001', 11.00, 'CARD'),
    ('CUST_003', 4.25, 'COIN'),
    ('CUST_002', 9.80, 'CARD')
]

analyzer = VendingMachineAnalyzer()
for transaction in transactions:
    analyzer.process_transaction(*transaction)

analyzer.finalize_scores()

# Calculate final score as weighted sum of all customer scores
weights = [1, 2, 3]  # Weights for first three customers
final_customer_score = 0
sorted_customers = sorted(analyzer.customer_scores.keys())

for i, customer in enumerate(sorted_customers[:3]):
    weight = weights[i] if i < len(weights) else 1
    final_customer_score += analyzer.customer_scores[customer] * weight

print(f"Result: {final_customer_score}")