def preparation_tracker(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 1.15
    return wrapper

def get_base_time(pastry_type):
    switcher = {
        'croissant': 45,
        'muffin': 20,
        'danish': 35
    }
    return switcher.get(pastry_type, 0)

@preparation_tracker
def calculate_preparation_time(base_time):
    return base_time

pastry = 'croissant'
base_preparation_time = get_base_time(pastry)
final_preparation_time = calculate_preparation_time(base_preparation_time)
print(f'Result: {final_preparation_time}')