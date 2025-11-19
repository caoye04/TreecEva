from functools import reduce
from contextlib import contextmanager
class Portfolio:
    def __init__(self, assets):
        self.assets = assets
        self.trade_log = []

@contextmanager
def trade_context(portfolio, day):
    initial_assets = portfolio.assets.copy()
    try:
        yield portfolio
    finally:
        # Log changes
        changes = {k: portfolio.assets[k] - initial_assets[k] for k in portfolio.assets}
        portfolio.trade_log.append((day, changes))

def calculate_adjustment(base_value, factors):
    adjusted = base_value
    for f in factors:
        if f > 0:
            adjusted += f * 2
        else:
            adjusted -= abs(f) // 2
    return adjusted

portfolio = Portfolio({'AAPL': 100, 'GOOGL': 200, 'TSLA': 50})
trade_signals = [1, -2, 3, 0, -1]
encoded_signal = 0
with trade_context(portfolio, 'Day1') as p:
    for i, signal in enumerate(trade_signals):
        if signal != 0:
            factor = 1 << i if signal > 0 else 0
            encoded_signal |= factor
        adjustment = calculate_adjustment(p.assets['AAPL'], [signal, i])
        p.assets['AAPL'] = adjustment

# Execution point Y
print(f'Result: {encoded_signal}')