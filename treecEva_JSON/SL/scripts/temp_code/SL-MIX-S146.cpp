#define M_PI 3.14159265358979323846
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
    
    // Step 1: Calculate sum of all elements in matrix
    int matrix_sum = 0;
    for (const auto& row : matrix) {
        for (int val : row) {
            matrix_sum += val;
        }
    }
    
    // Step 2: Perform bitwise operations on primes
    int bitwise_result = primes[0];
    for (size_t i = 1; i < primes.size(); ++i) {
        if (i % 2 == 0) {
            bitwise_result ^= primes[i];
        } else {
            bitwise_result &= primes[i];
        }
    }
    
    // Step 3: Complex mathematical computation
    double math_result = pow(matrix_sum, 1.5) + log(static_cast<double>(bitwise_result)) * sin(M_PI/4);
    
    // Step 4: Manipulate data structures
    vector<int> combined;
    for (const auto& row : matrix) {
        combined.insert(combined.end(), row.begin(), row.end());
    }
    combined.insert(combined.end(), primes.begin(), primes.end());
    
    // Sort in descending order
    sort(combined.begin(), combined.end(), greater<int>());
    
    // Step 5: Advanced logical operations
    int logical_sum = 0;
    for (size_t i = 0; i < combined.size(); ++i) {
        if ((combined[i] > 20) && (i % 2 == 0 || combined[i] % 3 != 0)) {
            logical_sum += combined[i];
        }
    }
    
    // Step 6: Final calculation combining all results
    int final_result = static_cast<int>(math_result) ^ logical_sum;
    
    // Apply modulus to ensure positive result
    final_result = abs(final_result) % 1000;
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}