import math
import random

def gcd(a,b):
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd       

# print(gcd(15,15))

def is_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        return True
    else:
        return False
    
def generate_random_prime(min_value,max_value):
    if min_value < 2:
        min_value=2

    while True:
        num = random.randint(min_value,max_value)
        if (is_prime(num)):
            return num     
        
p=generate_random_prime(1,1000)
q=generate_random_prime(1,1000)
print("The First prime number is",p)        
print("The Second prime number is",q)

n= p*q
phi=(p-1)*(q-1)

e=2
while(e<phi):
    if(gcd(e,phi)==1):
        break
    e=e+1

print("The public key is",e)    

x=0
while True:
    if((e*x-1) % phi==0):
        d=x
        break
    x=x+1

m=int(input("Enter a message:"))

c=pow(m,e,n)
print("Cipher text is :",c)

r=pow(c,d,n)
print("The previous message sent was :",r)
