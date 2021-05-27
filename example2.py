'''
file = open("new_text.txt","w")
for i in range(1,11):
    data = "{}번째 줄입니다.\n".format(i)
    file.write(data)
    pass
file.close()
'''
file = open("ABC1115.txt","r")
lines = file.readlines()
file.close()
print(lines[0])
print(len(lines))

for line in lines:
    print(line)
    pass
