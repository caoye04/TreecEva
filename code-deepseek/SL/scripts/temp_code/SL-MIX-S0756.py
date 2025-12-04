def compute_accuracy(data_samples):
    processed_samples = []
    total_correct = 0
    predicted_labels = []
    
    # Process each data sample
    for sample in data_samples:
        feature_vector = sample['features']
        prediction_score = sum(feature_vector) % 10
        processed_samples.append(prediction_score)
        
        # Determine predicted label
        predicted_label = 1 if prediction_score >= 5 else 0
        predicted_labels.append(predicted_label)
        
        # Check if prediction matches true label
        if predicted_label == sample['true_label']:
            total_correct += 1
    
    # Calculate accuracy
    accuracy = total_correct / len(data_samples)
    
    # Additional processing that doesn't affect final result
    intermediate_sum = sum(processed_samples)
    max_prediction = max(predicted_labels)
    temp_adjustment = intermediate_sum * 0.01
    
    # Final accuracy calculation
    final_accuracy = accuracy * 100
    
    # Print result
    print(f"Result: {final_accuracy}")
    return final_accuracy

# Validation dataset
validation_data = [
    {'features': [1, 3, 5], 'true_label': 1},
    {'features': [2, 4, 1], 'true_label': 0},
    {'features': [7, 2, 6], 'true_label': 1},
    {'features': [0, 1, 2], 'true_label': 0},
    {'features': [4, 8, 3], 'true_label': 1},
    {'features': [1, 1, 1], 'true_label': 0},
    {'features': [9, 2, 4], 'true_label': 1},
    {'features': [3, 3, 3], 'true_label': 0}
]

# Execute the function
result = compute_accuracy(validation_data)