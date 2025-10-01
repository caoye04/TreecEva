#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_SIZE 10

struct DataPoint {
    double value;
    int flag;
};

typedef struct {
    struct DataPoint points[MAX_SIZE];
    int count;
} DataSet;

int factorial(int n) {
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

double compute_series(double x, int terms) {
    double sum = 0;
    for (int i = 0; i < terms; i++) {
        sum += pow(x, i) / factorial(i);
    }
    return sum;
}

void process_dataset(DataSet* dataset) {
    for (int i = 0; i < dataset->count; i++) {
        if (dataset->points[i].flag) {
            dataset->points[i].value = sqrt(fabs(dataset->points[i].value)) +
                                     sin(dataset->points[i].value) * cos(dataset->points[i].value);
        } else {
            dataset->points[i].value = ceil(dataset->points[i].value) -
                                     floor(dataset->points[i].value / 2.0);
        }
    }
}

int main() {
    DataSet data = {
        .points = {
            {.value = 4.0, .flag = 1},
            {.value = -9.0, .flag = 0},
            {.value = 16.0, .flag = 1},
            {.value = -25.0, .flag = 0},
            {.value = 36.0, .flag = 1}
        },
        .count = 5
    };
    
    process_dataset(&data);
    
    double accumulator = 0.0;
    for (int i = 0; i < data.count; i++) {
        accumulator += data.points[i].value;
    }
    
    char buffer[50];
    sprintf(buffer, "%.2f", accumulator);
    int len = strlen(buffer);
    int digit_sum = 0;
    for (int i = 0; i < len; i++) {
        if (buffer[i] >= '0' && buffer[i] <= '9') {
            digit_sum += buffer[i] - '0';
        }
    }
    
    double intermediate = compute_series(accumulator / 10.0, 5);
    long long result = (long long)(intermediate * digit_sum) & 0xFF;
    result ^= (result >> 2) | (digit_sum << 3);
    
    printf("Result: %lld\n", result);
    return 0;
}