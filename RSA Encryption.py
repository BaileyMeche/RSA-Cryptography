import sys
import math

def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

def isprime(a):
    if a>1: 
        for i in range(2, int(a/2)+1):
            if a%i == 0:
                return False
                break
        else:
           return True
    else: return False


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


#message cleaning
m = input("Enter message to be encrypted: ")

m = m.lower()   #cleaning messsage to work with number conversions
#NEED TO COVER NUMBERS AND PUNCTUATION

#dependent 
n=p*q
Phi = (p-1)*(q-1)


#public key
e = int(input("Enter public key: "))

Ereqs = [ e > 1,  e < Phi, gcd(e,Phi) == 1]

while(all(Ereqs)== False):
   e = int(input("Invalid. Enter public key: "))
   Ereqs = [ e > 1,  e < Phi, gcd(e,Phi) == 1]

#private key
           # PRINT OUT A LIST OF POSSIBLE PRIVATE KEYS ON ENCRYPTION SIDE
d = int(input("Enter private key: "))

while(((d*e-1)%Phi == 0)== False):
   d = int(input("Invalid. Enter private key: "))



#plaintext conversion

pt = []
for x in m:
   pt.append(ord(x) - 96)



#RSA Encryption

rsa = []
for y in pt:
    rsa.append((y**e)%n)
print("Encrypted messsage to be sent: ",rsa)


#RSA Decryption

pt_d = []
for z in rsa:
    pt_d.append((z**d)%n)

#plaintext reconversion

m_f = ""
for t in pt_d:
    if t==69:
        m_f += " "
    else: m_f += chr(t+96)
print("Decrypted message: ",m_f)

