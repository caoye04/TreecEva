#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int accumulator = 0;
    
    for (size_t i = 0; i < matrix.size(); ++i) {
        for (size_t j = 0; j < matrix[i].size(); ++j) {
            if ((i + j) % 2 == 0) {
                accumulator += matrix[i][j];
            } else {
                accumulator -= matrix[i][j];
            }
        }
    }
    
    string text = "HELLO";
    int char_sum = 0;
    for (char c : text) {
        char_sum += static_cast<int>(c);
    }
    
    double angle_rad = M_PI / 4.0;
    double sine_val = sin(angle_rad);
    int scaled_sine = static_cast<int>(sine_val * 1000);
    
    int x = 12;
    int y = 18;
    int gcd_val = __gcd(x, y);
    int lcm_val = (x * y) / gcd_val;
    
    int bitwise = (x & y) | (x << 2);
    
    vector<int> numbers = {1, 2, 3, 4, 5};
    int product = 1;
    for (int num : numbers) {
        product *= num;
    }
    
    int final_result = (accumulator + char_sum + scaled_sine + lcm_val + bitwise + product) % 10000;
    
    cout << "Result: " << final_result << endl;
    return 0;
}