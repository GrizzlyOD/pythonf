f = open("cj.txt")
sum = 0
count = 0
while True:
    line = f.readline()
    if len(line)==0:
        break
    else:
        line=line.strip('\n'or' ')
        try:
            number = int(line[0])*1+int(line[2])*0.1
            sum+=number
            count = count + 1
        except IndexError as err:
            pass
f.close()


print(sum)
print(count)