import numpy as np

# Neural signal processing simulation
data_stream = [12, 8, 15, 3, 9, 14, 7, 11]
baseline_correction = sum(data_stream[:4])
activation_score = sum(data_stream[4:]) * 2

# Extract response segment and apply normalization
response_slice = np.array(data_stream[2:6])
response_slice = response_slice - response_slice.mean()

# Evaluate alert condition based on activation and response coherence
distraction_variable_1 = activation_score + 100
random_offset = 5
threshold_flag = not (activation_score > 75) or (response_slice.sum() < 30)

# Print final result for evaluation
print(f"Result: {threshold_flag}")