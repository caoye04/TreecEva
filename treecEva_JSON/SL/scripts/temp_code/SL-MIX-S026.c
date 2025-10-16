#define _USE_MATH_DEFINES
#include <stdio.h>
#include <string.h>

int main() {
    volatile int signal_changed = 0;
    int transition_counter = 0;
    char signal_log[] = "001110001011";
    int prev_state = signal_log[0] - '0';
    
    for (int i = 1; i < strlen(signal_log); i++) {
        int curr_state = signal_log[i] - '0';
        if (curr_state != prev_state) {
            signal_changed = 1;
            if (signal_changed) {
                transition_counter += 1;
                signal_changed = 0;
            }
        }
        prev_state = curr_state;
    }
    
    printf("Result: %d\n", transition_counter);
    return 0;
}