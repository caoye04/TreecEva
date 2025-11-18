import re
import math
from functools import reduce

def tokenize_log(entry):
    pattern = r'(\w+):(\d+\.\d+)'
    return dict(re.findall(pattern, entry))

def compute_weighted_volatility(prices, decay_factor=0.9):
    if not prices:
        return 0.0
    weighted_sum = 0.0
    weight = 1.0
    for price in reversed(prices):
        weighted_sum += price * weight
        weight *= decay_factor
    return weighted_sum / len(prices)

class VolatilityTracker:
    def __init__(self):
        self.price_history = []
        self.event_counter = 0
    
    def process_entry(self, log_entry):
        tokens = tokenize_log(log_entry)
        if 'PRICE' in tokens:
            price = float(tokens['PRICE'])
            self.price_history.append(price)
            if len(self.price_history) > 10:
                self.price_history.pop(0)
        
        if 'EVENT' in tokens and re.match(r'VOLATILE_', tokens['EVENT']):
            self.event_counter += 1
            return True
        return False

log_entries = [
    "TYPE:TRADE PRICE:423.56 TIME:162345",
    "TYPE:TRADE PRICE:425.12 EVENT:NORMAL_TIME:162346",
    "TYPE:TRADE PRICE:420.89 TIME:162347",
    "TYPE:TRADE PRICE:418.75 EVENT:VOLATILE_SPIKE TIME:162348",
    "TYPE:TRADE PRICE:428.33 TIME:162349",
    "TYPE:TRADE PRICE:430.21 TIME:162350",
    "TYPE:TRADE PRICE:427.65 EVENT:VOLATILE_DROP TIME:162351",
    "TYPE:TRADE PRICE:422.44 TIME:162352"
]

tracker = VolatilityTracker()
volatility_scores = []

for i, entry in enumerate(log_entries):
    has_event = tracker.process_entry(entry)
    if has_event or (i > 0 and i % 3 == 0):
        vol_score = compute_weighted_volatility(tracker.price_history)
        volatility_scores.append(vol_score)
    elif len(tracker.price_history) >= 5:
        recent_prices = tracker.price_history[-5:]
        avg_price = sum(recent_prices) / len(recent_prices)
        log_val = math.log(avg_price) if avg_price > 0 else 0
        exp_val = math.exp(log_val / 10)
        adjusted_score = exp_val * (1 + tracker.event_counter * 0.1)
        volatility_scores.append(adjusted_score)

# Calculate final volatility index
if volatility_scores:
    volatility_index = reduce(lambda x, y: x + y * math.log(y + 1), volatility_scores, 0)
else:
    volatility_index = 0.0

print(f"Result: {round(volatility_index, 6)}")