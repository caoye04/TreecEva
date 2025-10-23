from itertools import combinations
from statistics import variance
from functools import lru_cache

class SignalProcessor:
    def __init__(self):
        self.coeff_cache = {}
    
    @lru_cache(maxsize=None)
    def fib_coeff(self, n):
        if n <= 1:
            return n
        return self.fib_coeff(n-1) + self.fib_coeff(n-2)
    
    def process(self, amplitudes):
        # Initialize coefficients
        for i in range(1, 6):
            self.coeff_cache[i] = self.fib_coeff(i*2)
        
        # Process signal
        filtered = []
        for idx, amp in enumerate(amplitudes):
            if idx % 2 == 0:
                coeff_key = (idx // 2) % 5 + 1
                adjusted = amp * self.coeff_cache[coeff_key]
                if adjusted > 100:
                    filtered.append(adjusted / 2)
                else:
                    filtered.append(adjusted * 2)
            else:
                prev_filtered = filtered[-1] if filtered else 0
                combined = amp + prev_filtered
                if combined < 0:
                    filtered.append(combined * -1)
                else:
                    filtered.append(combined)
        
        # Apply combinatorial enhancement
        enhanced = []
        for i in range(len(filtered)):
            window = filtered[max(0, i-2):i+1]
            if len(window) >= 2:
                combos = list(combinations(window, 2))
                avg_combo = sum(a*b for a, b in combos) / len(combos) if combos else 0
                enhanced.append(avg_combo)
            else:
                enhanced.append(window[0] if window else 0)
        
        # Calculate energy using statistical variance
        if len(enhanced) > 1:
            processed_signal_energy = int(variance(enhanced) * 1000)
        else:
            processed_signal_energy = sum(enhanced)
        
        return processed_signal_energy

def main():
    processor = SignalProcessor()
    test_amplitudes = [10, -5, 20, -15, 30, 25, -10, 40]
    result = processor.process(test_amplitudes)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()