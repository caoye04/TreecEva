def production_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

total_production_count = 0

@production_counter
def prepare_croissants():
    global total_production_count
    total_production_count += 12
    return "Croissants ready"

@production_counter
def prepare_eclairs():
    global total_production_count
    total_production_count += 8
    return "Eclairs ready"

@production_counter
def prepare_apple_tarts():
    global total_production_count
    total_production_count += 15
    return "Apple tarts ready"

pastry_type = 'eclairs'

match pastry_type:
    case 'croissants':
        prepare_croissants()
        prepare_croissants()
    case 'eclairs':
        prepare_eclairs()
        prepare_croissants()
        prepare_apple_tarts()
    case 'apple_tarts':
        prepare_apple_tarts()
        prepare_apple_tarts()
    case _:
        pass

result_dict = {
    'croissant_batches': prepare_croissants.count,
    'eclair_batches': prepare_eclairs.count,
    'tart_batches': prepare_apple_tarts.count
}

final_summary = {**result_dict, 'total_items': total_production_count}

print(f"Result: {final_summary['total_items']}")