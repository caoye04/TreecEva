#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    // Initialize nested data structure
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    
    // Step 1: Compute the product of each row
    vector<long long> row_products;
    for (const auto& row : matrix) {
        long long product = 1;
        for (int val : row) {
            product *= val;
        }
        row_products.push_back(product);
    }
    
    // Step 2: Apply mathematical transformation
    vector<double> transformed;
    for (long long prod : row_products) {
        double t = pow(prod, 1.0/3.0) + log(prod) - sin(prod % 10);
        transformed.push_back(t);
    }
    
    // Step 3: Perform bitwise operations
    int bitwise_result = 0;
    for (size_t i = 0; i < transformed.size(); ++i) {
        int truncated = (int)transformed[i];
        bitwise_result ^= (truncated << i) & 0xFF;
    }
    
    // Step 4: Complex conditional logic
    int conditional_value = 0;
    for (size_t i = 0; i < matrix.size(); ++i) {
        int sum = 0;
        for (int val : matrix[i]) {
            sum += val;
        }
        if ((sum & 1) && (row_products[i] > 100)) {
            conditional_value += sum;
        } else if (!(sum & 1) || (transformed[i] < 10.0)) {
            conditional_value -= sum;
        }
    }
    
    // Step 5: Final calculation combining all previous results
    int final_result = (bitwise_result * conditional_value) % 1000;
    
    // Adjust based on mathematical properties
    if (final_result < 0) {
        final_result += 1000;
    }
    
    cout << "Result: " << final_result << endl;
    return 0;
}