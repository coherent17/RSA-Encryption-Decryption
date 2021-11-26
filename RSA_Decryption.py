# calculate a^b (mod c)
def modular_exponentiation(a,b,c):
    ans = 1
    a = a % c
    while(b!=0):
        #check whethter to multiply the partial product
        if b&1:
            ans = (ans*a)%c
        #b//2 equals to b>>1
        b>>=1;
        a = (a * a)%c
    return ans

# get the amount of the number from 1~n which has no common factor with n
def euler_totient_function(n):
    result = n
    i = 2
    while i*i <= n:
        # if i has common factor with n, then minus all of the number which has the fator of i in 1~n
        if n % i == 0:
            result = result - (result//i)
            # keep divide n until no common factor of i
            while n % i == 0:
                n = n // i
        i += 1
    # if there still exists a prime in n:
    if n != 1:
        result = result - (result//n)
    return result

# get the mod inverse by using extend euclidean method
# find x such that ex = 1 (mod phi)
# -> ex - phi * y = 1
def mod_inv(a,b):
    # left_number = left_coeff_a * a + left_coeff_b * b, initial condition: a = 1 * a + 0 * b
    left_coeff_a = 1
    left_coeff_b = 0
    left_number = a
    # right_number = right_coeff_a * a + right_coeff_b * b, initial condition: b = 0 * a + 1 * b
    right_coeff_a = 0
    right_coeff_b = 1
    right_number = b

    while(right_number !=0):
        quotient = left_number // right_number
        left_coeff_a = left_coeff_a - quotient * right_coeff_a
        left_coeff_b = left_coeff_b - quotient * right_coeff_b
        left_number = left_number - quotient * right_number
        # exchange the number (right <-> left)
        left_number, right_number = right_number, left_number
        left_coeff_a, right_coeff_a = right_coeff_a, left_coeff_a
        left_coeff_b, right_coeff_b = right_coeff_b, left_coeff_b
    return left_coeff_a % b

# read private key and the encrypted message
n,e,c = input().split()

n = int(n)
e = int(e)
c = str(c)
c = c.split(',')

# calculate the private key:
phi = euler_totient_function(n)
private_key= mod_inv(e,phi)

for i in range(len(c)):
    temp = modular_exponentiation(int(c[i]),private_key,n)
    print(chr(temp), end='')