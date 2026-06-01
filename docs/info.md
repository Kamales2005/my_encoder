<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

# 8-bit Priority Encoder

## How it works

This project implements an 8-bit priority encoder.

The eight dedicated input pins (`ui_in[7:0]`) are examined from the highest bit to the lowest bit. The output (`uo_out[7:0]`) contains the binary index of the highest-priority asserted input.

Examples:

| Input    | Output   |
| -------- | -------- |
| 00000001 | 00000000 |
| 00000010 | 00000001 |
| 00000100 | 00000010 |
| 00001000 | 00000011 |
| 10000000 | 00000111 |

If no input bit is asserted, the output is `11111111`.

The design is purely combinational and does not use the clock or reset signals.

## How to test

Apply a one-hot value to the input pins.

Examples:

* `ui_in = 00000001` → `uo_out = 00000000`
* `ui_in = 00000100` → `uo_out = 00000010`
* `ui_in = 00100000` → `uo_out = 00000101`
* `ui_in = 10000000` → `uo_out = 00000111`

When multiple bits are high simultaneously, the highest-order bit has priority.

Example:

* `ui_in = 10100010` → `uo_out = 00000111`

## External hardware

No external hardware is required.

Inputs may be driven using switches or GPIO signals, and outputs may be observed using LEDs, logic analyzers, or simulation tools.
