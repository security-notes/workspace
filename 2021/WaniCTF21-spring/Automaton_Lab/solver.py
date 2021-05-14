from pwn import *

rule = {'111':'0', '110':'0', '101':'0', '100':'1', 
        '011':'1', '010':'1', '001':'1', '000':'0'}

def rule30(state, gen):
    # Found Gen(46) = Gen(1501)
    if gen > 1500:
        gen = gen % 1455
    for _ in range(gen):
        next_state = ""
        state = state[-1] + state + state[0]
        for i in range(15):
            next_state += rule[state[i:i+3]]
        state = next_state
    return state

io = remote('automaton.mis.wanictf.org','50020')
io.recvuntil('(press enter key to continue)')
io.sendline()
for _ in range(3):
    io.recvuntil('= ')
    init = io.recvline().decode('utf-8').replace('\n','')
    io.recvuntil('= ')
    gen = int(io.recvline().decode('utf-8'))
    print(rule30(init,gen))
    io.recvuntil('> ')
    io.sendline(rule30(init,gen))
    print(io.recvline())
print(io.recvline())
io.close()