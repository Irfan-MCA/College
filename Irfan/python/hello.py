'''sum=0
for i in range(0, 5):
    sum+=i;
print(sum)
for i in range(0, 11):
    if i%2==0:
        print(i)
x =5
if x<100:
    print(x/2)
elif x<10:
    print(x*2)
    if x<0:
    print(x,"negative number")
else:
    print(x,"is positve number")


x= int (input("enter a number"))
if x%2==0 and x>0:
    print(x," is even number and positive")
elif x%2==1 and x>0:
    print(x,"is an odd number and positive")
elif x%2==0 and x<0:
    print(x,"is an even number and negative")
elif x%2==1 and x<0:
    print(x,"is an odd number and negative")
else:
    print("invalid input")
    
for i in range (1,11):
    sum=i*5
    print(i ,"x 5 =",sum)

x= int (input("enter a number : "))
print("even") if (x%2==0)else print("odd")'''

'' ending'odd num between a given range using while loop
i=1
x= int (input("enter a limit : "))
while i<=x:
    if (i%2==1):
        print(i)
    i=i+1  
for i in range(90,100):
    print(i)
  
list="nivedh"
for i in list:
    print(i)
      
print prime number in a given range

x= int (input("enter a number to check prime : "))
is_prime=True 
for i in range(2,x):
    if(x%i==0):
         is_prime=False
         break  
if is_prime:
     print("prime")
else:
    print("not prime")

x= int (input("enter a range : "))
if x<2:
    for num in range(2,x+1):
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
else:
    print("invalid")'''
'''
num = input("Enter a number to check for Armstrong: ")  
total = 0 
length = len(num)
n = int(num)
for digit in num:
    total += int(digit) ** length
if n == total:
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")  

  '''
'''

#Functions

def hello():
    print("hello")


hello()

#num=int(input("enter thenumber" ))
#def odd_or_even(x=5):
def odd_or_even(*args):
    x=args[0]

    
    if x%2==0:
        print("Even")
    else:
        print("odd")
odd_or_even(6,7,8)


def check_list(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

check_list([1, 2, 3, 4, 5])
'''

'''
#program to find sum of 1 to 10
x=0
for i in range(0,11):
    x+=i
print("sum of 1 to 10 is:",x)

a=int(input("enter thenumber" ))
def f(n):
    if n < a:
        print(n+1)
        f(n + 1)

f(0) 
'''

'''

#Addition:
X = [[12,7,3], [4 ,5,6], [7 ,8,9]]
Y = [[5,8,1], [6,7,3], [4,5,9]]
result = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(len(X)):
     for j in range(len(X[0])):
          result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)


# Transpose:


X = [[12,7], [4 ,5], [3 ,8]]
result = [[0,0,0], [0,0,0]]
for i in range(len(X)):    
     for j in range(len(X[0])):
          result[j][i] = X[i][j]
for r in result:
    print(r)


#Multiplication:

X = [[12,7,3], [4 ,5,6], [7 ,8,9]]
Y = [[5,8,1,2], [6,7,3,0], [4,5,9,1]]
result = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
for i in range(len(X)):
     for j in range(len(Y[0])):
          for k in range(len(Y)):
               result[i][j] += X[i][k] * Y[k][j]


for r in result:
    print(r)
'''

'''
#Addition:
X = [[12,7,3], [4 ,5,6], [7 ,8,9]]
Y = [[5,8,1], [6,7,3], [4,5,9]]
result = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(len(X)):
     for j in range(len(X[0])):
          result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)

'''
'''
#Addition:

row = int(input("Number of row: "))
column = int(input("numbre of column: "))

matrix_1 = []
matrix_2 = []
result = []


print("\nEnter values for Matrix 1:")
for i in range(row):
    temp = []
    for j in range(column):
        val = int(input(f"Matrix 1[{i}][{j}]: "))
        temp.append(val)
    matrix_1.append(temp)

print("\nEnter values for Matrix 2:")
for i in range(row):
    temp = []
    for j in range(column):
        val = int(input(f"Matrix 2[{i}][{j}]: "))
        temp.append(val)
    matrix_2.append(temp)


for i in range(row):
    temp = []
    for j in range(column):
        temp.append(matrix_1[i][j] + matrix_2[i][j])
    result.append(temp)


print("\nMatrix 1:")
for r in matrix_1:
    print(r)

print("\nMatrix 2:")
for r in matrix_2:
    print(r)

print("\nResult (Matrix 1 + Matrix 2):")
for r in result:
    print(r)


'''









