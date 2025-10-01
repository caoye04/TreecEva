#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

double compute_recursive_sum(vector<vector<double>>& matrix, int depth) {
    if (depth <= 0) return 0.0;
    
    double sum = 0.0;
    for (size_t i = 0; i < matrix.size(); ++i) {
        for (size_t j = 0; j < matrix[i].size(); ++j) {
            if (i == j) {
                sum += sin(matrix[i][j]) * cos(matrix[i][j]);
            } else {
                sum += sqrt(abs(matrix[i][j]));
            }
        }
    }
    
    vector<vector<double>> sub_matrix;
    if (matrix.size() > 1 && matrix[0].size() > 1) {
        sub_matrix.resize(matrix.size() - 1);
        for (size_t i = 1; i < matrix.size(); ++i) {
            sub_matrix[i-1].resize(matrix[i].size() - 1);
            for (size_t j = 1; j < matrix[i].size(); ++j) {
                sub_matrix[i-1][j-1] = matrix[i][j] / 2.0;
            }
        }
        sum += compute_recursive_sum(sub_matrix, depth - 1);
    }
    
    return sum;
}

int main() {
    vector<vector<double>> data = {{M_PI, 2.718, 1.414}, {3.14159, 2.0, 7.0}, {5.0, 8.0, 1.732}};
    
    // Apply transformation: element-wise power with index-based exponent
    for (size_t i = 0; i < data.size(); ++i) {
        for (size_t j = 0; j < data[i].size(); ++j) {
            data[i][j] = pow(data[i][j], (double)(i+j+1));
        }
    }
    
    // Bitwise manipulation on a derived value
    int bit_pattern = 0xF0 ^ ((int)data[0][0] & 0xFF);
    bit_pattern >>= 2;
    
    // Calculate recursive sum with depth of 2
    double recursive_component = compute_recursive_sum(data, 2);
    
    // Combine results with modulo arithmetic
    long long big_num = 123456789LL * 98765LL;
    int modulus_result = (int)(big_num % 1000);
    
    // Final calculation
    double final_result = (recursive_component + bit_pattern) * modulus_result;
    final_result = floor(final_result * 100.0 + 0.5) / 100.0; // Round to 2 decimal places
    
    cout << "Result: " << final_result << endl;
    return 0;
}