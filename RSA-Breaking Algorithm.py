#works with 23, 1633 :/

import math

def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

e = input("Input first public key 'e': ")
n = input("Input product of primes 'n': ")

e = int(e)
n = int(n)

b = bin(n).count("1")+bin(n).count("0")-1

d = math.ceil(b/4)




k=1
s = []  #s is an array since we can have multiple solutions
while k<e:
    ed = e*d%(2**d)-1   #reduced remainder
    
    if k==1:
        s_0 = (-(ed - k*(n+1)))%(2**d)
        s.append(s_0)
    else:   #solving for s if k not = 1
        eq_r = ((ed-1) - k*(n+1))%(2**d)
        s_0 = pow(k,eq_r,2**d)

        #all possible solutions for s
        g_d = gcd(k,2**d)
        t=0
        
        while t < (g_d+1):      
            s.append(s_0 + ((2**d)/g_d)*t)
            t += 1
#    print(s)
    p_0=0
    for i in s:
        #y = 2p - i
        det = (i**2 - 4*n)%(2**d) #det == y since the only possibilities for y are 0 and 1. These are equal when squared
        p_0= (det + i)/2
        p_0=int(p_0)
        if (p_0**2 - i*p_0 + n)%(2**d) == 0:
#           print("fix: ",i)
            break
        else:
            print("ERROR: p does not compute")

    p_1 = p_0+1     #looking for second solution by Lagrange's thm
    while p_1 < 2**d:
        if (p_1**2 - i*p_1 + n)%(2**d) == 0:
            break
        else:
            p_1 += 1
#           print(p_1,p_0)

    sols_p = [p_0,p_1]  #all initial solutions for p collected in one array

    if p_0 >0:
        break
    else:      
        k += 1
        
q_0 = pow(p_0,-n,2**d)
q_1 = pow(p_1,-n,2**d)
sols_q = [q_0,q_1]  #all initial solutions for q collected in one array

x=0
j=0
##
while j<2:
    while x < math.ceil((n/sols_q[j]-sols_p[j])/(2**d)):
        y = ((n/((2**d)*x+sols_p[j]))-sols_q[j])/(2**d)#something goes wrong with modulo
        
        if ((n/((2**d)*x+sols_p[j]))-sols_q[j])%(2**d) == 0:          #^main computation 
        #if str(y)[-2:] == ".0":
            break
        else:
            x += 1

    y = ((n/((2**d)*x+sols_p[j]))-sols_q[j])/(2**d)
            #y = ((n/((2**d)*x+sols_p[j]))-sols_q[j])%(2**d)
    if ((n/((2**d)*x+sols_p[j]))-sols_q[j])%(2**d) == 0: 
    #if str(y)[-2:] == ".0":
        break
    else:
        x=0
        j += 1


if not str(y)[-2:] == ".0":
    print("ERROR")

y = int(y)

p = x*(2**d)+sols_p[j]  #using the variable j (still in the data stream) for which set of solutions worked
q = y*(2**d)+sols_q[j]

theta = (p-1)*(q-1)

SecretKey = (1+k*theta)/e  #luckily, the k that we found a working e is still in the data stream

#print("The primes p and q are probably: ", p,q)
print("The Secret key is: ", int(SecretKey))


