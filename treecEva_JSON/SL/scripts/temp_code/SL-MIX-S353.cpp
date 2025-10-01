#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 4}, {5, 6, 7}, {8, 9, 10}};
    int base = 3;
    int exp = 4;
    double log_val = log2(1024.0);
    string s = "Hello";
    
    int power_result = pow(base, exp);
    int sum = 0;
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            sum += matrix[i][j] * (i+1) * (j+1);
        }
    }
    
    int a = 15, b = 25;
    int xor_result = a ^ b;
    int bit_shift = (xor_result << 2) | (xor_result >> 1);
    
    int combined = (power_result + static_cast<int>(log_val) + s.length()) & bit_shift;
    
    int final_result = (sum + combined) % 1000;
    
    // Execution point Y
    cout << "Result: " << final_result << endl;
    
    return 0;
}