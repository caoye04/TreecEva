#define _USE_MATH_DEFINES
#include <stdio.h>

void process_signal(int* start, int* end, int threshold) {
    if (start >= end) return;
    
    int* mid = start + (end - start) / 2;
    process_signal(start, mid, threshold);
    process_signal(mid + 1, end, threshold);
    
    if (start <= mid && mid < end) {
        if (*mid < threshold) {
            *mid = 0;
        }
        if (mid + 1 < end && *(mid + 1) < threshold) {
            *(mid + 1) = 0;
        }
    }
}

int main() {
    int signal_data[] = {5, 12, 3, 9, 15, 7, 20, 1, 8, 11};
    int length = sizeof(signal_data) / sizeof(signal_data[0]);
    int avg_threshold = 0;
    for (int i = 0; i < length; i++) {
        avg_threshold += signal_data[i];
    }
    avg_threshold /= length;
    
    process_signal(signal_data, signal_data + length, avg_threshold);
    
    int significant_peaks = 0;
    for (int i = 0; i < length; i++) {
        if (signal_data[i] != 0) {
            significant_peaks++;
        }
    }
    
    printf("Result: %d\n", significant_peaks);
    return 0;
}