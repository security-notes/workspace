value = [7941081424088616006, 7311705455698409823, 3560223458505028963, 35295634984951667]

flag = ""
for v in value:
    flag += bytes.fromhex(hex(v)[2:]).decode('utf-8')[::-1]
print(flag)
