#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

struct Point {
    double x;
    double y;
};

typedef struct {
    int count;
    double values[5];
} DataArray;

int factorial(int n) {
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

double compute_distance(struct Point p1, struct Point p2) {
    double dx = p1.x - p2.x;
    double dy = p1.y - p2.y;
    return sqrt(dx*dx + dy*dy);
}

int main() {
    // Initialize variables
    int a = 15, b = 7;
    double x = 3.14159, y = 2.71828;
    char buffer[MAX_LEN] = "HelloWorldProgramming";
    
    // Step 1: Perform arithmetic and bitwise operations
    int step1 = ((a << 2) & 0xFF) + (b | 0x0F);
    
    // Step 2: Mathematical computations
    double step2 = pow(x, 2) + log(y) * sin(M_PI/4);
    
    // Step 3: String manipulation
    int str_len = strlen(buffer);
    int vowels = 0;
    for(int i=0; i<str_len; i++) {
        char c = buffer[i];
        if(c=='A'||c=='E'||c=='I'||c=='O'||c=='U'||
           c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
            vowels++;
    }
    
    // Step 4: Work with structs and arrays
    struct Point points[3] = {{0,0}, {3,4}, {1,1}};
    DataArray data = {3, {2.5, -1.2, 3.14, 0, 0}};
    
    double distances[3];
    for(int i=0; i<3; i++) {
        distances[i] = compute_distance(points[0], points[i]);
    }
    
    // Step 5: Complex calculations combining previous results
    double sum_distances = 0;
    for(int i=0; i<3; i++) {
        sum_distances += distances[i];
    }
    
    // Step 6: Advanced logic with multiple conditions
    int condition_check = (step1 > 50) && (vowels >= 5) ? 1 : 0;
    
    // Step 7: Final computation sequence
    double intermediate = (step2 * sum_distances) / (double)(str_len - vowels);
    
    long long final_computation = (long long)(intermediate * 1000);
    
    // Apply factorial only if condition is met
    if(condition_check) {
        final_computation += factorial(5);
    } else {
        final_computation -= data.values[2] * 100;
    }
    
    // Bitwise manipulation on final result
    final_computation ^= 0xABCDEF;
    
    // Final adjustment
    int final_result = (int)((final_computation % 10000) + data.count * vowels);
    
    printf("Result: %d\n", final_result);
    return 0;
}