#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    // Initialize complex nested data structures
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<pair<int, double>> data_points = {{1, 2.5}, {2, 3.7}, {3, 5.1}};
    
    // Step 1: Perform mathematical transformations on matrix
    int sum_of_products = 0;
    for (int i = 0; i < matrix.size(); i++) {
        int row_product = 1;
        for (int j = 0; j < matrix[i].size(); j++) {
            // Apply exponentiation and modulo operations
            matrix[i][j] = (int)(pow(matrix[i][j], 1.5)) % 100;
            row_product *= matrix[i][j];
        }
        sum_of_products += row_product;
    }
    
    // Step 2: Process data points with trigonometric functions
    double trig_sum = 0.0;
    for (auto& point : data_points) {
        // Apply sine and cosine transformations
        double transformed = sin(point.first) * cos(point.second) + cos(point.first) * sin(point.second);
        point.second = abs(transformed);
        trig_sum += point.second;
    }
    
    // Step 3: Combine results using bitwise operations
    int bitwise_result = (sum_of_products & 0xFF) | ((int)(trig_sum * 100) << 2);
    
    // Step 4: Apply advanced logical conditions
    int conditional_value = 0;
    if ((bitwise_result % 7) && (bitwise_result > 100)) {
        conditional_value = bitwise_result / 3;
    } else if (!(bitwise_result & 1)) {
        conditional_value = bitwise_result * 2;
    } else {
        conditional_value = bitwise_result + 42;
    }
    
    // Step 5: Final calculation involving all previous results
    int final_result = ((conditional_value ^ 0xAA) + sum_of_products) % 1000;
    
    // Adjust final result based on complex condition
    if (final_result > 500) {
        final_result = (int)sqrt(final_result) * 10;
    } else {
        final_result = final_result * 3 - 17;
    }
    
    cout << "Result: " << final_result << endl;
    return 0;
}