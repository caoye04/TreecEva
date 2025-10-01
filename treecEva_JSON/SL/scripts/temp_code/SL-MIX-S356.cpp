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
    
    // Step 1: Perform element-wise exponentiation on matrix
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            matrix[i][j] = pow(matrix[i][j], 2);
        }
    }
    
    // Step 2: Calculate sum of each row in matrix
    vector<int> row_sums;
    for (const auto& row : matrix) {
        int sum = 0;
        for (int val : row) {
            sum += val;
        }
        row_sums.push_back(sum);
    }
    
    // Step 3: Apply bitwise operations on primes
    for (int i = 0; i < primes.size() - 1; i++) {
        primes[i] = primes[i] & primes[i+1];
    }
    
    // Step 4: Complex calculation using row sums and primes
    double accumulator = 0.0;
    for (int i = 0; i < min(row_sums.size(), primes.size()); i++) {
        accumulator += (double)row_sums[i] / (double)primes[i];
    }
    
    // Step 5: Trigonometric transformation
    int trig_result = (int)(sin(accumulator) * 1000);
    
    // Step 6: Logical operations with conditional assignments
    int condition_a = (trig_result > 0) ? trig_result : -trig_result;
    int condition_b = (row_sums[0] > primes[0]) && (row_sums[1] < primes[1]) ? 1 : 0;
    
    // Step 7: Final calculation combining all previous results
    int final_result = (condition_a ^ condition_b) + (row_sums[2] | primes[2]);
    
    cout << "Result: " << final_result << endl;
    return 0;
}