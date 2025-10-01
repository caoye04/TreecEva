#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    // Initialize data structures
    vector<vector<int>> matrix = {{2, 3, 4}, {5, 6, 7}, {8, 9, 10}};
    vector<int> coefficients = {3, -2, 5};
    string key = "COMPLEX_OPERATION";
    
    // Step 1: Perform matrix row operations with coefficients
    for(int i = 0; i < matrix.size(); i++) {
        for(int j = 0; j < matrix[i].size(); j++) {
            matrix[i][j] = matrix[i][j] * coefficients[j % coefficients.size()];
        }
    }
    
    // Step 2: Calculate aggregated sums
    vector<int> row_sums(matrix.size(), 0);
    for(int i = 0; i < matrix.size(); i++) {
        for(int j = 0; j < matrix[i].size(); j++) {
            row_sums[i] += matrix[i][j];
        }
    }
    
    // Step 3: Apply mathematical transformations
    double transformed_value = 0.0;
    for(int i = 0; i < row_sums.size(); i++) {
        transformed_value += pow(row_sums[i], 1.0/3.0) * sin(M_PI / 6.0);
    }
    
    // Step 4: Bitwise operations
    int bitwise_result = static_cast<int>(floor(transformed_value));
    bitwise_result = (bitwise_result << 2) ^ 0xF;
    
    // Step 5: String-based conditional logic
    int selector = 0;
    if(key.length() > 10 && key[0] == 'C') {
        selector = 1;
    } else if(key.find("OPERATION") != string::npos) {
        selector = 2;
    } else {
        selector = 3;
    }
    
    // Step 6: Final calculation combining all components
    int final_result = ((bitwise_result & 0xFF) * selector) + static_cast<int>(ceil(transformed_value));
    
    cout << "Result: " << final_result << endl;
    return 0;
}