import re

def calculate_animation_index(target_hour):
    animation_index = 0
    pattern = r'[369]|12'  # Regex to detect multiples of 3
    
    for hour in range(1, target_hour + 1):
        if re.fullmatch(pattern, str(hour)):
            animation_index = 0
        else:
            animation_index = (animation_index + 1) % 7
    
    return animation_index

final_index = calculate_animation_index(10)
print(f"Result: {final_index}")