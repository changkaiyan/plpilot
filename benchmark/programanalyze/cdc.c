#include <stdio.h>

int main() {
    int x = 5;
    
    // This code is executed
    printf("x = %d\n", x);  
    
    if (x > 10) {
        // This code is dead since the condition is false
        printf("x is greater than 10\n");  
    }
    
    // This code is executed 
    printf("Continuing ...\n");  
    
    while (x < 0) {
        // This loop never executes since the condition is false
        printf("In loop\n");
        x++;
    }
    
    // This is dead code since the loop above never executes 
    printf("After loop\n");  
}