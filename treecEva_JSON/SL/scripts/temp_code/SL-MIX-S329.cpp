#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

double compute_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) + log(c + 1);
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    
    int x = matrix[1][2] << 2;  // Left shift: 13 << 2 = 52
    int y = matrix[0][1] | matrix[2][0];  // Bitwise OR: 3 | 17 = 19
    
    string s1 = "hello";
    string s2 = "world";
    string s3 = s1 + s2;
    
    int len_combined = static_cast<int>(s3.length());  // Length of "helloworld" = 10
    
    double val = compute_expression(matrix[2][1], matrix[0][0], static_cast<double>(len_combined));
    
    int z = static_cast<int>(val) % 100;
    
    vector<int> arr(10);
    for (int i = 0; i < 10; ++i) {
        arr[i] = (i * z) & 0xF;  // Mask with 15
    }
    
    int sum_arr = 0;
    for (int i = 0; i < 10; ++i) {
        sum_arr += arr[i];
    }
    
    int final_result = ((x ^ y) + sum_arr) * (matrix[1][1] - matrix[0][2]);
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}