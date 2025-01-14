# Writeup

与えられたプログラムを実行する。

```
$ ./timer 

  ████████╗██╗███╗   ███╗███████╗██████╗ 
  ╚══██╔══╝██║████╗ ████║██╔════╝██╔══██╗
     ██║   ██║██╔████╔██║█████╗  ██████╔╝
     ██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗
     ██║   ██║██║ ╚═╝ ██║███████╗██║  ██║
     ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝

I'll show the flag when the timer is 0 seconds.

259200 seconds left.
259199 seconds left.
259198 seconds left.
```

長時間待つわけにもいかないので問題文の指示にある通り、GDBで起動する。

timer関数内の`cmp,jl`部分で`jump *address`することで強制的にtimerを抜ける。

```
[----------------------------------registers-----------------------------------]
RAX: 0x3 
RBX: 0x555555555510 (<__libc_csu_init>:	endbr64)
RCX: 0x7ffff7ea0334 (<__GI___clock_nanosleep+84>:	mov    edx,eax)
RDX: 0x0 
RSI: 0x0 
RDI: 0x0 
RBP: 0x7fffffffde40 --> 0x7fffffffde50 --> 0x0 
RSP: 0x7fffffffde30 --> 0x0 
RIP: 0x5555555554e3 (<timer+70>:	cmp    eax,DWORD PTR [rbp-0x4])
R8 : 0x0 
R9 : 0x15 
R10: 0x7fffffffddf0 --> 0x1 
R11: 0x246 
R12: 0x555555555080 (<_start>:	endbr64)
R13: 0x7fffffffdf40 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x206 (carry PARITY adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x5555555554d7 <timer+58>:	call   0x555555555060 <sleep@plt>
   0x5555555554dc <timer+63>:	add    DWORD PTR [rbp-0x8],0x1
   0x5555555554e0 <timer+67>:	mov    eax,DWORD PTR [rbp-0x8]
=> 0x5555555554e3 <timer+70>:	cmp    eax,DWORD PTR [rbp-0x4]
   0x5555555554e6 <timer+73>:	jl     0x5555555554b9 <timer+28>
   0x5555555554e8 <timer+75>:	mov    eax,0x0
   0x5555555554ed <timer+80>:	leave  
   0x5555555554ee <timer+81>:	ret
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffde30 --> 0x0 
0008| 0x7fffffffde38 --> 0x3f48000000003 
0016| 0x7fffffffde40 --> 0x7fffffffde50 --> 0x0 
0024| 0x7fffffffde48 --> 0x555555555501 (<main+18>:	)
0032| 0x7fffffffde50 --> 0x0 
0040| 0x7fffffffde58 --> 0x7ffff7de70b3 (<__libc_start_main+243>:	mov    edi,eax)
0048| 0x7fffffffde60 --> 0x7ffff7ffc620 --> 0x5081200000000 
0056| 0x7fffffffde68 --> 0x7fffffffdf48 --> 0x7fffffffe272 ("/media/sf_workspace/2021/WaniCTF21-spring/timer/rev-timer/timer")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x00005555555554e3 in timer ()
gdb-peda$ jump *0x5555555554e8
Continuing at 0x5555555554e8.
The time has come. Flag is "FLAG{S0rry_Hav3_you_b3en_wai7ing_lon6?_No_I_ju5t_g0t_her3}"
[Inferior 1 (process 65534) exited normally]
```

`jump`を実行するとフラグが表示された。

<!-- FLAG{S0rry_Hav3_you_b3en_wai7ing_lon6?_No_I_ju5t_g0t_her3} -->
