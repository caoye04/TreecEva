#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    // Initialize complex nested data structures
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<string> tokens = {"abc", "def", "ghi"};
    
    // Step 1: Compute the sum of all elements in the matrix
    int sum_matrix = 0;
    for (const auto& row : matrix) {
        for (int val : row) {
            sum_matrix += val;
        }
    }
    
    // Step 2: Compute the product of the lengths of all strings in tokens
    int product_lengths = 1;
    for (const string& s : tokens) {
        product_lengths *= s.length();
    }
    
    // Step 3: Perform a mathematical operation using sum_matrix and product_lengths
    double intermediate = pow(sum_matrix, 1.0 / 3.0) * sqrt(product_lengths);
    
    // Step 4: Bitwise operations
    int bitwise_result = (sum_matrix & 0xFF) | (product_lengths << 2);
    
    // Step 5: Logical evaluations
    bool condition1 = (intermediate > 20.0);
    bool condition2 = (bitwise_result % 7 == 0);
    
    // Step 6: Complex conditional assignment
    int final_result = 0;
    if (condition1 && condition2) {
        final_result = static_cast<int>(intermediate) + bitwise_result;
    } else if (condition1 || condition2) {
        final_result = static_cast<int>(intermediate) ^ bitwise_result;
    } else {
        final_result = static_cast<int>(intermediate) - bitwise_result;
    }
    
    // Output the result
    cout << "Result: " << final_result << endl;
    
    return 0;
}