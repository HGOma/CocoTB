module adder(a,b,c);
    output wire [2:0]c;
    input wire [1:0]a,b;
    assign c=a+b;

    initial begin
        $dumpfile("adder_result.vcd");
        $dumpvars(1,adder);
    end
endmodule