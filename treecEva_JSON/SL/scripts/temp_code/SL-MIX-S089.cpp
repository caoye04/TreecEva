#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    // Initialize nested data structures
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<int> primes = {29, 31, 37, 41, 43};
    
    // Step 1: Calculate the sum of each row in the matrix
    vector<int> row_sums;
    for (const auto& row : matrix) {
        int sum = 0;
        for (int val : row) {
            sum += val;
        }
        row_sums.push_back(sum);
    }
    
    // Step 2: Find the maximum row sum
    int max_row_sum = *max_element(row_sums.begin(), row_sums.end());
    
    // Step 3: Perform mathematical operations
    double sqrt_max = sqrt(static_cast<double>(max_row_sum));
    int rounded_sqrt = static_cast<int>(round(sqrt_max));
    
    // Step 4: Bitwise operations
    int bitwise_result = (rounded_sqrt << 2) ^ 0xF;  // Left shift by 2, then XOR with 15
    
    // Step 5: Use primes array
    int prime_sum = 0;
    for (int i = 0; i < 3; i++) {
        prime_sum += primes[i];
    }
    
    // Step 6: Complex calculation combining multiple values
    int intermediate = (bitwise_result & 0x1F) * 3;  // Bitwise AND with 31, then multiply by 3
    double power_result = pow(static_cast<double>(intermediate), 1.5);
    int final_intermediate = static_cast<int>(power_result) % 100;
    
    // Step 7: Final calculation
    int final_result = ((prime_sum - final_intermediate) >> 1) + max_row_sum;  // Right shift by 1, then add max_row_sum
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}