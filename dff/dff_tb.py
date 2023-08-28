import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock

async def generate_clock(dut):
    """Generate clock pulses."""

    for cycle in range(10):
        dut.clk.value = 0
        await Timer(1, units="ns")
        dut.clk.value = 1
        await Timer(1, units="ns")


@cocotb.test()
async def Dflipflop_test(dut):
    """Try accessing the design."""

    await cocotb.start(generate_clock(dut))  # run the clock "in the background"

    dut.en.value=0
    await Timer(5, units="ns")  # wait a bit
    #await FallingEdge(dut.clk)  # wait for falling edge/"negedge"
    dut.en.value=1
    dut.d.value=0
    await Timer(2,units="ns")
    dut._log.info("Q id %s",dut.q.value)
    assert dut.q.value==0
    dut.d.value=1
    await Timer(2,units="ns")
    dut._log.info("Q id %s",dut.q.value)
    assert dut.q.value==1
