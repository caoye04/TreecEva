#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_SIZE 10

struct Point {
    double x;
    double y;
};

struct DataContainer {
    struct Point points[MAX_SIZE];
    int count;
};

double calculateDistance(struct Point p1, struct Point p2) {
    return sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2));
}

int main() {
    struct DataContainer container = {{{{1.0, 2.0}, {3.0, 4.0}, {5.0, 6.0}, {7.0, 8.0}, {9.0, 10.0}, {11.0, 12.0}, {13.0, 14.0}, {15.0, 16.0}, {17.0, 18.0}, {19.0, 20.0}}, 10}};
    
    double distances[MAX_SIZE - 1];
    int i;
    for (i = 0; i < container.count - 1; i++) {
        distances[i] = calculateDistance(container.points[i], container.points[i+1]);
    }
    
    double sum = 0;
    for (i = 0; i < container.count - 1; i++) {
        sum += distances[i];
    }
    
    double average = sum / (container.count - 1);
    
    double variance = 0;
    for (i = 0; i < container.count - 1; i++) {
        variance += pow(distances[i] - average, 2);
    }
    variance /= (container.count - 1);
    
    int indices[3] = {2, 5, 7};
    double product = 1;
    for (i = 0; i < 3; i++) {
        product *= distances[indices[i]];
    }
    
    int binary = 0b110101;
    int mask = 0xF;
    int masked_value = binary & mask;
    
    double result = round((variance * product + masked_value) * 1000) / 1000;
    
    printf("Result: %.3f\n", result);
    return 0;
}