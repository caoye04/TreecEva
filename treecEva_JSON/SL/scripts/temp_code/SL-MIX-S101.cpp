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
    double z = M_PI / 4.0;
    
    double temp = compute_expression(x, y, z);
    
    int arr[] = {static_cast<int>(temp), 42, 100};
    int* ptr = arr;
    
    int sum = 0;
    for (int i = 0; i < 3; ++i) {
        sum += *(ptr + i);
    }
    
    bool condition1 = (sum > 150);
    bool condition2 = (matrix[2][0] & 1);
    
    int intermediate = condition1 ? (condition2 ? sum * 2 : sum / 2) : (condition2 ? sum + 10 : sum - 10);
    
    vector<int> values = {intermediate, static_cast<int>(temp), x, y};
    sort(values.begin(), values.end());
    
    int final_result = 0;
    for (size_t i = 0; i < values.size(); ++i) {
        final_result ^= (values[i] << i);
    }
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}