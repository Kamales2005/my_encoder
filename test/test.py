# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    await ClockCycles(dut.clk, 5)

    dut.rst_n.value = 1

    # Test input bit 0
    dut.ui_in.value = 0b00000001
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0

    # Test input bit 2
    dut.ui_in.value = 0b00000100
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 2

    # Test input bit 5
    dut.ui_in.value = 0b00100000
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 5

    # Test input bit 7
    dut.ui_in.value = 0b10000000
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 7

    # Test no bits set
    dut.ui_in.value = 0
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 255
