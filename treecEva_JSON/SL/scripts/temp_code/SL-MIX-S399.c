#define _USE_MATH_DEFINES
#include <stdio.h>

int apply_filter(int index, int value);
int operation_selector(int index, int value);

int (*filter_operations[])(int, int) = {
    operation_selector,
    apply_filter
};

volatile int processed_signal = 0;

int operation_selector(int index, int value) {
    int result;
    switch(index % 3) {
        case 0:
            result = value + 2;
            break;
        case 1:
            result = value * 2;
            break;
        case 2:
            result = value - 1;
            break;
        default:
            result = value;
    }
    return result;
}

int apply_filter(int index, int value) {
    if (index <= 0) {
        return value;
    }
    int transformed = filter_operations[0](index, value);
    return transformed + apply_filter(index-1, transformed);
}

int main() {
    int sensor_data[] = {3, 5, 2, 7};
    int data_size = 4;
    
    for (int i = 0; i < data_size; i++) {
        processed_signal += filter_operations[1](i, sensor_data[i]);
    }
    
    printf("Result: %d\n", processed_signal);
    return 0;
}