__global__ void crop_kernel(unsigned char *input, unsigned char *output, 
                            int input_rows, int input_cols,
                            int output_rows, int output_cols,
                            int row_start, int col_start) {
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    
    if (row < output_rows && col < output_cols) {
        int input_row = row + row_start;
        int input_col = col + col_start;
        output[row * output_cols + col] = input[input_row * input_cols + input_col];
    } 
}