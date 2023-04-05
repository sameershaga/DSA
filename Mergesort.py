import random
li = [random.randint(0,10000) for i in range(500)]
#print(li, len(li))
ls = sorted(li)
mc= 0
def mergesort(a):
    if len(a)<=1:
        return 0
    b = a[:len(a) // 2]
    c = a[len(a) // 2:]
    mergesort(b)
    mergesort(c)
    merge(b, c, a)
def merge(b, c, a):
    global mc
    mc+=1
    i = j = k = 0
    #print(f"merge {mc} started---------\n{b=} \n{c=}\n{a=}")
    while i < len(b) and j < len(c):
        if b[i] <= c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
        k += 1
    while i < len(b):
        a[k] = b[i]
        i += 1
        k += 1
    while j < len(c):
        a[k] = c[j]
        j += 1
        k += 1
    #print(f"merge {mc} ended------------ \n now {a=}")
mergesort(li)
print(li==ls)
