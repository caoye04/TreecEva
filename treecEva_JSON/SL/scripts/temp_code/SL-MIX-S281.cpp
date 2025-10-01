#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <string>

using namespace std;

double compute_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * c - (a & b);
}

int main() {
    vector<int> nums = {4, 9, 16, 25};
    map<string, double> values;
    values["alpha"] = 3.5;
    values["beta"] = 2.0;
    values["gamma"] = compute_expression(nums[1], nums[2], values["alpha"]);

    int x = static_cast<int>(values["gamma"]) % 7;
    int y = (x | 3) ^ 1;
    double z = pow(y, 2) + log(values["alpha"] + values["beta"]);

    string label = "result_" + to_string(y);
    values[label] = z;

    vector<vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int sum_diag = 0;
    for(int i = 0; i < 3; i++) {
        sum_diag += matrix[i][i];
    }

    double final_result = values[label] * sum_diag - (static_cast<int>(values["gamma"]) & x);
    cout << "Result: " << final_result << endl;
    return 0;
}