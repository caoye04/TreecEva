class HashProcessor:
    def __init__(self, base_value):
        self.base = base_value
        self.temp_cache = {}
        self.unused_counter = 0  # Distractor variable
        
    def process_data(self, data):
        # Main processing logic with distractions
        processed_set = set()
        intermediate = 0
        
        # Distractor operation - never used in final calculation
        fake_processing = lambda x: (x * 3) // 2 + 7
        distractor_result = fake_processing(len(data))
        
        # Actual processing logic
        for item in data:
            if item % 2 == 0:
                processed_set.add(item * 2)
            else:
                processed_set.add(item + self.base)
        
        # More distractions
        unused_list = [i for i in range(10)]  # Dead code path
        misleading_sum = sum(unused_list)  # Never used
        
        # Key computation
        filtered_data = filter(lambda x: x > 15, processed_set)
        mapped_values = map(lambda x: x // 3 if x % 3 == 0 else x - 1, filtered_data)
        
        # Final calculation with set operations
        unique_values = set(mapped_values)
        result = sum(unique_values) ^ (len(unique_values) * self.base)
        
        return result

# Main execution with distractions
data_stream = [5, 8, 12, 3, 17, 20, 6, 11]

# Multiple irrelevant variables and operations
aux_processor = HashProcessor(7)  # Distractor instance
aux_result = aux_processor.process_data([1, 2, 3])  # Never used

unrelated_calc = (8 * 3) + (15 // 4) - 2  # Dead computation
misleading_var = unrelated_calc * 2  # Never referenced

# Actual processing
hash_processor = HashProcessor(5)
final_hash = hash_processor.process_data(data_stream)

# Final output
print(f"Result: {final_hash}")