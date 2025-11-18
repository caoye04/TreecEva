from collections import Counter

def calculate_balance(potency_list):
    if not potency_list:
        return 0
    head, *tail = potency_list
    if head % 2 == 0:
        return 2 + calculate_balance(tail)
    else:
        return -1 + calculate_balance(tail)

ingredient_potencies = [12, 7, 4, 9, 3, 16, 5]
final_score = calculate_balance(ingredient_potencies)
print(f"Result: {final_score}")