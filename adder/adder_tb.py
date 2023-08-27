import cocotb
#from cocotb.runner import get_runner
from cocotb.triggers import Timer
from cocotb.clock import Clock

@cocotb.test()

async def adder_test(dut):
    dut.a.value = 0b00
    dut.b.value = 0b10
    await Timer(2, units='ns')
    dut._log.info("c is %s", dut.c.value)
    assert dut.c.value == 0b010
    dut.a.value = 0b11
    dut.b.value = 0b11
    await Timer(2, units='ns')
    dut._log.info("c is %s", dut.c.value)
    assert dut.c.value == 0b111