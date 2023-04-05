def primes_sieve(k):
    a=[True]*(k+1); a[0]=a[1]=False
    for (i,boolean) in enumerate(a):
        if boolean:
            yield i
            for n in range(i*i,k+1,i):
                a[n] = False# Mark factors non-prime
def primefactorize(i):
    A=[]
    for p in primes_sieve(i):
        while i%p == 0:
            A.append(p)
            i = i//p
    return A
def gcd(a,b):
   a=primefactorize(a);b=primefactorize(b);print(a, b)
   p=1;i=0;j=0
   while i< len(a) and j< len(b):
      if a[i]==b[j]:
         p*=a[i];i+=1;j+=1
      elif a[i]<b[j]:i+=1
      else:j+=1
   return p
def inpt(p,min=1):
    while True:
        a = int(input(p))
        if a <= min:
            print("its<= 1. try again.")
        else:
            return a
while True:
    m=inpt("Num1: ")
    n=inpt("Num2: ")
    print(gcd(m,n))
    if input("(y to continue) ").lower() != 'y':
        break
