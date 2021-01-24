# Writeup

添付のzipファイルを解凍すると、拡張子が`v`のファイルが3つある。

これらは、問題画像の通り、`Verilog Source Code Format`のファイルである。

怪しいのは`t_chall.v`の以下の部分であり、これを文字列に変換すると、`flag{vhis_is_fake_fake_fake_!!!}`となっている。

```v
  assign flag[0] = 102;
  assign flag[1] = 108;
  assign flag[2] = 97;
  assign flag[3] = 103;
  assign flag[4] = 123;
  assign flag[5] = 116;
  assign flag[6] = 104;
  assign flag[7] = 105;
  assign flag[8] = 115;
  assign flag[9] = 95;
  assign flag[10] = 105;
  assign flag[11] = 115;
  assign flag[12] = 95;
  assign flag[13] = 102;
  assign flag[14] = 97;
  assign flag[15] = 107;
  assign flag[16] = 101;
  assign flag[17] = 95;
  assign flag[18] = 102;
  assign flag[19] = 97;
  assign flag[20] = 107;
  assign flag[21] = 101;
  assign flag[22] = 95;
  assign flag[23] = 102;
  assign flag[24] = 97;
  assign flag[25] = 107;
  assign flag[26] = 101;
  assign flag[27] = 95;
  assign flag[28] = 33;
  assign flag[29] = 33;
  assign flag[30] = 33;
  assign flag[31] = 125;
```

次に、オンラインでVerilogコードを実行して動作確認を行った。

* [Compile and Execute Verilog Online](https://www.tutorialspoint.com/compile_verilog_online.php)

試しにfor文の中で`ok`の値を出力してみると、先頭の5つが`1`、残りが`0`となっていた。これは、`flag{`の5文字が本物のフラグと一致しているからだと推測できる。そこで、`ok=1`となるような`flag[6] ~ flag[31]`を探してみる。

```verilog
    for (idx = 0; idx < 32; idx++) begin
      inp = flag[idx];
      tmp = target[idx];
      #4;
      $display(ok); // add
    end
```

```
1
1
1
1
1
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
no
```

以下のコードを実行すると`ok == 1'b1`が成り立つようなフラグがASCIIコードとして出力される。

```verilog
// Testbench
`timescale 1ns/10ps

module magic(
  input clk,
  input rst,
  input[7:0] inp,
  input[1:0] val,
  output reg[7:0] res
);
  always @(*) begin
    case (val)
      2'b00: res = (inp >> 3) | (inp << 5);
      2'b01: res = (inp << 2) | (inp >> 6);
      2'b10: res = inp + 8'b110111;
      2'b11: res = inp ^ 8'd55;
    endcase
    // $display("val1 =",val);
    // $display("res1 =",res);
  end
endmodule

module chall(
  input clk,
  input rst,
  input[7:0] inp,
  output reg[7:0] res
);
  wire[1:0] val0 = inp[1:0];
  wire[1:0] val1 = inp[3:2];
  wire[1:0] val2 = inp[5:4];
  wire[1:0] val3 = inp[7:6];
  wire[7:0] res0, res1, res2, res3;

  magic m0(.clk(clk), .rst(rst), .inp(inp), .val(val0), .res(res0));
  magic m1(.clk(clk), .rst(rst), .inp(res0), .val(val1), .res(res1));
  magic m2(.clk(clk), .rst(rst), .inp(res1), .val(val2), .res(res2));
  magic m3(.clk(clk), .rst(rst), .inp(res2), .val(val3), .res(res3));

  always @(posedge clk) begin
    if (rst) begin
      assign res = inp;
    end else begin
      assign res = res3;
    end
    // $display("res2 =",res);
  end
endmodule

module t_chall();
  reg clk, rst, ok;
  reg[7:0] inp, idx, tmp;
  reg[7:0] res[32:0];
  wire[7:0] out;
  wire[7:0] target[32:0], flag[32:0];

  assign {target[0], target[1], target[2], target[3], target[4], target[5], target[6], target[7], target[8], target[9], target[10], target[11], target[12], target[13], target[14], target[15], target[16], target[17], target[18], target[19], target[20], target[21], target[22], target[23], target[24], target[25], target[26], target[27], target[28], target[29], target[30], target[31]} = {8'd182, 8'd199, 8'd159, 8'd225, 8'd210, 8'd6, 8'd246, 8'd8, 8'd172, 8'd245, 8'd6, 8'd246, 8'd8, 8'd245, 8'd199, 8'd154, 8'd225, 8'd245, 8'd182, 8'd245, 8'd165, 8'd225, 8'd245, 8'd7, 8'd237, 8'd246, 8'd7, 8'd43, 8'd246, 8'd8, 8'd248, 8'd215};

  // change the content of the flag as you need
  assign flag[0] = 102;
  assign flag[1] = 108;
  assign flag[2] = 97;
  assign flag[3] = 103;
  assign flag[4] = 123;
  assign flag[5] = 116;
  assign flag[6] = 104;
  assign flag[7] = 105;
  assign flag[8] = 115;
  assign flag[9] = 95;
  assign flag[10] = 105;
  assign flag[11] = 115;
  assign flag[12] = 95;
  assign flag[13] = 102;
  assign flag[14] = 97;
  assign flag[15] = 107;
  assign flag[16] = 101;
  assign flag[17] = 95;
  assign flag[18] = 102;
  assign flag[19] = 97;
  assign flag[20] = 107;
  assign flag[21] = 101;
  assign flag[22] = 95;
  assign flag[23] = 102;
  assign flag[24] = 97;
  assign flag[25] = 107;
  assign flag[26] = 101;
  assign flag[27] = 95;
  assign flag[28] = 33;
  assign flag[29] = 33;
  assign flag[30] = 33;
  assign flag[31] = 125;

  chall ch(.clk(clk), .rst(rst), .inp(inp), .res(out));

  initial begin
    $dumpfile("chall.vcd");
    $dumpvars;

    clk = 1'b0;
    #1 rst = 1'b1;
    #1 rst = 1'b0;
    inp = flag[0];
    tmp = target[0];

    ok = 1'b1;
    for (idx = 0; idx < 32; idx++) begin
      //inp = flag[idx];
      tmp = target[idx];
      // add below
      for (inp = 33; inp <= 125; inp++) begin
        ok = 1'b1;
        #4;
        if (ok == 1'b1) begin
            $display(inp);
        end
      end
    end

    if (ok) begin
      $display("ok");
    end else begin
      $display("no");
    end

    $finish;
  end

  always @(posedge clk) begin
    #1 ok = ok & (out == tmp);
  end

  always begin
    #2 clk = ~clk;
  end
endmodule
```

上記Verilogの出力を文字列に直す。

```py
flag = [102,108, 97,103,123,118, 51,114,121, 49, 95,118, 51,114, 49, 95,108,111,103, 49, 95,102, 49, 95, 52,100,103, 49, 95, 99,104, 51, 99,107, 51,114, 33,125]
msg = ''.join([chr(i) for i in flag])
print(msg)
```

`flag{v3ry1_v3r1_log1_f1_4dg1_ch3ck3r!}`

このまま入力するとIncorrectになった。どうやら、`49 = 1`と`95 = _`のペア、`52 = 4`と`100 = d`のペアはどちらも`ok = 1`になる条件を満たしているようなので、意味が通るようにどちらか一方を選択する。

<!-- flag{v3ry_v3r1log_f14g_ch3ck3r!} -->

