import heapq

class Trade:
    def __init__(self, impact, timestamp):
        self.impact = impact
        self.timestamp = timestamp
    
def calculate_priority(trade, depth=0):
    if depth > 3:
        return 0
    base_score = trade.impact << (depth + 1)
    adjustment = (trade.timestamp & 0xF) * (-1 if trade.impact < 0 else 1)
    child_score = calculate_priority(Trade(trade.impact >> 1, trade.timestamp + 1), depth + 1)
    return base_score + adjustment + child_score

def process_trades(trade_list):
    heap = []
    for trade in trade_list:
        priority = calculate_priority(trade)
        heapq.heappush(heap, (-priority, trade))
    
    total_score = 0
    executed = 0
    while heap and executed < 3:
        neg_priority, trade = heapq.heappop(heap)
        priority = -neg_priority
        weight = 1 if executed == 0 else (executed * 0.5)
        total_score += priority * weight
        executed += 1
    return total_score

trades = [
    Trade(12, 100),
    Trade(-5, 200),
    Trade(8, 150),
    Trade(15, 120)
]

final_score = process_trades(trades)
print(f"Result: {int(final_score)}")