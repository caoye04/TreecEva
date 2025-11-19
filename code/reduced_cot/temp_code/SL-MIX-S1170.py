class MessageProcessor:
    def __init__(self):
        self.processed_chars = 0
        self.unique_transformations = set()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def transform_text(self, text):
        # Character substitution map
        cipher_map = {chr(i): chr((i - 97 + 13) % 26 + 97) for i in range(97, 123)}
        
        # Apply transformation and track unique chars
        transformed = ''
        for char in text.lower():
            if char.isalpha():
                new_char = cipher_map[char]
                transformed += new_char
                self.unique_transformations.add(new_char)
                self.processed_chars += 1
            else:
                transformed += char
        
        return transformed

# Process the intercepted message
intercepted_message = "Operation midnight chronicle proceeds at dawn"
substitution_weights = {'a': 3, 'b': 7, 'c': 2, 'd': 5, 'e': 1, 'f': 9}
filtered_chars = frozenset(['a', 'e', 'i', 'o', 'u'])

with MessageProcessor() as processor:
    # First transformation layer
    stage_one_result = processor.transform_text(intercepted_message)
    
    # Second filtering layer
    vowel_positions = [i for i, c in enumerate(stage_one_result) if c in filtered_chars]
    
    # Third evaluation layer
    position_scores = {pos: (pos * 3) % 7 for pos in vowel_positions if pos < 20}
    
    # Fourth aggregation layer
    weighted_score = sum(substitution_weights.get(c, 0) for c in stage_one_result[:20] if c in substitution_weights)
    
    # Final calculation
    unique_count = len(processor.unique_transformations)
    position_sum = sum(position_scores.values())
    
    # Logical evaluation combining all factors
    final_score = (
        (weighted_score > 15 and unique_count >= 10) * 42 +
        (position_sum > 30 or unique_count < 15) * 28 +
        (not (weighted_score < 10)) * 15
    )

print(f"Result: {final_score}")