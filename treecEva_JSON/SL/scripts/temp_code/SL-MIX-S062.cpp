#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 4}, {5, 6, 7}, {8, 9, 10}};
    int base_value = 0;
    
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            base_value += matrix[i][j] * (i + 1) * (j + 1);
        }
    }
    
    double temp = pow(base_value, 1.0/3.0);
    int intermediate = static_cast<int>(floor(temp));
    
    string s = to_string(intermediate);
    int digit_sum = 0;
    for (char c : s) {
        if (isdigit(c)) {
            digit_sum += c - '0';
        }
    }
    
    int final_result = (intermediate & 0xF) ^ digit_sum;
    
    cout << "Result: " << final_result << endl;
    return 0;
}