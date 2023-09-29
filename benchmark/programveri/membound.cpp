#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    printf("Enter size of array: ");
    scanf("%d", &n);

    int* arr = (int*) malloc(n * sizeof(int));

    if(arr == NULL) {
        printf("Memory allocation failed. Exiting program.\n");
        return 1;
    }
    
    << n>0 >>

    for(int i = 0; i < n; i++) {
        // Accessing memory out of bounds
        arr[i] = i;
        << i<n >>
    }

    free(arr);
    return 0;
}