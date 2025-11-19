import re
from collections import defaultdict
from statistics import variance

def tokenize_prices(data_string):
    return [float(x) for x in re.findall(r'-?\d+\.\d+', data_string)]

def filter_significant(changes):
    return [x for x in changes if abs(x) >= 0.5]

class TradeAnalyzer:
    def __init__(self):
        self.price_movements = []
        
    @property
    def positive_moves(self):
        return [m for m in self.price_movements if m > 0]
    
    def process_trades(self, raw_data):
        tokens = tokenize_prices(raw_data)
        self.price_movements = filter_significant(tokens)
        return len(self.price_movements)

# Execution begins here
market_feed = "BTC: +1.2 ETH: -0.3 LTC: +0.7 XRP: +0.4 BCH: -0.6 DOGE: +1.8"
analyzer = TradeAnalyzer()
analyzer.process_trades(market_feed)

positive_values = analyzer.positive_moves
if len(positive_values) > 1:
    adjusted_positive_variance = variance(positive_values) * 100
else:
    adjusted_positive_variance = 0.0

print(f"Result: {adjusted_positive_variance}")