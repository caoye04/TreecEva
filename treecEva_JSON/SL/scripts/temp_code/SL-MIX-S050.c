#define _USE_MATH_DEFINES
#include <stdio.h>
#include <string.h>

#define SENSOR_PATTERN "S[0-9]{3}V[0-9]{2}"
#define MATCH(p, s) (strstr(s, p) != NULL)

int ascending(int a, int b) { return a > b; }
int descending(int a, int b) { return a < b; }

void bubble_sort(int* arr, int n, int (*compare)(int, int)) {
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (compare(arr[j], arr[j + 1])) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
}

int main() {
    int sensor_readings[] = {45, 12, 67, 23, 89, 34, 56};
    int n = sizeof(sensor_readings) / sizeof(sensor_readings[0]);
    int calibration_index = 0;
    char identifiers[][10] = {"S123V45", "S456V67", "S789V23"};
    
    // Pattern validation
    for (int i = 0; i < 3; i++) {
        if (MATCH(SENSOR_PATTERN, identifiers[i])) {
            calibration_index += i;
        }
    }
    
    // Sorting phase
    if (calibration_index % 2 == 0) {
        bubble_sort(sensor_readings, n, ascending);
    } else {
        bubble_sort(sensor_readings, n, descending);
    }
    
    // Final index computation
    for (int i = 0; i < n; i++) {
        if (sensor_readings[i] > 50) {
            calibration_index += i;
            break;
        }
    }
    
    printf("Result: %d\n", calibration_index);
    return 0;
}