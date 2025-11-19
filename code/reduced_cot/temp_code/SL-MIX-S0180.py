from collections import deque

class SignalProcessor:
    def __init__(self):
        self.filters = deque()
        self.signal_strength = 100
    
    def add_filter(self, filter_type, value):
        self.filters.append((filter_type, value))
    
    def process_signal(self):
        # Dynamic programming table for filter optimization
        dp = [0] * (len(self.filters) + 1)
        dp[0] = self.signal_strength
        
        i = 1
        while self.filters:
            filter_type, value = self.filters.popleft()
            if filter_type == 'amplify':
                dp[i] = dp[i-1] + (value * 2)
            elif filter_type == 'attenuate':
                dp[i] = dp[i-1] - (value // 3)
            elif filter_type == 'modulate':
                dp[i] = dp[i-1] ^ value
            i += 1
        
        # Binary search for optimal signal strength
        target = 150
        low, high = 0, len(dp) - 1
        while low <= high:
            mid = (low + high) // 2
            if dp[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        
        # Apply final adjustment based on search result
        final_signal_strength = dp[low] if low < len(dp) else dp[-1]
        return final_signal_strength

# Initialize processor
processor = SignalProcessor()

# Add filters in specific order
processor.add_filter('amplify', 25)
processor.add_filter('attenuate', 30)
processor.add_filter('modulate', 15)
processor.add_filter('amplify', 40)

# Process the signal
final_signal_strength = processor.process_signal()
print(f'Result: {final_signal_strength}')