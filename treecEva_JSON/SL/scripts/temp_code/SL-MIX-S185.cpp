#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

double calculateFee(double amount) {
    return (amount < 1000) ? amount * 0.02 : 
           (amount < 5000) ? amount * 0.015 : 
           amount * 0.01;
}

void merge(vector<double>& arr, int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;
    vector<double> L(n1), R(n2);
    for (int i = 0; i < n1; i++) L[i] = arr[l + i];
    for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];
    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(vector<double>& arr, int l, int r) {
    if (l >= r) return;
    int m = l + (r - l) / 2;
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);
    merge(arr, l, m, r);
}

int main() {
    vector<double> transactions = {1200.0, 800.0, 6500.0, 300.0, 4500.0};
    auto feeLambda = [](double amt) -> double { return calculateFee(amt); };
    vector<double> fees(transactions.size());
    
    for (size_t i = 0; i < transactions.size(); ++i) {
        fees[i] = feeLambda(transactions[i]);
    }
    
    mergeSort(fees, 0, static_cast<int>(fees.size()) - 1);
    
    double total_fee_aggregate = 0.0;
    for (const auto& fee : fees) {
        total_fee_aggregate += fee;
    }
    
    cout << "Result: " << total_fee_aggregate << endl;
    return 0;
}