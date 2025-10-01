#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int accumulator = 0;
    double temp = 0.0;
    string code = "COMPLEX";
    
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            if (i == j) {
                accumulator += matrix[i][j];
            }
        }
    }
    
    temp = pow(accumulator, 2) - 100;
    
    if (temp > 500) {
        temp = sqrt(temp);
    } else {
        temp = pow(temp, 1.5);
    }
    
    int x = static_cast<int>(floor(temp));
    int y = 0;
    
    switch(code.length()) {
        case 5:
            y = x * 2;
            break;
        case 6:
            y = x + 100;
            break;
        case 7:
            y = x / 2;
            break;
        default:
            y = x - 50;
    }
    
    vector<int> numbers = {y, 2 * y, y / 2, y + 10};
    int product = 1;
    
    for (int i = 0; i < numbers.size(); i++) {
        if (numbers[i] % 2 == 0) {
            product *= numbers[i];
        }
    }
    
    int final_result = product - (x * y);
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}