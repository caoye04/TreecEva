def str_length_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return len(result)
    return wrapper

@str_length_decorator
def format_profile(profile_dict):
    return "Name: {}, Age: {}, City: {}".format(
        profile_dict['name'], 
        profile_dict['age'], 
        profile_dict['city']
    )

engineer_profile = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

formatted_length = format_profile(engineer_profile)
print(f'Result: {formatted_length}')