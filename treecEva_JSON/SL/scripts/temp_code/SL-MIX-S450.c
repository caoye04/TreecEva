#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_LEN 10

// Recursive factorial with bitwise masking
typedef struct {
    int values[MAX_LEN];
    int size;
} IntArray;

long long masked_factorial(int n, int mask) {
    if (n <= 1) return (1 & mask);
    return ((n * masked_factorial(n - 1, mask)) & mask);
}

void process_array(IntArray* arr, int* result) {
    int i, temp_sum = 0;
    for (i = 0; i < arr->size; i++) {
        // Apply transformation based on index parity
        if (i % 2 == 0) {
            arr->values[i] = (arr->values[i] << 1) ^ 0xF;
        } else {
            arr->values[i] = (int)sqrt((double)(arr->values[i])) + 5;
        }
        temp_sum += arr->values[i];
    }
    *result = temp_sum;
}

int main() {
    // Initialize data structures
    IntArray data = {{2, 8, 3, 15, 7, 12, 5, 20, 9, 1}, 10};
    int sum_result = 0;
    long long fact_masked = 0;
    int xor_chain = 0;
    int ptr_offset = 3;
    int* ptr = data.values;
    
    // Step 1: Process array with transformations
    process_array(&data, &sum_result);
    
    // Step 2: Compute masked factorial using transformed value at index 4
    fact_masked = masked_factorial(data.values[4], 0xFF);
    
    // Step 3: Perform XOR chain over transformed elements at even indices
    for (int i = 0; i < data.size; i += 2) {
        xor_chain ^= data.values[i];
    }
    
    // Step 4: Pointer arithmetic and modular exponentiation
    int base_val = *(ptr + ptr_offset);
    int exp_val = (*(ptr + ptr_offset + 2)) % 7;
    int mod_exp_result = (int)fmod(pow((double)base_val, (double)exp_val), 100.0);
    
    // Final computation combining all intermediate results
    int final_result = ((sum_result + (int)fact_masked) ^ xor_chain) + mod_exp_result;
    
    printf("Result: %d\n", final_result);
    return 0;
}