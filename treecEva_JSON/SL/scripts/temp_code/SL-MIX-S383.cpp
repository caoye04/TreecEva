#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    // Initialize complex nested data structures
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<pair<int, double>> data_pairs = {{1, 1.5}, {2, 2.5}, {3, 3.5}};
    
    // Step 1: Perform mathematical operations on matrix
    int matrix_sum = 0;
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            matrix_sum += matrix[i][j] * (i + 1) * (j + 1);
        }
    }
    
    // Step 2: Process data pairs with mathematical functions
    double pair_product = 1.0;
    for (auto& p : data_pairs) {
        pair_product *= pow(p.first, p.second) / sqrt(p.first + p.second);
    }
    
    // Step 3: Complex bitwise and logical operations
    int bitwise_result = 0;
    for (int i = 0; i < 10; i++) {
        if ((i & 1) && !(i % 3)) {  // Odd numbers divisible by 3
            bitwise_result |= (1 << i);
        } else if (!(i & 1) || (i % 5)) {  // Even numbers or not divisible by 5
            bitwise_result ^= i;
        }
    }
    
    // Step 4: Advanced calculations combining previous results
    double intermediate = pow(matrix_sum, 1.0/3.0) * log(pair_product + 1) + sin(bitwise_result);
    
    // Step 5: Conditional processing with multiple branches
    int condition_counter = 0;
    for (int i = 1; i <= 20; i++) {
        bool cond1 = (i % 3 == 0) && (i * i > 50);
        bool cond2 = (i % 7 == 0) || (pow(i, 0.5) < 5);
        
        if (cond1 && !cond2) {
            condition_counter += i * 2;
        } else if (!cond1 && cond2) {
            condition_counter -= i;
        } else if (cond1 && cond2) {
            condition_counter += i * i;
        }
    }
    
    // Step 6: Final complex computation
    int final_result = static_cast<int>(
        (intermediate * condition_counter) / 
        (bitwise_result ? bitwise_result : 1) +
        ceil(pair_product) * floor(sqrt(matrix_sum))
    ) % 1000;
    
    cout << "Result: " << final_result << endl;
    return 0;
}