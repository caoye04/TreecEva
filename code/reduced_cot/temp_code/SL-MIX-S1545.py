import statistics
from functools import wraps

def track_steps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.steps.append(result)
        return result
    wrapper.steps = []
    return wrapper

@track_steps
def encode_nucleotide(seq):
    mapping = {'A': 1, 'T': 2, 'G': 3, 'C': 4}
    return [mapping[n] for n in seq]

@track_steps
def apply_transform(encoded):
    transform = lambda x: [v * 2 if i % 2 == 0 else v + 1 for i, v in enumerate(x)]
    return transform(encoded)

@track_steps
def compute_metrics(transformed):
    mean_val = statistics.mean(transformed)
    squared_diffs = [(x - mean_val) ** 2 for x in transformed]
    return statistics.mean(squared_diffs)

# Process pipeline
sequence = "ATCGATCG"
encoded_seq = encode_nucleotide(sequence)
transformed_vals = apply_transform(encoded_seq)
final_metric = compute_metrics(transformed_vals)

print(f"Result: {final_metric}")