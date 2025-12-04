def calculate_final_result(data_items, modifier):
    base_data = [item for item in data_items if item % 2 == 0]
    temp_scores = list(map(lambda x: x * 2 + 1, base_data))
    
    # Distractor computation that doesn't affect final result
    irrelevant_stats = {x: len(str(x)) for x in temp_scores}
    dummy_sum = sum(irrelevant_stats.values())  # Not used in final calculation
    
    processed_values = [modifier(val) for val in temp_scores]
    weighted_scores = {idx: score * 0.75 for idx, score in enumerate(processed_values)}
    
    intermediate_total = sum(weighted_scores.values())
    final_score = int(intermediate_total * 1.1)
    
    return final_score

initial_dataset = [8, 15, 22, 37, 42, 51]
adjustment_fn = lambda x: x - 3 if x > 10 else x + 5

filtered_data = [x for x in initial_dataset if x > 20]
final_score = calculate_final_result(filtered_data, adjustment_fn)
print(f"Result: {final_score}")