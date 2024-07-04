a = "Hello"
up = 0
lo = 0
for i in range(len(a)):
    if a[i].isupper():
        up+=1
    else:
        lo+=1
print(up,lo)
print(a[::-1])