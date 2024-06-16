a = [1,2,'hi',2]
print(a.index('hi'))
print(a.count(2))

print(len(a))
print(type(a))

a.append(2)
a.extend([3,5,'hello'])
print(a)

a.insert(2,100)
print(a)

a.pop()
print(a)

del a[2]
print(a)

a.remove(5)
print(a)

a.clear()
print(a)

a.extend([1,2,3,4,5,6])
print(a)

# del a
print(a[4])
print(a[4:])
print(a[4::-1])
print(a[1:6:2])
# print(a[4])

b = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(b)):
    print(b[i])