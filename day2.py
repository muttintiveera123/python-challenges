#1.day2 loops and strings
'''n,p=map(int,input("enter person and slices").split(" "))
m=n*p
if(m%4==0):
    print("pizzas need",m//4)
else:
    print("pizzas need",(m//4)+1)'''
'''import math
n,p=map(int,input("enter person and slices").split(" "))
m=n*p
np=math.ceil(m/4)
print(np)'''
#2.what is profit if 70% is loss for wages and default p=50
'''n,p=map(int,input("enter the number of glasses and each glass price").split(" "))
i=n*p
m=i-(i*(70/100))
print("profit is",m)'''
#3.not divisible by 6,7,8 in range
'''n,p=map(int,input("enter the range").split(" "))
for i in range(n,p,1):
    if(i%6!=0 and i%7!=0 and i%8!=0):
        print(" range of numbers not divisible by 6,7,8: ",i)
    else:
        print("no numbers")
#while
'n,p=map(int,input("enter the range").split(" "))
i=1
while(i<=p):
    i=range(n,p)
    if(i%6!=0 and i%7!=0 and i%8!=0):
        print(" range of numbers not divisible by 6,7,8: ",i)'''

#4.prime numbers
'''n,p=map(int,input("enter the n and p").split(" "))
sum=0
for i in range(n,p):
    if(i%==0):
        sum=sum+1
print("factors",sum)
if(sum<=2):
    print("prime number")
else:
    print("not a prime number")'''
'''n=int(input("enter the number"))
for i in range(2,n):
    if(n%i==0):
        print("not a prime")
        break
else:
    print("prime")'''

'''n=int(input("enter the number"))
for i in range(2,(n//2)+1):
    if(n%i==0):
        print("not a prime")
        break
else:
    print("prime")'''

#5.to find perfect number
'''n=int(input("enter the number"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
if(sum==n):
    print("perfect number")
else:
    print("not a perfect number")'''

#6.to print reverse of number
'''n=int(input("enter the number"))
sum=0
while(n>0):
    r=n%10
    sum=sum*10+r
    n=n//10
print(sum)'''

#for loop
'''n=int(input("enter the number"))
sum=0
for i in range(n):
    if n>0:
        r=n%10
        sum=sum*10+r
        n=n//10
    else:
        break
print(sum)'''
#sum of digits
'''n=int(input("enter the number"))
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)'''
#armstrong number
'''n=int(input("enter the number"))
temp=n
sum=0
while n>0:
    r=n%10
    sum=sum+r*r*r
    n=n//10
print(sum)
if(sum==temp):
    print("armstrong")
else:
    print("not armstrong")'''
#program to print armstrong numbers in a range
'''def armstrong(n,p):
    for i in range(n,p+1):
        sum=0
        x=i
        while i>0:
            r=i%10
            sum=sum+r*r*r
            i=i//10
        if(sum==x):
            print("armstrong",sum)
        else:
            print("not armstrong")
n,p=map(int,input("enter the n and p").split(" "))
print(armstrong(n,p))'''

#prime numbers
'''def prime_numbers(n,m):
    for i in range(n,m+1):
        c=0
        for j in range(1,i+1):
           if i%j==0:
               c+=1
        if c==2:
            print("prime",i)
n=int(input("enter the n"))
m=int(input("enter the m"))
print(prime_numbers(n,m))'''

#strong number
'''def strong(n):
    x,sum=n,0
    while n>0:
        digit=n%10
        fact=1
        for i in range(1,digit+1):
            fact*=i
        sum+=fact
        n//=10
    if sum==x:
        return "strong number"
    else:
        return "not a strong number"
n=int(input("enter the input"))
print(strong(n))'''

#range in strong number
'''def strong(n,p):
    for i in range(n,p+1):
        x,sum=i,0
        while i>0:
            digit=i%10
            fact=1
            for j in range(1,digit+1):
                fact*=j
            sum+=fact
            i//=10
        if sum==x:
            print(x)
n,p=map(int,input("enter the input").split(" "))
print(strong(n,p))'''

#strings
'''s=input("enter the string:")
s1=""
for i in s:
    if(i not in s1):
        s1+=i
print(s1)'''
# to remove conjugative duplicatives in string
'''s=input("enter the string")
s1=s[0]
for i in range(1,len(s)):
    if(s[i-1]!=s[i]):
        s1+=s[i]
print(s1)'''
#count a vowels in odd and even position
n=input("enter the string")
count1,count2=0
for i in range(len(s)):
    if(i%2==0):
        if(s[i]=='a' and s[i]=='e' and s[i]=='i' and s[i]=='o' and s[i]=='u'):
            count1=count1+1
    else:
        if(s[i]=='a' and s[i]=='e' and s[i]=='i' and s[i]=='o' and s[i]=='u'):
            count2=count2+1
print(count1,count2)

        
            
            









