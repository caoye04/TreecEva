from collections import defaultdict

def calculate_arbitrage(transactions):
    # State machine states: 'IDLE', 'PROCESSING', 'OPTIMIZING', 'FINALIZED'
    state = 'IDLE'
    dp_table = defaultdict(lambda: 0)
    max_gain = float('-inf')
    
    for tx in transactions:
        if state == 'IDLE':
            if tx['type'] == 'START':
                state = 'PROCESSING'
                dp_table[tx['currency']] = tx['amount']
        elif state == 'PROCESSING':
            if tx['type'] == 'TRADE':
                current_value = dp_table[tx['from_curr']] * tx['rate']
                dp_table[tx['to_curr']] = max(dp_table[tx['to_curr']], current_value)
            elif tx['type'] == 'CHECKPOINT':
                state = 'OPTIMIZING'
                for curr, value in dp_table.items():
                    gain = value - 1000  # Base currency unit
                    if gain > 0:
                        max_gain = max(max_gain, gain)
        elif state == 'OPTIMIZING':
            if tx['type'] == 'END':
                state = 'FINALIZED'
                break
    
    return max_gain if max_gain != float('-inf') else 0

# Transaction log for currency arbitrage detection
transaction_log = [
    {'type': 'START', 'currency': 'USD', 'amount': 1000},
    {'type': 'TRADE', 'from_curr': 'USD', 'to_curr': 'EUR', 'rate': 0.85},
    {'type': 'TRADE', 'from_curr': 'USD', 'to_curr': 'GBP', 'rate': 0.75},
    {'type': 'TRADE', 'from_curr': 'EUR', 'to_curr': 'JPY', 'rate': 130.0},
    {'type': 'TRADE', 'from_curr': 'GBP', 'to_curr': 'JPY', 'rate': 150.0},
    {'type': 'CHECKPOINT'},
    {'type': 'TRADE', 'from_curr': 'JPY', 'to_curr': 'USD', 'rate': 0.009},
    {'type': 'END'}
]

max_arbitrage_gain = calculate_arbitrage(transaction_log)
print(f"Result: {max_arbitrage_gain}")