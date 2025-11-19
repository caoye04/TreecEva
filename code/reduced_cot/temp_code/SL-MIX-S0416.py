from itertools import permutations

# Bird species counts per forest zone
avian_surveys = {
    'zone_alpha': 4,
    'zone_beta': 3,
    'zone_gamma': 5
}

def calibration_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        max_count = max(avian_surveys.values())
        return result + max_count
    return wrapper

@calibration_decorator
def compute_biodiversity(zone_data):
    total_permutations = 0
    for count in zone_data.values():
        if count >= 2:
            total_permutations += len(list(permutations(range(count), 2)))
    return total_permutations

biodiversity_index = compute_biodiversity(avian_surveys)
print(f"Result: {biodiversity_index}")