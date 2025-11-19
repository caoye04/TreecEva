def usage_tracker(func):
    usage_log = []
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        usage_log.append(result)
        return result
    wrapper.log = usage_log
    return wrapper

ingredients_set = frozenset(['basil', 'oregano', 'thyme', 'rosemary', 'sage', 'parsley', 'chives'])
available_spices = ['cumin', 'paprika', 'turmeric', 'ginger', 'cinnamon', 'cardamom', 'cloves']
recipe_requirements = [3, 7, 2, 9, 1, 5, 4]
sorted_requirements = sorted(enumerate(recipe_requirements), key=lambda x: x[1], reverse=True)

@usage_tracker
def select_ingredient(index):
    return available_spices[index] if index < len(available_spices) else None

current_inventory = set(ingredients_set)
selected_spices = set()
final_selection_count = 0

for idx, req in sorted_requirements:
    spice_name = select_ingredient(idx % len(available_spices))
    if spice_name and spice_name not in selected_spices:
        is_sufficient = req > 3 if req <= 5 else (req > 6 if req <= 8 else False)
        current_inventory.add(spice_name) if is_sufficient else current_inventory.discard(spice_name)
        selected_spices.add(spice_name)
        final_selection_count = final_selection_count + 1 if is_sufficient else final_selection_count
    else:
        final_selection_count = final_selection_count - 1 if final_selection_count > 0 else final_selection_count

comparison_result = len(current_inventory) > 8
final_selection_count = final_selection_count * 2 if comparison_result else final_selection_count
print(f"Result: {final_selection_count}")