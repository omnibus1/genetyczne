arr=[]
for line in open("input.txt","r"):
    line=line.replace(",",".")
    arr.append(float(line))
print(arr)