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

def DHKE(p,alpha):
    private_key_A=random.randint(1,p-1)
    private_key_B=random.randint(1,p-1)

    public_key_A=pow(alpha,private_key_A,p)
    public_key_B=pow(alpha,private_key_B,p)

    print("Public key of A is ",public_key_A)
    print("Public key of B is ",public_key_B)

    secret_key_A=pow(public_key_B,private_key_A,p)
    secret_key_B=pow(public_key_A,private_key_B,p)

    print("Secret Key for A is",secret_key_A)
    print("Secret Key for B is",secret_key_B)

    if(secret_key_A==secret_key_B):
        print("Diffie Hellman Key Exchange is successful")

random_p=generate_random_prime(1,1000)
alpha=random.randint(1,random_p-2)
print("prime number is ",random_p)
print("alpha is ",alpha)

DHKE(random_p,alpha)                