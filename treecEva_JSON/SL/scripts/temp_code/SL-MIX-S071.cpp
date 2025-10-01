#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

double complex_calculation(vector<vector<int>>& matrix, string& modifier) {
    double sum = 0.0;
    int rows = matrix.size();
    int cols = matrix[0].size();
    
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (i % 2 == 0 && j % 2 == 0) {
                sum += sqrt(abs(matrix[i][j]));
            } else if (i % 2 != 0 && j % 2 != 0) {
                sum += pow(matrix[i][j], 2);
            } else {
                sum += matrix[i][j] * 1.5;
            }
        }
    }
    
    if (modifier == "exp") {
        sum = exp(sum / (rows * cols));
    } else if (modifier == "log") {
        sum = log(sum + 1);
    }
    
    return sum;
}

int main() {
    vector<vector<int>> data = {{4, -9, 16}, {25, -36, 49}, {64, -81, 100}};
    string mode = "exp";
    
    double intermediate = complex_calculation(data, mode);
    
    // Perform bit manipulations
    int bit_value = static_cast<int>(intermediate * 1000) & 0xFF;
    bit_value = bit_value ^ (bit_value >> 2);
    
    // Mathematical transformations
    double trig_result = sin(intermediate) * cos(intermediate/2);
    
    // Complex conditional logic
    double final_result;
    if (bit_value > 100) {
        final_result = intermediate * trig_result;
    } else if (bit_value > 50) {
        final_result = intermediate + trig_result;
    } else {
        final_result = pow(intermediate, 1.0/3.0) * trig_result;
    }
    
    // Execution point Y
    cout << "Result: " << final_result << endl;
    
    return 0;
}