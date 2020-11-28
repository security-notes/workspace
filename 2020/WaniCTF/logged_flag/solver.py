import re

cmd = ''

with open('./key_log.txt') as f:
    for _ in range(317):
        line = f.readline()
        key = re.findall(r'(?<=\[).+?(?=\])',line)
        if len(key) == 0:
            continue
        if key[0] == 'Enter':
            cmd += '\n'
        elif key[0] == 'Shift':
            continue
        elif key[0] == 'Space':
            cmd += ' '
        elif key[0] == 'BackSpace':
            cmd = cmd[:-1]
        else:
            cmd += key[0].lower()
    
    print(cmd)