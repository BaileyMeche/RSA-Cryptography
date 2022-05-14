import math

def isprime(a):
    if a>1: 
        for i in range(2, int(a/2)+1):
            if a%i == 0:
                return False
                break
        else:
           return True
    else: return False

e = int(input("Welcome to private key generator. \nInput public key: "))

#independent
p = int(input("Enter first prime: "))
check = False
while check == False:
   if isprime(p) == True:
      check = True
      break
   else:
     p = int(input("Invalid: not prime. Enter first prime: "))


q = int(input("Enter second prime prime: "))
check = False
while check == False:
   if (isprime(q) == True) and not(p==q):
      check = True
      break
   else:
     q = int(input("Invalid: not prime. Enter second prime: "))

phi = (p-1)*(q-1)

d = pow(e,-1,phi)
print("Private key: ", d) 
