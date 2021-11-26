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

#read private key and message to encrypt
n,e,m = input().split()

n = int(n)
e = int(e)
m = str(m)

ans = []
for character in m:
    # the argument 1 is the ASCII of the character
    temp = modular_exponentiation(ord(character),e,n)
    ans.append(str(temp))

# put comma between the string
joined_string = ",".join(ans)
print(joined_string)