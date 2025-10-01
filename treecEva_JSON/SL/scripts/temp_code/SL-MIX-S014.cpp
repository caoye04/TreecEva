#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    // Initialize complex nested data structure
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    
    // Perform element-wise exponentiation and store results
    vector<vector<double>> exp_matrix(3, vector<double>(3));
    for(int i=0; i<3; i++) {
        for(int j=0; j<3; j++) {
            exp_matrix[i][j] = pow(matrix[i][j], 2);
        }
    }
    
    // Compute sum of each row in exp_matrix
    vector<double> row_sums(3);
    for(int i=0; i<3; i++) {
        double sum = 0;
        for(int j=0; j<3; j++) {
            sum += exp_matrix[i][j];
        }
        row_sums[i] = sum;
    }
    
    // Convert row sums to integers by flooring
    vector<int> int_row_sums(3);
    for(int i=0; i<3; i++) {
        int_row_sums[i] = static_cast<int>(floor(row_sums[i]));
    }
    
    // Perform bitwise XOR on all elements of int_row_sums
    int xor_result = 0;
    for(int i=0; i<3; i++) {
        xor_result ^= int_row_sums[i];
    }
    
    // Manipulate string based on xor_result
    string base_str = "HELLO";
    int shift_val = xor_result % 5;
    string shifted_str = "";
    for(char c : base_str) {
        shifted_str += static_cast<char>((c - 'A' + shift_val) % 26 + 'A');
    }
    
    // Calculate ASCII sum of shifted_str
    int ascii_sum = 0;
    for(char c : shifted_str) {
        ascii_sum += static_cast<int>(c);
    }
    
    // Final computation
    int result = (xor_result * 3) + (ascii_sum / 2) - 100;
    
    cout << "Result: " << result << endl;
    return 0;
}