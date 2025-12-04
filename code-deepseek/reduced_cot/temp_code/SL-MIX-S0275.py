def calculate_multiples():
    # Calculate sum of multiples of 3 from 1 to 20
    base_range = list(range(1, 21))
    temp_list = [x for x in base_range if x % 3 == 0]
    final_output = sum(temp_list)
    print(f"Result: {final_output}")

calculate_multiples()