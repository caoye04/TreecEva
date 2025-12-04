def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def calculate_prime_product(nums, threshold):
    """Calculate product of prime numbers in list that are below threshold."""
    product = 1
    prime_count = 0
    non_prime_sum = 0
    
    filtered_nums = [n for n in nums if n > 0]
    
    # Dictionary to track frequency of each number
    frequency = {}
    for num in filtered_nums:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Sort numbers for better visualization (doesn't affect result)
    sorted_nums = sorted(filtered_nums)
    
    # Calculate some statistics that aren't used in the final result
    average = sum(filtered_nums) / len(filtered_nums) if filtered_nums else 0
    median_idx = len(sorted_nums) // 2
    median = sorted_nums[median_idx] if len(sorted_nums) % 2 == 1 else (sorted_nums[median_idx-1] + sorted_nums[median_idx]) / 2
    
    for num in filtered_nums:
        # Skip numbers that exceed the threshold
        if num >= threshold:
            continue
            
        # Check if prime and update product
        if is_prime(num):
            prime_count += 1
            # Use conditional expression to handle the case where we've seen this prime before
            multiplier = 1 if frequency.get(num, 0) <= 1 else num
            product *= num
        else:
            non_prime_sum += num
    
    # This doesn't affect the result but adds complexity
    result_stats = {
        'prime_count': prime_count,
        'non_prime_sum': non_prime_sum,
        'average': average,
        'median': median
    }
    
    return product

# Input data
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
threshold = 10  # Only consider numbers below 10

# Calculate the prime product
prime_product = calculate_prime_product(numbers, threshold)

# Print the result
print(f"Result: {prime_product}")