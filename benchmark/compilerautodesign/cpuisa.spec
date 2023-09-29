Instruction 	Description 	Opcode	Bit Function	Opcode length(bit)
Computating Instructions				
add	Add reg[op2] to reg[op1]	00000	12b'x+5bop1+5b'op2+10b'x	32
mul	Mul reg[op2] to reg[op1]	00001	12b'x+5bop1+5b'op2+10b'x	32
cmp	Determine the equality of reg[op1] and reg[op2].	00011	12b'x+5bop1+5b'op2+10b'x	32
Control  Instructions				
beq	Determine if reg[op1] is greater than or equal to reg[op2].	00100	12b'x+5bop1+5b'op2+10b'x	32
ble	Determine if reg[op1] is less than or equal to reg[op2]	00101	12b'x+5bop1+5b'op2+10b'x	32
blt	Determine if reg[op1] is less than reg[op2].	00110	12b'x+5bop1+5b'op2+10b'x	32
bge	Determine if reg[op1] is greater than or equal to reg[op2].	00111	12b'x+5bop1+5b'op2+10b'x	32
br	PC Jump  to reg[26:0]	00010	32b'M	32
Memory Instructions				
store	Store data_in to reg[op1]. 	01000	12b'x+5bop1+15b'x	32
load	Load the value from reg[op1] into data_out.	01001	12b'x+5bop1+15b'x	32
