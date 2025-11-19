import math

def tokenize(transactions_str):
    return [t.strip() for t in transactions_str.split(',')]

transaction_weights = {
    'buy': lambda x: x * 1.2,
    'sell': lambda x: x * 0.9,
    'hold': lambda x: x * 1.05
}

class TransactionProcessor:
    def __init__(self):
        self.cache = {}
    
    def compute_score(self, action, amount):
        if (action, amount) in self.cache:
            return self.cache[(action, amount)]
        
        base = amount
        if action == 'buy':
            score = base + (base * 0.1)  # 10% bonus
        elif action == 'sell':
            score = base - (base * 0.05)  # 5% penalty
        else:
            score = base
        
        weighted_score = transaction_weights[action](score)
        self.cache[(action, amount)] = weighted_score
        return weighted_score

processor = TransactionProcessor()
raw_data = "buy 100, sell 50, hold 75, buy 200, sell 30"
tokens = tokenize(raw_data)

score_map = {}
for token in tokens:
    parts = token.split()
    action, amount_str = parts[0], parts[1]
    amount = int(amount_str)
    score = processor.compute_score(action, amount)
    if action in score_map:
        score_map[action] += score
    else:
        score_map[action] = score

aggregated = {k: round(v) for k, v in score_map.items()}
final_score = sum(aggregated.values())
print(f"Result: {final_score}")