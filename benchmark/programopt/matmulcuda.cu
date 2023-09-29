__global__ void matmul_kernel(float *a, float *b, float *c, 
                              int a_rows, int a_cols, int b_cols) {
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    
    if (row < a_rows && col < b_cols) {
        float total = 0;
        for (int k = 0; k < a_cols; k++) {
            total += a[row * a_cols + k] * b[k * b_cols + col];
        }
        c[row * b_cols + col] = total;
    } 
}   