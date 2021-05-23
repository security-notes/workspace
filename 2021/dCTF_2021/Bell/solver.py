from pwn import *

def main(uVar2:int):
    process(uVar2)

def process(param_1:int):
    local_24 = 1
    while local_24 <= param_1:
        lVar3 = triangle(param_1, local_24)
        print(lVar3)
        io.sendline(str(lVar3))
        local_24 += 1

def triangle(param_1:int, param_2:int):
    if param_1 < param_2:
        ret = 0
    else:
        if param_1 == 1 and param_2 == 1:
            ret = 1
        else:
            if param_2 == 1:
                ret = triangle(param_1 -1, param_1 -1)
            else:
                ret2 = triangle(param_1, param_2 -1)
                ret1 = triangle(param_1 -1, param_2 -1)
                ret = ret1 + ret2
    return ret

if __name__ == "__main__":
    io = remote('dctf-chall-bell.westeurope.azurecontainer.io','5311')
    var = int(io.recvline())
    print(var)

    main(var)
    
    print(io.recvall())
    io.close()
