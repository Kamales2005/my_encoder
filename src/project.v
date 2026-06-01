/*
 * Copyright (c) 2026 Kamales D
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_kamales_encoder (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    // Priority encoder
    assign uo_out =
        ui_in[7] ? 8'd7 :
        ui_in[6] ? 8'd6 :
        ui_in[5] ? 8'd5 :
        ui_in[4] ? 8'd4 :
        ui_in[3] ? 8'd3 :
        ui_in[2] ? 8'd2 :
        ui_in[1] ? 8'd1 :
        ui_in[0] ? 8'd0 :
                   8'hFF;

    // Unused bidirectional pins
    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

    // Mark unused signals
    wire _unused = &{ena, clk, rst_n, uio_in, 1'b0};

endmodule
