import math

def process_signal_batches():
    batch_data = {
        'alpha': [1.2, 3.5, 2.1, 4.8],
        'beta': [2.7, 1.9, 3.3],
        'gamma': [4.1, 2.8, 3.7, 1.5, 5.2]
    }
    
    # Dictionary comprehension to create transformed signal maps
    signal_maps = {
        batch_id: [round(freq ** 1.5, 2) for freq in freq_list]
        for batch_id, freq_list in batch_data.items()
    }
    
    # Merge with additional batch using dictionary merging
    additional_batch = {'delta': [3.3, 2.2, 4.4]}
    signal_maps = signal_maps | {k: [round(f**1.5, 2) for f in v] for k, v in additional_batch.items()}
    
    # Lambda function for energy calculation
    energy_func = lambda x: math.floor(x * 10) if x > 3 else math.ceil(x * 5)
    
    # Nested loops for processing
    aggregated_energy = 0
    for batch_values in signal_maps.values():
        batch_energy = 0
        for freq in batch_values:
            transformed_freq = energy_func(freq)
            batch_energy += transformed_freq
        aggregated_energy += batch_energy
    
    return aggregated_energy

aggregated_energy = process_signal_batches()
print(f"Result: {aggregated_energy}")