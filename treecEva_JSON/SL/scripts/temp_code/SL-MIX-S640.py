import itertools
import math
from contextlib import contextmanager

data_matrix = [
    [2.5, 3.7, 1.2],
    [4.1, 0.9, 2.8],
    [3.3, 2.2, 5.0]
]

@contextmanager
def signal_logger():
    log_entries = []
    try:
        yield log_entries
    finally:
        pass

transformation_map = {
    'amp': lambda x: round(x * 1.5, 2),
    'att': lambda x: round(x * 0.7, 2),
    'boost': lambda x: round(x ** 1.2, 2)
}

with signal_logger() as log:
    adjusted_values = []
    for row in data_matrix:
        transformed_row = []
        for val in row:
            ops = list(itertools.combinations(transformation_map.keys(), 2))
            interim_results = []
            for op1, op2 in ops:
                res = transformation_map[op2](transformation_map[op1](val))
                interim_results.append(res)
            max_transformed = max(interim_results)
            transformed_row.append(max_transformed)
            log.append(f"Processed {val} -> {max_transformed}")
        adjusted_values.append(transformed_row)
    
    aggregate_sums = [sum(row) for row in adjusted_values]
    peak_aggregate = max(aggregate_sums)

print(f"Result: {peak_aggregate}")