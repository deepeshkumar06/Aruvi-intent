# def funtion_name(name,age):
#     # print(name,"  ",age)
#     print(f'{name} and {age}')

# funtion_name('deepesh',20)
# funtion_name('Kumar' , 20)

# def bodmas(x,y,z=5):
#     print((x/2)+y*(z-y))
# bodmas(45,20)
# bodmas(45,20,10)

# def student(name,deg,role):
#     print(f'My Name is {name}, I have completed {deg} & and working as the role {role}')
# student('Deepesh','B.E','Software Developer')

# def odd(a):
#     if a%2 == 0:
#         print('even')
#     else:
#         print('odd')
# a = int(input("enter : "))
# odd(a)

# b = [1,2,3,4,5]

# def no(a):
#     print("Number is ",a)

# for i in range(len(b)):
#     no(b[i])

# def add(a,b):
#     print(a+b)

# add(10,20)
# add(40,5)

# n=10
# c = n>8

#Arbitary function:*,**:

def lang(*a):
    for l in a:
        print("I Like to learn : ",l)
lang("C","C++","Python")

def stu(**karg):
    for key,value in karg.items():
        print(key,value)
stu(Name="Deepesh",Degree="B.E",Role="Developer")

def stu(**karg):
    for key,value in karg.items():
        print('%s == %s'%(key,value))
stu(Name="Deepesh",Degree="B.E",Role="Developer")


#Lambda Function

a = lambda x,y,z : print('%s'%(x+y+z))
a(4,5,6)

li = [1,2,3,4,5,6]
even = list(filter(lambda x : x%2==0,li))
print(even)

li = list(range(10))
square = list(map(lambda s : s**2,li))
print(square)