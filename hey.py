'''#leap year

from datetime import datetime
current_year=datetime.now().year
final_year=int(input("Enter the final year:"))

print("Leap year from",current_year,"to",final_year,":")
               
for year in range(current_year,final_year+1):
               if(year%4==0 and year%10!=0)or(year%400==0):
                   print(year)'''
               
               

'''#list comprehension

#a
numbers=[-7,-5,-2,0,1,2,-8,10]
positive_numbers=[num for num in numbers if num>0]
print(positive_numbers)

#b
N=[1,2,3,4,5]
squares=[num**2 for num in N]
print(squares)

#c
word="Programming"
vowels=[ch for ch in word if ch.lower() in 'aeiou']
print(vowels)

#d
word="Hello"
ordinals=[ord(ch) for ch in word]
print(ordinals)'''



'''#compare 2 list

list1=list(map(int,input("Enter the numbers for first list:").split()))
list2=list(map(int,input("Enter the numbers for second list:").split()))

#a
if len(list1)==len(list2):
    print("Both list are of same length")
else:
    print("Both list areb of different length")


#b
if sum(list1)==sum(list2):
    print("Both list are of same sum")
else:
    print("Both list are of different sum")


#c
common=set(list1)&set(list2)
if common:
    print("The common values are:",common)
else:
    print("no common values found !")'''



'''#string replace
s=input("Enter a string:")
ch=s[0]
s_new=ch+s[1:].replace(ch,'$')
print(s_new)'''



'''#n+nn+nnn
n=int(input("Enter a number:"))
result=n+int(str(n)*2)+int(str(n)*3)
print("Result is:",result)'''



'''#gcd
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
while b!=0:
    a,b=b,a%b
print("GCD is:",a)'''



'''#matrix addition

rows=int(input("Enter the number of rows:"))
cols=int(input("Enter the number of cols:"))

print("Enter the elements of first matrix:")
matrix1=[[int(input())for j in range(cols)]for i in range(rows)]

print("Enter the elements of second matrix:")
matrix2=[[int(input())for j in range(cols)]for i in range(rows)]

result=[[matrix1[i][j]+matrix2[i][j] for j in range(cols)]for i in range(rows)]

print("Result after matrix addition:")
for r in result:
    print(r)'''



'''#dictionary
d={}
n=int(input("Enter the number of items:"))
for i in range(n):
    key=input("Enter a key:")
    value=int(input("Enter the value:"))
    d[key]=value

asc=dict(sorted(d.items()))
print("Ascending order:",asc)

desc=dict(sorted(d.items(),reverse=True))
print("Descending order:",desc)'''



'''#factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter the number:"))
print("factorial of",num,"is",factorial(num))'''



'''#fibonacci
n=int(input("Enter the number of terms:"))
a,b=0,1
for i in range(n):
      print(a, end=" ")
      a,b=b,a+b'''



         

