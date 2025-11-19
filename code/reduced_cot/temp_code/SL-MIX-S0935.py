import math

def indicator_switch(ind_type, value):
    match ind_type:
        case 'RSI':
            return math.sqrt(value) if value >= 0 else -math.sqrt(-value)
        case 'MACD':
            return value ** 1.5 if value > 0 else -((-value) ** 1.5)
        case 'ATR':
            return math.log(abs(value) + 1) * (1 if value >= 0 else -1)
        case _:
            return 0.0

class SignalProcessor:
    def __init__(self):
        self.weights = {'RSI': 0.4, 'MACD': 0.35, 'ATR': 0.25}
        self.thresholds = {'RSI': 10.0, 'MACD': 5.0, 'ATR': 2.0}
    
    def process(self, indicators):
        weighted_sum = 0.0
        for ind_type, value in indicators.items():
            transformed = indicator_switch(ind_type, value)
            if abs(transformed) > self.thresholds[ind_type]:
                weighted_sum += transformed * self.weights[ind_type]
        return round(weighted_sum, 4)

def categorize_signal(signal):
    match signal:
        case s if s > 1.0:
            return 'STRONG_BUY'
        case s if 0.5 <= s <= 1.0:
            return 'BUY'
        case s if -0.5 < s < 0.5:
            return 'HOLD'
        case s if -1.0 <= s <= -0.5:
            return 'SELL'
        case s if s < -1.0:
            return 'STRONG_SELL'
        case _:
            return 'INVALID'

# Market data
market_indicators = {
    'RSI': 16.0,
    'MACD': -8.0,
    'ATR': 3.5
}

processor = SignalProcessor()
raw_signal = processor.process(market_indicators)

# Apply signal transformation
if raw_signal > 0:
    adjusted_signal = raw_signal * (1 + math.sin(raw_signal))
else:
    adjusted_signal = raw_signal * (1 + math.cos(raw_signal))

signal_category = categorize_signal(adjusted_signal)

# Final signal calculation
match signal_category:
    case 'STRONG_BUY':
        final_signal = int(adjusted_signal * 100) | 0b1111
    case 'BUY':
        final_signal = int(adjusted_signal * 100) ^ 0b1010
    case 'HOLD':
        final_signal = int(adjusted_signal * 100) & 0b1100
    case 'SELL':
        final_signal = int(adjusted_signal * 100) >> 1
    case 'STRONG_SELL':
        final_signal = int(adjusted_signal * 100) << 1
    case _:
        final_signal = 0

print(f"Result: {final_signal}")