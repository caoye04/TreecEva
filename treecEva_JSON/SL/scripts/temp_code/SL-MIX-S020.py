from functools import reduce

def digital_filter_transform(signal_samples):
    transform_lambda = lambda x, y: (x * 2 + y) % 100
    initial_accumulator = 5
    return reduce(transform_lambda, signal_samples, initial_accumulator)

audio_samples = [12, 7, 23, 8, 15]
processed_signal_strength = digital_filter_transform(audio_samples)
print(f"Result: {processed_signal_strength}")