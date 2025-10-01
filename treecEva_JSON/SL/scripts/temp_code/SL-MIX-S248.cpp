#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    // Initialize complex nested data structure
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<vector<double>> results(3, vector<double>(3, 0.0));
    
    // Step 1: Perform mathematical transformations on matrix
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            double value = matrix[i][j];
            // Apply complex mathematical formula
            results[i][j] = pow(value, 1.5) + log(value + 1) - sin(value * 0.1);
        }
    }
    
    // Step 2: Apply logical conditions to filter values
    double accumulator = 0.0;
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            // Complex logical condition
            if((results[i][j] > 10.0 && (int)results[i][j] % 2 == 1) || 
               (results[i][j] <= 10.0 && (int)results[i][j] % 3 == 0)) {
                accumulator += results[i][j];
            }
        }
    }
    
    // Step 3: Bitwise operations on transformed values
    int bitwise_result = 0;
    for(int i = 0; i < 3; i++) {
        int row_sum = 0;
        for(int j = 0; j < 3; j++) {
            row_sum ^= (int)(results[i][j] * 100);  // XOR operation
        }
        bitwise_result |= row_sum;  // OR operation
    }
    
    // Step 4: Combine accumulator and bitwise results with advanced math
    double combined_value = sqrt(abs(accumulator)) * cos(bitwise_result * 0.01);
    
    // Step 5: Final complex calculation
    int final_result = (int)(combined_value * 1000) % 1000;
    
    // Apply correction based on prime number check
    bool is_prime = true;
    if(final_result < 2) is_prime = false;
    else {
        for(int i = 2; i <= sqrt(final_result); i++) {
            if(final_result % i == 0) {
                is_prime = false;
                break;
            }
        }
    }
    
    if(is_prime) {
        final_result = final_result ^ 0xFF;  // XOR with 255 if prime
    } else {
        final_result = final_result & 0x7F;  // AND with 127 if not prime
    }
    
    cout << "Result: " << final_result << endl;
    return 0;
}