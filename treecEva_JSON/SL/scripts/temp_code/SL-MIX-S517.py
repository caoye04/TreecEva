import math
from collections import deque

def process_audio_signals():
    # Initialize frequency coefficients stack (LIFO)
    freq_coefficients = [10, 100, 1000, 10000]
    
    # Initialize amplitude adjustments queue (FIFO)
    amp_adjustments = deque([0.5, 2.0, 0.25, 4.0])
    
    # Dictionary comprehension for pre-calculating log scales
    log_scales = {i: math.log(freq) for i, freq in enumerate(freq_coefficients)}
    
    # Process signals through multiple stages
    stage_results = {}
    
    # Stage 1: Apply logarithmic transformation to coefficients
    processed_freq = [math.log(freq) for freq in freq_coefficients]
    
    # Stage 2: Apply exponential amplification to adjustments
    amplified_amp = [math.exp(amp) for amp in amp_adjustments]
    
    # Stage 3: Combine using lambda function for dynamic weighting
    weight_func = lambda f, a: f * math.pow(a, 0.5)
    
    # Process pairs of values
    combined_signals = []
    for i in range(min(len(processed_freq), len(amplified_amp))):
        weighted = weight_func(processed_freq[i], amplified_amp[i])
        combined_signals.append(weighted)
    
    # Stage 4: Stack-based filtering (keep only values > threshold)
    threshold = math.log(1000)
    filtered_stack = [s for s in combined_signals if s > threshold]
    
    # Stage 5: Queue-based normalization
    normalization_factor = sum(filtered_stack) / len(filtered_stack) if filtered_stack else 1
    
    # Final calculation using both data structures
    final_signal_strength = 0
    if filtered_stack:
        # Pop from stack and dequeue from queue
        top_signal = filtered_stack.pop()
        front_adjustment = amp_adjustments.popleft() if amp_adjustments else 1
        final_signal_strength = top_signal * math.exp(front_adjustment) / normalization_factor
    
    return final_signal_strength

# Execute the signal processing
result = process_audio_signals()
print(f"Result: {result}")