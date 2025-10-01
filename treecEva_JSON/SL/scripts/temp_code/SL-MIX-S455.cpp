#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

double compute_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * sin(c);
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int x = matrix[1][2];
    int y = matrix[0][1] << 2;
    double z = M_PI / 4;
    
    double expr1 = compute_expression(x, y, z);
    
    int arr[] = {static_cast<int>(floor(expr1)), 42, 100};
    int* ptr = arr;
    int val = *(ptr + 1) ^ (~(*ptr));
    
    vector<int> numbers = {val, x, y, static_cast<int>(expr1)};
    sort(numbers.begin(), numbers.end());
    
    int sum = 0;
    for (size_t i = 0; i < numbers.size(); ++i) {
        sum += numbers[i] & 0xFF;
    }
    
    double final_result = (sum * cos(M_PI / 3)) + log(static_cast<double>(sum));
    cout << "Result: " << final_result << endl;
    return 0;
}