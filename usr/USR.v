module usr#(parameter N=8)(clk,serial_in,parallel_in,enable,serial_out);
    input wire serial_in,clk;
    input wire [1:0]enable;
    input wire [N-1:0] parallel_in;

    output reg serial_out;

    reg [N-1:0]data,next;

    always@(posedge clk) begin
        data<=next;
    end

    always@ * begin
        case(enable)
            2'b00: next=data; //Memory case
            2'b01: next={serial_in,data[N-1:1]}; //right shift case
            2'b10: next={data[N-2:0],1'b0}; //left shift case
            2'b11: next=parallel_in; // load case
        endcase
    end

    always@ * begin
        if(enable==2'b01)
            serial_out=data[0];
    end
    
    initial begin
        $dumpfile("usr.vcd");
        $dumpvars(1,usr);
    end
endmodule

