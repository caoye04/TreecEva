class TraderNode:
    def __init__(self, pair, volume):
        self.pair = pair
        self.volume = volume
        self.next = None

def build_trader_list():
    head = TraderNode(('USD', 'EUR'), 1500)
    head.next = TraderNode(('EUR', 'JPY'), 2300)
    head.next.next = TraderNode(('JPY', 'GBP'), 800)
    head.next.next.next = TraderNode(('GBP', 'USD'), 3100)
    return head

def process_exchanges(trader_head):
    max_volume = 0
    current = trader_head
    
    while current and (current.pair[0] != 'INVALID' or current.volume > 0):
        if current.volume > max_volume and current.pair[0] in ['USD', 'EUR', 'JPY']:
            max_volume = current.volume
        current = current.next
    
    return max_volume

from functools import wraps
def volume_monitor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@volume_monitor
def calculate_max_volume():
    traders = build_trader_list()
    return process_exchanges(traders)

from collections import defaultdict
exchange_stats = defaultdict(int)
exchange_stats['processed'] += 1

max_volume = calculate_max_volume()
print(f"Result: {max_volume}")