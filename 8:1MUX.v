module _2to1(a,b,s,out);
    input wire a,b,s;
    output wire out;
    assign out=s?b:a;

endmodule

module _8to1(a,b,s,out);
    input wire [3:0]a,b;
    input wire [2:0]s;
    output out;
    wire n0,n1,n2,n4,n5;
    _2to1(a[0],b[0],s[0],n0);
    _2to1(a[1],b[1],s[0],n1);
    _2to1(a[2],b[2],s[0],n2);
    _2to1(a[3],b[3],s[0],n3);
    _2to1(n0,n1,s[1],n4);
    _2to1(n2,n3,s[1],n5);
    _2to1(n4,n5,s[2],out);
endmodule
