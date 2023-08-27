`include "8:1MUX.v"

module _16to1(a,b,s,out);
    input wire [7:0]a,b;
    input wire [3:0]s;
    output wire out;
    wire n0,n1;

    _8to1(a[7:4],b[7:4],s[3:1],n0);
    _8to1(a[3:0],b[3:0],s[3:1],n1);
    _2to1(n0,n1,s[0],out);
endmodule
    