import math
import random

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
alpha=random.randint(1,p-2)
print("prime number is ",p)
print("alpha is ",alpha)

private_key_B=random.randint(1,p-1)
public_key_B=pow(alpha,private_key_B,p)

k=random.randint(1,p-2)

m=int(input("Enter a message:"))

c1=pow(alpha,k,p)
share=pow(public_key_B,k,p)
c2=(m*share)%p

print(f"Ciphertext is ({c1}),({c2})")

s=pow(c1,private_key_B,p)
s_inv=pow(s,-1,p)
r=(s_inv*c2)%p
print("previous message sent was ",r)