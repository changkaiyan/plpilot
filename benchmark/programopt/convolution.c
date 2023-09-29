Matrix convolve(Matrix input, Matrix kernel) {
    int new_rows = input.rows - kernel.rows + 1;  
    int new_cols = input.cols - kernel.cols + 1;
    
    Matrix result = create_matrix(new_rows, new_cols);
    
    for (int row = 0; row < new_rows; row++) {
        for (int col = 0; col < new_cols; col++) {
            double total = 0; 
            for (int k_row = 0; k_row < kernel.rows; k_row++) {
                for (int k_col = 0; k_col < kernel.cols; k_col++) {
                    total += kernel.values[k_row][k_col] *  
                             input.values[row + k_row][col + k_col];          
                }
             }
            result.values[row][col] = total;
         }
     }
    
    return result; 
}
