import statistics

def call_tracker(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

def process_ancient_text():
    # Ancient text word frequencies
    word_frequencies = [12, 8, 15, 22, 9, 18, 9, 11, 14, 16, 7, 20, 13, 10, 17]
    
    # Filter out low frequency words
    significant_words = [freq for freq in word_frequencies if freq > 10]
    
    # Apply transformations using set operations
    unique_freq_set = frozenset(significant_words)
    transformed_freqs = []
    
    # Process each frequency with potential multiple transformations
    for freq in unique_freq_set:
        # Short-circuit evaluation pattern
        if freq > 15 and (freq % 2 == 0 or freq > 18):
            transformed_freqs.append(freq * 2)
        elif freq <= 15 or freq < 12:
            transformed_freqs.append(freq + 5)
        else:
            transformed_freqs.append(freq)
    
    # Calculate statistical measures
    mean_freq = statistics.mean(transformed_freqs)
    variance_freq = statistics.variance(transformed_freqs) if len(transformed_freqs) > 1 else 0
    
    # Apply final scoring algorithm
    @call_tracker
    def calculate_score(base_value, modifier):
        return base_value * modifier + len(transformed_freqs)
    
    # Multiple function calls to test decorator
    score1 = calculate_score(mean_freq, 1.5)
    score2 = calculate_score(variance_freq, 0.75)
    
    # Final calculation combining all factors
    final_score = int(score1 + score2 + calculate_score.call_count)
    
    return final_score

final_score = process_ancient_text()
print(f"Result: {final_score}")