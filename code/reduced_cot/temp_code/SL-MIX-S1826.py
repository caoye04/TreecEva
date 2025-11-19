from collections import defaultdict
import math

class ExchangeNode:
    def __init__(self, timestamp, rate):
        self.timestamp = timestamp
        self.rate = rate
        self.next = None

def build_rate_chain():
    head = ExchangeNode(1000, 1.234)
    current = head
    rates = [1.238, 1.229, 1.245, 1.251, 1.248]
    timestamps = [1005, 1010, 1015, 1020, 1025]
    for i in range(len(rates)):
        current.next = ExchangeNode(timestamps[i], rates[i])
        current = current.next
    return head

def analyze_market_behavior(head):
    volatility_tracker = defaultdict(list)
    current = head
    trend_state = 'STABLE'
    assessment_score = 0.0
    
    while current:
        rate = current.rate
        timestamp = current.timestamp
        
        # Market behavior classifier
        if rate > 1.24:
            market_phase = 'BULLISH'
        elif rate < 1.23:
            market_phase = 'BEARISH'
        else:
            market_phase = 'NEUTRAL'
        
        # State transition logic
        if trend_state == 'STABLE':
            if market_phase == 'BULLISH':
                trend_state = 'RISING'
            elif market_phase == 'BEARISH':
                trend_state = 'FALLING'
        elif trend_state == 'RISING':
            if market_phase == 'BEARISH':
                trend_state = 'VOLATILE'
            elif market_phase == 'NEUTRAL':
                trend_state = 'STABLE'
        elif trend_state == 'FALLING':
            if market_phase == 'BULLISH':
                trend_state = 'RECOVERING'
            elif market_phase == 'NEUTRAL':
                trend_state = 'STABLE'
        
        # Scoring mechanism
        score_modifier = 0.0
        match trend_state:
            case 'STABLE':
                score_modifier = rate * 0.1
            case 'RISING':
                score_modifier = rate * 0.15 + 0.5
            case 'FALLING':
                score_modifier = rate * 0.15 - 0.5
            case 'RECOVERING':
                score_modifier = rate * 0.2
            case 'VOLATILE':
                score_modifier = rate * 0.25
        
        assessment_score += score_modifier
        volatility_tracker[market_phase].append(rate)
        current = current.next
    
    # Final adjustment based on volatility patterns
    volatility_set = set(volatility_tracker.keys())
    required_patterns = frozenset(['BULLISH', 'BEARISH', 'NEUTRAL'])
    if volatility_set.issuperset(required_patterns):
        assessment_score *= 1.2
    
    return round(assessment_score, 4)

rate_chain_head = build_rate_chain()
final_assessment_score = analyze_market_behavior(rate_chain_head)
print(f"Result: {final_assessment_score}")