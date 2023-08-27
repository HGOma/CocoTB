import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock

async def generate_clock(dut):
    """Generate clock pulses."""

    for cycle in range(20):
        dut.clk.value = 0
        await Timer(1, units="ns")
        dut.clk.value = 1
        await Timer(1, units="ns")


@cocotb.test()
async def loadcase_test(dut):
    """Try accessing the design."""

    await cocotb.start(generate_clock(dut))  # run the clock "in the background"

    dut.enable.value=0b11
    await Timer(2, units="ns")  # wait a bit
    #await FallingEdge(dut.clk)  # wait for falling edge/"negedge"
    
    dut.parallel_in.value=0b10101000
    await Timer(2,units="ns")
    dut._log.info("Data id %s",dut.data.value)
    assert dut.data.value==0b10101000


    dut.parallel_in.value=0b00000000
    await Timer(2,units="ns")
    dut._log.info("Data id %s",dut.data.value)
    assert dut.data.value==0b00000000


@cocotb.test()
async def memorycase_test(dut):
    """Try accessing the design."""

    await cocotb.start(generate_clock(dut))  # run the clock "in the background"
    dut.enable.value=0b11
    
    dut.parallel_in.value=0b11111111
    await Timer(2,units="ns")
    dut.enable.value=0b00
    await Timer(1,units="ns")
    dut.parallel_in.value=0b0010
    await Timer(4,units="ns")
    dut._log.info("data=%s",dut.data.value)
    assert dut.data.value==0b11111111


@cocotb.test()
async def rightshift(dut):
    await cocotb.start(generate_clock(dut))
    dut.enable.value=0b11
    dut.parallel_in.value=0b0
    await Timer(4,units="ns")
    dut.enable.value=0b01
    dut.serial_in.value=0b1
    await Timer(16,units="ns")
    assert dut.data.value==0b11111111

@cocotb.test()
async def leftshift(dut):
    await cocotb.start(generate_clock(dut))
    dut.enable.value=0b11
    dut.parallel_in.value=0b11111111
    await Timer(4,units="ns")
    dut.enable.value=0b10
    #dut.serial_in.value=0b1
    await Timer(16,units="ns")
    assert dut.data.value==0b0
