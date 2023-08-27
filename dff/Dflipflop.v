module dff(d,clk,en,q);
    input wire d,clk,en;
    output reg q;

    always@(posedge clk) begin
        if(en==1'b1) begin
            q<=d;
        end
    end 

    initial begin
        $dumpfile("dff.vcd");
        $dumpvars(1,dff);
    end
endmodule

