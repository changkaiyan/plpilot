module adder(
    input [3:0] a, b,    // 4-bit inputs
    input cin,            // Carry in
    output [4:0] sum,     // 4-bit sum 
    output cout           // Carry out
);

// Internal wires
wire [3:0] c;

// Assign sum 
assign sum = a ^ b ^ cin;  

// Carry propagate and generate  
assign c[0] = a[0] & b[0];  
assign c[1] = a[1] & b[1];  
assign c[2] = a[2] & b[2];
assign c[3] = a[3] & b[3];

// Ripple carry  
assign cout = c[0] | (c[1] & cin) | (c[2] & c[1]) | (c[3] & c[2]);

endmodule